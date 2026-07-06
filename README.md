# PingCode REST API Skill

> 🤖 为 AI Agent 封装的 PingCode REST API 全模块调用能力

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![PingCode API](https://img.shields.io/badge/PingCode%20API-v1-blue.svg)](https://open.pingcode.com/)
[![OpenCode](https://img.shields.io/badge/OpenCode-compatible-blue.svg)](https://opencode.ai)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-compatible-green.svg)](https://claude.ai)
[![QwenPaw](https://img.shields.io/badge/QwenPaw-compatible-orange.svg)](https://github.com/QwenPaw/QwenPaw)

## 这是什么

一个为 **AI Agent**（OpenCode / QwenPaw / Claude / Cursor 等）设计的 PingCode API Skill，让 Agent 能够：

- 📋 读取工作项、需求、缺陷
- 💻 管理代码仓库、分支、PR
- 🧪 操作测试用例与执行记录
- 🚀 触发构建、部署、发布
- ✍️ 回写评论、更新状态、上传附件

**核心场景：** Agent 从 PingCode 读取需求 → 实现需求 → 将结果回写 PingCode

---

## 🚀 快速安装

### 方法一：Agent 自动安装（推荐）

将以下提示词发送给你的 AI Agent：

```
请帮我安装 pingcode-skill：
1. 从 https://github.com/hby07/pingcode-skill 克隆仓库
2. 检测当前 agent 类型并安装到正确的 skills 目录
3. 配置环境变量 PINGCODE_CLIENT_ID 和 PINGCODE_CLIENT_SECRET
4. 验证安装成功
```

### 方法二：手动安装

```bash
git clone https://github.com/hby07/pingcode-skill.git
cp -r pingcode-skill .opencode/skills/pingcode  # OpenCode
# 或 .claude/skills/pingcode  # Claude Code
# 或 ~/.agents/skills/pingcode  # 通用
```

**详细安装说明：** 查看 [INSTALL.md](INSTALL.md)

---

## 特性

- **语言无关** — 不绑定任何编程语言，curl / Python / Go / Node.js 均可调用
- **566 个 API** 全覆盖，按 11 个业务模块拆分
- **按需加载** — Agent 只读取需要的模块，节省 95% 上下文
- **零依赖** — 纯文档驱动，无第三方包要求
- **附带脚本** — 可选 Python 便捷脚本（自动处理令牌）

## 目录结构

```
pingcode-skill/
├── SKILL.md                    # 🚪 路由入口（模块索引 + 规则）
├── INSTALL.md                  # 📖 安装指南
├── AGENT_INSTALL_PROMPT.md     # 🤖 Agent 自动安装提示词
├── REFERENCE.md                # 📖 多语言完整调用参考
├── auth/                       # 🔑 认证与鉴权
├── org/                        # 🏢 组织管理
├── product/                    # 📦 产品管理
├── workitem/                   # 📋 工作项（最常用）
├── code/                       # 💻 代码管理
├── test/                       # 🧪 测试管理
├── release/                    # 🚀 交付与发布
├── plan/                       # 📅 计划管理
├── wiki/                       # 📚 知识库与文档
├── project/                    # ⚙️ 项目管理
├── project_config/             # 🔧 项目配置中心
├── workflow/                   # 🔄 工作流示例
├── scripts/                    # 🔧 可选 Python 脚本
│   ├── pingcode.py             # 通用调用脚本
│   ├── generate_docs.py        # API 文档生成器
│   └── .env.example            # 凭据模板
├── REFERENCE.md                # 📖 多语言完整调用参考
├── README.md
├── CONTRIBUTING.md
└── LICENSE
```

每个模块包含：

- `SKILL.md` — 模块说明 + 快速调用 + 常用 API（轻量，< 2KB）
- `APIs.md` — 完整参数表、请求体、返回字段（按需加载）

## 快速开始

### 1. 获取 PingCode 凭据

前往 PingCode 企业后台 → 凭据管理 → 创建应用，获取 `Client ID` 和 `Client Secret`。

### 2. 配置环境变量

```bash
export PINGCODE_CLIENT_ID="your_client_id"
export PINGCODE_CLIENT_SECRET="your_client_secret"
```

### 3. 测试连通性

```bash
curl -s "https://open.pingcode.com/v1/auth/token?grant_type=client_credentials&client_id=$PINGCODE_CLIENT_ID&client_secret=$PINGCODE_CLIENT_SECRET"
```

### 4. 在 Agent 中使用

将此目录复制到 Agent 的 skills 路径下：

```bash
# QwenPaw / OpenCode
cp -r pingcode-skill .agent/skills/pingcode
```

## 多语言调用参考

每个模块的 SKILL.md 只展示 curl 示例（最通用、零依赖）。  
如需 **Python**、**Go**、**Node.js** 的完整调用代码，见 [`REFERENCE.md`](REFERENCE.md)。

## 模块速查

| 模块 | 触发场景 | API 数 |
|------|----------|--------|
| `auth` | 🔑 需要获取/刷新 API 令牌 | 6 |
| `org` | 🏢 管理成员、部门、团队 | 50 |
| `product` | 📦 管理产品、工单、客户 | 85 |
| `workitem` | 📋 操作需求、任务、缺陷、评论 | 94 |
| `code` | 💻 管理仓库、分支、PR | 44 |
| `test` | 🧪 测试用例与执行 | 70 |
| `release` | 🚀 构建、部署、发布 | 42 |
| `plan` | 📅 迭代、计划、路线图 | 34 |
| `wiki` | 📚 知识空间与页面 | 21 |
| `project` | ⚙️ 项目、看板 | 45 |
| `project_config` | 🔧 字段、状态、类型配置 | 75 |

## Before / After：用与不用本 Skill 的对比

### ❌ Before（没有 Skill）

> 用户："帮我查一下 PingCode 里这个迭代的 Bug 数量"
>
> Agent：打开浏览器 → 手动搜 PingCode API → 看文档 → 试错 → 被 401 卡住 → …
> **耗时：5-10 分钟，容易出错**

### ✅ After（有了本 Skill）

> 用户："帮我查一下 PingCode 里这个迭代的 Bug 数量"
>
> Agent：读 `auth/SKILL.md` → 获取 token → 读 `workitem/SKILL.md` → 调用 GET work_items → 按 `work_item_type_id` 过滤 → 返回结果
> **耗时：30 秒，一次成功**

## 工作流

详见 `workflow/apis.md`：

- **需求实现回写** — 读取需求 → 实现 → 回写评论 → 更新状态
- **代码关联** — 创建分支 → 关联提交 → 创建 PR
- **部署发布** — 获取环境 → 触发部署 → 创建版本

## 环境变量

| 变量 | 说明 | 必填 |
|------|------|------|
| `PINGCODE_CLIENT_ID` | 应用 Client ID | ✅ |
| `PINGCODE_CLIENT_SECRET` | 应用 Client Secret | ✅ |
| `PINGCODE_BASE_URL` | API 根地址 | ❌（默认 `https://open.pingcode.com`）|

## 贡献

欢迎提交 Issue 和 PR！详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

API 文档更新方式：
```bash
python3 scripts/generate_docs.py <path_to>/api_data.js
```

## License

[MIT](LICENSE)