# 🧪 测试管理 — API 详细文档

> 本文档包含 70 个接口的完整参数说明。
> 来源: https://open.pingcode.com/

---

## 执行用例配置

### `GET` 获取一个执行用例执行结果

**路径:** `/v1/testhub/run_statuses/{status_id}`

用于查看一个执行用例执行结果。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `status_id` | String | 是 | 执行用例执行结果的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 执行用例执行结果的id。 |
| `url` | String | 执行用例执行结果的资源地址。 |
| `name` | String | 执行用例执行结果的名称。 |
| `is_system` | Number | 是否为系统内置结果。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取全部执行用例执行结果列表

**路径:** `/v1/testhub/run_statuses`

用于查询全部执行用例执行结果列表。

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_index` | Number | 页码，从0开始。 |
| `page_size` | Number | 每页条数。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 全部执行用例执行结果全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
## 测试库

### `POST` 创建一个测试库

**路径:** `/v1/testhub/libraries`

用于创建一个测试库。

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `scope_type` | String | 否 | 测试库的所属类型。默认值`organization`。允许值分别表示企业可见和团队可见。 |
| `scope_id` | String | 否 | 测试库的所属id。当`scope_type`为`user_group`时，该字段必填，且表示团队id；当`scope_type`为其他值时，该字段无效。 |
| `name` | String | 是 | 测试库的名称。 |
| `visibility` | String | 否 | 测试库的可见范围。允许值分别表示组织全部成员可见和仅项目成员可见。 |
| `identifier` | String | 是 | 测试库的标识。在一个企业中这个标识是唯一的。项目的标识由大写英文字母/数字/下划线/连接线组成（不超过15个字符）。 |
| `description` | String | 否 | 测试库的描述。 |
| `members` | Object[] | 否 | 测试库成员的列表。当测试库的`scope_type`变为`user_group`时，测试库成员必须是`scope_id`指定的团队内的成员；当`scope_type`为其他值时，测试库成员可以是任意成员或团队。 |
| `members.id` | String | 是 | 企业成员或团队的id。 |
| `members.type` | String | 是 | 测试库成员的类型。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 测试库的id。 |
| `url` | String | 测试库的资源地址。 |
| `identifier` | String | 测试库的标识。 |
| `name` | String | 测试库的名称。 |
| `scope_type` | String | 测试库的所属类型。 |
| `scope_id` | String | 测试库的所属id。 |
| `visibility` | String | 测试库的可见性。 |
| `color` | String | 测试库的主题色。 |
| `description` | String | 测试库的描述。 |
| `members` | Object[] | 测试库的成员列表。 |
| `created_at` | Number | 测试库的创建时间。 |
| `created_by` | Object | 测试库的创建人。 |
| `updated_at` | Number | 测试库的更新时间。 |
| `updated_by` | Object | 测试库的更新人。 |
| `is_archived` | Number | 是否已归档。 |
| `is_deleted` | Number | 是否已删除。 |

**权限:** 企业令牌/用户令牌

---
### `POST` 向测试库中添加一个成员

**路径:** `/v1/testhub/libraries/{library_id}/members`

用于向测试库中添加一个成员。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `library_id` | String | 是 | 测试库的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `member` | Object | 否 | 测试库的成员。 |
| `member.id` | String | 是 | 企业成员或团队的id。 |
| `member.type` | String | 是 | 成员的类型。 |
| `role_id` | String | 否 | 角色的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 测试库成员的id。 |
| `url` | String | 测试库成员的资源地址。 |
| `library` | Object | 所属测试库的引用结构数据。 |
| `type` | String | 测试库成员的类型。 |
| `user` | Object | 企业成员的引用结构数据。当`type`为`user`时，该字段返回。 |
| `user_group` | Object | 团队的引用结构数据。当`type`为`user_group`时，该字段返回。 |
| `role` | Object | 成员角色的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `POST` 向测试库中添加一个用例模块

**路径:** `/v1/testhub/libraries/{library_id}/suites`

用于向测试库中添加一个用例模块。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `library_id` | String | 是 | 测试库的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 是 | 测试模块名称。测试模块为树形结构，同一层次下的名称不能重复。 |
| `parent_id` | String | 否 | 父测试模块的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 用例模块的id。 |
| `url` | String | 用例模块的资源地址。 |
| `library` | Object | 所属测试库的引用结构数据。 |
| `name` | String | 用例模块的名称。 |
| `parent` | Object | 父测试模块的引用结构数据。 |
| `paths` | String | 用例模块的路径，以`/`分隔。 |

**权限:** 企业令牌/用户令牌

---
### `DELETE` 在测试库中移除一个成员

**路径:** `/v1/testhub/libraries/{library_id}/members/{member_id}`

用于在测试库中移除一个成员。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `library_id` | String | 是 | 测试库的id。 |
| `member_id` | String | 是 | 企业成员或团队的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 测试库成员的id。 |
| `url` | String | 测试库成员的资源地址。 |
| `library` | Object | 所属测试库的引用结构数据。 |
| `type` | String | 测试库成员的类型。 |
| `user` | Object | 企业成员的引用结构数据。当`type`为`user`时，该字段返回。 |
| `user_group` | Object | 团队的引用结构数据。当`type`为`user_group`时，该字段返回。 |
| `role` | Object | 成员角色的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `DELETE` 在测试库中移除一个用例模块

**路径:** `/v1/testhub/libraries/{library_id}/suites/{suite_id}`

用于在测试库中移除一个用例模块。  请注意，删除一个模块会自动删除其所有的子模块。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `library_id` | String | 是 | 测试库的id。 |
| `suite_id` | String | 是 | 测试模块的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 用例模块的id。 |
| `url` | String | 用例模块的资源地址。 |
| `library` | Object | 所属测试库的引用结构数据。 |
| `name` | String | 用例模块的名称。 |
| `parent` | Object | 父测试模块的引用结构数据。 |
| `paths` | String | 用例模块的路径，以`/`分隔。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个测试库

**路径:** `/v1/testhub/libraries/{library_id}`

用于查看一个测试库。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `library_id` | String | 是 | 测试库的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 测试库的id。 |
| `url` | String | 测试库的资源地址。 |
| `identifier` | String | 测试库的标识。 |
| `name` | String | 测试库的名称。 |
| `scope_type` | String | 测试库的所属类型。 |
| `scope_id` | String | 测试库的所属id。 |
| `visibility` | String | 测试库的可见性。 |
| `color` | String | 测试库的主题色。 |
| `description` | String | 测试库的描述。 |
| `members` | Object[] | 测试库的成员列表。 |
| `created_at` | Number | 测试库的创建时间。 |
| `created_by` | Object | 测试库的创建人。 |
| `updated_at` | Number | 测试库的更新时间。 |
| `updated_by` | Object | 测试库的更新人。 |
| `is_archived` | Number | 是否已归档。 |
| `is_deleted` | Number | 是否已删除。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取测试库中的一个成员

**路径:** `/v1/testhub/libraries/{library_id}/members/{member_id}`

用于查看一个测试库成员。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `library_id` | String | 是 | 测试库的id。 |
| `member_id` | String | 是 | 测试库成员的id，即企业成员或团队的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 测试库成员的id。 |
| `url` | String | 测试库成员的资源地址。 |
| `library` | Object | 所属测试库的引用结构数据。 |
| `type` | String | 测试库成员的类型。 |
| `user` | Object | 企业成员的引用结构数据。当`type`为`user`时，该字段返回。 |
| `user_group` | Object | 团队的引用结构数据。当`type`为`user_group`时，该字段返回。 |
| `role` | Object | 成员角色的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取测试库中的一个用例模块

**路径:** `/v1/testhub/libraries/{library_id}/suites/{suite_id}`

用于查看一个用例模块。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `library_id` | String | 是 | 测试库的id。 |
| `suite_id` | String | 是 | 用例模块的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 用例模块的id。 |
| `url` | String | 用例模块的资源地址。 |
| `library` | Object | 所属测试库的引用结构数据。 |
| `name` | String | 用例模块的名称。 |
| `parent` | Object | 父测试模块的引用结构数据。 |
| `paths` | String | 用例模块的路径，以`/`分隔。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取测试库中的成员列表

**路径:** `/v1/testhub/libraries/{library_id}/members`

用于查询测试库中的成员列表。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `library_id` | String | 是 | 测试库的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 测试库中的成员全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取测试库中的用例模块列表

**路径:** `/v1/testhub/libraries/{library_id}/suites`

用于查询测试库中的用例模块列表。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `library_id` | String | 是 | 测试库的id。 |

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `parent_id` | String | 否 | 父测试模块的id。值可以是`root`或者某个模块id，当为空时，获取到所有的模块，当为`root`时，获取到所有的一级模块，当为某个模块id时，获取到该模块的直属子模块。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 测试库中的用例模块全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取测试库列表

**路径:** `/v1/testhub/libraries`

用于查询测试库列表。

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 否 | 测试库的名称。 |
| `scope_type` | String | 否 | 测试库的所属类型。 |
| `scope_id` | String | 否 | 测试库的所属id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 测试库全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `PATCH` 部分更新一个测试库

**路径:** `/v1/testhub/libraries/{library_id}`

用于部分更新一个测试库。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `library_id` | String | 是 | 测试库的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 否 | 测试库的名称。 |
| `identifier` | String | 否 | 测试库的标识。在一个企业中这个标识是唯一的。项目的标识由大写英文字母/数字/下划线/连接线组成（不超过15个字符）。 |
| `description` | String | 否 | 测试库的描述。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 测试库的id。 |
| `url` | String | 测试库的资源地址。 |
| `identifier` | String | 测试库的标识。 |
| `name` | String | 测试库的名称。 |
| `scope_type` | String | 测试库的所属类型。 |
| `scope_id` | String | 测试库的所属id。 |
| `visibility` | String | 测试库的可见性。 |
| `color` | String | 测试库的主题色。 |
| `description` | String | 测试库的描述。 |
| `members` | Object[] | 测试库的成员列表。 |
| `created_at` | Number | 测试库的创建时间。 |
| `created_by` | Object | 测试库的创建人。 |
| `updated_at` | Number | 测试库的更新时间。 |
| `updated_by` | Object | 测试库的更新人。 |
| `is_archived` | Number | 是否已归档。 |
| `is_deleted` | Number | 是否已删除。 |

**权限:** 企业令牌/用户令牌

---
### `PATCH` 部分更新一个测试库中用例模块

**路径:** `/v1/testhub/libraries/{library_id}/suites/{suite_id}`

用于部分更新一个测试库中用例模块。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `library_id` | String | 是 | 测试库的id。 |
| `suite_id` | String | 是 | 测试模块的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 否 | 测试模块名称。测试模块为树形结构，同一层次下的名称不能重复。 |
| `parent_id` | String | 否 | 父测试模块的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 测试库中用例模块的id。 |
| `url` | String | 测试库中用例模块的资源地址。 |
| `library` | Object | 所属测试库的引用结构数据。 |
| `name` | String | 测试库中用例模块的名称。 |
| `parent` | Object | 父测试模块的引用结构数据。 |
| `paths` | String | 用例模块的路径，以`/`分隔。 |

**权限:** 企业令牌/用户令牌

---
### `PATCH` 部分更新一个测试库内的成员

**路径:** `/v1/testhub/libraries/{library_id}/members/{member_id}`

用于部分更新一个测试库内的成员。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `library_id` | String | 是 | 测试库的id。 |
| `member_id` | String | 是 | 企业成员或团队的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `role_id` | String | 否 | 角色的id。管理员可以更改其他用户的角色，但非管理员用户无权更改其他用户的角色。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 测试库成员的id。 |
| `url` | String | 测试库成员的资源地址。 |
| `library` | Object | 所属测试库的引用结构数据。 |
| `type` | String | 测试库成员的类型。 |
| `user` | Object | 企业成员的引用结构数据。当`type`为`user`时，该字段返回。 |
| `user_group` | Object | 团队的引用结构数据。当`type`为`user_group`时，该字段返回。 |
| `role` | Object | 成员角色的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
## 测试管理

### `` 测试库

**路径:** `测试库`

---
### `` 测试库

**路径:** `测试库`

---
### `` 测试库

**路径:** `测试库`

---
### `` 测试配置中心

**路径:** `测试配置中心`

---
### `` 用例

**路径:** `用例`

---
### `` 用例

**路径:** `用例`

---
### `` 用例

**路径:** `用例`

---
### `` 用例

**路径:** `用例`

---
### `` 用例

**路径:** `用例`

---
### `` 用例

**路径:** `用例`

---
### `` 计划

**路径:** `计划`

---
### `` 计划

**路径:** `计划`

---
### `` 计划

**路径:** `计划`

---
### `` 计划

**路径:** `计划`

---
### `` 计划

**路径:** `计划`

---
### `` 计划

**路径:** `计划`

---
## 测试配置中心

### `` 执行用例配置

**路径:** `执行用例配置`

---
### `` 执行用例配置

**路径:** `执行用例配置`

---
### `` 用例配置

**路径:** `用例配置`

---
### `` 用例配置

**路径:** `用例配置`

---
### `` 用例配置

**路径:** `用例配置`

---
### `` 用例配置

**路径:** `用例配置`

---
### `` 用例配置

**路径:** `用例配置`

---
### `` 用例配置

**路径:** `用例配置`

---
### `` 计划配置

**路径:** `计划配置`

---
### `` 计划配置

**路径:** `计划配置`

---
## 用例

### `POST` 创建一个用例

**路径:** `/v1/testhub/cases`

用于创建一个用例。

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `test_library_id` | String | 是 | 测试库的id。 |
| `title` | String | 是 | 测试用例的标题。 |
| `suite_id` | String | 否 | 测试用例所属模块的id。 |
| `type_id` | String | 否 | 测试用例类型的id。 |
| `important_level_id` | String | 否 | 测试用例重要程度的id。 |
| `maintenance_id` | String | 否 | 测试用例维护人的id。 |
| `participant_ids` | String[] | 否 | 测试用例关注人的id列表。 |
| `properties` | Object | 否 | 测试用例属性的键值对集合，需要注意的是，当前测试用例对应的属性方案需要包含这些测试用例属性，例如属性方案中包含`prop_a`和`prop_b`。 |
| `properties.prop_a` | Object | 否 | 测试用例属性`prop_a`。 |
| `properties.prop_b` | Object | 否 | 测试用例属性`prop_b`。 |
| `description` | String | 否 | 测试用例的描述。 |
| `precondition` | String | 否 | 测试用例的前置条件。 |
| `steps` | Object[] | 否 | 测试用例的步骤列表。steps是整体更新的。 |
| `steps.step_id` | String | 否 | 测试用例步骤的id。 |
| `steps.description` | String | 否 | 测试用例步骤的描述。 |
| `steps.expected_value` | String | 否 | 测试用例步骤的期望值。 |
| `steps.is_group` | Boolean | 否 | 测试用例步骤类型是否为分组。 |
| `steps.group_id` | String | 否 | 测试用例步骤所属分组的id。`group_id`是分组类型步骤的`step_id`，分组类型的步骤不需要该参数。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 用例的id。 |
| `url` | String | 用例的资源地址。 |
| `library` | Object | 用例所属的测试库。 |
| `identifier` | String | 用例的标识。 |
| `title` | String | 用例的标题。 |
| `level` | String | 用例重要程度的名字。 |
| `short_id` | String | 用例的短id。 |
| `html_url` | String | 用例的html地址。 |
| `important_level` | Object | 用例的重要程度。 |
| `suite` | Object | 用例所属的测试模块。 |
| `state` | Object | 用例的状态。 |
| `type` | Object | 用例的类型。 |
| `maintenance` | Object | 用例的维护人。 |
| `test_type` | String | 用例的测试类型。允许值分别表示自动测试和手动测试。 |
| `description` | String | 用例的描述。 |
| `precondition` | String | 用例的前置条件。 |
| `properties` | Object | 用例的自定义属性。 |
| `estimated_workload` | Number | 用例的预估工时。 |
| `remaining_workload` | Number | 用例的剩余工时。 |
| `steps` | Object[] | 用例的步骤列表。 |
| `participants` | Object[] | 用例的关注人列表。 |
| `created_at` | Number | 用例的创建时间。 |
| `created_by` | Object | 用例的创建人。 |
| `updated_at` | Number | 用例的更新时间。 |
| `updated_by` | Object | 用例的更新人。 |
| `is_archived` | Number | 是否已归档。 |
| `is_deleted` | Number | 是否已删除。 |

**权限:** 企业令牌/用户令牌

---
### `DELETE` 删除一个用例

**路径:** `/v1/testhub/cases/{case_id}`

用于删除一个用例。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `case_id` | String | 是 | 测试用例的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 用例的id。 |
| `url` | String | 用例的资源地址。 |
| `library` | Object | 用例所属的测试库。 |
| `identifier` | String | 用例的标识。 |
| `title` | String | 用例的标题。 |
| `level` | String | 用例重要程度的名字。 |
| `short_id` | String | 用例的短id。 |
| `html_url` | String | 用例的html地址。 |
| `important_level` | Object | 用例的重要程度。 |
| `suite` | Object | 用例所属的测试模块。 |
| `state` | Object | 用例的状态。 |
| `type` | Object | 用例的类型。 |
| `maintenance` | Object | 用例的维护人。 |
| `test_type` | String | 用例的测试类型。允许值分别表示自动测试和手动测试。 |
| `description` | String | 用例的描述。 |
| `precondition` | String | 用例的前置条件。 |
| `properties` | Object | 用例的自定义属性。 |
| `estimated_workload` | Number | 用例的预估工时。 |
| `remaining_workload` | Number | 用例的剩余工时。 |
| `steps` | Object[] | 用例的步骤列表。 |
| `participants` | Object[] | 用例的关注人列表。 |
| `created_at` | Number | 用例的创建时间。 |
| `created_by` | Object | 用例的创建人。 |
| `updated_at` | Number | 用例的更新时间。 |
| `updated_by` | Object | 用例的更新人。 |
| `is_archived` | Number | 是否已归档。 |
| `is_deleted` | Number | 是否已删除。 |

**权限:** 企业令牌/用户令牌

---
### `POST` 批量创建用例

**路径:** `/v1/testhub/cases/bulk`

用于批量创建用例。

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `cases` | Object[] | 是 | 创建单个测试用例必要参数的数组，数组内对象不能超过100个。 |
| `cases.test_library_id` | String | 是 | 测试用例所属测试库id。 |
| `cases.title` | String | 是 | 测试用例的标题，长度1～200有效字符。 |
| `cases.important_level_id` | String | 否 | 测试用例重要程度的id。 |
| `cases.maintenance_id` | String | 否 | 测试用例维护人的id。 |
| `cases.participant_ids` | String[] | 否 | 测试用例关注人的id列表。 |
| `cases.properties` | String | 否 | 测试用例属性的键值对集合。 |
| `cases.description` | String | 否 | 测试用例的描述。 |
| `cases.precondition` | String | 否 | 测试用例的前置条件。 |
| `cases.steps` | Object[] | 否 | 测试用例的步骤列表。 |
| `cases.steps.step_id` | String | 否 | 测试用例步骤的id。 |
| `cases.steps.description` | String | 否 | 测试用例步骤的描述。 |
| `cases.steps.expected_value` | String | 否 | 测试用例步骤的期望值。 |
| `cases.steps.is_group` | Boolean | 否 | 测试用例步骤类型是否为分组。 |
| `cases.steps.group_id` | String | 否 | 测试用例步骤所属分组的id。`group_id`是分组类型步骤的`step_id`，分组类型的步骤不需要该参数。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `state` | String | 操作状态。 |
| `case` | Object | 测试用例的全量结构数据。操作成功时返回。 |

**权限:** 企业令牌/用户令牌

---
### `PATCH` 批量部分更新用例

**路径:** `/v1/testhub/cases/bulk`

用于批量部分更新用例。

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `cases` | Object[] | 是 | 部分更新测试用例的数组。 |
| `cases.case_id` | String | 是 | 测试用例的id。 |
| `cases.state_id` | String | 否 | 测试用例状态的id。 |
| `cases.type_id` | String | 否 | 测试用例类型的id。 |
| `cases.title` | String | 否 | 测试用例的标题。 |
| `cases.important_level_id` | String | 否 | 测试用例重要程度的id。 |
| `cases.maintenance_id` | String | 否 | 测试用例维护人的id。 |
| `cases.properties` | Object[] | 否 | 测试用例属性的键值对集合，property中包含propertyKey、propertyValue和propertyType三个字段。需要注意的是，当前测试用例对应的属性方案需要包含这些测试用例属性。 |
| `cases.properties.prop_a` | Object | 否 | 测试用例属性的自定义属性prop_a。 |
| `cases.properties.prop_b` | Object | 否 | 测试用例属性的自定义属性prop_b。 |
| `cases.description` | String | 否 | 测试用例的备注。 |
| `cases.precondition` | String | 否 | 测试用例的前置条件。 |
| `cases.steps` | Object[] | 否 | 测试用例的步骤列表。steps是整体更新的。 |
| `cases.steps.step_id` | String | 否 | 测试用例的步骤的id。如果step中不包含用于确定唯一性的`step_id`，那么这个step将被视为新建，并为之创建新的`step_id`。 |
| `cases.steps.description` | String | 否 | 测试用例的步骤的描述。 |
| `cases.steps.expected_value` | String | 否 | 测试用例的步骤的期望值。 |
| `cases.steps.is_group` | Boolean | 否 | 测试用例步骤类型是否为分组。 |
| `cases.steps.group_id` | String | 否 | 测试用例步骤所属分组的id。`group_id`是分组类型步骤的`step_id`，分组类型的步骤不需要该参数。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `state` | String | 操作状态。 |
| `case` | Object | 测试用例的全量结构数据。操作成功时返回。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个用例

**路径:** `/v1/testhub/cases/{case_id}`

用于查看一个用例。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `case_id` | String | 是 | 测试用例的id或short_id。 |

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `include_public_image_token` | String | 否 | 包含获取图片资源token的属性。使用','分割，最多只能20个，支持`description`和自定义多行文本类型的属性。参数示例`description,properties.prop_b`。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 用例的id。 |
| `url` | String | 用例的资源地址。 |
| `library` | Object | 用例所属的测试库。 |
| `identifier` | String | 用例的标识。 |
| `title` | String | 用例的标题。 |
| `level` | String | 用例重要程度的名字。 |
| `short_id` | String | 用例的短id。 |
| `html_url` | String | 用例的html地址。 |
| `important_level` | Object | 用例的重要程度。 |
| `suite` | Object | 用例所属的测试模块。 |
| `state` | Object | 用例的状态。 |
| `type` | Object | 用例的类型。 |
| `maintenance` | Object | 用例的维护人。 |
| `test_type` | String | 用例的测试类型。允许值分别表示自动测试和手动测试。 |
| `description` | String | 用例的描述。 |
| `precondition` | String | 用例的前置条件。 |
| `properties` | Object | 用例的自定义属性。 |
| `estimated_workload` | Number | 用例的预估工时。 |
| `remaining_workload` | Number | 用例的剩余工时。 |
| `steps` | Object[] | 用例的步骤列表。 |
| `participants` | Object[] | 用例的关注人列表。 |
| `public_image_token` | String | 用例描述和自定义多行文本类型属性里获取图片资源token。获取一个用例和获取用例列表参数`include_public_image_token`值有效时返回。 |
| `created_at` | Number | 用例的创建时间。 |
| `created_by` | Object | 用例的创建人。 |
| `updated_at` | Number | 用例的更新时间。 |
| `updated_by` | Object | 用例的更新人。 |
| `is_archived` | Number | 是否已归档。 |
| `is_deleted` | Number | 是否已删除。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取用例列表

**路径:** `/v1/testhub/cases`

用于查询用例列表。

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `library_id` | String | 否 | 测试库的id。 |
| `maintenance_id` | String | 否 | 维护人的id。 |
| `state_ids` | String | 否 | 状态的id，使用','分割，最多只能20个。 |
| `important_level_ids` | String | 否 | 重要程度的id，使用','分割，最多只能20个。 |
| `tag_ids` | String | 否 | 标签的id，使用','分割，最多只能20个。 |
| `created_between` | String | 否 | 创建时间介于的时间范围，通过','分割起始时间。 |
| `updated_between` | String | 否 | 更新时间介于的时间范围，通过','分割起始时间。 |
| `include_public_image_token` | String | 否 | 包含获取图片资源token的属性。使用','分割，最多只能20个，支持`description`和自定义多行文本类型的属性。参数示例`description,properties.prop_b`。 |
| `include_deleted` | Boolean | 否 | 是否查询已删除的用例。该值默认为`false`。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 用例全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取用例属性列表

**路径:** `/v1/testhub/case/properties?library_id={library_id}`

用于查询用例属性列表。

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `library_id` | String | 是 | 测试库的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 用例属性的全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取用例模块列表

**路径:** `/v1/testhub/case/suites?library_id={library_id}`

用于查询用例模块列表。

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `library_id` | String | 是 | 测试库的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 用例模块的全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取用例状态列表

**路径:** `/v1/testhub/case/states?library_id={library_id}`

用于查询用例状态列表。

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `library_id` | String | 是 | 测试库的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_index` | Number | 页码，从0开始。 |
| `page_size` | Number | 每页条数。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 用例状态全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取用例的执行历史列表

**路径:** `/v1/testhub/cases/{case_id}/histories`

用于查询用例的执行历史列表。  获取测试用例所有执行用例的最后一次执行结果。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `case_id` | String | 是 | 测试用例的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 用例的执行历史的全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取用例类型列表

**路径:** `/v1/testhub/case/types?library_id={library_id}`

用于查询用例类型列表。

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `library_id` | String | 是 | 测试库的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 用例类型的全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `PATCH` 部分更新一个用例

**路径:** `/v1/testhub/cases/{case_id}`

用于部分更新一个用例。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `case_id` | String | 是 | 测试用例的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `suite_id` | String | 否 | 测试用例所属模块的id。 |
| `state_id` | String | 否 | 测试用例状态的id。 |
| `type_id` | String | 否 | 测试用例类型的id。 |
| `title` | String | 否 | 测试用例的标题。 |
| `important_level_id` | String | 否 | 测试用例重要程度的id。 |
| `maintenance_id` | String | 否 | 测试用例维护人的id。 |
| `properties` | Object | 否 | 测试用例属性的键值对集合。需要注意的是，当前测试用例对应的属性方案需要包含这些测试用例属性。 |
| `properties.prop_a` | Object | 否 | 测试用例属性`prop_a`。 |
| `properties.prop_b` | Object | 否 | 测试用例属性`prop_b`。 |
| `description` | String | 否 | 测试用例的备注。 |
| `precondition` | String | 否 | 测试用例的前置条件。 |
| `steps` | Object[] | 否 | 测试用例的步骤列表。steps是整体更新的。 |
| `steps.step_id` | String | 否 | 测试用例的步骤的id。如果step中不包含用于确定唯一性的`step_id`，那么这个step将被视为新建，并为之创建新的`step_id`。 |
| `steps.description` | String | 否 | 测试用例的步骤的描述。 |
| `steps.expected_value` | String | 否 | 测试用例的步骤的期望值。 |
| `steps.is_group` | Boolean | 否 | 测试用例步骤类型是否为分组。 |
| `steps.group_id` | String | 否 | 测试用例步骤所属分组的id。`group_id`是分组类型步骤的`step_id`，分组类型的步骤不需要该参数。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 用例的id。 |
| `url` | String | 用例的资源地址。 |
| `library` | Object | 用例所属的测试库。 |
| `identifier` | String | 用例的标识。 |
| `title` | String | 用例的标题。 |
| `level` | String | 用例重要程度的名字。 |
| `short_id` | String | 用例的短id。 |
| `html_url` | String | 用例的html地址。 |
| `important_level` | Object | 用例的重要程度。 |
| `suite` | Object | 用例所属的测试模块。 |
| `state` | Object | 用例的状态。 |
| `type` | Object | 用例的类型。 |
| `maintenance` | Object | 用例的维护人。 |
| `test_type` | String | 用例的测试类型。允许值分别表示自动测试和手动测试。 |
| `description` | String | 用例的描述。 |
| `precondition` | String | 用例的前置条件。 |
| `properties` | Object | 用例的自定义属性。 |
| `estimated_workload` | Number | 用例的预估工时。 |
| `remaining_workload` | Number | 用例的剩余工时。 |
| `steps` | Object[] | 用例的步骤列表。 |
| `participants` | Object[] | 用例的关注人列表。 |
| `created_at` | Number | 用例的创建时间。 |
| `created_by` | Object | 用例的创建人。 |
| `updated_at` | Number | 用例的更新时间。 |
| `updated_by` | Object | 用例的更新人。 |
| `is_archived` | Number | 是否已归档。 |
| `is_deleted` | Number | 是否已删除。 |

**权限:** 企业令牌/用户令牌

---
## 用例配置

### `POST` 创建一个用例属性

**路径:** `/v1/testhub/case_properties`

用于创建一个用例属性。

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 是 | 用例属性的名称。在一个企业中这个名称是唯一的。 |
| `type` | String | 是 | 用例属性的类型。 |
| `options` | Object[] | 否 | 选择项列表。当用例属性类型为`select,multi_select,cascade_select,cascade_multi_select`时可选填此项。 |
| `options._id` | String | 否 | 选择项id。该值在选择项中是唯一的。 |
| `options.text` | String | 是 | 选择项内容。该值在选择项中是唯一的。 |
| `options.parent_id` | String | 否 | 选择项父级id。当属性类型为`cascade_select,cascade_multi_select`时，`parent_id`参数有效，用于构建级联类型选择项之间的父子关系，最多存在4级。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 用例属性的id。 |
| `url` | String | 用例属性的资源地址。 |
| `name` | String | 用例属性的名称。 |
| `type` | String | 用例属性的类型。 |
| `options` | Object[] | 下拉选项值。 |
| `is_removable` | Number | 是否允许删除。 |
| `is_name_editable` | Number | 是否允许修改名称。 |
| `is_options_editable` | Number | 是否允许修改下拉选项值。 |

**权限:** 企业令牌/用户令牌

---
### `POST` 向属性方案中添加一个用例属性

**路径:** `/v1/testhub/case_property_plans/{property_plan_id}/case_properties`

用于向属性方案中添加一个用例属性。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `property_plan_id` | String | 是 | 测试用例属性方案的id。 |

**参数 (请求参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `property_id` | String | 是 | 测试用例属性的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 属性方案中用例属性关联的id。 |
| `url` | String | 属性方案中用例属性关联的资源地址。 |
| `property_plan` | Object | 用例属性方案的引用结构数据。 |
| `property` | Object | 用例属性的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `DELETE` 在属性方案中移除一个用例属性

**路径:** `/v1/testhub/case_property_plans/{property_plan_id}/case_properties/{property_id}`

用于在属性方案中移除一个用例属性。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `property_plan_id` | String | 是 | 测试用例属性方案的id。 |
| `property_id` | String | 是 | 测试用例属性的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 属性方案中用例属性关联的id。 |
| `url` | String | 属性方案中用例属性关联的资源地址。 |
| `property_plan` | Object | 用例属性方案的引用结构数据。 |
| `property` | Object | 用例属性的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个用例属性

**路径:** `/v1/testhub/case_properties/{property_id}`

用于查看一个用例属性。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `property_id` | String | 是 | 用例属性的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 用例属性的id。 |
| `url` | String | 用例属性的资源地址。 |
| `name` | String | 用例属性的名称。 |
| `type` | String | 用例属性的类型。 |
| `options` | Object[] | 下拉选项值。 |
| `is_removable` | Number | 是否允许删除。 |
| `is_name_editable` | Number | 是否允许修改名称。 |
| `is_options_editable` | Number | 是否允许修改下拉选项值。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个用例属性方案

**路径:** `/v1/testhub/case_property_plans/{property_plan_id}`

用于查看一个用例属性方案。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `property_plan_id` | String | 是 | 用例属性方案的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 用例属性方案的id。 |
| `url` | String | 用例属性方案的资源地址。 |
| `category` | String | 用例属性方案的类别。 |
| `host` | String | 用例属性方案所属资源类型。 |
| `library` | Object | 用例属性方案关联测试库的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个用例状态

**路径:** `/v1/testhub/case_states/{state_id}`

用于查看一个用例状态。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `state_id` | String | 是 | 用例状态的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 用例状态的id。 |
| `url` | String | 用例状态的资源地址。 |
| `name` | String | 用例状态的名称。 |
| `type` | String | 用例状态的类型。 |
| `color` | String | 用例状态的颜色。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个用例类型

**路径:** `/v1/testhub/case_types/{type_id}`

用于查看一个用例类型。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `type_id` | String | 是 | 用例类型的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 用例类型的id。 |
| `url` | String | 用例类型的资源地址。 |
| `name` | String | 用例类型的名称。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个用例重要程度

**路径:** `/v1/testhub/case_important_levels/{important_level_id}`

用于查看一个用例重要程度。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `important_level_id` | String | 是 | 用例重要程度的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 用例重要程度的id。 |
| `url` | String | 用例重要程度的资源地址。 |
| `name` | String | 用例重要程度的名称。 |
| `color` | String | 用例重要程度的颜色。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取全部用例属性列表

**路径:** `/v1/testhub/case_properties`

用于查询全部用例属性列表。

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 用例属性的全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取全部用例状态列表

**路径:** `/v1/testhub/case_states`

用于查询全部用例状态列表。

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_index` | Number | 页码，从0开始。 |
| `page_size` | Number | 每页条数。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 全部用例状态全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取全部用例类型列表

**路径:** `/v1/testhub/case_types`

用于查询全部用例类型列表。

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 全部用例类型全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取全部重要程度列表

**路径:** `/v1/testhub/case_important_levels`

用于查询全部重要程度列表。

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 重要程度的全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取属性方案中的一个用例属性

**路径:** `/v1/testhub/case_property_plans/{property_plan_id}/case_properties/{property_id}`

用于查询属性方案中的一个用例属性。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `property_plan_id` | String | 是 | 用例属性方案的id。 |
| `property_id` | String | 是 | 用例属性的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 属性方案中用例属性关联的id。 |
| `url` | String | 属性方案中用例属性关联的资源地址。 |
| `property_plan` | Object | 用例属性方案的引用结构数据。 |
| `property` | Object | 用例属性的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取属性方案中的用例属性列表

**路径:** `/v1/testhub/case_property_plans/{property_plan_id}/case_properties`

用于查询属性方案中的用例属性列表。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `property_plan_id` | String | 是 | 测试用例属性方案的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 属性方案中的用例属性全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取用例属性方案列表

**路径:** `/v1/testhub/case_property_plans`

用于查询用例属性方案列表。

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `library_id` | String | 否 | 测试库的id。查询开启本地配置的方案时传入。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 用例属性方案全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `PATCH` 部分更新一个用例属性

**路径:** `/v1/testhub/case_properties/{property_id}`

用于部分更新一个用例属性。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `property_id` | String | 是 | 用例属性的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 否 | 用例属性的名称。在一个企业中这个名称是唯一的。 |
| `options` | Object[] | 否 | 选择项列表。`options`是整体更新的。当用例属性类型为`select,multi_select,cascade_select,cascade_multi_select`时可选填此项。 |
| `options._id` | String | 否 | 选择项id。该值在选择项中是唯一的。 |
| `options.text` | String | 是 | 选择项内容。该值在选择项中是唯一的。 |
| `options.parent_id` | String | 否 | 选择项父级id。当属性类型为`cascade_select,cascade_multi_select`时，`parent_id`参数有效，用于构建级联类型选择项之间的父子关系，最多存在4级。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 用例属性的id。 |
| `url` | String | 用例属性的资源地址。 |
| `name` | String | 用例属性的名称。 |
| `type` | String | 用例属性的类型。 |
| `options` | Object[] | 下拉选项值。 |
| `is_removable` | Number | 是否允许删除。 |
| `is_name_editable` | Number | 是否允许修改名称。 |
| `is_options_editable` | Number | 是否允许修改下拉选项值。 |

**权限:** 企业令牌/用户令牌

---
