---
name: pingcode
description: "PingCode REST API 全模块索引：组织管理、产品、工作项、代码、测试、发布、计划、知识库、项目管理。根据用户意图加载对应模块的 SKILL.md 和 APIs.md，通过 HTTP 请求调用 API。"
metadata:
  qwenpaw:
    emoji: "🔗"
    requires:
      env: ["PINGCODE_CLIENT_ID", "PINGCODE_CLIENT_SECRET"]
---

# PingCode API Skill

## 概述

本 Skill 封装了 [PingCode REST API](https://open.pingcode.com/) 全部接口，按业务模块拆分为 **11 个子模块**，每个模块独立维护。

**语言无关** — 本 skill 不绑定任何编程语言。AI Agent 可使用任意 HTTP 客户端（curl / Python / Go / Node.js 等）调用 API。附带的 Python 脚本仅为可选便捷工具。

**工作方式：**

1. 根据用户意图，判断需要操作哪个模块
2. 读取该模块的 `SKILL.md` 了解用法
3. 如需查看具体 API 参数，读取该模块的 `APIs.md`
4. 使用任意 HTTP 客户端调用 API（推荐先读 `auth/SKILL.md` 了解认证流程）

**⚠️ 不要一次性加载所有模块的 APIs.md，按需加载以节省上下文。**

## 认证

详见 `auth/SKILL.md`，简要流程：

```
1. 用 CLIENT_ID + CLIENT_SECRET 换取 access_token
2. 后续请求 Header 加上 Authorization: Bearer {access_token}
3. token 有效期 30 天，过期重新换取
```

**环境变量：**

| 变量 | 说明 | 必填 |
|------|------|------|
| `PINGCODE_CLIENT_ID` | 应用 Client ID | ✅ |
| `PINGCODE_CLIENT_SECRET` | 应用 Client Secret | ✅ |
| `PINGCODE_BASE_URL` | API 根地址 | ❌（默认 `https://open.pingcode.com`）|

## 快速调用（curl 示例）

```bash
# 1. 获取令牌
TOKEN=$(curl -s "https://open.pingcode.com/v1/auth/token?grant_type=client_credentials&client_id=$PINGCODE_CLIENT_ID&client_secret=$PINGCODE_CLIENT_SECRET" | python3 -c "import sys,json;print(json.load(sys.stdin)['access_token'])")

# 2. 调用 API
curl -s -H "Authorization: Bearer $TOKEN" "https://open.pingcode.com/v1/myself"
```

## 可选：Python 便捷脚本

如果你的环境有 Python，可以使用附带的脚本简化调用：

```bash
python3 {baseDir}/scripts/pingcode.py '{"method":"GET","path":"/v1/myself"}'
```

脚本自动处理令牌获取、缓存、刷新。详见 `scripts/README.md`。

## 模块索引

| 模块 ID | 模块名 | 说明 | API 数 |
|---------|--------|------|--------|
| `auth` | 🔑 认证与鉴权 | 企业令牌获取、用户授权码流程 | 6 |
| `org` | 🏢 组织管理 | 企业信息、成员、部门、团队、角色、职位 | 50 |
| `product` | 📦 产品管理 | 产品、工单、客户、标签、模块 | 85 |
| `workitem` | 📋 工作项 | 需求、任务、缺陷、评论、附件、工时 | 94 |
| `code` | 💻 代码管理 | 仓库、分支、提交、PR、评审 | 44 |
| `test` | 🧪 测试管理 | 用例、执行、测试库、配置 | 70 |
| `release` | 🚀 交付与发布 | 构建、部署、发布、环境 | 42 |
| `plan` | 📅 计划管理 | 迭代、计划、路线图 | 34 |
| `wiki` | 📚 知识库 | 空间、页面、评论、附件 | 21 |
| `project` | ⚙️ 项目管理 | 项目、看板、配置 | 45 |
| `project_config` | 🔧 配置中心 | 字段、状态、类型、自定义实体 | 75 |

## API 通用约定

| 约定 | 说明 |
|------|------|
| 格式 | JSON（请求/响应均为 `application/json`）|
| 时间 | 10 位 Unix 时间戳（秒级）|
| 分页 | `page` + `size`，默认每页 30 条，最大 100 条 |
| 状态码 | 标准 HTTP 状态码（200/201/400/401/403/404/429）|
| 限流 | 响应头 `X-RateLimit-Remaining` 显示剩余次数 |
| ID 格式 | 24 位十六进制字符串（如 `5e05d8448f8461dada9ba29c`）|
| URL 格式 | `https://{rest_api_root}/v1/{resource}` |

## 工作流示例

详见 `workflow/apis.md`，包含：

- **需求实现回写** — 读取需求 → 实现 → 回写评论 → 更新状态
- **代码关联** — 创建分支 → 关联提交 → 创建 PR
- **部署发布** — 获取环境 → 触发部署 → 创建版本

## 贡献

欢迎提交 Issue 和 PR！详见 `CONTRIBUTING.md`。

API 文档更新方式：下载最新的 `api_data.js`，运行 `python3 scripts/generate_docs.py api_data.js`。
