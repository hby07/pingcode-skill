# ⚙️ 项目管理 — API 详细文档

> 本文档包含 45 个接口的完整参数说明。
> 来源: https://open.pingcode.com/

---

## 看板

### `POST` 创建一个泳道

**路径:** `/v1/pjm/projects/{project_id}/boards/{board_id}/swimlanes`

用于创建一个泳道。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 是 | 项目的id。 |
| `board_id` | String | 是 | 看板的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 是 | 泳道的名称。在同一看板下该名称是唯一的。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 泳道的id。 |
| `url` | String | 泳道的地址。 |
| `project` | Object | 所属项目的引用结构数据。 |
| `board` | Object | 所属看板的引用结构数据。 |
| `name` | String | 泳道的名称。 |
| `is_system` | Number | 是否为系统内置泳道。 |

**权限:** 企业令牌/用户令牌

---
### `POST` 创建一个看板

**路径:** `/v1/pjm/projects/{project_id}/boards`

用于创建一个看板。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 是 | 项目的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 是 | 看板的名字。在同一个项目中该名字是唯一的。 |
| `work_item_types` | String[] | 否 | 看板支持的工作项类型列表。自定义工作项类型只支持`hybrid`类型项目里的看板。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 看板的id。 |
| `url` | String | 看板的地址。 |
| `project` | Object | 所属项目的引用结构数据。 |
| `name` | String | 看板的名称。 |
| `work_item_types` | String[] | 看板支持的工作项类型列表。 |

**权限:** 企业令牌/用户令牌

---
### `POST` 创建一个看板栏

**路径:** `/v1/pjm/projects/{project_id}/boards/{board_id}/entries`

用于创建一个看板栏。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 是 | 项目的id。 |
| `board_id` | String | 是 | 看板的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 是 | 看板栏的名称。在同一看板下该名称是唯一的。 |
| `wip_limit` | Number | 否 | 在制品数量。 |
| `is_split` | Boolean | 否 | 是否将看板栏拆分为进行中和已完成。 |
| `definition_of_done` | String | 否 | 完成的定义。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 看板栏的id。 |
| `url` | String | 看板栏的地址。 |
| `project` | Object | 所属项目的引用结构数据。 |
| `board` | Object | 所属看板的引用结构数据。 |
| `name` | String | 看板栏的名称。 |
| `is_system` | Number | 是否为系统内置看板栏。 |
| `is_split` | Boolean | 是否将看板栏拆分为进行中和已完成。 |
| `wip_limit` | Number | 在制品数量。 |
| `definition_of_done` | String | 完成的定义。 |

**权限:** 企业令牌/用户令牌

---
### `DELETE` 删除一个泳道

**路径:** `/v1/pjm/projects/{project_id}/boards/{board_id}/swimlanes/{swimlane_id}`

用于删除一个泳道。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 是 | 项目的id。 |
| `board_id` | String | 是 | 看板的id。 |
| `swimlane_id` | String | 是 | 泳道的id. |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 泳道的id。 |
| `url` | String | 泳道的地址。 |
| `project` | Object | 所属项目的引用结构数据。 |
| `board` | Object | 所属看板的引用结构数据。 |
| `name` | String | 泳道的名称。 |
| `is_system` | Number | 是否为系统内置泳道。 |

**权限:** 企业令牌/用户令牌

---
### `DELETE` 删除一个看板

**路径:** `/v1/pjm/projects/{project_id}/boards/{board_id}`

用于删除一个看板。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 是 | 项目的id。 |
| `board_id` | String | 是 | 看板的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 看板的id。 |
| `url` | String | 看板的地址。 |
| `project` | Object | 所属项目的引用结构数据。 |
| `name` | String | 看板的名称。 |
| `work_item_types` | String[] | 看板支持的工作项类型列表。 |

**权限:** 企业令牌/用户令牌

---
### `DELETE` 删除一个看板栏

**路径:** `/v1/pjm/projects/{project_id}/boards/{board_id}/entries/{entry_id}`

用于删除一个看板栏。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 是 | 项目的id。 |
| `board_id` | String | 是 | 看板的id。 |
| `entry_id` | String | 是 | 看板栏的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 看板栏的id。 |
| `url` | String | 看板栏的地址。 |
| `project` | Object | 所属项目的引用结构数据。 |
| `board` | Object | 所属看板的引用结构数据。 |
| `name` | String | 看板栏的名称。 |
| `is_system` | Number | 是否为系统内置看板栏。 |
| `is_split` | Boolean | 是否将看板栏拆分为进行中和已完成。 |
| `wip_limit` | Number | 在制品数量。 |
| `definition_of_done` | String | 完成的定义。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个泳道

**路径:** `/v1/pjm/projects/{project_id}/boards/{board_id}/swimlanes/{swimlane_id}`

用于获取一个泳道。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 是 | 项目的id。 |
| `board_id` | String | 是 | 看板的id。 |
| `swimlane_id` | String | 是 | 泳道的id. |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 泳道的id。 |
| `url` | String | 泳道的地址。 |
| `project` | Object | 所属项目的引用结构数据。 |
| `board` | Object | 所属看板的引用结构数据。 |
| `name` | String | 泳道的名称。 |
| `is_system` | Number | 是否为系统内置泳道。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个看板

**路径:** `/v1/pjm/projects/{project_id}/boards/{board_id}`

用于查看一个看板。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 是 | 项目的id。 |
| `board_id` | String | 是 | 看板的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 看板的id。 |
| `url` | String | 看板的地址。 |
| `project` | Object | 所属项目的引用结构数据。 |
| `name` | String | 看板的名称。 |
| `work_item_types` | String[] | 看板支持的工作项类型列表。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个看板栏

**路径:** `/v1/pjm/projects/{project_id}/boards/{board_id}/entries/{entry_id}`

用于获取一个看板栏。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 是 | 项目的id。 |
| `board_id` | String | 是 | 看板的id。 |
| `entry_id` | String | 是 | 看板栏的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 看板栏的id。 |
| `url` | String | 看板栏的地址。 |
| `project` | Object | 所属项目的引用结构数据。 |
| `board` | Object | 所属看板的引用结构数据。 |
| `name` | String | 看板栏的名称。 |
| `is_system` | Number | 是否为系统内置看板栏。 |
| `is_split` | Boolean | 是否将看板栏拆分为进行中和已完成。 |
| `wip_limit` | Number | 在制品数量。 |
| `definition_of_done` | String | 完成的定义。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取泳道列表

**路径:** `/v1/pjm/projects/{project_id}/boards/{board_id}/swimlanes`

用于查询泳道列表。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 是 | 项目的id。 |
| `board_id` | String | 是 | 看板的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 泳道全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取看板列表

**路径:** `/v1/pjm/projects/{project_id}/boards`

用于查询看板列表。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 是 | 项目的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 看板全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取看板栏列表

**路径:** `/v1/pjm/projects/{project_id}/boards/{board_id}/entries`

用于查询看板栏列表。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 是 | 项目的id。 |
| `board_id` | String | 是 | 看板的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 看板栏全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `PATCH` 部分更新一个泳道

**路径:** `/v1/pjm/projects/{project_id}/boards/{board_id}/swimlanes/{swimlane_id}`

用于部分更新一个泳道。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 是 | 项目的id。 |
| `board_id` | String | 是 | 看板的id。 |
| `swimlane_id` | String | 是 | 泳道的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 否 | 泳道的名称。在同一看板下该名称是唯一的。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 泳道的id。 |
| `url` | String | 泳道的地址。 |
| `project` | Object | 所属项目的引用结构数据。 |
| `board` | Object | 所属看板的引用结构数据。 |
| `name` | String | 泳道的名称。 |
| `is_system` | Number | 是否为系统内置泳道。 |

**权限:** 企业令牌/用户令牌

---
### `PATCH` 部分更新一个看板

**路径:** `/v1/pjm/projects/{project_id}/boards/{board_id}`

用于部分更新一个看板。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 是 | 项目的id。 |
| `board_id` | String | 是 | 看板的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 否 | 看板的名字。在同一个项目中该名字是唯一的。 |
| `work_item_types` | String[] | 否 | 看板支持的工作项类型列表。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 看板的id。 |
| `url` | String | 看板的地址。 |
| `project` | Object | 所属项目的引用结构数据。 |
| `name` | String | 看板的名称。 |
| `work_item_types` | String[] | 看板支持的工作项类型列表。 |

**权限:** 企业令牌/用户令牌

---
### `PATCH` 部分更新一个看板栏

**路径:** `/v1/pjm/projects/{project_id}/boards/{board_id}/entries/{entry_id}`

用于部分更新一个看板栏。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 是 | 项目的id。 |
| `board_id` | String | 是 | 看板的id。 |
| `entry_id` | String | 是 | 看板栏的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 否 | 看板栏的名称。在同一看板下该名称是唯一的。 |
| `wip_limit` | Number | 否 | 在制品数量。 |
| `is_split` | Boolean | 否 | 是否将看板栏拆分为进行中和已完成 |
| `definition_of_done` | String | 否 | 完成的定义。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 看板栏的id。 |
| `url` | String | 看板栏的地址。 |
| `project` | Object | 所属项目的引用结构数据。 |
| `board` | Object | 所属看板的引用结构数据。 |
| `name` | String | 看板栏的名称。 |
| `is_system` | Number | 是否为系统内置看板栏。 |
| `is_split` | Boolean | 是否将看板栏拆分为进行中和已完成。 |
| `wip_limit` | Number | 在制品数量。 |
| `definition_of_done` | String | 完成的定义。 |

**权限:** 企业令牌/用户令牌

---
## 项目

### `POST` 创建一个项目

**路径:** `/v1/pjm/projects`

用于创建一个项目。

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `scope_type` | String | 否 | 项目的所属类型。默认值`organization`。允许值分别表示企业可见和团队可见。 |
| `scope_id` | String | 否 | 项目的所属id。当`scope_type`为`user_group`时，该字段必填，且表示团队id；当`scope_type`为其他值时，该字段无效。 |
| `name` | String | 是 | 项目的名称。最大长度为255。 |
| `visibility` | String | 否 | 项目的可见范围。允许值分别表示组织全部成员可见和仅项目成员可见。 |
| `type` | String | 是 | 项目的类型。 |
| `process_id` | String | 否 | 项目流程的id。项目流程可以通过`获取全部项目流程`获取。 |
| `identifier` | String | 是 | 项目的标识。在一个企业中这个标识是唯一的。项目的标识由大写英文字母/数字/下划线/连接线组成（不超过15个字符）。 |
| `description` | String | 否 | 项目的描述。 |
| `members` | Object[] | 否 | 项目成员的列表。当项目的`scope_type`变为`user_group`时，项目成员必须是`scope_id`指定的团队内的成员；当`scope_type`为其他值时，项目成员可以是任意成员或团队。 |
| `members.id` | String | 是 | 企业成员或团队的id。 |
| `members.type` | String | 是 | 项目成员的类型。 |
| `start_at` | Number | 否 | 项目开始的时间。 |
| `end_at` | Number | 否 | 项目结束的时间。 |
| `assignee_id` | String | 否 | 项目负责人的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 项目的id。 |
| `url` | String | 项目的地址。 |
| `type` | String | 项目的类型。 |
| `process_id` | String | 项目流程的id。 |
| `scope_id` | String | 项目的所属id。 |
| `scope_type` | String | 项目的所属类型。 |
| `name` | String | 项目的名称。 |
| `color` | String | 项目的主题色。 |
| `identifier` | String | 项目的标识。 |
| `visibility` | String | 项目的可见性。 |
| `description` | String | 项目的描述。 |
| `state` | Object | 项目状态的引用结构数据。 |
| `assignee` | Object | 项目负责人的引用结构数据。 |
| `start_at` | Number | 项目的开始时间。 |
| `end_at` | Number | 项目的结束时间。 |
| `properties` | Object | 项目的自定义属性键值对集合。 |
| `members` | Object[] | 项目成员的引用结构数据列表。 |
| `is_local_config_enabled` | Number | 是否已启用本地配置。 |
| `created_at` | Number | 项目的创建时间。 |
| `created_by` | Object | 项目创建人的引用结构数据。 |
| `updated_at` | Number | 项目的更新时间。 |
| `updated_by` | Object | 项目更新人的引用结构数据。 |
| `is_archived` | Number | 是否已归档。 |
| `is_deleted` | Number | 是否已删除。 |

**权限:** 企业令牌/用户令牌

---
### `POST` 向项目中添加一个成员

**路径:** `/v1/pjm/projects/{project_id}/members`

用于向项目中添加一个成员。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 是 | 项目的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `member` | Object | 是 | 项目的成员。 |
| `member.id` | String | 是 | 企业成员或团队的id。 |
| `member.type` | String | 是 | 项目成员的类型。 |
| `role_id` | String | 否 | 角色的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 资源的id。 |
| `url` | String | 资源的地址。 |
| `project` | Object | 所属项目的引用结构数据。 |
| `type` | String | 项目成员的类型。 |
| `user` | Object | 用户的引用结构数据。 |
| `user_group` | Object | 团队的引用结构数据。 |
| `role` | Object | role的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `POST` 向项目中添加一个项目属性

**路径:** `/v1/pjm/projects/{project_id}/project_properties`

用于向项目中添加一个项目属性。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 是 | 项目的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `property_id` | String | 是 | 项目属性的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 资源的id。 |
| `url` | String | 资源的地址。 |
| `project` | Object | 所属项目的引用结构数据。 |
| `property` | Object | 项目属性的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `DELETE` 在项目中移除一个成员

**路径:** `/v1/pjm/projects/{project_id}/members/{member_id}`

用于在项目中移除一个成员。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 是 | 项目的id。 |
| `member_id` | String | 是 | 企业成员或团队的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 资源的id。 |
| `url` | String | 资源的地址。 |
| `project` | Object | 所属项目的引用结构数据。 |
| `type` | String | 项目成员的类型。 |
| `user` | Object | 用户的引用结构数据。 |
| `user_group` | Object | 团队的引用结构数据。 |
| `role` | Object | role的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `DELETE` 在项目中移除一个项目属性

**路径:** `/v1/pjm/projects/{project_id}/project_properties/{property_id}`

用于在项目中移除一个项目属性。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 是 | 项目的id。 |
| `property_id` | String | 是 | 项目属性的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 资源的id。 |
| `url` | String | 资源的地址。 |
| `project` | Object | 所属项目的引用结构数据。 |
| `property` | Object | 属性的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `POST` 复制一个项目

**路径:** `/v1/pjm/projects/{project_id}/clone`

用于复制一个项目。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 是 | 项目的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `scope_type` | String | 否 | 项目的所属类型。默认使用原项目的所属。允许值分别表示企业可见和团队可见。 |
| `scope_id` | String | 否 | 项目的所属id。当`scope_type`为`user_group`时，该字段必填，且表示团队id；当`scope_type`为其他值时，该字段无效。 |
| `name` | String | 否 | 项目的名称。最大长度为255。默认使用原项目的名称。 |
| `visibility` | String | 否 | 项目的可见范围。默认使用原项目的可见范围。允许值分别表示组织全部成员可见和仅项目成员可见。 |
| `identifier` | String | 是 | 项目的标识。在一个企业中这个标识是唯一的。项目的标识由大写英文字母/数字/下划线/连接线组成（不超过15个字符）。 |
| `description` | String | 否 | 项目的描述。默认使用原项目的描述。 |
| `members` | Object[] | 否 | 项目成员的列表。当项目的`scope_type`变为`user_group`时，项目成员必须是`scope_id`指定的团队内的成员；当`scope_type`为其他值时，项目成员可以是任意成员或团队，默认使用原项目的成员列表。 |
| `members.id` | String | 是 | 企业成员或团队的id。 |
| `members.type` | String | 是 | 项目成员的类型。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 项目的id。 |
| `url` | String | 项目的地址。 |
| `type` | String | 项目的类型。 |
| `process_id` | String | 项目流程的id。 |
| `scope_id` | String | 项目的所属id。 |
| `scope_type` | String | 项目的所属类型。 |
| `name` | String | 项目的名称。 |
| `color` | String | 项目的主题色。 |
| `identifier` | String | 项目的标识。 |
| `visibility` | String | 项目的可见性。 |
| `description` | String | 项目的描述。 |
| `state` | Object | 项目状态的引用结构数据。 |
| `assignee` | Object | 项目负责人的引用结构数据。 |
| `start_at` | Number | 项目的开始时间。 |
| `end_at` | Number | 项目的结束时间。 |
| `properties` | Object | 项目的自定义属性键值对集合。 |
| `members` | Object[] | 项目成员的引用结构数据列表。 |
| `is_local_config_enabled` | Number | 是否已启用本地配置。 |
| `created_at` | Number | 项目的创建时间。 |
| `created_by` | Object | 项目创建人的引用结构数据。 |
| `updated_at` | Number | 项目的更新时间。 |
| `updated_by` | Object | 项目更新人的引用结构数据。 |
| `is_archived` | Number | 是否已归档。 |
| `is_deleted` | Number | 是否已删除。 |

**权限:** 企业令牌/用户令牌

---
### `POST` 开启项目本地配置

**路径:** `/v1/pjm/projects/{project_id}/local_config/enable`

用于开启项目本地配置。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 是 | 项目的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 项目的id。 |
| `url` | String | 项目的地址。 |
| `type` | String | 项目的类型。 |
| `process_id` | String | 项目流程的id。 |
| `scope_type` | String | 项目的所属类型。 |
| `scope_id` | String | 项目的所属id。 |
| `name` | String | 项目的名称。 |
| `color` | String | 项目的主题色。 |
| `identifier` | String | 项目的标识。 |
| `visibility` | String | 项目的可见性。 |
| `description` | String | 项目的描述。 |
| `is_local_config_enabled` | Number | 是否已启用本地配置。 |
| `created_at` | Number | 项目的创建时间。 |
| `created_by` | Object | 项目的创建人。 |
| `updated_at` | Number | 项目的更新时间。 |
| `updated_by` | Object | 项目的更新人。 |
| `is_archived` | Number | 是否已归档。 |
| `is_deleted` | Number | 是否已删除。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个项目

**路径:** `/v1/pjm/projects/{project_id}`

用于查看一个项目。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 是 | 项目的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 项目的id。 |
| `url` | String | 项目的地址。 |
| `type` | String | 项目的类型。 |
| `process_id` | String | 项目流程的id。 |
| `scope_id` | String | 项目的所属id。 |
| `scope_type` | String | 项目的所属类型。 |
| `name` | String | 项目的名称。 |
| `color` | String | 项目的主题色。 |
| `identifier` | String | 项目的标识。 |
| `visibility` | String | 项目的可见性。 |
| `description` | String | 项目的描述。 |
| `state` | Object | 项目状态的引用结构数据。 |
| `assignee` | Object | 项目负责人的引用结构数据。 |
| `start_at` | Number | 项目的开始时间。 |
| `end_at` | Number | 项目的结束时间。 |
| `properties` | Object | 项目的自定义属性键值对集合。 |
| `members` | Object[] | 项目成员的引用结构数据列表。 |
| `is_local_config_enabled` | Number | 是否已启用本地配置。 |
| `created_at` | Number | 项目的创建时间。 |
| `created_by` | Object | 项目创建人的引用结构数据。 |
| `updated_at` | Number | 项目的更新时间。 |
| `updated_by` | Object | 项目更新人的引用结构数据。 |
| `is_archived` | Number | 是否已归档。 |
| `is_deleted` | Number | 是否已删除。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个项目进度

**路径:** `/v1/pjm/projects/{project_id}/progress`

用于查看一个项目进度。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 是 | 项目的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `work_item` | Object | 项目工作项进度统计。 |
| `work_item.total` | Number | 工作项总数。 |
| `work_item.pending_count` | Number | 待处理工作项数量。 |
| `work_item.in_progress_count` | Number | 进行中工作项数量。 |
| `work_item.completed_count` | Number | 已完成工作项数量。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取项目中的一个成员

**路径:** `/v1/pjm/projects/{project_id}/members/{member_id}`

用于查看项目中的一个成员。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 是 | 项目的id。 |
| `member_id` | String | 是 | 企业成员或团队的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 资源的id。 |
| `url` | String | 资源的地址。 |
| `project` | Object | 所属项目的引用结构数据。 |
| `type` | String | 项目成员的类型。 |
| `user` | Object | 用户的引用结构数据。 |
| `user_group` | Object | 团队的引用结构数据。 |
| `role` | Object | role的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取项目中的一个项目属性

**路径:** `/v1/pjm/projects/{project_id}/project_properties/{property_id}`

用于查看一个项目属性。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 是 | 项目的id。 |
| `property_id` | String | 是 | 项目属性的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 资源的id。 |
| `url` | String | 资源的地址。 |
| `project` | Object | 所属项目的引用结构数据。 |
| `property` | Object | 属性的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取项目中的成员列表

**路径:** `/v1/pjm/projects/{project_id}/members`

用于查询项目中的成员列表。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 是 | 项目的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 项目中的成员的全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取项目中的项目属性列表

**路径:** `/v1/pjm/projects/{project_id}/project_properties`

用于查询项目中的项目属性列表。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 是 | 项目的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 项目中的项目属性全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取项目列表

**路径:** `/v1/pjm/projects`

用于查询项目列表。

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `identifier` | String | 否 | 项目的标识。 |
| `type` | String | 否 | 项目的类型。 |
| `include_deleted` | Boolean | 否 | 是否查询已删除的项目。该值默认为`false`。 |
| `include_archived` | Boolean | 否 | 是否查询已归档的项目。该值默认为`false`。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 项目全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取项目状态列表

**路径:** `/v1/pjm/project/states?project_id={project_id}`

用于查询项目状态列表。

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 是 | 项目的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_index` | Number | 页码，从0开始。 |
| `page_size` | Number | 每页条数。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 项目状态全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `PATCH` 部分更新一个项目

**路径:** `/v1/pjm/projects/{project_id}`

用于部分更新一个项目。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 是 | 项目的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 否 | 项目的名称。最大长度为255。 |
| `identifier` | String | 否 | 项目的标识。在一个企业中这个标识是唯一的。项目的标识由大写英文字母/数字/下划线/连接线组成（不超过15个字符）。 |
| `description` | String | 否 | 项目的描述。 |
| `start_at` | Number | 否 | 项目开始的时间。 |
| `end_at` | Number | 否 | 项目结束的时间。 |
| `assignee_id` | String | 否 | 项目负责人的id。 |
| `state_id` | String | 否 | 项目状态的id。项目状态可以通过`获取项目状态列表`获取。 |
| `properties` | Object | 否 | 项目自定义属性的键值对集合。需要注意自定义属性需要包含在项目属性方案中。例如属性方案中包含`prop_a`和`prop_b`。 |
| `properties.prop_a` | Object | 否 | 项目自定义属性`prop_a`。 |
| `properties.prop_b` | Object | 否 | 项目自定义属性`prop_b`。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 项目的id。 |
| `url` | String | 项目的地址。 |
| `type` | String | 项目的类型。 |
| `process_id` | String | 项目流程的id。 |
| `scope_id` | String | 项目的所属id。 |
| `scope_type` | String | 项目的所属类型。 |
| `name` | String | 项目的名称。 |
| `color` | String | 项目的主题色。 |
| `identifier` | String | 项目的标识。 |
| `visibility` | String | 项目的可见性。 |
| `description` | String | 项目的描述。 |
| `state` | Object | 项目状态的引用结构数据。 |
| `assignee` | Object | 项目负责人的引用结构数据。 |
| `start_at` | Number | 项目的开始时间。 |
| `end_at` | Number | 项目的结束时间。 |
| `properties` | Object | 项目的自定义属性键值对集合。 |
| `members` | Object[] | 项目成员的引用结构数据列表。 |
| `is_local_config_enabled` | Number | 是否已启用本地配置。 |
| `created_at` | Number | 项目的创建时间。 |
| `created_by` | Object | 项目创建人的引用结构数据。 |
| `updated_at` | Number | 项目的更新时间。 |
| `updated_by` | Object | 项目更新人的引用结构数据。 |
| `is_archived` | Number | 是否已归档。 |
| `is_deleted` | Number | 是否已删除。 |

**权限:** 企业令牌/用户令牌

---
### `PATCH` 部分更新一个项目内的成员

**路径:** `/v1/pjm/projects/{project_id}/members/{member_id}`

用于部分更新一个项目内的成员。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 是 | 项目的id。 |
| `member_id` | String | 是 | 企业成员或团队的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `role_id` | String | 否 | 角色的id。管理员可以更改其他用户的角色，但非管理员用户无权更改其他用户的角色。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 项目内的成员的id。 |
| `url` | String | 项目内的成员的地址。 |
| `project` | Object | 所属项目的引用结构数据。 |
| `type` | String | 项目成员的类型。 |
| `user` | Object | 用户的引用结构数据。 |
| `user_group` | Object | 团队的引用结构数据。 |
| `role` | Object | role的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
## 项目管理

### `` 发布

**路径:** `发布`

---
### `` 工作项

**路径:** `工作项`

---
### `` 看板

**路径:** `看板`

---
### `` 迭代

**路径:** `迭代`

---
### `` 项目

**路径:** `项目`

---
### `` 项目配置中心

---
## 项目配置

### `POST` 创建一个项目属性

**路径:** `/v1/pjm/project_properties`

用于创建一个项目属性。

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 是 | 项目属性的名称。在一个企业中这个名称是唯一的。 |
| `type` | String | 是 | 项目属性的类型。 |
| `options` | Object[] | 否 | 选择项列表。当属性类型为`select,multi_select,cascade_select,cascade_multi_select`时可选填此项。 |
| `options._id` | String | 否 | 选择项id。该值在选择项中是唯一的。 |
| `options.text` | String | 是 | 选择项内容。该值在选择项中是唯一的。 |
| `options.parent_id` | String | 否 | 选择项父级id。当属性类型为`cascade_select,cascade_multi_select`时，`parent_id`参数有效，用于构建级联类型选择项之间的父子关系，最多存在4级。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 项目属性的id。 |
| `url` | String | 项目属性的地址。 |
| `name` | String | 项目属性的名称。 |
| `type` | String | 项目属性的类型。 |
| `options` | Object[] | 下拉选项值。 |
| `is_removable` | Number | 是否允许删除。 |
| `is_name_editable` | Number | 是否允许修改名称。 |
| `is_options_editable` | Number | 是否允许修改下拉选项值。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个项目属性

**路径:** `/v1/pjm/project_properties/{property_id}`

用于查看一个项目属性。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `property_id` | String | 是 | 项目属性的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 项目属性的id。 |
| `url` | String | 项目属性的地址。 |
| `name` | String | 项目属性的名称。 |
| `type` | String | 项目属性的类型。 |
| `options` | Object[] | 下拉选项值。 |
| `is_removable` | Number | 是否允许删除。 |
| `is_name_editable` | Number | 是否允许修改名称。 |
| `is_options_editable` | Number | 是否允许修改下拉选项值。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个项目流程

**路径:** `/v1/pjm/processes/{process_id}`

用于查看一个项目流程。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `process_id` | String | 是 | 项目流程的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 项目流程的id。 |
| `url` | String | 项目流程的资源地址。 |
| `name` | String | 项目流程的名称。 |
| `type` | String | 项目流程的类型。 |
| `description` | String | 项目流程的描述。 |
| `is_system` | Number | 是否为系统内置流程。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个项目状态

**路径:** `/v1/pjm/project_states/{state_id}`

用于查看一个项目状态。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `state_id` | String | 是 | 项目状态的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 项目状态的id。 |
| `url` | String | 项目状态的地址。 |
| `name` | String | 项目状态的名称。 |
| `type` | String | 项目状态的类型。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取全部项目流程

**路径:** `/v1/pjm/processes`

用于查询全部项目流程。

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 项目流程全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取项目属性列表

**路径:** `/v1/pjm/project_properties`

用于查询项目属性列表。

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 项目属性全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `PATCH` 部分更新一个项目属性

**路径:** `/v1/pjm/project_properties/{property_id}`

用于部分更新一个项目属性。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `property_id` | String | 是 | 项目属性的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 否 | 项目属性的名称。在一个企业中这个名称是唯一的。 |
| `options` | Object[] | 否 | 选择项列表。`options`是整体更新的。 |
| `options._id` | Sting | 否 | 选择项的`_id`。如果`option`中不包含用于确定唯一性的`_id`，那么这个`option`将被视为新建，并为之创建新的`_id`。 |
| `options.text` | String | 是 | 选择项内容。 |
| `options.parent_id` | String | 否 | 选择项父级id。当属性类型为`cascade_select,cascade_multi_select`时，`parent_id`参数有效，用于构建级联类型选择项之间的父子关系，最多存在4级。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 项目属性的id。 |
| `url` | String | 项目属性的地址。 |
| `name` | String | 项目属性的名称。 |
| `type` | String | 项目属性的类型。 |
| `options` | Object[] | 下拉选项值。 |
| `is_removable` | Number | 是否允许删除。 |
| `is_name_editable` | Number | 是否允许修改名称。 |
| `is_options_editable` | Number | 是否允许修改下拉选项值。 |

**权限:** 企业令牌/用户令牌

---
