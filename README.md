# PingCode REST API Skill

> 🤖 为 AI Agent 封装的 PingCode REST API 全模块调用能力

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![PingCode API](https://img.shields.io/badge/PingCode%20API-v1-blue.svg)](https://open.pingcode.com/)

## 这是什么

一个为 **AI Agent**（OpenCode / QwenPaw / Claude / Cursor 等）设计的 PingCode API Skill，让 Agent 能够：

- 📋 读取工作项、需求、缺陷
- 💻 管理代码仓库、分支、PR
- 🧪 操作测试用例与执行记录
- 🚀 触发构建、部署、发布
- ✍️ 回写评论、更新状态、上传附件

**核心场景：** Agent 从 PingCode 读取需求 → 实现需求 → 将结果回写 PingCode

## 特性

- **语言无关** — 不绑定任何编程语言，curl / Python / Go / Node.js 均可调用
- **566 个 API** 全覆盖，按 11 个业务模块拆分
- **按需加载** — Agent 只读取需要的模块，节省 95% 上下文
- **零依赖** — 纯文档驱动，无第三方包要求
- **附带脚本** — 可选 Python 便捷脚本（自动处理令牌）

## 目录结构

```
pingcode-skill/
├── SKILL.md                    # 🚪 路由入口（模块索引）
├── auth/                       # 🔑 认证与鉴权（含 curl/Python/Go 示例）
├── org/                        # 🏢 组织管理
├── product/                    # 📦 产品管理
├── workitem/                   # 📋 工作项
├── code/                       # 💻 代码管理
├── test/                       # 🧪 测试管理
├── release/                    # 🚀 交付与发布
├── plan/                       # 📅 计划管理
├── wiki/                       # 📚 知识库与文档
├── project/                    # ⚙️ 项目管理
├── project_config/             # 🔧 项目配置中心
├── workflow/                   # 🔄 工作流示例
├── scripts/                    # 🔧 可选 Python 脚本
│   ├── pingcode.py             #    通用调用脚本
│   ├── generate_docs.py        #    API 文档生成器
│   └── .env.example            #    凭据模板
├── README.md
├── CONTRIBUTING.md
└── LICENSE
```

每个模块包含：

- `SKILL.md` — 模块说明 + API 列表（轻量，2-10KB）
- `APIs.md` — 完整参数表、请求体、返回字段（详细）

## 快速开始

### 1. 获取 PingCode 凭据

前往 PingCode 企业后台 → 凭据管理 → 创建应用，获取 `Client ID` 和 `Client Secret`。

### 2. 配置环境变量

```bash
export PINGCODE_CLIENT_ID="your_client_id"
export PINGCODE_CLIENT_SECRET="your_client_secret"
```

### 3. 测试连通性

**curl:**
```bash
curl -s "https://open.pingcode.com/v1/auth/token?grant_type=client_credentials&client_id=$PINGCODE_CLIENT_ID&client_secret=$PINGCODE_CLIENT_SECRET"
```

**Python（可选）:**
```bash
python3 scripts/pingcode.py '{"method":"GET","path":"/v1/myself"}'
```

### 4. 在 Agent 中使用

将此目录复制到 Agent 的 skills 路径下：

```bash
# QwenPaw / OpenCode
cp -r pingcode-skill .agent/skills/pingcode
```

## 多语言调用示例

### curl

```bash
# 获取令牌
TOKEN=$(curl -s "https://open.pingcode.com/v1/auth/token?grant_type=client_credentials&client_id=$PINGCODE_CLIENT_ID&client_secret=$PINGCODE_CLIENT_SECRET" | python3 -c "import sys,json;print(json.load(sys.stdin)['access_token'])")

# 调用 API
curl -s -H "Authorization: Bearer $TOKEN" "https://open.pingcode.com/v1/pjm/work_items?project_id=xxx"
```

### Python

```python
import json, os, urllib.request

base = "https://open.pingcode.com"
cid = os.environ["PINGCODE_CLIENT_ID"]
csec = os.environ["PINGCODE_CLIENT_SECRET"]

# 获取令牌
url = f"{base}/v1/auth/token?grant_type=client_credentials&client_id={cid}&client_secret={csec}"
token = json.loads(urllib.request.urlopen(url).read())["access_token"]

# 调用 API
req = urllib.request.Request(f"{base}/v1/pjm/work_items?project_id=xxx")
req.add_header("Authorization", f"Bearer {token}")
result = json.loads(urllib.request.urlopen(req).read())
```

### Go

```go
// 获取令牌
authURL := fmt.Sprintf("%s/v1/auth/token?grant_type=client_credentials&client_id=%s&client_secret=%s", base, cid, csec)
resp, _ := http.Get(authURL)
body, _ := io.ReadAll(resp.Body)
var tokenResp struct { AccessToken string `json:"access_token"` }
json.Unmarshal(body, &tokenResp)

// 调用 API
req, _ := http.NewRequest("GET", base+"/v1/pjm/work_items?project_id=xxx", nil)
req.Header.Set("Authorization", "Bearer "+tokenResp.AccessToken)
resp, _ = http.DefaultClient.Do(req)
```

## 模块速查

| 模块 | 说明 | API 数 |
|------|------|--------|
| `auth` | 企业令牌、用户授权 | 6 |
| `org` | 企业、成员、部门、团队 | 50 |
| `product` | 产品、工单、客户 | 85 |
| `workitem` | 需求、任务、缺陷、评论 | 94 |
| `code` | 仓库、分支、PR、评审 | 44 |
| `test` | 用例、执行、测试库 | 70 |
| `release` | 构建、部署、发布 | 42 |
| `plan` | 迭代、计划、路线图 | 34 |
| `wiki` | 知识空间、页面 | 21 |
| `project` | 项目、看板、配置 | 45 |
| `project_config` | 字段、状态、类型配置 | 75 |

## 工作流

详见 `workflow/apis.md`，包含：

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
