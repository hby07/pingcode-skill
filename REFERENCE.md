# 多语言调用参考

> ⚡ 每个模块的 SKILL.md 只展示 **curl** 示例（最通用、零依赖）。  
> 本文件集中存放 Python / Go / Node.js 完整调用代码，按需读取。

## 认证（所有语言通用）

先获取 `access_token`（30 天有效）：

```bash
TOKEN=$(curl -s "https://open.pingcode.com/v1/auth/token?grant_type=client_credentials&client_id=$PINGCODE_CLIENT_ID&client_secret=$PINGCODE_CLIENT_SECRET" | python3 -c "import sys,json;print(json.load(sys.stdin)['access_token'])")
```

---

## Python（标准库，零依赖）

```python
import json, os, urllib.request

base = os.environ.get("PINGCODE_BASE_URL", "https://open.pingcode.com")
cid = os.environ["PINGCODE_CLIENT_ID"]
csec = os.environ["PINGCODE_CLIENT_SECRET"]

# 1. 获取令牌
url = f"{base}/v1/auth/token?grant_type=client_credentials&client_id={cid}&client_secret={csec}"
token = json.loads(urllib.request.urlopen(url).read())["access_token"]

# 2. 调用 API（以工作项列表为例）
req = urllib.request.Request(f"{base}/v1/pjm/work_items?project_id=xxx")
req.add_header("Authorization", f"Bearer {token}")
result = json.loads(urllib.request.urlopen(req).read())
print(json.dumps(result, indent=2, ensure_ascii=False))
```

**便捷脚本：** 也可用附带的 `scripts/pingcode.py`，自动处理令牌缓存与刷新：

```bash
python3 scripts/pingcode.py '{"method":"GET","path":"/v1/pjm/work_items","params":{"project_id":"xxx","page":1,"size":30}}'
```

---

## Go

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

    // 1. 获取令牌
    authURL := fmt.Sprintf("%s/v1/auth/token?grant_type=client_credentials&client_id=%s&client_secret=%s", base, cid, csec)
    resp, _ := http.Get(authURL)
    body, _ := io.ReadAll(resp.Body)
    var tokenResp struct { AccessToken string `json:"access_token"` }
    json.Unmarshal(body, &tokenResp)

    // 2. 调用 API
    req, _ := http.NewRequest("GET", base+"/v1/pjm/work_items?project_id=xxx", nil)
    req.Header.Set("Authorization", "Bearer "+tokenResp.AccessToken)
    apiResp, _ := http.DefaultClient.Do(req)
    apiBody, _ := io.ReadAll(apiResp.Body)
    fmt.Println(string(apiBody))
}
```

---

## Node.js

```javascript
const https = require('https');

const BASE_URL = process.env.PINGCODE_BASE_URL || 'https://open.pingcode.com';
const CID = process.env.PINGCODE_CLIENT_ID;
const CSEC = process.env.PINGCODE_CLIENT_SECRET;

// 1. 获取令牌
const authUrl = `${BASE_URL}/v1/auth/token?grant_type=client_credentials&client_id=${CID}&client_secret=${CSEC}`;
https.get(authUrl, (res) => {
  let data = '';
  res.on('data', chunk => data += chunk);
  res.on('end', () => {
    const token = JSON.parse(data).access_token;

    // 2. 调用 API
    const options = {
      hostname: new URL(BASE_URL).hostname,
      path: '/v1/pjm/work_items?project_id=xxx',
      headers: { 'Authorization': `Bearer ${token}` }
    };
    https.get(options, (apiRes) => {
      let apiData = '';
      apiRes.on('data', chunk => apiData += chunk);
      apiRes.on('end', () => console.log(JSON.parse(apiData)));
    });
  });
});
```
