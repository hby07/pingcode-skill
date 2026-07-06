---
name: pingcode-code
description: "Use when managing PingCode code repositories: branches, commits, pull requests, code reviews, or hosted platform settings."
metadata:
  qwenpaw:
    emoji: "💻"
    requires:
      env: ["PINGCODE_CLIENT_ID", "PINGCODE_CLIENT_SECRET"]
---

# 💻 代码管理

代码仓库、分支、提交、提交引用、拉取请求、代码评审、托管平台。本模块包含 **44** 个 API。

## 快速调用

```bash
curl -s -H "Authorization: Bearer $TOKEN" "https://open.pingcode.com/v1/scm/repositories"
```

## ⚠️ 注意事项

- 创建 PR 前先查目标仓库是否已关联分支
- 代码评审（review）是独立实体，与 PR 通过 `principal_type` / `principal_id` 关联

## 本模块 API 列表

| 方法 | 路径 | 说明 |
|------|------|------|
| `GET` | `/v1/scm/repositories` | 获取仓库列表 |
| `GET` | `/v1/scm/repositories/{repo_id}/branches` | 获取分支列表 |
| `POST` | `/v1/scm/repositories/{repo_id}/pull_requests` | 创建 PR |
| `GET` | `/v1/scm/repositories/{repo_id}/pull_requests` | 获取 PR 列表 |
| `PATCH` | `/v1/scm/pull_requests/{pr_id}` | 更新 PR |
| … | … | 共 44 个接口，详见 `APIs.md` |

完整参数表见 `APIs.md`。