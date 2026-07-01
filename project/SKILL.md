---
name: pingcode-project
description: "项目、项目看板、项目配置 — 项目管理 相关的 PingCode REST API。需要查看具体接口参数时读取本目录 APIs.md。"
metadata:
  qwenpaw:
    emoji: "⚙️"
    requires:
      env: ["PINGCODE_CLIENT_ID", "PINGCODE_CLIENT_SECRET"]
---

# ⚙️ PingCode 项目管理

## 概述

项目、项目看板、项目配置

本模块包含 **45** 个 API 接口。

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
| `POST` | `/v1/pjm/projects/{project_id}/boards/{board_id}/swimlanes` | 创建一个泳道 |
| `POST` | `/v1/pjm/projects/{project_id}/boards` | 创建一个看板 |
| `POST` | `/v1/pjm/projects/{project_id}/boards/{board_id}/entries` | 创建一个看板栏 |
| `DELETE` | `/v1/pjm/projects/{project_id}/boards/{board_id}/swimlanes/{swimlane_id}` | 删除一个泳道 |
| `DELETE` | `/v1/pjm/projects/{project_id}/boards/{board_id}` | 删除一个看板 |
| `DELETE` | `/v1/pjm/projects/{project_id}/boards/{board_id}/entries/{entry_id}` | 删除一个看板栏 |
| `GET` | `/v1/pjm/projects/{project_id}/boards/{board_id}/swimlanes/{swimlane_id}` | 获取一个泳道 |
| `GET` | `/v1/pjm/projects/{project_id}/boards/{board_id}` | 获取一个看板 |
| `GET` | `/v1/pjm/projects/{project_id}/boards/{board_id}/entries/{entry_id}` | 获取一个看板栏 |
| `GET` | `/v1/pjm/projects/{project_id}/boards/{board_id}/swimlanes` | 获取泳道列表 |
| `GET` | `/v1/pjm/projects/{project_id}/boards` | 获取看板列表 |
| `GET` | `/v1/pjm/projects/{project_id}/boards/{board_id}/entries` | 获取看板栏列表 |
| `PATCH` | `/v1/pjm/projects/{project_id}/boards/{board_id}/swimlanes/{swimlane_id}` | 部分更新一个泳道 |
| `PATCH` | `/v1/pjm/projects/{project_id}/boards/{board_id}` | 部分更新一个看板 |
| `PATCH` | `/v1/pjm/projects/{project_id}/boards/{board_id}/entries/{entry_id}` | 部分更新一个看板栏 |
| `POST` | `/v1/pjm/projects` | 创建一个项目 |
| `POST` | `/v1/pjm/projects/{project_id}/members` | 向项目中添加一个成员 |
| `POST` | `/v1/pjm/projects/{project_id}/project_properties` | 向项目中添加一个项目属性 |
| `DELETE` | `/v1/pjm/projects/{project_id}/members/{member_id}` | 在项目中移除一个成员 |
| `DELETE` | `/v1/pjm/projects/{project_id}/project_properties/{property_id}` | 在项目中移除一个项目属性 |
| `POST` | `/v1/pjm/projects/{project_id}/clone` | 复制一个项目 |
| `POST` | `/v1/pjm/projects/{project_id}/local_config/enable` | 开启项目本地配置 |
| `` | `发布` | 发布 |
| `` | `工作项` | 工作项 |
| `` | `看板` | 看板 |
| `` | `迭代` | 迭代 |
| `` | `项目` | 项目 |
| `` | `` | 项目配置中心 |
| `GET` | `/v1/pjm/projects/{project_id}` | 获取一个项目 |
| `GET` | `/v1/pjm/projects/{project_id}/progress` | 获取一个项目进度 |
| `GET` | `/v1/pjm/projects/{project_id}/members/{member_id}` | 获取项目中的一个成员 |
| `GET` | `/v1/pjm/projects/{project_id}/project_properties/{property_id}` | 获取项目中的一个项目属性 |
| `GET` | `/v1/pjm/projects/{project_id}/members` | 获取项目中的成员列表 |
| `GET` | `/v1/pjm/projects/{project_id}/project_properties` | 获取项目中的项目属性列表 |
| `GET` | `/v1/pjm/projects` | 获取项目列表 |
| `GET` | `/v1/pjm/project/states?project_id={project_id}` | 获取项目状态列表 |
| `PATCH` | `/v1/pjm/projects/{project_id}` | 部分更新一个项目 |
| `PATCH` | `/v1/pjm/projects/{project_id}/members/{member_id}` | 部分更新一个项目内的成员 |
| `POST` | `/v1/pjm/project_properties` | 创建一个项目属性 |
| `GET` | `/v1/pjm/project_properties/{property_id}` | 获取一个项目属性 |
| `GET` | `/v1/pjm/processes/{process_id}` | 获取一个项目流程 |
| `GET` | `/v1/pjm/project_states/{state_id}` | 获取一个项目状态 |
| `GET` | `/v1/pjm/processes` | 获取全部项目流程 |
| `GET` | `/v1/pjm/project_properties` | 获取项目属性列表 |
| `PATCH` | `/v1/pjm/project_properties/{property_id}` | 部分更新一个项目属性 |

## 详细参数

如需查看某个接口的完整参数表、请求体、返回字段，请阅读本目录的 **`APIs.md`**。

## 常用操作速查

- **POST 创建一个泳道**: `/v1/pjm/projects/{project_id}/boards/{board_id}/swimlanes` — 用于创建一个泳道。
- **POST 创建一个看板**: `/v1/pjm/projects/{project_id}/boards` — 用于创建一个看板。
- **POST 创建一个看板栏**: `/v1/pjm/projects/{project_id}/boards/{board_id}/entries` — 用于创建一个看板栏。
- **DELETE 删除一个泳道**: `/v1/pjm/projects/{project_id}/boards/{board_id}/swimlanes/{swimlane_id}` — 用于删除一个泳道。
- **DELETE 删除一个看板**: `/v1/pjm/projects/{project_id}/boards/{board_id}` — 用于删除一个看板。
- **DELETE 删除一个看板栏**: `/v1/pjm/projects/{project_id}/boards/{board_id}/entries/{entry_id}` — 用于删除一个看板栏。
- **GET 获取一个泳道**: `/v1/pjm/projects/{project_id}/boards/{board_id}/swimlanes/{swimlane_id}` — 用于获取一个泳道。
- **GET 获取一个看板**: `/v1/pjm/projects/{project_id}/boards/{board_id}` — 用于查看一个看板。
- **GET 获取一个看板栏**: `/v1/pjm/projects/{project_id}/boards/{board_id}/entries/{entry_id}` — 用于获取一个看板栏。
- **GET 获取泳道列表**: `/v1/pjm/projects/{project_id}/boards/{board_id}/swimlanes` — 用于查询泳道列表。
- ... 共 45 个接口，详见 `APIs.md`
