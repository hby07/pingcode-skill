---
name: pingcode-workitem
description: "Use when reading or updating PingCode work items: requirements, tasks, bugs, comments, attachments, work logs, or item relationships."
metadata:
  qwenpaw:
    emoji: "📋"
    requires:
      env: ["PINGCODE_CLIENT_ID", "PINGCODE_CLIENT_SECRET"]
---

# 📋 工作项

需求、任务、缺陷、评论、附件、关注人、关联、活动记录、工时。**最常用的模块**，包含 **94** 个 API。

## 快速调用

```bash
# 获取工作项列表
curl -s -H "Authorization: Bearer $TOKEN" "https://open.pingcode.com/v1/pjm/work_items?project_id=xxx&page=1&size=30"

# 创建评论
curl -s -X POST -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" \
  -d '{"content":"实现完成，已提交 PR","principal_type":"pjm_work_item","principal_id":"xxx"}' \
  "https://open.pingcode.com/v1/comments"
```

## ⚠️ 注意事项

- 工作项类型（需求/任务/缺陷）通过 `work_item_type_id` 区分，先调 GET types 获取
- 更新工作项用 **PATCH**（部分更新），不要 PUT
- 评论通过 `principal_type` + `principal_id` 关联到工作项
- 分页参数 `size` 最大 100

## 本模块 API 列表

| 方法 | 路径 | 说明 |
|------|------|------|
| `POST` | `/v1/pjm/work_items` | 创建工作项 |
| `GET` | `/v1/pjm/work_items` | 获取工作项列表 |
| `GET` | `/v1/pjm/work_items/{id}` | 获取工作项详情 |
| `PATCH` | `/v1/pjm/work_items/{id}` | 更新工作项 |
| `DELETE` | `/v1/pjm/work_items/{id}` | 删除工作项 |
| `GET` | `/v1/pjm/work_item/types?project_id={id}` | 工作项类型列表 |
| `GET` | `/v1/pjm/work_item/states?project_id={id}&work_item_type_id={type}` | 工作项状态列表 |
| `POST` | `/v1/comments` | 创建评论 |
| `POST` | `/v1/attachments` | 上传附件 |
| `POST` | `/v1/workloads` | 创建工时 |
| … | … | 共 94 个接口，详见 `APIs.md` |

完整参数表见 `APIs.md`。