# 🔑 认证与鉴权 — API 详细文档

> 本文档包含 6 个接口的完整参数说明。
> 来源: https://open.pingcode.com/

---

## 客户端凭据

### `GET` 获取企业令牌

**路径:** `/v1/auth/token?grant_type=client_credentials`

客户端凭据模式（`OAuth2 Client Credentials`）是最简单、直接的授权方式。通过该方式获取的访问令牌（`access_token`）不区分用户身份，在 PingCode 中被称为企业令牌。企业令牌拥有系统管理员权限，主要用于访问、操作全局数据，请谨慎保管。  获取企业令牌需提供 `client_id` 和 `client_secret`。您可前往 PingCode 企业后台的凭据管理页面创建应用、配置数据范围，即可获取这两个参数。调用接口时，只需在 HTTP 请求的请求头中添加 `Authorization: Bearer {access_token}`，就能访问受保护数据。  注：`access_token` 有效期为 30 天；删除应用或重置应用密钥（`Secret`），都会导致当前令牌立即失效。

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `grant_type` | String | 是 | 授权类型，这里固定为：`client_credentials`。 |
| `client_id` | String | 是 | PingCode应用的Client ID |
| `client_secret` | String | 是 | PingCode应用的Secret |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `access_token` | String | 令牌 |
| `token_type` | String | 类型类型 |
| `expires_in` | String | 过期时间 |

---
## 授权码

### `GET` 刷新用户令牌

**路径:** `/v1/auth/token?grant_type=refresh_token`

开发者可通过 `refresh_token` 刷新获取全新的 `access_token`，从而避免用户频繁重复授权的问题。PingCode 中 `refresh_token` 的默认有效期为90天；删除应用或重置应用密钥（`Secret`），都会导致当前令牌立即失效。

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `grant_type` | String | 是 | 授权类型，这里固定为：`refresh_token`。 |
| `refresh_token` | String | 是 | 通过`authorization_code`获取`access_token`时，一起返回的`refresh_token`。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `access_token` | String | 令牌 |
| `refresh_token` | String | 刷新令牌 |
| `token_type` | String | 类型类型 |
| `expires_in` | String | 过期时间 |

---
### `GET` 获取用户令牌

**路径:** `/v1/auth/token?grant_type=authorization_code`

用于获取用户令牌。  注：`access_token` 有效期为 30 天；删除应用或重置应用密钥（`Secret`），都会导致当前令牌立即失效。

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `grant_type` | String | 是 | 授权类型，这里固定为：`authorization_code`。 |
| `client_id` | String | 是 | PingCode应用的Client ID |
| `client_secret` | String | 是 | PingCode应用的Secret |
| `code` | String | 是 | 用户授权后，在回调地址中拿到的`code`值。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `access_token` | String | 令牌 |
| `refresh_token` | String | 刷新令牌 |
| `token_type` | String | 类型类型 |
| `expires_in` | String | 过期时间 |

---
### `GET` 请求授权

**路径:** `https://{oauth2_root}/authorize?response_type=code`

授权码模式（`OAuth2 Authorization Code`）是最常用的授权方式，适用于企业员工管理个人数据。通过该方式获取的访问令牌（`access_token`）在 PingCode 中被称为用户令牌，该令牌归属指定用户，仅可访问对应用户权限范围内的数据。  开发者可通过引导用户手动授权的方式获取用户令牌，使用该模式需提前准备 `client_id` 和 `redirect_uri` 两个核心参数。开发者可登录 PingCode 企业后台，在凭据管理模块创建应用、配置对应数据权限范围，同时获取应用唯一标识 `client_id` 以及授权回调地址 `redirect_uri`。完成配置后，需在第三方应用的页面引导用户通过浏览器访问 PingCode 授权页面，由用户自主完成授权确认操作；授权成功后，页面将自动跳转至预设的 `redirect_uri` 回调地址，同时在 URL 参数中返回临时授权码 `code`。开发者可凭借已获取的 `client_id` 和临时 `code` 兑换正式的用户令牌，后续调用接口、访问受保护资源时，只需在 HTTP 请求头部配置 `Authorization: Bearer {access_token}` 格式参数，即可完成权限校验与数据访问。  用户访问授权页面前需已登录 PingCode。  授权页面地址：`https://{oauth2_root}/authorize`。

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `response_type` | String | 是 | 响应类型，这里固定为code类型。 |
| `client_id` | String | 是 | PingCode应用的Client ID |

---
## 鉴权

### `` 客户端凭据

**路径:** `客户端凭据`

---
### `` 授权码

**路径:** `授权码`

---
