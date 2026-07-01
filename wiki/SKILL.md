---
name: pingcode-wiki
description: "知识空间、页面、评论、附件 — 知识库与文档 相关的 PingCode REST API。需要查看具体接口参数时读取本目录 APIs.md。"
metadata:
  qwenpaw:
    emoji: "📚"
    requires:
      env: ["PINGCODE_CLIENT_ID", "PINGCODE_CLIENT_SECRET"]
---

# 📚 PingCode 知识库与文档

## 概述

知识空间、页面、评论、附件

本模块包含 **21** 个 API 接口。

## 认证

从环境变量获取（与主模块共用）：

| 环境变量 | 说明 |
|----------|------|
| `PINGCODE_CLIENT_ID` | 应用 Client ID |
| `PINGCODE_CLIENT_SECRET` | 应用 Client Secret |
| `PINGCODE_BASE_URL` | API 根地址（可选，默认 `https://open.pingcode.com`）|

**认证流程：** 详见 `auth/SKILL.md`

## 调用方式

使用任意 HTTP 客户端，先获取 token，再调用 API：

**curl:**
```bash
curl -s -H "Authorization: Bearer $TOKEN" "https://open.pingcode.com/v1/myself"
```

**Python:**
```python
import urllib.request, json
req = urllib.request.Request(base_url + "/v1/myself")
req.add_header("Authorization", "Bearer " + token)
result = json.loads(urllib.request.urlopen(req).read())
```

**Go:**
```go
req, _ := http.NewRequest("GET", baseURL+"/v1/myself", nil)
req.Header.Set("Authorization", "Bearer "+token)
resp, _ := http.DefaultClient.Do(req)
```

或使用附带的 Python 便捷脚本：
```bash
python3 {{baseDir}}/../scripts/pingcode.py '{{"method":"GET","path":"/v1/myself"}}'
```

## 本模块 API 列表

| 方法 | 路径 | 说明 |
|------|------|------|
| `` | `空间` | 空间 |
| `` | `页面` | 页面 |
| `POST` | `/v1/wiki/spaces` | 创建一个空间 |
| `DELETE` | `/v1/wiki/spaces/{space_id}` | 删除一个空间 |
| `POST` | `/v1/wiki/spaces/{space_id}/members` | 向空间中添加一个成员 |
| `DELETE` | `/v1/wiki/spaces/{space_id}/members/{member_id}` | 在空间中移除一个成员 |
| `GET` | `/v1/wiki/spaces/{space_id}` | 获取一个空间 |
| `GET` | `/v1/wiki/spaces/{space_id}/members/{member_id}` | 获取空间中的一个成员 |
| `GET` | `/v1/wiki/spaces/{space_id}/members` | 获取空间中的成员列表 |
| `GET` | `/v1/wiki/spaces` | 获取空间列表 |
| `PATCH` | `/v1/wiki/spaces/{space_id}` | 部分更新一个空间 |
| `POST` | `/v1/wiki/pages` | 创建一个页面 |
| `DELETE` | `/v1/wiki/pages/{page_id}` | 删除一个页面 |
| `POST` | `/v1/wiki/pages/{page_id}/versions/{version_id}/restore` | 恢复一个页面到指定版本 |
| `PUT` | `/v1/wiki/pages/{page_id}/content` | 更新一个文档正文 |
| `GET` | `/v1/wiki/pages/{page_id}/content` | 获取一个文档正文 |
| `GET` | `/v1/wiki/pages/{page_id}` | 获取一个页面 |
| `GET` | `/v1/wiki/pages/{page_id}/versions/{version_id}` | 获取一个页面版本 |
| `GET` | `/v1/wiki/pages/{page_id}/versions` | 获取一个页面的版本列表 |
| `GET` | `/v1/wiki/pages` | 获取页面列表 |
| `PATCH` | `/v1/wiki/pages/{page_id}` | 部分更新一个页面 |

## 详细参数

如需查看某个接口的完整参数表、请求体、返回字段，请阅读本目录的 **`APIs.md`**。

## 常用操作速查

- ** 空间**: `空间` — 
- ** 页面**: `页面` — 
- **POST 创建一个空间**: `/v1/wiki/spaces` — 用于创建一个空间。   企业令牌不能创建`scope_type`为`user`类型的空间。
- **DELETE 删除一个空间**: `/v1/wiki/spaces/{space_id}` — 用于删除一个空间。
- **POST 向空间中添加一个成员**: `/v1/wiki/spaces/{space_id}/members` — 用于向空间中添加一个成员。
- **DELETE 在空间中移除一个成员**: `/v1/wiki/spaces/{space_id}/members/{member_id}` — 用于在空间中移除一个成员。
- **GET 获取一个空间**: `/v1/wiki/spaces/{space_id}` — 用于查看一个空间。
- **GET 获取空间中的一个成员**: `/v1/wiki/spaces/{space_id}/members/{member_id}` — 用于查看一个空间成员。
- **GET 获取空间中的成员列表**: `/v1/wiki/spaces/{space_id}/members` — 用于查询空间中的成员列表。
- **GET 获取空间列表**: `/v1/wiki/spaces` — 用于查询空间列表。
- ... 共 21 个接口，详见 `APIs.md`
