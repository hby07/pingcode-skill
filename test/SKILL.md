---
name: pingcode-test
description: "测试库、用例、用例执行、执行用例配置、测试管理、测试配置中心 — 测试管理 相关的 PingCode REST API。需要查看具体接口参数时读取本目录 APIs.md。"
metadata:
  qwenpaw:
    emoji: "🧪"
    requires:
      env: ["PINGCODE_CLIENT_ID", "PINGCODE_CLIENT_SECRET"]
---

# 🧪 PingCode 测试管理

## 概述

测试库、用例、用例执行、执行用例配置、测试管理、测试配置中心

本模块包含 **70** 个 API 接口。

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
| `GET` | `/v1/testhub/run_statuses/{status_id}` | 获取一个执行用例执行结果 |
| `GET` | `/v1/testhub/run_statuses` | 获取全部执行用例执行结果列表 |
| `POST` | `/v1/testhub/libraries` | 创建一个测试库 |
| `POST` | `/v1/testhub/libraries/{library_id}/members` | 向测试库中添加一个成员 |
| `POST` | `/v1/testhub/libraries/{library_id}/suites` | 向测试库中添加一个用例模块 |
| `DELETE` | `/v1/testhub/libraries/{library_id}/members/{member_id}` | 在测试库中移除一个成员 |
| `DELETE` | `/v1/testhub/libraries/{library_id}/suites/{suite_id}` | 在测试库中移除一个用例模块 |
| `GET` | `/v1/testhub/libraries/{library_id}` | 获取一个测试库 |
| `GET` | `/v1/testhub/libraries/{library_id}/members/{member_id}` | 获取测试库中的一个成员 |
| `GET` | `/v1/testhub/libraries/{library_id}/suites/{suite_id}` | 获取测试库中的一个用例模块 |
| `GET` | `/v1/testhub/libraries/{library_id}/members` | 获取测试库中的成员列表 |
| `GET` | `/v1/testhub/libraries/{library_id}/suites` | 获取测试库中的用例模块列表 |
| `GET` | `/v1/testhub/libraries` | 获取测试库列表 |
| `PATCH` | `/v1/testhub/libraries/{library_id}` | 部分更新一个测试库 |
| `PATCH` | `/v1/testhub/libraries/{library_id}/suites/{suite_id}` | 部分更新一个测试库中用例模块 |
| `PATCH` | `/v1/testhub/libraries/{library_id}/members/{member_id}` | 部分更新一个测试库内的成员 |
| `` | `测试库` | 测试库 |
| `` | `测试库` | 测试库 |
| `` | `测试库` | 测试库 |
| `` | `测试配置中心` | 测试配置中心 |
| `` | `用例` | 用例 |
| `` | `用例` | 用例 |
| `` | `用例` | 用例 |
| `` | `用例` | 用例 |
| `` | `用例` | 用例 |
| `` | `用例` | 用例 |
| `` | `计划` | 计划 |
| `` | `计划` | 计划 |
| `` | `计划` | 计划 |
| `` | `计划` | 计划 |
| `` | `计划` | 计划 |
| `` | `计划` | 计划 |
| `` | `执行用例配置` | 执行用例配置 |
| `` | `执行用例配置` | 执行用例配置 |
| `` | `用例配置` | 用例配置 |
| `` | `用例配置` | 用例配置 |
| `` | `用例配置` | 用例配置 |
| `` | `用例配置` | 用例配置 |
| `` | `用例配置` | 用例配置 |
| `` | `用例配置` | 用例配置 |
| `` | `计划配置` | 计划配置 |
| `` | `计划配置` | 计划配置 |
| `POST` | `/v1/testhub/cases` | 创建一个用例 |
| `DELETE` | `/v1/testhub/cases/{case_id}` | 删除一个用例 |
| `POST` | `/v1/testhub/cases/bulk` | 批量创建用例 |
| `PATCH` | `/v1/testhub/cases/bulk` | 批量部分更新用例 |
| `GET` | `/v1/testhub/cases/{case_id}` | 获取一个用例 |
| `GET` | `/v1/testhub/cases` | 获取用例列表 |
| `GET` | `/v1/testhub/case/properties?library_id={library_id}` | 获取用例属性列表 |
| `GET` | `/v1/testhub/case/suites?library_id={library_id}` | 获取用例模块列表 |
| `GET` | `/v1/testhub/case/states?library_id={library_id}` | 获取用例状态列表 |
| `GET` | `/v1/testhub/cases/{case_id}/histories` | 获取用例的执行历史列表 |
| `GET` | `/v1/testhub/case/types?library_id={library_id}` | 获取用例类型列表 |
| `PATCH` | `/v1/testhub/cases/{case_id}` | 部分更新一个用例 |
| `POST` | `/v1/testhub/case_properties` | 创建一个用例属性 |
| `POST` | `/v1/testhub/case_property_plans/{property_plan_id}/case_properties` | 向属性方案中添加一个用例属性 |
| `DELETE` | `/v1/testhub/case_property_plans/{property_plan_id}/case_properties/{property_id}` | 在属性方案中移除一个用例属性 |
| `GET` | `/v1/testhub/case_properties/{property_id}` | 获取一个用例属性 |
| `GET` | `/v1/testhub/case_property_plans/{property_plan_id}` | 获取一个用例属性方案 |
| `GET` | `/v1/testhub/case_states/{state_id}` | 获取一个用例状态 |
| `GET` | `/v1/testhub/case_types/{type_id}` | 获取一个用例类型 |
| `GET` | `/v1/testhub/case_important_levels/{important_level_id}` | 获取一个用例重要程度 |
| `GET` | `/v1/testhub/case_properties` | 获取全部用例属性列表 |
| `GET` | `/v1/testhub/case_states` | 获取全部用例状态列表 |
| `GET` | `/v1/testhub/case_types` | 获取全部用例类型列表 |
| `GET` | `/v1/testhub/case_important_levels` | 获取全部重要程度列表 |
| `GET` | `/v1/testhub/case_property_plans/{property_plan_id}/case_properties/{property_id}` | 获取属性方案中的一个用例属性 |
| `GET` | `/v1/testhub/case_property_plans/{property_plan_id}/case_properties` | 获取属性方案中的用例属性列表 |
| `GET` | `/v1/testhub/case_property_plans` | 获取用例属性方案列表 |
| `PATCH` | `/v1/testhub/case_properties/{property_id}` | 部分更新一个用例属性 |

## 详细参数

如需查看某个接口的完整参数表、请求体、返回字段，请阅读本目录的 **`APIs.md`**。

## 常用操作速查

- **GET 获取一个执行用例执行结果**: `/v1/testhub/run_statuses/{status_id}` — 用于查看一个执行用例执行结果。
- **GET 获取全部执行用例执行结果列表**: `/v1/testhub/run_statuses` — 用于查询全部执行用例执行结果列表。
- **POST 创建一个测试库**: `/v1/testhub/libraries` — 用于创建一个测试库。
- **POST 向测试库中添加一个成员**: `/v1/testhub/libraries/{library_id}/members` — 用于向测试库中添加一个成员。
- **POST 向测试库中添加一个用例模块**: `/v1/testhub/libraries/{library_id}/suites` — 用于向测试库中添加一个用例模块。
- **DELETE 在测试库中移除一个成员**: `/v1/testhub/libraries/{library_id}/members/{member_id}` — 用于在测试库中移除一个成员。
- **DELETE 在测试库中移除一个用例模块**: `/v1/testhub/libraries/{library_id}/suites/{suite_id}` — 用于在测试库中移除一个用例模块。  请注意，删除一个模块会自动删除其所有的子模块。
- **GET 获取一个测试库**: `/v1/testhub/libraries/{library_id}` — 用于查看一个测试库。
- **GET 获取测试库中的一个成员**: `/v1/testhub/libraries/{library_id}/members/{member_id}` — 用于查看一个测试库成员。
- **GET 获取测试库中的一个用例模块**: `/v1/testhub/libraries/{library_id}/suites/{suite_id}` — 用于查看一个用例模块。
- ... 共 70 个接口，详见 `APIs.md`
