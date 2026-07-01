---
name: pingcode-auth
description: "企业令牌获取、用户授权码流程 — 认证与鉴权 相关的 PingCode REST API。需要查看具体接口参数时读取本目录 APIs.md。"
metadata:
  qwenpaw:
    emoji: "🔑"
    requires:
      bins: ["python3"]
      env: ["PINGCODE_CLIENT_ID", "PINGCODE_CLIENT_SECRET"]
---

# 🔑 PingCode 认证与鉴权

## 概述

企业令牌获取、用户授权码流程

本模块包含 **6** 个 API 接口。

## 认证

从环境变量获取（与主模块共用）：

| 环境变量 | 说明 |
|----------|------|
| `PINGCODE_CLIENT_ID` | 应用 Client ID |
| `PINGCODE_CLIENT_SECRET` | 应用 Client Secret |
| `PINGCODE_BASE_URL` | API 根地址（可选，默认 `https://open.pingcode.com`）|

## 调用方式

```bash
python3 {{baseDir}}/../scripts/pingcode.py '{{"method":"GET","path":"/v1/myself"}}'
```

## 本模块 API 列表

| 方法 | 路径 | 说明 |
|------|------|------|
| `GET` | `/v1/auth/token?grant_type=client_credentials` | 获取企业令牌 |
| `GET` | `/v1/auth/token?grant_type=refresh_token` | 刷新用户令牌 |
| `GET` | `/v1/auth/token?grant_type=authorization_code` | 获取用户令牌 |
| `GET` | `https://{oauth2_root}/authorize?response_type=code` | 请求授权 |
| `` | `客户端凭据` | 客户端凭据 |
| `` | `授权码` | 授权码 |


## 详细参数

如需查看某个接口的完整参数表、请求体、返回字段，请阅读本目录的 **`APIs.md`**。

## 常用操作速查

- **GET 获取企业令牌**: `/v1/auth/token?grant_type=client_credentials` — 客户端凭据模式（`OAuth2 Client Credentials`）是最简单、直接的授权方式。通过该方式获取的访问令牌（`access_token`）不区分
- **GET 刷新用户令牌**: `/v1/auth/token?grant_type=refresh_token` — 开发者可通过 `refresh_token` 刷新获取全新的 `access_token`，从而避免用户频繁重复授权的问题。PingCode 中 `refres
- **GET 获取用户令牌**: `/v1/auth/token?grant_type=authorization_code` — 用于获取用户令牌。  注：`access_token` 有效期为 30 天；删除应用或重置应用密钥（`Secret`），都会导致当前令牌立即失效。
- **GET 请求授权**: `https://{oauth2_root}/authorize?response_type=code` — 授权码模式（`OAuth2 Authorization Code`）是最常用的授权方式，适用于企业员工管理个人数据。通过该方式获取的访问令牌（`access_t
- ** 客户端凭据**: `客户端凭据` — 
- ** 授权码**: `授权码` — 
