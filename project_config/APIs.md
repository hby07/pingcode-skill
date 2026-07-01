# 🔧 项目配置中心 — API 详细文档

> 本文档包含 75 个接口的完整参数说明。
> 来源: https://open.pingcode.com/

---

## CES

### `POST` 创建自定义实体

**路径:** `/v1/nexus/ces/insert`

用于创建自定义实体。

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `entity_name` | String | 是 | 自定义实体的名字。 |
| `value` | Object[] | 是 | 自定义实体的值。 |
| `options` | Object | 否 | 创建的可选参数。 |
| `options.ordered` | Boolean | 否 | 是否按顺序插入，默认值为 false。 |

**权限:** 企业令牌

---
### `POST` 删除自定义实体

**路径:** `/v1/nexus/ces/delete`

用于删除自定义实体。

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `entity_name` | String | 是 | 自定义实体的名字。 |
| `condition` | Object | 是 | 查询条件。 |

**权限:** 企业令牌

---
### `POST` 查询自定义实体

**路径:** `/v1/nexus/ces/find`

用于查询自定义实体。

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `entity_name` | String | 是 | 自定义实体的名字。 |
| `condition` | Object | 是 | 查询条件。 |
| `options` | Object | 否 | 查询的可选参数。 |
| `options.skip` | Number | 否 | 跳过的数据条数（用于分页）。 |
| `options.limit` | Number | 否 | 返回的最大数据条数（用于分页）。 |
| `options.sort` | Object[] | 否 | 排序配置。 |
| `options.sort.property_key` | String | 否 | 要排序的字段名。 |
| `options.sort.order` | Number | 否 | 排序的方向。 |
| `options.hint` | String | 否 | 指定索引。 |
| `options.projection` | String[] | 否 | 指定要返回的字段列表。 |
| `options.includes` | Object | 否 | 附加返回的内容配置。 |
| `options.includes.metadata` | Boolean | 否 | 是否返回元数据。 |

**权限:** 企业令牌

---
### `POST` 获取自定义实体数量

**路径:** `/v1/nexus/ces/count`

用于获取自定义实体数量。

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `entity_name` | String | 是 | 自定义实体的名字。 |
| `condition` | Object | 是 | 查询条件。 |

**权限:** 企业令牌

---
### `POST` 部分更新自定义实体

**路径:** `/v1/nexus/ces/update`

用于部分更新自定义实体。

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `entity_name` | String | 是 | 自定义实体的名字。 |
| `condition` | Object | 是 | 查询条件。 |
| `value` | Object | 是 | 更新的值。 |

**权限:** 企业令牌

---
## DevOps_数据集成

### `` 交付

---
### `` 代码

---
### `` 构建

---
## Storage

### `` CES

**路径:** `CES`

用于查看和管理 CES 相关信息。

---
## 产品配置中心

### `` 工单配置

**路径:** `工单配置`

---
### `` 工单配置

**路径:** `工单配置`

---
### `` 工单配置

**路径:** `工单配置`

---
### `` 工单配置

**路径:** `工单配置`

---
### `` 工单配置

**路径:** `工单配置`

---
### `` 工单配置

**路径:** `工单配置`

---
### `` 工单配置

**路径:** `工单配置`

---
### `` 工单配置

**路径:** `工单配置`

---
### `` 需求配置

**路径:** `需求配置`

---
### `` 需求配置

**路径:** `需求配置`

---
### `` 需求配置

**路径:** `需求配置`

---
### `` 需求配置

**路径:** `需求配置`

---
## 工作项配置

### `POST` 创建一个工作项属性

**路径:** `/v1/pjm/work_item_properties`

用于创建一个工作项属性。

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 是 | 工作项属性的名称。在一个企业中这个名称是唯一的。 |
| `type` | String | 是 | 工作项属性的类型。 |
| `options` | Object[] | 否 | 选择项列表。当工作项属性类型为`select,multi_select,cascade_select,cascade_multi_select`时可选填此项。 |
| `options._id` | String | 否 | 选择项id。该值在选择项中是唯一的。 |
| `options.text` | String | 是 | 选择项内容。该值在选择项中是唯一的。 |
| `options.parent_id` | String | 否 | 选择项父级id。当属性类型为`cascade_select,cascade_multi_select`时，`parent_id`参数有效，用于构建级联类型选择项之间的父子关系，最多存在4级。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工作项属性的id。 |
| `url` | String | 工作项属性的地址。 |
| `name` | String | 工作项属性的名称。 |
| `type` | String | 工作项属性的类型。 |
| `options` | Object[] | 下拉选项值。 |
| `is_removable` | Number | 是否允许删除。 |
| `is_name_editable` | Number | 是否允许修改名称。 |
| `is_options_editable` | Number | 是否允许修改下拉选项值。 |
| `select_all_level` | Boolean | 级联选择时是否允许选择全部层级。 |
| `display_all_level` | Boolean | 级联选择时是否展示全部层级。 |
| `display_separator` | String | 级联选择时的层级分隔符。 |

**权限:** 企业令牌/用户令牌

---
### `POST` 创建一个工作项标签

**路径:** `/v1/pjm/work_item_tags`

用于创建一个工作项标签。

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 是 | 标签的名称。在一个企业中这个名称是唯一的。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工作项标签的id。 |
| `url` | String | 工作项标签的地址。 |
| `name` | String | 工作项标签的名称。 |
| `color` | String | 工作项标签的颜色。 |

**权限:** 企业令牌/用户令牌

---
### `POST` 创建一个工作项状态

**路径:** `/v1/pjm/work_item_states`

用于创建一个工作项状态。

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 是 | 工作项状态的名称。在一个企业中这个名称是唯一的。 |
| `type` | String | 是 | 工作项状态的类型。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工作项状态的id。 |
| `url` | String | 工作项状态的地址。 |
| `name` | String | 工作项状态的名称。 |
| `type` | String | 工作项状态的类型。 |
| `color` | String | 工作项状态的颜色。 |
| `is_system` | Number | 是否为系统内置状态。 |

**权限:** 企业令牌/用户令牌

---
### `POST` 创建一个工作项类型

**路径:** `/v1/pjm/work_item_types`

用于创建一个工作项类型。

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 是 | 工作项类型的名称。在一个企业中这个名称是唯一的。 |
| `group` | String | 是 | 工作项类型的分组。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工作项类型的id。 |
| `url` | String | 工作项类型的地址。 |
| `name` | String | 工作项类型的名称。 |
| `group` | String | 工作项类型的分组。 |
| `is_system` | Number | 是否为系统内置工作项类型。 |

**权限:** 企业令牌/用户令牌

---
### `DELETE` 删除一个工作项标签

**路径:** `/v1/pjm/work_item_tags/{tag_id}`

用于删除一个工作项标签。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `tag_id` | String | 是 | 标签的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工作项标签的id。 |
| `url` | String | 工作项标签的地址。 |
| `name` | String | 工作项标签的名称。 |
| `color` | String | 工作项标签的颜色。 |

**权限:** 企业令牌/用户令牌

---
### `DELETE` 删除一个工作项类型

**路径:** `/v1/pjm/work_item_types/{work_item_type_id}`

用于删除一个工作项类型。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `work_item_type_id` | String | 是 | 工作项类型的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工作项类型的id。 |
| `url` | String | 工作项类型的地址。 |
| `name` | String | 工作项类型的名称。 |
| `group` | String | 工作项类型的分组。 |
| `is_system` | Number | 是否为系统内置工作项类型。 |

**权限:** 企业令牌/用户令牌

---
### `POST` 向属性方案中添加一个工作项属性

**路径:** `/v1/pjm/work_item_property_plans/{property_plan_id}/work_item_properties`

用于向属性方案中添加一个工作项属性。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `property_plan_id` | String | 是 | 工作项属性方案的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `property_id` | String | 是 | 工作项属性的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 资源的id。 |
| `url` | String | 资源的地址。 |
| `property_plan` | Object | 工作项属性方案的引用结构数据。 |
| `property` | Object | 属性的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `POST` 向工作项类型方案中添加一个工作项类型

**路径:** `/v1/pjm/work_item_type_plans/{work_item_type_plan_id}/work_item_types`

用于向工作项类型方案中添加一个工作项类型。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `work_item_type_plan_id` | String | 是 | 工作项类型方案的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `work_item_type_id` | String | 是 | 工作项类型的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工作项类型方案中工作项类型的id。 |
| `url` | String | 工作项类型方案中工作项类型的地址。 |
| `type_plan` | Object | 工作项类型方案的引用结构数据。 |
| `type` | Object | 工作项类型的引用结构数据。 |
| `sub_types` | Object[] | 子工作项类型的引用结构数据列表。 |

**权限:** 企业令牌/用户令牌

---
### `POST` 向状态方案中添加一个工作项状态

**路径:** `/v1/pjm/work_item_state_plans/{state_plan_id}/work_item_states`

用于向状态方案中添加一个工作项状态。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `state_plan_id` | String | 是 | 工作项状态方案的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `state_id` | String | 是 | 工作项状态的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 状态方案中工作项状态关联的id。 |
| `url` | String | 状态方案中工作项状态关联的地址。 |
| `state_plan` | Object | 工作项状态方案的引用结构数据。 |
| `state` | Object | 工作项状态的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `POST` 向状态方案中添加一个工作项状态流转

**路径:** `/v1/pjm/work_item_state_plans/{state_plan_id}/work_item_state_flows`

用于向状态方案中添加一个工作项状态流转。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `state_plan_id` | String | 是 | 工作项状态方案的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `from_state_id` | String | 是 | 起始工作项状态的id。 |
| `to_state_id` | String | 是 | 可更改为的工作项状态的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工作项状态流转的id。 |
| `url` | String | 工作项状态流转的地址。 |
| `state_plan` | Object | 工作项状态方案的引用结构数据。 |
| `from_state` | Object | 起始状态的引用结构数据。 |
| `to_state` | Object | 目标状态的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `DELETE` 在属性方案中移除一个工作项属性

**路径:** `/v1/pjm/work_item_property_plans/{property_plan_id}/work_item_properties/{property_id}`

用于在属性方案中移除一个工作项属性。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `property_plan_id` | String | 是 | 工作项属性方案的id。 |
| `property_id` | String | 是 | 工作项属性的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 资源的id。 |
| `url` | String | 资源的地址。 |
| `property_plan` | Object | 工作项属性方案的引用结构数据。 |
| `property` | Object | 属性的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `DELETE` 在工作项类型方案中移除一个工作项类型

**路径:** `/v1/pjm/work_item_type_plans/{work_item_type_plan_id}/work_item_types/{work_item_type_id}`

用于在工作项类型方案中移除一个工作项类型。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `work_item_type_plan_id` | String | 是 | 工作项类型方案的id。 |
| `work_item_type_id` | String | 是 | 工作项类型的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工作项类型方案中工作项类型的id。 |
| `url` | String | 工作项类型方案中工作项类型的地址。 |
| `type_plan` | Object | 工作项类型方案的引用结构数据。 |
| `type` | Object | 工作项类型的引用结构数据。 |
| `sub_types` | Object[] | 子工作项类型的引用结构数据列表。 |

**权限:** 企业令牌/用户令牌

---
### `DELETE` 在状态方案中移除一个工作项状态

**路径:** `/v1/pjm/work_item_state_plans/{state_plan_id}/work_item_states/{state_id}`

用于在状态方案中移除一个工作项状态。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `state_plan_id` | String | 是 | 工作项状态方案的id。 |
| `state_id` | String | 是 | 工作项状态的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 状态方案中工作项状态关联的id。 |
| `url` | String | 状态方案中工作项状态关联的地址。 |
| `state_plan` | Object | 工作项状态方案的引用结构数据。 |
| `state` | Object | 工作项状态的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `DELETE` 在状态方案中移除一个工作项状态流转

**路径:** `/v1/pjm/work_item_state_plans/{state_plan_id}/work_item_state_flows/{flow_id}`

用于在状态方案中移除一个工作项状态流转。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `state_plan_id` | String | 是 | 工作项状态方案的id。 |
| `flow_id` | String | 是 | 工作项状态流转的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工作项状态流转的id。 |
| `url` | String | 工作项状态流转的地址。 |
| `state_plan` | Object | 工作项状态方案的引用结构数据。 |
| `from_state` | Object | 起始状态的引用结构数据。 |
| `to_state` | Object | 目标状态的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个工作项优先级

**路径:** `/v1/pjm/work_item_priorities/{priority_id}`

用于查看一个工作项优先级。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `priority_id` | String | 是 | 工作项优先级的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工作项优先级的id。 |
| `url` | String | 工作项优先级的地址。 |
| `name` | String | 工作项优先级的名称。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个工作项属性

**路径:** `/v1/pjm/work_item_properties/{property_id}`

用于查看一个工作项属性。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `property_id` | String | 是 | 工作项属性的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工作项属性的id。 |
| `url` | String | 工作项属性的地址。 |
| `name` | String | 工作项属性的名称。 |
| `type` | String | 工作项属性的类型。 |
| `options` | Object[] | 下拉选项值。 |
| `is_removable` | Number | 是否允许删除。 |
| `is_name_editable` | Number | 是否允许修改名称。 |
| `is_options_editable` | Number | 是否允许修改下拉选项值。 |
| `select_all_level` | Boolean | 级联选择时是否允许选择全部层级。 |
| `display_all_level` | Boolean | 级联选择时是否展示全部层级。 |
| `display_separator` | String | 级联选择时的层级分隔符。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个工作项属性方案

**路径:** `/v1/pjm/work_item_property_plans/{property_plan_id}`

用于查看一个工作项属性方案。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `property_plan_id` | String | 是 | 工作项属性方案的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工作项属性方案的id。 |
| `url` | String | 工作项属性方案的地址。 |
| `project_type` | String | 工作项属性方案适用的项目类型。 |
| `process_id` | String | 工作项属性方案关联的流程id。 |
| `work_item_type` | String | 工作项属性方案适用的工作项类型。 |
| `project` | Object | 工作项属性方案关联项目的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个工作项标签

**路径:** `/v1/pjm/work_item_tags/{tag_id}`

用于查看一个工作项标签。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `tag_id` | String | 是 | 工作项标签的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工作项标签的id。 |
| `url` | String | 工作项标签的地址。 |
| `name` | String | 工作项标签的名称。 |
| `color` | String | 工作项标签的颜色。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个工作项状态

**路径:** `/v1/pjm/work_item_states/{state_id}`

用于查看一个工作项状态。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `state_id` | String | 是 | 工作项状态的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工作项状态的id。 |
| `url` | String | 工作项状态的地址。 |
| `name` | String | 工作项状态的名称。 |
| `type` | String | 工作项状态的类型。 |
| `color` | String | 工作项状态的颜色。 |
| `is_system` | Number | 是否为系统内置状态。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个工作项状态方案

**路径:** `/v1/pjm/work_item_state_plans/{state_plan_id}`

用于查看一个工作项状态方案。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `state_plan_id` | String | 是 | 工作项状态方案的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工作项状态方案的id。 |
| `url` | String | 工作项状态方案的地址。 |
| `project_type` | String | 工作项状态方案适用的项目类型。 |
| `process_id` | String | 工作项状态方案关联的流程id。 |
| `work_item_type` | String | 工作项状态方案适用的工作项类型。 |
| `project` | Object | 工作项状态方案关联项目的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个工作项类型

**路径:** `/v1/pjm/work_item_types/{work_item_type_id}`

用于查看一个工作项类型。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `work_item_type_id` | String | 是 | 工作项类型的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工作项类型的id。 |
| `url` | String | 工作项类型的地址。 |
| `name` | String | 工作项类型的名称。 |
| `group` | String | 工作项类型的分组。 |
| `is_system` | Number | 是否为系统内置工作项类型。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个工作项类型方案

**路径:** `/v1/pjm/work_item_type_plans/{work_item_type_plan_id}`

用于查看一个工作项类型方案。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `work_item_type_plan_id` | String | 是 | 工作项类型方案的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工作项类型方案的id。 |
| `url` | String | 工作项类型方案的地址。 |
| `project_type` | String | 工作项类型方案适用的项目类型。 |
| `process_id` | String | 工作项类型方案关联的流程id。 |
| `project` | Object | 工作项类型方案关联项目的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个状态方案中的工作项状态

**路径:** `/v1/pjm/work_item_state_plans/{state_plan_id}/work_item_states/{state_id}`

用于查看状态方案中的一个工作项状态。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `state_plan_id` | String | 是 | 工作项状态方案的id。 |
| `state_id` | String | 是 | 工作项状态的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 状态方案中工作项状态关联的id。 |
| `url` | String | 状态方案中工作项状态关联的地址。 |
| `state_plan` | Object | 工作项状态方案的引用结构数据。 |
| `state` | Object | 工作项状态的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取全部工作项属性列表

**路径:** `/v1/pjm/work_item_properties`

用于查询全部工作项属性列表。

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 工作项属性全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取全部工作项标签列表

**路径:** `/v1/pjm/work_item_tags`

用于查询全部工作项标签列表。

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 否 | 标签的名称。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 工作项标签的全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取全部工作项状态列表

**路径:** `/v1/pjm/work_item_states`

用于查询全部工作项状态列表。

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 工作项状态的全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取全部工作项类型列表

**路径:** `/v1/pjm/work_item_types`

用于查询全部工作项类型列表。

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 工作项类型的全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取属性方案中的一个工作项属性

**路径:** `/v1/pjm/work_item_property_plans/{property_plan_id}/work_item_properties/{property_id}`

用于查询属性方案中的一个工作项属性。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `property_plan_id` | String | 是 | 工作项属性方案的id。 |
| `property_id` | String | 是 | 工作项属性的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 属性方案中工作项属性关联的id。 |
| `url` | String | 属性方案中工作项属性关联的地址。 |
| `property_plan` | Object | 工作项属性方案的引用结构数据。 |
| `property` | Object | 工作项属性的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取属性方案中的工作项属性列表

**路径:** `/v1/pjm/work_item_property_plans/{property_plan_id}/work_item_properties`

用于查询属性方案中的工作项属性列表。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `property_plan_id` | String | 是 | 工作项属性方案的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 属性方案中的工作项属性的全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取工作项属性方案列表

**路径:** `/v1/pjm/work_item_property_plans`

用于查询工作项属性方案列表。

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 否 | 项目的id。查询指定项目应用的工作项属性方案时传入。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 工作项属性方案的全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取工作项状态方案列表

**路径:** `/v1/pjm/work_item_state_plans`

用于查询工作项状态方案列表。

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 否 | 项目的id。查询指定项目应用的工作项状态方案时传入。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 工作项状态方案的全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取工作项类型方案中的一个工作项类型

**路径:** `/v1/pjm/work_item_type_plans/{work_item_type_plan_id}/work_item_types/{work_item_type_id}`

用于查询工作项类型方案中的一个工作项类型。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `work_item_type_plan_id` | String | 是 | 工作项类型方案的id。 |
| `work_item_type_id` | String | 是 | 工作项类型的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工作项类型方案中工作项类型的id。 |
| `url` | String | 工作项类型方案中工作项类型的地址。 |
| `type_plan` | Object | 工作项类型方案的引用结构数据。 |
| `type` | Object | 工作项类型的引用结构数据。 |
| `sub_types` | Object[] | 子工作项类型的引用结构数据列表。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取工作项类型方案中的工作项类型列表

**路径:** `/v1/pjm/work_item_type_plans/{work_item_type_plan_id}/work_item_types`

用于查询工作项类型方案中的工作项类型列表。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `work_item_type_plan_id` | String | 是 | 工作项类型方案的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 工作项类型方案中的工作项类型的全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取工作项类型方案列表

**路径:** `/v1/pjm/work_item_type_plans`

用于查询工作项类型方案列表。

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 否 | 项目的id。查询指定项目应用的工作项类型方案时传入。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 工作项类型方案的全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取状态方案中的一个工作项状态流转

**路径:** `/v1/pjm/work_item_state_plans/{state_plan_id}/work_item_state_flows/{flow_id}`

用于查看一个工作项状态流转。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `state_plan_id` | String | 是 | 工作项状态方案的id。 |
| `flow_id` | String | 是 | 工作项状态流转的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工作项状态流转的id。 |
| `url` | String | 工作项状态流转的地址。 |
| `state_plan` | Object | 工作项状态方案的引用结构数据。 |
| `from_state` | Object | 起始状态的引用结构数据。 |
| `to_state` | Object | 目标状态的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取状态方案中的工作项状态列表

**路径:** `/v1/pjm/work_item_state_plans/{state_plan_id}/work_item_states`

用于查询状态方案中的工作项状态列表。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `state_plan_id` | String | 是 | 工作项状态方案的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 状态方案中的工作项状态的全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取状态方案中的工作项状态流转列表

**路径:** `/v1/pjm/work_item_state_plans/{state_plan_id}/work_item_state_flows`

用于查询状态方案中的工作项状态流转列表。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `state_plan_id` | String | 是 | 工作项状态方案的id。 |

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `from_state_id` | String | 否 | 起始状态的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 工作项状态流转的全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `PATCH` 部分更新一个工作项属性

**路径:** `/v1/pjm/work_item_properties/{property_id}`

用于部分更新一个工作项属性。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `property_id` | String | 是 | 工作项属性的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 否 | 工作项属性的名称。在一个企业中这个名称是唯一的。 |
| `options` | Object[] | 否 | 选择项列表。`options`是整体更新的。 |
| `options._id` | String | 否 | 选择项id。该值在选择项中是唯一的。 |
| `options.text` | String | 是 | 选择项内容。该值在选择项中是唯一的。 |
| `options.parent_id` | String | 否 | 选择项父级id。当属性类型为`cascade_select,cascade_multi_select`时，`parent_id`参数有效，用于构建级联类型选择项之间的父子关系，最多存在4级。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工作项属性的id。 |
| `url` | String | 工作项属性的地址。 |
| `name` | String | 工作项属性的名称。 |
| `type` | String | 工作项属性的类型。 |
| `options` | Object[] | 下拉选项值。 |
| `is_removable` | Number | 是否允许删除。 |
| `is_name_editable` | Number | 是否允许修改名称。 |
| `is_options_editable` | Number | 是否允许修改下拉选项值。 |
| `select_all_level` | Boolean | 级联选择时是否允许选择全部层级。 |
| `display_all_level` | Boolean | 级联选择时是否展示全部层级。 |
| `display_separator` | String | 级联选择时的层级分隔符。 |

**权限:** 企业令牌/用户令牌

---
### `PATCH` 部分更新一个工作项标签

**路径:** `/v1/pjm/work_item_tags/{tag_id}`

用于部分更新一个工作项标签。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `tag_id` | String | 是 | 标签的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 否 | 标签的名称。在一个企业中这个名称是唯一的。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工作项标签的id。 |
| `url` | String | 工作项标签的地址。 |
| `name` | String | 工作项标签的名称。 |
| `color` | String | 工作项标签的颜色。 |

**权限:** 企业令牌/用户令牌

---
### `PATCH` 部分更新一个工作项状态

**路径:** `/v1/pjm/work_item_states/{state_id}`

用于部分更新一个工作项状态。  只有非系统类型的工作项状态才能更新。

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 否 | 工作项状态的名称。在一个企业中这个名称是唯一的。 |
| `type` | String | 否 | 工作项状态的类型。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工作项状态的id。 |
| `url` | String | 工作项状态的地址。 |
| `name` | String | 工作项状态的名称。 |
| `type` | String | 工作项状态的类型。 |
| `color` | String | 工作项状态的颜色。 |
| `is_system` | Number | 是否为系统内置状态。 |

**权限:** 企业令牌/用户令牌

---
### `PATCH` 部分更新一个工作项类型

**路径:** `/v1/pjm/work_item_types/{work_item_type_id}`

用于部分更新一个工作项类型。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `work_item_type_id` | String | 是 | 工作项类型的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 是 | 工作项类型的名称。在一个企业中这个名称是唯一的。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工作项类型的id。 |
| `url` | String | 工作项类型的地址。 |
| `name` | String | 工作项类型的名称。 |
| `group` | String | 工作项类型的分组。 |
| `is_system` | Number | 是否为系统内置工作项类型。 |

**权限:** 企业令牌/用户令牌

---
### `PATCH` 部分更新工作项类型方案中的工作项类型

**路径:** `/v1/pjm/work_item_type_plans/{work_item_type_plan_id}/work_item_types/{work_item_type_id}`

用于部分更新工作项类型方案中的工作项类型。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `work_item_type_plan_id` | String | 是 | 工作项类型方案的id。 |
| `work_item_type_id` | String | 是 | 工作项类型的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `sub_type_ids` | String[] | 是 | 子工作项类型id的列表，使用','分割，最多只能20个。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工作项类型方案中工作项类型的id。 |
| `url` | String | 工作项类型方案中工作项类型的地址。 |
| `type_plan` | Object | 工作项类型方案的引用结构数据。 |
| `type` | Object | 工作项类型的引用结构数据。 |
| `sub_types` | Object[] | 子工作项类型的引用结构数据列表。 |

**权限:** 企业令牌/用户令牌

---
## 项目配置中心

### `` 工作项配置

**路径:** `工作项配置`

---
### `` 工作项配置

**路径:** `工作项配置`

---
### `` 工作项配置

**路径:** `工作项配置`

---
### `` 工作项配置

**路径:** `工作项配置`

---
### `` 工作项配置

**路径:** `工作项配置`

---
### `` 工作项配置

**路径:** `工作项配置`

---
### `` 工作项配置

**路径:** `工作项配置`

---
### `` 工作项配置

**路径:** `工作项配置`

---
### `` 工作项配置

**路径:** `工作项配置`

---
### `` 项目配置

**路径:** `项目配置`

---
### `` 项目配置

**路径:** `项目配置`

---
### `` 项目配置

**路径:** `项目配置`

---
