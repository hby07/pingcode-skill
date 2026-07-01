---
name: pingcode-plan
description: "迭代、计划、路线图 — 计划管理 相关的 PingCode REST API。需要查看具体接口参数时读取本目录 APIs.md。"
metadata:
  qwenpaw:
    emoji: "📅"
    requires:
      env: ["PINGCODE_CLIENT_ID", "PINGCODE_CLIENT_SECRET"]
---

# 📅 PingCode 计划管理

## 概述

迭代、计划、路线图

本模块包含 **34** 个 API 接口。

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
| `PUT` | `/v1/testhub/runs/{run_id}` | 全量更新一个执行用例 |
| `POST` | `/v1/testhub/runs` | 创建一个执行用例 |
| `POST` | `/v1/testhub/libraries/{library_id}/plans` | 创建一个计划 |
| `POST` | `/v1/testhub/runs/bulk` | 批量创建执行用例 |
| `POST` | `/v1/testhub/libraries/{library_id}/plans/{plan_id}/runs/bulk` | 批量操作执行用例 |
| `PATCH` | `/v1/testhub/runs/bulk` | 批量部分更新执行用例 |
| `GET` | `/v1/testhub/runs/{run_id}` | 获取一个执行用例 |
| `GET` | `/v1/testhub/libraries/{library_id}/plans/{plan_id}` | 获取一个计划 |
| `GET` | `/v1/testhub/libraries/{library_id}/plan_types/{plan_type_id}` | 获取一个计划类型 |
| `GET` | `/v1/testhub/runs/{run_id}/histories/{history_id}` | 获取一条执行用例的结果记录 |
| `GET` | `/v1/testhub/runs` | 获取执行用例列表 |
| `GET` | `/v1/testhub/run/statuses?library_id={library_id}` | 获取执行用例执行结果列表 |
| `GET` | `/v1/testhub/runs/{run_id}/histories` | 获取执行用例的结果记录列表 |
| `GET` | `/v1/testhub/libraries/{library_id}/plans` | 获取计划列表 |
| `GET` | `/v1/testhub/libraries/{library_id}/plan_types` | 获取计划类型列表 |
| `PATCH` | `/v1/testhub/runs/{run_id}` | 部分更新一个执行用例 |
| `PATCH` | `/v1/testhub/libraries/{library_id}/plans/{plan_id}` | 部分更新一个计划 |
| `GET` | `/v1/testhub/plan_states/{state_id}` | 获取一个计划状态 |
| `GET` | `/v1/testhub/plan_states` | 获取全部计划状态列表 |
| `POST` | `/v1/pjm/projects/{project_id}/sprints` | 创建一个迭代 |
| `POST` | `/v1/pjm/projects/{project_id}/sprint_sections` | 创建一个迭代分组 |
| `POST` | `/v1/pjm/projects/{project_id}/sprint_categories` | 创建一个迭代类别 |
| `DELETE` | `/v1/pjm/projects/{project_id}/sprint_sections/{section_id}` | 删除一个迭代分组 |
| `DELETE` | `/v1/pjm/projects/{project_id}/sprint_categories/{sprint_category_id}` | 删除一个迭代类别 |
| `POST` | `/v1/pjm/sprints/bulk` | 批量创建迭代 |
| `GET` | `/v1/pjm/projects/{project_id}/sprints/{sprint_id}` | 获取一个迭代 |
| `GET` | `/v1/pjm/projects/{project_id}/sprint_sections/{section_id}` | 获取一个迭代分组 |
| `GET` | `/v1/pjm/projects/{project_id}/sprint_categories/{sprint_category_id}` | 获取一个迭代类别 |
| `GET` | `/v1/pjm/projects/{project_id}/sprint_sections` | 获取迭代分组列表 |
| `GET` | `/v1/pjm/projects/{project_id}/sprints` | 获取迭代列表 |
| `GET` | `/v1/pjm/projects/{project_id}/sprint_categories` | 获取迭代类别列表 |
| `PATCH` | `/v1/pjm/projects/{project_id}/sprints/{sprint_id}` | 部分更新一个迭代 |
| `PATCH` | `/v1/pjm/projects/{project_id}/sprint_sections/{section_id}` | 部分更新一个迭代分组 |
| `PATCH` | `/v1/pjm/projects/{project_id}/sprint_categories/{sprint_category_id}` | 部分更新一个迭代类别 |

## 详细参数

如需查看某个接口的完整参数表、请求体、返回字段，请阅读本目录的 **`APIs.md`**。

## 常用操作速查

- **PUT 全量更新一个执行用例**: `/v1/testhub/runs/{run_id}` — 用于全量更新一个执行用例。
- **POST 创建一个执行用例**: `/v1/testhub/runs` — 用于创建一个执行用例。
- **POST 创建一个计划**: `/v1/testhub/libraries/{library_id}/plans` — 用于创建一个计划。
- **POST 批量创建执行用例**: `/v1/testhub/runs/bulk` — 用于批量创建执行用例。
- **POST 批量操作执行用例**: `/v1/testhub/libraries/{library_id}/plans/{plan_id}/runs/bulk` — 用于批量操作执行用例。
- **PATCH 批量部分更新执行用例**: `/v1/testhub/runs/bulk` — 用于批量部分更新执行用例。
- **GET 获取一个执行用例**: `/v1/testhub/runs/{run_id}` — 用于查看一个执行用例。
- **GET 获取一个计划**: `/v1/testhub/libraries/{library_id}/plans/{plan_id}` — 用于查看一个计划。
- **GET 获取一个计划类型**: `/v1/testhub/libraries/{library_id}/plan_types/{plan_type_id}` — 用于查看一个计划类型。
- **GET 获取一条执行用例的结果记录**: `/v1/testhub/runs/{run_id}/histories/{history_id}` — 用于查看一条执行用例结果记录。
- ... 共 34 个接口，详见 `APIs.md`
