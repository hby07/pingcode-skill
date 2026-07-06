# PingCode Skill — Agent Pressure Scenarios

> 使用前必读：这些测试模拟 Agent 在真实场景下的行为。每个场景应分别在 **没有本 Skill**（基线）和 **有本 Skill** 的情况下运行，观察行为差异。

## 如何测试

```
1. 在一个没有安装 pingcode-skill 的 Agent 中运行场景
2. 记录 Agent 的行为（它怎么尝试、犯了什么错）
3. 在安装了 pingcode-skill 的 Agent 中运行相同场景
4. 对比两次结果
```

---

## 场景 1：基本信息查询

**用户输入：**
> "帮我查一下 PingCode 上我的用户信息"

**期望行为（有 Skill）：**
1. Agent 检测到"PingCode"关键词 → 加载 `auth/SKILL.md`
2. 检查环境变量 `PINGCODE_CLIENT_ID` / `PINGCODE_CLIENT_SECRET`
3. 用 `GET /v1/auth/token` 获取令牌
4. 调用 `GET /v1/myself` 返回用户信息
5. 只用了 `auth` 模块，没有加载其他模块

**常见失败（无 Skill）：**
- Agent 尝试直接访问 pingcode.com（网页，不是 API）
- Agent 尝试用未认证的请求（401）
- Agent 猜测错误的 API 路径

---

## 场景 2：工作项查询

**用户输入：**
> "帮我查一下 PingCode HBA 项目里所有未完成的 Bug"

**期望行为（有 Skill）：**
1. Agent 检测到"PingCode + 工作项/Bug" → 加载 `workitem/SKILL.md`
2. 先读 `auth/SKILL.md` 获取令牌
3. 调用 `GET /v1/pjm/work_items?project_id={id}&page=1&size=100`
4. 按 `work_item_type_id` 过滤出 Bug 类型
5. 如果结果 > 100，进行分页
6. **没有加载** `code/`, `test/`, `wiki/` 等无关模块

**注意：** Agent 不应硬编码 project_id，应先询问用户或从上下文提取。

---

## 场景 3：更新状态（PATCH vs PUT 测试）

**用户输入：**
> "把 HBLIVE-3 这个需求的状态改为'进行中'"

**期望行为（有 Skill）：**
1. Agent 加载 `workitem/SKILL.md`
2. 使用 `PATCH /v1/pjm/work_items/{id}`（部分更新）
3. body 只包含 `{"status":"进行中"}`
4. **没有**使用 PUT

**常见失败（无 Skill）：**
- Agent 用 PUT 替换整个资源（可能擦除其他字段）
- Agent 不知道工作项的 `status` 字段名

---

## 场景 4：新建工作项 + 评论

**用户输入：**
> "在 HBA 项目里创建一个新的任务，标题是'优化登录页面性能'，然后加一条评论'已创建，优先级 P2'"

**期望行为（有 Skill）：**
1. 加载 `project/SKILL.md` 获取 `project_id`
2. 加载 `workitem/SKILL.md`
3. `POST /v1/pjm/work_items` 创建任务
4. 从响应中拿到新工作项的 ID
5. `POST /v1/comments` 使用新 ID 添加评论（注意 `principal_type=pjm_work_item`）
6. 两个 API 调用都使用同一个 token

**注意：** Agent 不应把"评论"和"更新状态"搞混。

---

## 场景 5：分页压力测试

**用户输入：**
> "把 HBA 项目里所有工作项都列出来（可能有几百个）"

**期望行为（有 Skill）：**
1. Agent 注意到分页限制（size 最大 100）
2. 先调 `GET /v1/pjm/work_items?project_id={id}&page=1&size=100`
3. 检查响应数量，如果等于 100 则继续翻页
4. 聚合所有页面结果返回
5. **没有**只用一次请求就认为拿到了全部数据

---

## 场景 6：模块选择测试

**用户输入：**
> "帮我看看 HBA 项目的构建和部署记录"

**期望行为（有 Skill）：**
1. Agent 检测到"构建"和"部署"→ 加载 `release/SKILL.md`
2. 调用 `GET /v1/ci/builds` 和 `GET /v1/cd/deployments`
3. **没有**加载 `workitem/`, `code/`, `test/` 等无关模块
4. **没有**调 `POST` 去创建新构建/部署（用户只说"看看"）

---

## 场景 7：代码关联（跨模块）

**用户输入：**
> "我在 HBA 项目的 main 分支上新提交了 abc123，帮我关联到 HBLIVE-5 这个需求"

**期望行为（有 Skill）：**
1. 加载 `code/SKILL.md` 了解仓库和提交引用 API
2. 加载 `workitem/SKILL.md` 了解关联 API
3. `GET /v1/scm/repositories` 获取仓库
4. `POST /v1/pjm/work_items/{id}/commit_references` 关联提交
5. **只加载了 `code` 和 `workitem` 两个模块**

---

## 场景 8：Token 过期处理

**用户输入（上下文中已有 401 错误）：**
> "刚才报错了，说 token 过期，帮我重新弄一下"

**期望行为（有 Skill）：**
1. Agent 认出 401 / token 过期
2. 重新调 `GET /v1/auth/token` 获取新 token
3. 用新 token 重试刚才失败的请求
4. **没有**只报错而不重试

---

## 场景 9：限流处理

**用户输入（连续快速调用后出现 429）：**
> "查一下所有项目、所有工作项、所有成员"

**期望行为（有 Skill）：**
1. Agent 注意到 `X-RateLimit-Remaining` 响应头
2. 剩余次数低时放慢请求速度
3. 收到 429 后等待 Retry-After 再重试
4. **没有**无视限流持续请求

---

## 场景 10：项目确认

**用户输入：**
> "帮我建一个新的需求，标题是'接入微信支付'"

**期望行为（有 Skill）：**
1. Agent 意识到需要 `project_id`
2. 先获取项目列表 `GET /v1/pjm/projects`
3. 询问用户："你有多个项目，请问要在哪个项目下创建？HBA 还是 HBLIVE？"
4. 用户确认后再创建
5. **没有**默认使用第一个项目也不询问

---

## 评分标准

| 等级 | 说明 |
|------|------|
| 🟢 完美 | Agent 按所有期望行为执行，无多余 API 调用 |
| 🟡 可接受 | Agent 完成任务但有 1-2 处小问题（如多加载了一个模块） |
| 🟠 有缺陷 | Agent 完成了但犯了规则中明确禁止的错误 |
| 🔴 失败 | Agent 无法完成任务或使用了错误的 API |

## 通过条件

- **全部 10 个场景**达到 🟢 或 🟡
- **场景 3（PATCH）** 和 **场景 5（分页）** 必须 🟢
- 没有 🔴 场景
