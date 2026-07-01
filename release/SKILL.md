---
name: pingcode-release
description: "构建记录、部署记录、发布版本、环境管理 — 交付与发布 相关的 PingCode REST API。需要查看具体接口参数时读取本目录 APIs.md。"
metadata:
  qwenpaw:
    emoji: "🚀"
    requires:
      env: ["PINGCODE_CLIENT_ID", "PINGCODE_CLIENT_SECRET"]
---

# 🚀 PingCode 交付与发布

## 概述

构建记录、部署记录、发布版本、环境管理

本模块包含 **42** 个 API 接口。

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
| `` | `环境` | 环境 |
| `` | `部署` | 部署 |
| `POST` | `/v1/pjm/projects/{project_id}/versions` | 创建一个发布 |
| `POST` | `/v1/pjm/projects/{project_id}/version_sections` | 创建一个发布分组 |
| `POST` | `/v1/pjm/projects/{project_id}/version_categories` | 创建一个发布类别 |
| `POST` | `/v1/pjm/stages` | 创建一个发布阶段 |
| `DELETE` | `/v1/pjm/projects/{project_id}/versions/{version_id}` | 删除一个发布 |
| `DELETE` | `/v1/pjm/projects/{project_id}/version_sections/{section_id}` | 删除一个发布分组 |
| `DELETE` | `/v1/pjm/projects/{project_id}/version_categories/{version_category_id}` | 删除一个发布类别 |
| `DELETE` | `/v1/pjm/stages/{stage_id}` | 删除一个发布阶段 |
| `POST` | `/v1/pjm/versions/bulk` | 批量创建发布 |
| `GET` | `/v1/pjm/projects/{project_id}/versions/{version_id}` | 获取一个发布 |
| `GET` | `/v1/pjm/projects/{project_id}/version_sections/{section_id}` | 获取一个发布分组 |
| `GET` | `/v1/pjm/projects/{project_id}/version_categories/{version_category_id}` | 获取一个发布类别 |
| `GET` | `/v1/pjm/stages/{stage_id}` | 获取一个发布阶段 |
| `GET` | `/v1/pjm/projects/{project_id}/version_sections` | 获取发布分组列表 |
| `GET` | `/v1/pjm/projects/{project_id}/versions` | 获取发布列表 |
| `GET` | `/v1/pjm/projects/{project_id}/version_categories` | 获取发布类别列表 |
| `GET` | `/v1/pjm/stages` | 获取发布阶段列表 |
| `PATCH` | `/v1/pjm/projects/{project_id}/versions/{version_id}` | 部分更新一个发布 |
| `PATCH` | `/v1/pjm/projects/{project_id}/version_sections/{section_id}` | 部分更新一个发布分组 |
| `PATCH` | `/v1/pjm/projects/{project_id}/version_categories/{version_category_id}` | 部分更新一个发布类别 |
| `PATCH` | `/v1/pjm/stages/{stage_id}` | 部分更新一个发布阶段 |
| `` | `构建记录` | 构建记录 |
| `PUT` | `/v1/build/builds/{build_id}` | 全量更新一条构建记录 |
| `POST` | `/v1/build/builds` | 创建一条构建记录 |
| `DEL` | `/v1/build/builds/{build_id}` | 删除一条构建记录 |
| `GET` | `/v1/build/builds/{build_id}` | 获取一个构建记录 |
| `GET` | `/v1/build/builds` | 获取构建记录列表 |
| `PATCH` | `/v1/build/builds/{build_id}` | 部分更新一条构建记录 |
| `PUT` | `/v1/release/environments/{env_id}` | 全量更新一个环境 |
| `POST` | `/v1/release/environments` | 创建一个环境 |
| `DELETE` | `/v1/release/environments/{env_id}` | 删除一个环境 |
| `GET` | `/v1/release/environments/{env_id}` | 获取一个环境 |
| `GET` | `/v1/release/environments` | 获取环境列表 |
| `PATCH` | `/v1/release/environments/{env_id}` | 部分更新一个环境 |
| `PUT` | `/v1/release/deploys/{deploy_id}` | 全量更新一个部署 |
| `POST` | `/v1/release/deploys` | 创建一个部署 |
| `DELETE` | `/v1/release/deploys/{deploy_id}` | 删除一个部署 |
| `GET` | `/v1/release/deploys/{deploy_id}` | 获取一个部署 |
| `GET` | `/v1/release/deploys` | 获取部署列表 |
| `PATCH` | `/v1/release/deploys/{deploy_id}` | 部分更新一个部署 |

## 详细参数

如需查看某个接口的完整参数表、请求体、返回字段，请阅读本目录的 **`APIs.md`**。

## 常用操作速查

- ** 环境**: `环境` — 
- ** 部署**: `部署` — 
- **POST 创建一个发布**: `/v1/pjm/projects/{project_id}/versions` — 用于创建一个发布。
- **POST 创建一个发布分组**: `/v1/pjm/projects/{project_id}/version_sections` — 用于创建一个发布分组。
- **POST 创建一个发布类别**: `/v1/pjm/projects/{project_id}/version_categories` — 用于创建一个发布类别。
- **POST 创建一个发布阶段**: `/v1/pjm/stages` — 用于创建一个发布阶段。
- **DELETE 删除一个发布**: `/v1/pjm/projects/{project_id}/versions/{version_id}` — 用于删除一个发布。
- **DELETE 删除一个发布分组**: `/v1/pjm/projects/{project_id}/version_sections/{section_id}` — 用于删除一个发布分组。
- **DELETE 删除一个发布类别**: `/v1/pjm/projects/{project_id}/version_categories/{version_category_id}` — 用于删除一个发布类别。
- **DELETE 删除一个发布阶段**: `/v1/pjm/stages/{stage_id}` — 用于删除一个发布阶段。
- ... 共 42 个接口，详见 `APIs.md`
