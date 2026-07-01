# PingCode API Python 便捷脚本

> 可选工具 — 如果你的环境有 Python，可以用这个脚本简化 API 调用。

## 功能

- 自动获取企业令牌并缓存
- 自动刷新过期令牌
- 统一的 JSON 输入/输出接口

## 使用

```bash
python3 pingcode.py '{"method":"GET","path":"/v1/myself"}'
python3 pingcode.py '{"method":"GET","path":"/v1/pjm/projects","params":{"page":1,"size":20}}'
python3 pingcode.py '{"method":"POST","path":"/v1/comments","body":{"principal_type":"work_item","principal_id":"xxx","content":"hello"}}'
```

## 参数

```json
{
  "method": "GET | POST | PUT | PATCH | DELETE",
  "path": "/v1/...",
  "params": {},
  "body": {}
}
```

| 字段 | 必填 | 说明 |
|------|------|------|
| `method` | ✅ | HTTP 方法 |
| `path` | ✅ | API 路径 |
| `params` | ❌ | URL 查询参数（GET/DELETE）|
| `body` | ❌ | 请求体（POST/PUT/PATCH）|

## 输出

```json
{
  "code": 200,
  "data": { ... },
  "rate_limit_remaining": 199
}
```

## 凭据

优先从环境变量读取，fallback 到 `.env` 文件：

```
PINGCODE_CLIENT_ID=xxx
PINGCODE_CLIENT_SECRET=xxx
PINGCODE_BASE_URL=https://open.pingcode.com
```

## 无 Python 环境？

直接用 curl 即可，参见 `auth/SKILL.md`。
