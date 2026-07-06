---
name: pingcode-plan
description: "Use when managing PingCode plans and sprints: iterations, roadmaps, releases, or plan configurations."
metadata:
  qwenpaw:
    emoji: "📅"
    requires:
      env: ["PINGCODE_CLIENT_ID", "PINGCODE_CLIENT_SECRET"]
---

# 📅 计划管理

迭代、计划、路线图。本模块包含 **34** 个 API。

## 快速调用

```bash
curl -s -H "Authorization: Bearer $TOKEN" "https://open.pingcode.com/v1/pjm/sprints"
```

## 本模块 API 列表

| 方法 | 路径 | 说明 |
|------|------|------|
| `GET` | `/v1/pjm/sprints` | 获取迭代列表 |
| `POST` | `/v1/pjm/sprints` | 创建迭代 |
| `PATCH` | `/v1/pjm/sprints/{sprint_id}` | 更新迭代 |
| `GET` | `/v1/pjm/roadmaps` | 获取路线图列表 |
| … | … | 共 34 个接口，详见 `APIs.md` |

完整参数表见 `APIs.md`。