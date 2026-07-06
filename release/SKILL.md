---
name: pingcode-release
description: "Use when managing PingCode releases and deployments: build records, deployment records, release versions, or environment management."
metadata:
  qwenpaw:
    emoji: "🚀"
    requires:
      env: ["PINGCODE_CLIENT_ID", "PINGCODE_CLIENT_SECRET"]
---

# 🚀 交付与发布

构建记录、部署记录、发布版本、环境管理。本模块包含 **42** 个 API。

## 快速调用

```bash
curl -s -H "Authorization: Bearer $TOKEN" "https://open.pingcode.com/v1/ci/builds"
```

## 本模块 API 列表

| 方法 | 路径 | 说明 |
|------|------|------|
| `GET` | `/v1/ci/builds` | 获取构建记录 |
| `POST` | `/v1/ci/builds` | 触发构建 |
| `GET` | `/v1/cd/deployments` | 获取部署记录 |
| `POST` | `/v1/cd/deployments` | 触发部署 |
| `POST` | `/v1/ship/versions` | 创建发布版本 |
| … | … | 共 42 个接口，详见 `APIs.md` |

完整参数表见 `APIs.md`。