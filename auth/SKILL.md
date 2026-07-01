---
name: pingcode-auth
description: "PingCode API 认证：企业令牌获取与刷新。所有 API 调用前必须先完成认证。"
metadata:
  qwenpaw:
    emoji: "🔑"
    requires:
      env: ["PINGCODE_CLIENT_ID", "PINGCODE_CLIENT_SECRET"]
---

# 🔑 PingCode API 认证

## 概述

PingCode REST API 使用 OAuth2 企业令牌（Client Credentials）认证。调用任何 API 前，需先用 Client ID + Secret 换取 `access_token`。

## 认证流程

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  Client ID      │────▶│  /v1/auth/token   │────▶│  access_token   │
│  Client Secret  │     │  grant_type=      │     │  (30 天有效)    │
└─────────────────┘     │  client_credentials│     └─────────────────┘
                        └──────────────────┘
                                │
                                ▼
                        ┌──────────────────┐
                        │  后续请求 Header: │
                        │  Authorization:   │
                        │  Bearer {token}   │
                        └──────────────────┘
```

## 获取企业令牌

### 请求

```
GET {base_url}/v1/auth/token?grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}
```

**参数（查询参数）：**

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `grant_type` | String | 是 | 固定值 `client_credentials` |
| `client_id` | String | 是 | 应用 Client ID |
| `client_secret` | String | 是 | 应用 Client Secret |

### 响应

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIs...",
  "token_type": "Bearer",
  "expires_in": 2592000
}
```

| 字段 | 类型 | 说明 |
|------|------|------|
| `access_token` | String | 令牌，后续请求放入 Header |
| `token_type` | String | 固定 `Bearer` |
| `expires_in` | Number | 过期时间（秒），默认 30 天 |

### 失败响应

```json
{
  "error": "invalid_client",
  "error_description": "client_id or client_secret is invalid"
}
```

## 使用令牌

获取 `access_token` 后，所有后续请求的 Header 中添加：

```
Authorization: Bearer {access_token}
```

## curl 示例

```bash
# 设置凭据
export PINGCODE_CLIENT_ID="your_client_id"
export PINGCODE_CLIENT_SECRET="your_client_secret"
export BASE_URL="https://open.pingcode.com"

# 获取令牌
TOKEN=$(curl -s "${BASE_URL}/v1/auth/token?grant_type=client_credentials&client_id=${PINGCODE_CLIENT_ID}&client_secret=${PINGCODE_CLIENT_SECRET}" | python3 -c "import sys,json;print(json.load(sys.stdin)['access_token'])")

# 调用 API
curl -s -H "Authorization: Bearer ${TOKEN}" "${BASE_URL}/v1/myself"
```

## Python 示例

```python
import json, os, urllib.request

base = os.environ.get("PINGCODE_BASE_URL", "https://open.pingcode.com")
cid = os.environ["PINGCODE_CLIENT_ID"]
csec = os.environ["PINGCODE_CLIENT_SECRET"]

# 获取令牌
url = f"{base}/v1/auth/token?grant_type=client_credentials&client_id={cid}&client_secret={csec}"
resp = json.loads(urllib.request.urlopen(url).read())
token = resp["access_token"]

# 调用 API
req = urllib.request.Request(f"{base}/v1/myself")
req.add_header("Authorization", f"Bearer {token}")
result = json.loads(urllib.request.urlopen(req).read())
print(result)
```

## Go 示例

```go
package main

import (
    "encoding/json"
    "fmt"
    "io"
    "net/http"
    "os"
)

func main() {
    base := os.Getenv("PINGCODE_BASE_URL")
    if base == "" {
        base = "https://open.pingcode.com"
    }
    cid := os.Getenv("PINGCODE_CLIENT_ID")
    csec := os.Getenv("PINGCODE_CLIENT_SECRET")

    // 获取令牌
    authURL := fmt.Sprintf("%s/v1/auth/token?grant_type=client_credentials&client_id=%s&client_secret=%s", base, cid, csec)
    resp, _ := http.Get(authURL)
    body, _ := io.ReadAll(resp.Body)
    var tokenResp struct {
        AccessToken string `json:"access_token"`
    }
    json.Unmarshal(body, &tokenResp)

    // 调用 API
    req, _ := http.NewRequest("GET", base+"/v1/myself", nil)
    req.Header.Set("Authorization", "Bearer "+tokenResp.AccessToken)
    client := &http.Client{}
    apiResp, _ := client.Do(req)
    apiBody, _ := io.ReadAll(apiResp.Body)
    fmt.Println(string(apiBody))
}
```

## 注意事项

- `access_token` 有效期 **30 天**
- 删除应用或重置 Secret 会导致令牌立即失效
- 企业令牌拥有系统管理员权限，请妥善保管
- 建议在本地缓存 token，避免频繁换取
- 生产环境建议将 Secret 存入密钥管理服务，不要硬编码

## 本模块 API

| 方法 | 路径 | 说明 |
|------|------|------|
| `GET` | `/v1/auth/token?grant_type=client_credentials` | 获取企业令牌 |
| `GET` | `/v1/auth/token?grant_type=authorization_code` | 获取用户令牌 |
| `GET` | `/v1/auth/token?grant_type=refresh_token` | 刷新用户令牌 |

如需查看完整参数表，读取 `APIs.md`。
