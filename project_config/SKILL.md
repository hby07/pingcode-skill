---
name: pingcode-project_config
description: "工作项/工单/用例/测试 字段、状态、类型配置，自定义实体 — 项目配置中心 相关的 PingCode REST API。需要查看具体接口参数时读取本目录 APIs.md。"
metadata:
  qwenpaw:
    emoji: "🔧"
    requires:
      env: ["PINGCODE_CLIENT_ID", "PINGCODE_CLIENT_SECRET"]
---

# 🔧 PingCode 项目配置中心

## 概述

工作项/工单/用例/测试 字段、状态、类型配置，自定义实体

本模块包含 **75** 个 API 接口。

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
| `POST` | `/v1/nexus/ces/insert` | 创建自定义实体 |
| `POST` | `/v1/nexus/ces/delete` | 删除自定义实体 |
| `POST` | `/v1/nexus/ces/find` | 查询自定义实体 |
| `POST` | `/v1/nexus/ces/count` | 获取自定义实体数量 |
| `POST` | `/v1/nexus/ces/update` | 部分更新自定义实体 |
| `` | `` | 交付 |
| `` | `` | 代码 |
| `` | `` | 构建 |
| `` | `CES` | CES |
| `` | `工单配置` | 工单配置 |
| `` | `工单配置` | 工单配置 |
| `` | `工单配置` | 工单配置 |
| `` | `工单配置` | 工单配置 |
| `` | `工单配置` | 工单配置 |
| `` | `工单配置` | 工单配置 |
| `` | `工单配置` | 工单配置 |
| `` | `工单配置` | 工单配置 |
| `` | `需求配置` | 需求配置 |
| `` | `需求配置` | 需求配置 |
| `` | `需求配置` | 需求配置 |
| `` | `需求配置` | 需求配置 |
| `POST` | `/v1/pjm/work_item_properties` | 创建一个工作项属性 |
| `POST` | `/v1/pjm/work_item_tags` | 创建一个工作项标签 |
| `POST` | `/v1/pjm/work_item_states` | 创建一个工作项状态 |
| `POST` | `/v1/pjm/work_item_types` | 创建一个工作项类型 |
| `DELETE` | `/v1/pjm/work_item_tags/{tag_id}` | 删除一个工作项标签 |
| `DELETE` | `/v1/pjm/work_item_types/{work_item_type_id}` | 删除一个工作项类型 |
| `POST` | `/v1/pjm/work_item_property_plans/{property_plan_id}/work_item_properties` | 向属性方案中添加一个工作项属性 |
| `POST` | `/v1/pjm/work_item_type_plans/{work_item_type_plan_id}/work_item_types` | 向工作项类型方案中添加一个工作项类型 |
| `POST` | `/v1/pjm/work_item_state_plans/{state_plan_id}/work_item_states` | 向状态方案中添加一个工作项状态 |
| `POST` | `/v1/pjm/work_item_state_plans/{state_plan_id}/work_item_state_flows` | 向状态方案中添加一个工作项状态流转 |
| `DELETE` | `/v1/pjm/work_item_property_plans/{property_plan_id}/work_item_properties/{property_id}` | 在属性方案中移除一个工作项属性 |
| `DELETE` | `/v1/pjm/work_item_type_plans/{work_item_type_plan_id}/work_item_types/{work_item_type_id}` | 在工作项类型方案中移除一个工作项类型 |
| `DELETE` | `/v1/pjm/work_item_state_plans/{state_plan_id}/work_item_states/{state_id}` | 在状态方案中移除一个工作项状态 |
| `DELETE` | `/v1/pjm/work_item_state_plans/{state_plan_id}/work_item_state_flows/{flow_id}` | 在状态方案中移除一个工作项状态流转 |
| `GET` | `/v1/pjm/work_item_priorities/{priority_id}` | 获取一个工作项优先级 |
| `GET` | `/v1/pjm/work_item_properties/{property_id}` | 获取一个工作项属性 |
| `GET` | `/v1/pjm/work_item_property_plans/{property_plan_id}` | 获取一个工作项属性方案 |
| `GET` | `/v1/pjm/work_item_tags/{tag_id}` | 获取一个工作项标签 |
| `GET` | `/v1/pjm/work_item_states/{state_id}` | 获取一个工作项状态 |
| `GET` | `/v1/pjm/work_item_state_plans/{state_plan_id}` | 获取一个工作项状态方案 |
| `GET` | `/v1/pjm/work_item_types/{work_item_type_id}` | 获取一个工作项类型 |
| `GET` | `/v1/pjm/work_item_type_plans/{work_item_type_plan_id}` | 获取一个工作项类型方案 |
| `GET` | `/v1/pjm/work_item_state_plans/{state_plan_id}/work_item_states/{state_id}` | 获取一个状态方案中的工作项状态 |
| `GET` | `/v1/pjm/work_item_properties` | 获取全部工作项属性列表 |
| `GET` | `/v1/pjm/work_item_tags` | 获取全部工作项标签列表 |
| `GET` | `/v1/pjm/work_item_states` | 获取全部工作项状态列表 |
| `GET` | `/v1/pjm/work_item_types` | 获取全部工作项类型列表 |
| `GET` | `/v1/pjm/work_item_property_plans/{property_plan_id}/work_item_properties/{property_id}` | 获取属性方案中的一个工作项属性 |
| `GET` | `/v1/pjm/work_item_property_plans/{property_plan_id}/work_item_properties` | 获取属性方案中的工作项属性列表 |
| `GET` | `/v1/pjm/work_item_property_plans` | 获取工作项属性方案列表 |
| `GET` | `/v1/pjm/work_item_state_plans` | 获取工作项状态方案列表 |
| `GET` | `/v1/pjm/work_item_type_plans/{work_item_type_plan_id}/work_item_types/{work_item_type_id}` | 获取工作项类型方案中的一个工作项类型 |
| `GET` | `/v1/pjm/work_item_type_plans/{work_item_type_plan_id}/work_item_types` | 获取工作项类型方案中的工作项类型列表 |
| `GET` | `/v1/pjm/work_item_type_plans` | 获取工作项类型方案列表 |
| `GET` | `/v1/pjm/work_item_state_plans/{state_plan_id}/work_item_state_flows/{flow_id}` | 获取状态方案中的一个工作项状态流转 |
| `GET` | `/v1/pjm/work_item_state_plans/{state_plan_id}/work_item_states` | 获取状态方案中的工作项状态列表 |
| `GET` | `/v1/pjm/work_item_state_plans/{state_plan_id}/work_item_state_flows` | 获取状态方案中的工作项状态流转列表 |
| `PATCH` | `/v1/pjm/work_item_properties/{property_id}` | 部分更新一个工作项属性 |
| `PATCH` | `/v1/pjm/work_item_tags/{tag_id}` | 部分更新一个工作项标签 |
| `PATCH` | `/v1/pjm/work_item_states/{state_id}` | 部分更新一个工作项状态 |
| `PATCH` | `/v1/pjm/work_item_types/{work_item_type_id}` | 部分更新一个工作项类型 |
| `PATCH` | `/v1/pjm/work_item_type_plans/{work_item_type_plan_id}/work_item_types/{work_item_type_id}` | 部分更新工作项类型方案中的工作项类型 |
| `` | `工作项配置` | 工作项配置 |
| `` | `工作项配置` | 工作项配置 |
| `` | `工作项配置` | 工作项配置 |
| `` | `工作项配置` | 工作项配置 |
| `` | `工作项配置` | 工作项配置 |
| `` | `工作项配置` | 工作项配置 |
| `` | `工作项配置` | 工作项配置 |
| `` | `工作项配置` | 工作项配置 |
| `` | `工作项配置` | 工作项配置 |
| `` | `项目配置` | 项目配置 |
| `` | `项目配置` | 项目配置 |
| `` | `项目配置` | 项目配置 |

## 详细参数

如需查看某个接口的完整参数表、请求体、返回字段，请阅读本目录的 **`APIs.md`**。

## 常用操作速查

- **POST 创建自定义实体**: `/v1/nexus/ces/insert` — 用于创建自定义实体。
- **POST 删除自定义实体**: `/v1/nexus/ces/delete` — 用于删除自定义实体。
- **POST 查询自定义实体**: `/v1/nexus/ces/find` — 用于查询自定义实体。
- **POST 获取自定义实体数量**: `/v1/nexus/ces/count` — 用于获取自定义实体数量。
- **POST 部分更新自定义实体**: `/v1/nexus/ces/update` — 用于部分更新自定义实体。
- ** 交付**: `` — 
- ** 代码**: `` — 
- ** 构建**: `` — 
- ** CES**: `CES` — 用于查看和管理 CES 相关信息。
- ** 工单配置**: `工单配置` — 
- ... 共 75 个接口，详见 `APIs.md`
