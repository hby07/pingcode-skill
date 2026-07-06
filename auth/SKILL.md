---
name: pingcode-auth
description: "Use when obtaining or refreshing PingCode API access tokens. Required before any other module can be used."
metadata:
  qwenpaw:
    emoji: "🔑"
    requires:
      env: ["PINGCODE_CLIENT_ID", "PINGCODE_CLIENT_SECRET"]
---

# 🔑 认证与鉴权

使用 OAuth2 Client Credentials 获取 `access_token`。**所有 API 调用前必须先完成认证。**

## 认证流程

```
Client ID + Secret  ──▶  /v1/auth/token  ──▶  access_token（30 天有效）
                                                    │
                                                    ▼
                                          后续请求 Header:
                                          Authorization: Bearer {token}
```

## 快速获取

```bash
curl -s "https://open.pingcode.com/v1/auth/token?grant_type=client_credentials&client_id=$PINGCODE_CLIENT_ID&client_secret=$PINGCODE_CLIENT_SECRET"
```

**响应：** `{"access_token": "eyJ...", "token_type": "Bearer", "expires_in": 2592000}`

## ⚠️ 注意事项

- Token 有效期 **30 天**，过期返回 401，重新获取即可
- 建议本地缓存 token，避免每次请求前都去换取
- 删除应用或重置 Secret 会导致 token 立即失效
- 企业令牌拥有系统管理员权限，妥善保管

## 本模块 API

| 方法 | 路径 | 说明 |
|------|------|------|
| `GET` | `/v1/auth/token?grant_type=client_credentials` | 企业令牌 |
| `GET` | `/v1/auth/token?grant_type=authorization_code` | 用户授权码 |
| `GET` | `/v1/auth/token?grant_type=refresh_token` | 刷新用户令牌 |

完整参数表见 `APIs.md`。