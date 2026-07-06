---
name: pingcode-product
description: "Use when managing PingCode products: tickets, customers, external users, modules, tags, or product members."
metadata:
  qwenpaw:
    emoji: "📦"
    requires:
      env: ["PINGCODE_CLIENT_ID", "PINGCODE_CLIENT_SECRET"]
---

# 📦 产品管理

产品、产品成员、工单、客户、外部用户、标签、模块。本模块包含 **85** 个 API。

## 快速调用

```bash
curl -s -H "Authorization: Bearer $TOKEN" "https://open.pingcode.com/v1/ship/products"
```

## ⚠️ 注意事项

- 产品 ID（`product_id`）与项目 ID（`project_id`）不同，不要混用
- 工单创建时可附带自定义字段，字段定义见 `product/APIs.md`

## 本模块 API 列表

| 方法 | 路径 | 说明 |
|------|------|------|
| `GET` | `/v1/ship/products` | 获取产品列表 |
| `POST` | `/v1/ship/products` | 创建产品 |
| `GET` | `/v1/ship/products/{product_id}` | 获取产品详情 |
| `PATCH` | `/v1/ship/products/{product_id}` | 更新产品 |
| … | … | 共 85 个接口，详见 `APIs.md` |

完整参数表见 `APIs.md`。