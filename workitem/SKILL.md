---
name: pingcode-workitem
description: "需求、任务、缺陷、迭代工作项、评论、附件、关注人、关联、活动记录、工时 — 工作项 相关的 PingCode REST API。需要查看具体接口参数时读取本目录 APIs.md。"
metadata:
  qwenpaw:
    emoji: "📋"
    requires:
      env: ["PINGCODE_CLIENT_ID", "PINGCODE_CLIENT_SECRET"]
---

# 📋 PingCode 工作项

## 概述

需求、任务、缺陷、迭代工作项、评论、附件、关注人、关联、活动记录、工时

本模块包含 **94** 个 API 接口。

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
| `POST` | `/v1/participants` | 添加一个关注人 |
| `DELETE` | `/v1/participants/{participant_id}?principal_type={principal_type}&principal_id={principal_id}` | 移除一个关注人 |
| `GET` | `/v1/participants/{participant_id}` | 获取一个关注人 |
| `GET` | `/v1/participants?principal_type={principal_type}&principal_id={principal_id}` | 获取关注人列表 |
| `POST` | `/v1/relations` | 创建一个关联 |
| `DELETE` | `/v1/relations/{relation_id}` | 删除一个关联 |
| `GET` | `/v1/relations/{relation_id}` | 获取一个关联 |
| `GET` | `/v1/relations?principal_type={principal_type}&principal_id={principal_id}&target_type={target_type}` | 获取关联列表 |
| `POST` | `/v1/pjm/work_items/{work_item_id}/relations` | 关联一个工作项 |
| `POST` | `/v1/pjm/work_items` | 创建一个工作项 |
| `POST` | `/v1/pjm/deliverables` | 创建一个工作项交付目标 |
| `DELETE` | `/v1/pjm/work_items/{work_item_id}` | 删除一个工作项 |
| `DELETE` | `/v1/pjm/deliverables/{deliverable_target_id}` | 删除一个工作项交付目标 |
| `DELETE` | `/v1/pjm/work_items/{work_item_id}/relations/{relation_id}` | 取消关联一个工作项 |
| `POST` | `/v1/pjm/work_items/{work_item_id}/tags` | 向工作项中添加一个标签 |
| `DELETE` | `/v1/pjm/work_items/{work_item_id}/tags/{tag_id}` | 在工作项中移除一个标签 |
| `PATCH` | `/v1/pjm/work_items` | 批量部分更新工作项属性 |
| `GET` | `/v1/pjm/work_items/{work_item_id}` | 获取一个工作项 |
| `GET` | `/v1/pjm/deliverables/{deliverable_target_id}` | 获取一个工作项交付目标 |
| `GET` | `/v1/pjm/work_items/{work_item_id}/relations/{relation_id}` | 获取一个工作项关联 |
| `GET` | `/v1/pjm/work_item_relation_types/{relation_type_id}` | 获取一个工作项关联类型 |
| `GET` | `/v1/pjm/work_items/{work_item_id}/transition_histories/{transition_history_id}` | 获取一个工作项流转记录 |
| `GET` | `/v1/pjm/work_items/{work_item_id}/relations` | 获取关联的工作项列表 |
| `GET` | `/v1/pjm/work_items/{work_item_id}/tags/{tag_id}` | 获取工作项中的一个标签 |
| `GET` | `/v1/pjm/deliverables` | 获取工作项交付目标列表 |
| `GET` | `/v1/pjm/work_item/priorities?project_id={project_id}` | 获取工作项优先级列表 |
| `GET` | `/v1/pjm/work_item/relation_types` | 获取工作项关联类型列表 |
| `GET` | `/v1/pjm/work_items` | 获取工作项列表 |
| `GET` | `/v1/pjm/work_item/properties?project_id={project_id}&work_item_type_id={work_item_type_id}` | 获取工作项属性列表 |
| `GET` | `/v1/pjm/work_item/tags` | 获取工作项标签列表 |
| `GET` | `/v1/pjm/work_items/{work_item_id}/transition_histories` | 获取工作项流转记录列表 |
| `GET` | `/v1/pjm/work_item/states?project_id={project_id}&work_item_type_id={work_item_type_id}` | 获取工作项状态列表 |
| `GET` | `/v1/pjm/work_item/types?project_id={project_id}` | 获取工作项类型列表 |
| `PATCH` | `/v1/pjm/work_items/{work_item_id}` | 部分更新一个工作项 |
| `PATCH` | `/v1/pjm/deliverables/{deliverable_target_id}` | 部分更新一个工作项交付目标 |
| `POST` | `/v1/workloads` | 创建一个工时 |
| `DELETE` | `/v1/workloads/{workload_id}` | 删除一个工时 |
| `GET` | `/v1/workloads/{workload_id}` | 获取一个工时 |
| `GET` | `/v1/workload_types/{type_id}` | 获取一个工时类型 |
| `GET` | `/v1/workloads` | 获取工时列表 |
| `GET` | `/v1/workload_types` | 获取工时类型列表 |
| `PATCH` | `/v1/workloads/{workload_id}` | 部分更新一个工时 |
| `GET` | `/v1/activities/{activity_id}` | 获取一个活动记录 |
| `GET` | `/v1/activities?principal_type={principal_type}&principal_id={principal_id}` | 获取活动记录列表 |
| `POST` | `/v1/reviews` | 创建一个评审 |
| `DELETE` | `/v1/reviews/{review_id}?principal_type={principal_type}` | 删除一个评审 |
| `POST` | `/v1/reviews/{review_id}/principals` | 向评审中添加一个评审内容 |
| `DELETE` | `/v1/reviews/{review_id}/principals/{principal_id}?principal_type={principal_type}` | 在评审中移除一个评审内容 |
| `GET` | `/v1/reviews/{review_id}` | 获取一个评审 |
| `GET` | `/v1/reviews/{review_id}/principals/{principal_id}?principal_type={principal_type}` | 获取一个评审内容 |
| `GET` | `/v1/reviews/{review_id}/principals?principal_type={principal_type}` | 获取评审内容列表 |
| `GET` | `/v1/reviews?principal_type={principal_type}&pilot_id={pilot_id}` | 获取评审列表 |
| `POST` | `/v1/comments` | 创建一个评论 |
| `DELETE` | `/v1/comments/{comment_id}?principal_type={principal_type}&principal_id={principal_id}` | 删除一个评论 |
| `GET` | `/v1/comments/{comment_id}` | 获取一个评论 |
| `GET` | `/v1/comments?principal_type={principal_type}&principal_id={principal_id}` | 获取评论列表 |
| `` | `关注人` | 关注人 |
| `` | `关联` | 关联 |
| `` | `活动记录` | 活动记录 |
| `` | `评审` | 评审 |
| `` | `评论` | 评论 |
| `` | `附件` | 附件 |
| `POST` | `/v1/attachments` | 上传一个代码段 |
| `POST` | `/v1/attachments?principal_type={principal_type}&principal_id={principal_id}` | 上传一个文件 |
| `DELETE` | `/v1/attachments/{attachment_id}?principal_type={principal_type}&principal_id={principal_id}` | 删除一个附件 |
| `GET` | `/v1/attachments/{attachment_id}` | 获取一个附件 |
| `GET` | `/v1/attachments?principal_type={principal_type}&principal_id={principal_id}` | 获取附件列表 |
| `POST` | `/v1/ship/ideas` | 创建一个需求 |
| `GET` | `/v1/ship/ideas/{idea_id}` | 获取一个需求 |
| `GET` | `/v1/ship/ideas/{idea_id}/transition_histories/{transition_history_id}` | 获取一条需求流转记录 |
| `GET` | `/v1/ship/idea/priorities?product_id={product_id}` | 获取需求优先级列表 |
| `GET` | `/v1/ship/ideas` | 获取需求列表 |
| `GET` | `/v1/ship/idea/properties?product_id={product_id}` | 获取需求属性列表 |
| `GET` | `/v1/ship/idea/plans?product_id={product_id}` | 获取需求排期列表 |
| `GET` | `/v1/ship/idea/suites?product_id={product_id}` | 获取需求模块列表 |
| `GET` | `/v1/ship/ideas/{idea_id}/transition_histories` | 获取需求流转记录列表 |
| `GET` | `/v1/ship/idea/states?product_id={product_id}` | 获取需求状态列表 |
| `PATCH` | `/v1/ship/ideas/{idea_id}` | 部分更新一个需求 |
| `POST` | `/v1/ship/idea_properties` | 创建一个需求属性 |
| `POST` | `/v1/ship/idea_property_plans/{property_plan_id}/idea_properties` | 向需求属性方案中添加一个需求属性 |
| `DELETE` | `/v1/ship/idea_property_plans/{property_plan_id}/idea_properties/{property_id}` | 在需求属性方案中移除一个需求属性 |
| `GET` | `/v1/ship/idea_priorities/{priority_id}` | 获取一个需求优先级 |
| `GET` | `/v1/ship/idea_properties/{property_id}` | 获取一个需求属性 |
| `GET` | `/v1/ship/idea_property_plans/{property_plan_id}` | 获取一个需求属性方案 |
| `GET` | `/v1/ship/idea_states/{idea_state_id}` | 获取一个需求状态 |
| `GET` | `/v1/ship/idea_priorities` | 获取全部需求优先级列表 |
| `GET` | `/v1/ship/idea_properties` | 获取全部需求属性列表 |
| `GET` | `/v1/ship/idea_states` | 获取全部需求状态列表 |
| `GET` | `/v1/ship/idea_property_plans/{property_plan_id}/idea_properties/{property_id}` | 获取需求属性方案中的一个需求属性 |
| `GET` | `/v1/ship/idea_property_plans/{property_plan_id}/idea_properties` | 获取需求属性方案中的需求属性列表 |
| `GET` | `/v1/ship/idea_property_plans` | 获取需求属性方案列表 |
| `PATCH` | `/v1/ship/idea_properties/{property_id}` | 部分更新一个需求属性 |
| `` | `需求模块` | 需求模块 |
| `` | `需求流转记录` | 需求流转记录 |

## 详细参数

如需查看某个接口的完整参数表、请求体、返回字段，请阅读本目录的 **`APIs.md`**。

## 常用操作速查

- **POST 添加一个关注人**: `/v1/participants` — 用于添加一个关注人。
- **DELETE 移除一个关注人**: `/v1/participants/{participant_id}?principal_type={principal_type}&principal_id={principal_id}` — 用于移除一个关注人。
- **GET 获取一个关注人**: `/v1/participants/{participant_id}` — 用于查看一个关注人。
- **GET 获取关注人列表**: `/v1/participants?principal_type={principal_type}&principal_id={principal_id}` — 用于查询关注人列表。
- **POST 创建一个关联**: `/v1/relations` — 用于创建一个关联。
- **DELETE 删除一个关联**: `/v1/relations/{relation_id}` — 用于删除一个关联。
- **GET 获取一个关联**: `/v1/relations/{relation_id}` — 用于查看一个关联。
- **GET 获取关联列表**: `/v1/relations?principal_type={principal_type}&principal_id={principal_id}&target_type={target_type}` — 用于查询关联列表。
- **POST 关联一个工作项**: `/v1/pjm/work_items/{work_item_id}/relations` — 用于关联一个工作项。
- **POST 创建一个工作项**: `/v1/pjm/work_items` — 用于创建一个工作项。
- ... 共 94 个接口，详见 `APIs.md`
