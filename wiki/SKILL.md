---
name: pingcode-wiki
description: "Use when managing PingCode knowledge base: wiki spaces, pages, comments, attachments, or space configurations."
metadata:
  qwenpaw:
    emoji: "📚"
    requires:
      env: ["PINGCODE_CLIENT_ID", "PINGCODE_CLIENT_SECRET"]
---

# 📚 知识库

知识空间、页面、评论、附件。本模块包含 **21** 个 API。

## 快速调用

```bash
curl -s -H "Authorization: Bearer $TOKEN" "https://open.pingcode.com/v1/wiki/spaces"
```

## 本模块 API 列表

| 方法 | 路径 | 说明 |
|------|------|------|
| `GET` | `/v1/wiki/spaces` | 获取空间列表 |
| `POST` | `/v1/wiki/spaces` | 创建空间 |
| `GET` | `/v1/wiki/spaces/{space_id}/pages` | 获取页面列表 |
| `POST` | `/v1/wiki/pages` | 创建页面 |
| … | … | 共 21 个接口，详见 `APIs.md` |

完整参数表见 `APIs.md`。