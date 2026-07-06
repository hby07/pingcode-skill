---
name: pingcode-project
description: "Use when managing PingCode projects: project settings, boards, configurations, or project-level permissions."
metadata:
  qwenpaw:
    emoji: "⚙️"
    requires:
      env: ["PINGCODE_CLIENT_ID", "PINGCODE_CLIENT_SECRET"]
---

# ⚙️ 项目管理

项目、项目看板、项目配置。本模块包含 **45** 个 API。

## 快速调用

```bash
curl -s -H "Authorization: Bearer $TOKEN" "https://open.pingcode.com/v1/pjm/projects"
```

## ⚠️ 注意事项

- 项目 ID（`project_id`）是工作项/迭代等操作的必填参数，先从此模块获取
- 看板配置通过 `board_id` 关联

## 本模块 API 列表

| 方法 | 路径 | 说明 |
|------|------|------|
| `GET` | `/v1/pjm/projects` | 获取项目列表 |
| `POST` | `/v1/pjm/projects` | 创建项目 |
| `GET` | `/v1/pjm/projects/{project_id}` | 获取项目详情 |
| `PATCH` | `/v1/pjm/projects/{project_id}` | 更新项目 |
| `GET` | `/v1/boards` | 获取看板列表 |
| … | … | 共 45 个接口，详见 `APIs.md` |

完整参数表见 `APIs.md`。