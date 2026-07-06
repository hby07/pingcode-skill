---
name: pingcode-project_config
description: "Use when customizing PingCode project configurations: custom fields, workflow states, work item types, or entity configurations."
metadata:
  qwenpaw:
    emoji: "🔧"
    requires:
      env: ["PINGCODE_CLIENT_ID", "PINGCODE_CLIENT_SECRET"]
---

# 🔧 项目配置中心

工作项/工单/用例/测试 字段、状态、类型配置，自定义实体。本模块包含 **75** 个 API。

## 快速调用

```bash
# 获取项目的自定义字段
curl -s -H "Authorization: Bearer $TOKEN" "https://open.pingcode.com/v1/pjm/work_item/properties?project_id=xxx&work_item_type_id=yyy"
```

## ⚠️ 注意事项

- 读取配置时先确定 `project_id` + `work_item_type_id`
- 自定义字段的 `property_id` 在创建/更新工作项时传入

## 本模块 API 列表

| 方法 | 路径 | 说明 |
|------|------|------|
| `GET` | `/v1/pjm/work_item/properties?project_id={id}&work_item_type_id={type}` | 工作项属性列表 |
| `GET` | `/v1/pjm/work_item/states?project_id={id}&work_item_type_id={type}` | 工作项状态列表 |
| `GET` | `/v1/pjm/work_item/types?project_id={id}` | 工作项类型列表 |
| `GET` | `/v1/pjm/work_item/tags` | 标签列表 |
| … | … | 共 75 个接口，详见 `APIs.md` |

完整参数表见 `APIs.md`。