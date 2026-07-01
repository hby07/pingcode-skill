# 📦 产品管理 — API 详细文档

> 本文档包含 85 个接口的完整参数说明。
> 来源: https://open.pingcode.com/

---

## 产品

### `` 产品成员

**路径:** `产品成员`

---
### `POST` 创建一个产品

**路径:** `/v1/ship/products`

用于创建一个产品。

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 是 | 产品的名称（不超过32个字符）。 |
| `identifier` | String | 是 | 产品的标识。在一个企业中这个标识是唯一的。产品的标识由大写英文字母/数字/下划线/连接线组成（不超过15个字符）。 |
| `description` | String | 否 | 产品的描述。 |
| `members` | Object[] | 否 | 产品成员的列表。 |
| `members.id` | String | 是 | 企业成员或团队的id。 |
| `members.type` | String | 是 | 产品成员的类型。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 产品的id。 |
| `url` | String | 产品的资源地址。 |
| `identifier` | String | 产品的标识。 |
| `name` | String | 产品的名称。 |
| `scope_type` | String | 产品的所属类型。 |
| `scope_id` | String | 产品的所属id。 |
| `visibility` | String | 产品的可见性。 |
| `color` | String | 产品的主题色。 |
| `description` | String | 产品的描述。 |
| `members` | Object[] | 产品的成员列表。 |
| `created_at` | Number | 创建时间，单位为秒。 |
| `created_by` | Object | 创建人的引用结构数据。 |
| `updated_at` | Number | 更新时间，单位为秒。 |
| `updated_by` | Object | 更新人的引用结构数据。 |
| `is_archived` | Number | 是否已归档。 |
| `is_deleted` | Number | 是否已删除。 |

**权限:** 企业令牌/用户令牌

---
### `POST` 创建一个外部用户

**路径:** `/v1/ship/products/{product_id}/users`

用于创建一个外部用户。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 产品的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 是 | 外部用户的名称。 |
| `email` | String | 否 | 外部用户的邮箱地址，邮箱地址和手机号其中一个必填。 |
| `mobile` | String | 否 | 外部用户的手机号，邮箱地址和手机号其中一个必填，如果同时存在，以手机号为准。 |
| `customer_id` | String | 否 | 外部用户所属客户的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 外部用户的id。 |
| `url` | String | 外部用户的资源地址。 |
| `name` | String | 外部用户的名称。 |
| `display_name` | String | 外部用户的显示名称。 |
| `avatar` | String | 外部用户的头像。 |
| `email` | String | 外部用户的邮箱地址。 |
| `mobile` | String | 外部用户的手机号。 |
| `product` | Object | 外部用户关联产品的引用结构数据。 |
| `customer` | Object | 外部用户所属客户的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `POST` 创建一个客户

**路径:** `/v1/ship/products/{product_id}/customers`

用于创建一个客户。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 产品的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 是 | 客户的名称。 |
| `assignee_id` | String | 否 | 客户的负责人id。 |
| `scale` | Number | 否 | 客户的规模。 |
| `description` | String | 否 | 客户的描述。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 客户的id。 |
| `url` | String | 客户的资源地址。 |
| `product` | Object | 客户关联产品的引用结构数据。 |
| `name` | String | 客户的名称。 |
| `assignee` | Object | 客户负责人的引用结构数据。 |
| `scale` | Number | 客户的规模。 |
| `description` | String | 客户的描述。 |
| `created_at` | Number | 创建时间，单位为秒。 |
| `created_by` | Object | 创建人的引用结构数据。 |
| `updated_at` | Number | 更新时间，单位为秒。 |
| `updated_by` | Object | 更新人的引用结构数据。 |
| `is_archived` | Number | 是否已归档。 |
| `is_deleted` | Number | 是否已删除。 |

**权限:** 企业令牌/用户令牌

---
### `DELETE` 删除一个外部用户

**路径:** `/v1/ship/products/{product_id}/users/{user_id}`

用于删除一个外部用户。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 产品的id。 |
| `user_id` | String | 是 | 外部用户的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 外部用户的id。 |
| `url` | String | 外部用户的资源地址。 |
| `name` | String | 外部用户的名称。 |
| `display_name` | String | 外部用户的显示名称。 |
| `avatar` | String | 外部用户的头像。 |
| `email` | String | 外部用户的邮箱地址。 |
| `mobile` | String | 外部用户的手机号。 |
| `product` | Object | 外部用户关联产品的引用结构数据。 |
| `customer` | Object | 外部用户所属客户的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `POST` 向产品中添加一个成员

**路径:** `/v1/ship/products/{product_id}/members`

用于向产品中添加一个成员。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 产品的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `member` | Object | 是 | 产品的成员。 |
| `member.id` | String | 是 | 企业成员或团队的id。 |
| `member.type` | String | 是 | 产品成员的类型。 |
| `role_id` | String | 否 | 角色的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 产品成员的id。 |
| `url` | String | 产品成员的资源地址。 |
| `product` | Object | 所属产品的引用结构数据。 |
| `type` | String | 产品成员的类型。 |
| `user` | Object | 企业成员的引用结构数据。当`type`为`user`时，该字段返回。 |
| `user_group` | Object | 团队的引用结构数据。当`type`为`user_group`时，该字段返回。 |
| `role` | Object | 成员角色的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `POST` 向产品中添加一个标签

**路径:** `/v1/ship/products/{product_id}/tags`

用于向产品中添加一个标签。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 产品的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 是 | 标签的名称。在一个产品中这个名称是唯一的。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 标签的id。 |
| `url` | String | 标签的资源地址。 |
| `product` | Object | 所属产品的引用结构数据。 |
| `name` | String | 标签的名称。 |
| `color` | String | 标签的颜色。 |

**权限:** 企业令牌/用户令牌

---
### `POST` 向产品中添加一个需求模块

**路径:** `/v1/ship/products/{product_id}/suites`

用于向产品中添加一个需求模块。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 产品的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 是 | 模块名称。需求模块为树形结构，同一层次下的名称不能重复。 |
| `type` | String | 是 | 模块类型。允许值分别表示子产品和模块。 |
| `parent_id` | String | 否 | 父模块的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 需求模块的id。 |
| `url` | String | 需求模块的资源地址。 |
| `product` | Object | 所属产品的引用结构数据。 |
| `name` | String | 需求模块的名称。 |
| `type` | String | 需求模块的类型。 |
| `parent` | Object | 父级需求模块的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `DELETE` 在产品中移除一个成员

**路径:** `/v1/ship/products/{product_id}/members/{member_id}`

用于在产品中移除一个成员。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 产品的id。 |
| `member_id` | String | 是 | 企业成员或团队的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 产品成员的id。 |
| `url` | String | 产品成员的资源地址。 |
| `product` | Object | 所属产品的引用结构数据。 |
| `type` | String | 产品成员的类型。 |
| `user` | Object | 企业成员的引用结构数据。当`type`为`user`时，该字段返回。 |
| `user_group` | Object | 团队的引用结构数据。当`type`为`user_group`时，该字段返回。 |
| `role` | Object | 成员角色的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `DELETE` 在产品中移除一个标签

**路径:** `/v1/ship/products/{product_id}/tags/{tag_id}`

用于在产品中移除一个标签。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 产品的id。 |
| `tag_id` | String | 是 | 标签的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 标签的id。 |
| `url` | String | 标签的资源地址。 |
| `product` | Object | 所属产品的引用结构数据。 |
| `name` | String | 标签的名称。 |
| `color` | String | 标签的颜色。 |

**权限:** 企业令牌/用户令牌

---
### `DELETE` 在产品中移除一个需求模块

**路径:** `/v1/ship/products/{product_id}/suites/{suite_id}`

用于在产品中移除一个需求模块。  请注意，删除一个模块会自动删除其所有的子模块。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 产品的id。 |
| `suite_id` | String | 是 | 模块id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 需求模块的id。 |
| `url` | String | 需求模块的资源地址。 |
| `product` | Object | 所属产品的引用结构数据。 |
| `name` | String | 需求模块的名称。 |
| `type` | String | 需求模块的类型。 |
| `parent` | Object | 父级需求模块的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `` 外部用户

**路径:** `外部用户`

---
### `` 客户

**路径:** `客户`

---
### `` 标签

**路径:** `标签`

---
### `GET` 获取一个产品

**路径:** `/v1/ship/products/{product_id}`

用于查看一个产品。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 产品的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 产品的id。 |
| `url` | String | 产品的资源地址。 |
| `identifier` | String | 产品的标识。 |
| `name` | String | 产品的名称。 |
| `scope_type` | String | 产品的所属类型。 |
| `scope_id` | String | 产品的所属id。 |
| `visibility` | String | 产品的可见性。 |
| `color` | String | 产品的主题色。 |
| `description` | String | 产品的描述。 |
| `members` | Object[] | 产品的成员列表。 |
| `created_at` | Number | 创建时间，单位为秒。 |
| `created_by` | Object | 创建人的引用结构数据。 |
| `updated_at` | Number | 更新时间，单位为秒。 |
| `updated_by` | Object | 更新人的引用结构数据。 |
| `is_archived` | Number | 是否已归档。 |
| `is_deleted` | Number | 是否已删除。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个外部用户

**路径:** `/v1/ship/products/{product_id}/users/{user_id}`

用于查看一个外部用户。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 产品的id。 |
| `user_id` | String | 是 | 外部用户的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 外部用户的id。 |
| `url` | String | 外部用户的资源地址。 |
| `name` | String | 外部用户的名称。 |
| `display_name` | String | 外部用户的显示名称。 |
| `avatar` | String | 外部用户的头像。 |
| `email` | String | 外部用户的邮箱地址。 |
| `mobile` | String | 外部用户的手机号。 |
| `product` | Object | 外部用户关联产品的引用结构数据。 |
| `customer` | Object | 外部用户所属客户的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个客户

**路径:** `/v1/ship/products/{product_id}/customers/{customer_id}`

用于查看一个客户。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 产品的id。 |
| `customer_id` | String | 是 | 客户的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 客户的id。 |
| `url` | String | 客户的资源地址。 |
| `product` | Object | 客户关联产品的引用结构数据。 |
| `name` | String | 客户的名称。 |
| `assignee` | Object | 客户负责人的引用结构数据。 |
| `scale` | Number | 客户的规模。 |
| `description` | String | 客户的描述。 |
| `created_at` | Number | 创建时间，单位为秒。 |
| `created_by` | Object | 创建人的引用结构数据。 |
| `updated_at` | Number | 更新时间，单位为秒。 |
| `updated_by` | Object | 更新人的引用结构数据。 |
| `is_archived` | Number | 是否已归档。 |
| `is_deleted` | Number | 是否已删除。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取产品中的一个工单渠道

**路径:** `/v1/ship/products/{product_id}/channels/{channel_id}`

用于查看一个工单渠道。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 产品的id。 |
| `channel_id` | String | 是 | 工单渠道的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工单渠道的id。 |
| `url` | String | 工单渠道的资源地址。 |
| `name` | String | 工单渠道的名称。 |
| `product` | Object | 工单渠道关联产品的引用结构数据。 |
| `description` | String | 工单渠道的描述。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取产品中的一个工单类型

**路径:** `/v1/ship/products/{product_id}/ticket_types/{ticket_type_id}`

用于查询产品中的一个工单类型。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 产品的id。 |
| `ticket_type_id` | String | 是 | 工单类型的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 产品中工单类型关联的id。 |
| `url` | String | 产品中工单类型关联的资源地址。 |
| `product` | Object | 产品的引用结构数据。 |
| `ticket_type` | Object | 工单类型的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取产品中的一个成员

**路径:** `/v1/ship/products/{product_id}/members/{member_id}`

用于查看一个产品成员。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 产品的id。 |
| `member_id` | String | 是 | 产品成员的id，即企业成员或团队的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 产品成员的id。 |
| `url` | String | 产品成员的资源地址。 |
| `product` | Object | 所属产品的引用结构数据。 |
| `type` | String | 产品成员的类型。 |
| `user` | Object | 企业成员的引用结构数据。当`type`为`user`时，该字段返回。 |
| `user_group` | Object | 团队的引用结构数据。当`type`为`user_group`时，该字段返回。 |
| `role` | Object | 成员角色的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取产品中的一个标签

**路径:** `/v1/ship/products/{product_id}/tags/{tag_id}`

用于查看一个标签。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 产品的id。 |
| `tag_id` | String | 是 | 标签的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 标签的id。 |
| `url` | String | 标签的资源地址。 |
| `product` | Object | 所属产品的引用结构数据。 |
| `name` | String | 标签的名称。 |
| `color` | String | 标签的颜色。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取产品中的一个需求排期

**路径:** `/v1/ship/products/{product_id}/plans/{plan_id}`

用于查看一个需求排期。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 产品的id。 |
| `plan_id` | String | 是 | 需求排期的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 需求排期的id。 |
| `url` | String | 需求排期的资源地址。 |
| `product` | Object | 需求排期所属产品的引用结构数据。 |
| `name` | String | 需求排期的名称。 |
| `assignee` | Object | 需求排期负责人的引用结构数据。 |
| `start_at` | Number | 需求排期的开始时间，单位为秒。 |
| `end_at` | Number | 需求排期的结束时间，单位为秒。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取产品中的一个需求模块

**路径:** `/v1/ship/products/{product_id}/suites/{suite_id}`

用于查看一个需求模块。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 产品的id。 |
| `suite_id` | String | 是 | 需求模块的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 需求模块的id。 |
| `url` | String | 需求模块的资源地址。 |
| `product` | Object | 所属产品的引用结构数据。 |
| `name` | String | 需求模块的名称。 |
| `type` | String | 需求模块的类型。 |
| `parent` | Object | 父级需求模块的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取产品中的工单渠道列表

**路径:** `/v1/ship/products/{product_id}/channels`

用于查询产品中的工单渠道列表。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 产品的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 产品中的工单渠道全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取产品中的工单类型列表

**路径:** `/v1/ship/products/{product_id}/ticket_types`

用于查询产品中的工单类型列表。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 产品的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 产品中的工单类型全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取产品中的成员列表

**路径:** `/v1/ship/products/{product_id}/members`

用于查询产品中的成员列表。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 产品的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 产品成员全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取产品中的标签列表

**路径:** `/v1/ship/products/{product_id}/tags`

用于查询产品中的标签列表。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 产品的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 产品中的标签全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取产品中的需求排期列表

**路径:** `/v1/ship/products/{product_id}/plans`

用于查询产品中的需求排期列表。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 产品的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 产品中的需求排期全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取产品中的需求模块列表

**路径:** `/v1/ship/products/{product_id}/suites`

用于查询产品中的需求模块列表。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 产品的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 产品中的需求模块全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取产品列表

**路径:** `/v1/ship/products`

用于查询产品列表。

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 产品全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取外部用户列表

**路径:** `/v1/ship/products/{product_id}/users`

用于查询外部用户列表。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 产品的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 外部用户全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取客户列表

**路径:** `/v1/ship/products/{product_id}/customers`

用于查询客户列表。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 产品的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 客户全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `PATCH` 部分更新一个产品

**路径:** `/v1/ship/products/{product_id}`

用于部分更新一个产品。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 产品的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 否 | 产品的名称（不超过32个字符）。 |
| `identifier` | String | 否 | 产品的标识。在一个企业中这个标识是唯一的。产品的标识由大写英文字母/数字/下划线/连接线组成（不超过15个字符）。 |
| `description` | String | 否 | 产品的描述。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 产品的id。 |
| `url` | String | 产品的资源地址。 |
| `identifier` | String | 产品的标识。 |
| `name` | String | 产品的名称。 |
| `scope_type` | String | 产品的所属类型。 |
| `scope_id` | String | 产品的所属id。 |
| `visibility` | String | 产品的可见性。 |
| `color` | String | 产品的主题色。 |
| `description` | String | 产品的描述。 |
| `members` | Object[] | 产品的成员列表。 |
| `created_at` | Number | 创建时间，单位为秒。 |
| `created_by` | Object | 创建人的引用结构数据。 |
| `updated_at` | Number | 更新时间，单位为秒。 |
| `updated_by` | Object | 更新人的引用结构数据。 |
| `is_archived` | Number | 是否已归档。 |
| `is_deleted` | Number | 是否已删除。 |

**权限:** 企业令牌/用户令牌

---
### `PATCH` 部分更新一个外部用户

**路径:** `/v1/ship/products/{product_id}/users/{user_id}`

用于部分更新一个外部用户。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 产品的id。 |
| `user_id` | String | 是 | 外部用户的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `customer_id` | String | 否 | 外部用户所属客户的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 外部用户的id。 |
| `url` | String | 外部用户的资源地址。 |
| `name` | String | 外部用户的名称。 |
| `display_name` | String | 外部用户的显示名称。 |
| `avatar` | String | 外部用户的头像。 |
| `email` | String | 外部用户的邮箱地址。 |
| `mobile` | String | 外部用户的手机号。 |
| `product` | Object | 外部用户关联产品的引用结构数据。 |
| `customer` | Object | 外部用户所属客户的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `PATCH` 部分更新一个客户

**路径:** `/v1/ship/products/{product_id}/customers/{customer_id}`

用于部分更新一个客户。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 产品的id。 |
| `customer_id` | String | 是 | 客户的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 否 | 客户的名称。 |
| `assignee_id` | String | 否 | 客户的负责人id。 |
| `scale` | Number | 否 | 客户的规模。 |
| `description` | String | 否 | 客户的描述。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 客户的id。 |
| `url` | String | 客户的资源地址。 |
| `product` | Object | 客户关联产品的引用结构数据。 |
| `name` | String | 客户的名称。 |
| `assignee` | Object | 客户负责人的引用结构数据。 |
| `scale` | Number | 客户的规模。 |
| `description` | String | 客户的描述。 |
| `created_at` | Number | 创建时间，单位为秒。 |
| `created_by` | Object | 创建人的引用结构数据。 |
| `updated_at` | Number | 更新时间，单位为秒。 |
| `updated_by` | Object | 更新人的引用结构数据。 |
| `is_archived` | Number | 是否已归档。 |
| `is_deleted` | Number | 是否已删除。 |

**权限:** 企业令牌/用户令牌

---
### `` 需求排期

**路径:** `需求排期`

---
### `` 需求模块

**路径:** `需求模块`

---
## 产品管理

### `` 产品

**路径:** `产品`

---
### `` 产品配置中心

---
### `` 工单

**路径:** `工单`

---
### `` 需求

**路径:** `需求`

---
## 工单

### `POST` 创建一个工单

**路径:** `/v1/ship/tickets`

用于创建一个工单。

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 工单的产品id。 |
| `title` | String | 是 | 工单的标题，最大长度为255。 |
| `type_id` | String | 是 | 工单的类型id，您可以在 “获取工单类型列表” API获取。 |
| `description` | String | 否 | 工单的描述。 |
| `submitter_id` | String | 否 | 工单的提交人id，企业授权时，该值有效；个人鉴权时，指定无效。 |
| `customer_id` | String | 否 | 工单的客户id，您可以在 “获取产品客户列表” API获取。 |
| `channel_id` | String | 否 | 工单的渠道id，您可以在 “获取渠道列表” API获取。 |
| `assignee_id` | String | 否 | 工单的负责人id。 |
| `priority_id` | String | 否 | 工单的优先级id，您可以在 “获取工单优先级列表” API获取。 |
| `properties` | Object | 否 | 工单的自定义属性。 |
| `properties.prop_a` | Object | 否 | 工单的自定义属性`prop_a`。 |
| `properties.prop_b` | Object | 否 | 工单的自定义属性`prop_b`。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工单的id。 |
| `url` | String | 工单的资源地址。 |
| `product` | Object | 工单的所属产品。 |
| `identifier` | String | 工单的标识。 |
| `title` | String | 工单的标题。 |
| `short_id` | String | 工单的短id。 |
| `html_url` | String | 工单的html地址。 |
| `assignee` | Object | 工单的负责人。 |
| `state` | Object | 工单的状态。 |
| `type` | Object | 工单的类型。 |
| `customer` | Object | 工单的客户。 |
| `solution` | Object | 工单的解决方案。 |
| `priority` | Object | 工单的优先级。 |
| `channel` | Object/String | 工单的渠道。外部渠道提交的工单的渠道是Object类型，内部工单的渠道是 `internal` 字符串。 |
| `description` | String | 工单的描述。 |
| `properties` | Object | 工单的自定义属性。 |
| `estimated_at` | Object | 工单的预计时间。 |
| `tags` | Object[] | 工单的标签列表。 |
| `participants` | Object[] | 工单的关注人列表。 |
| `submitted_at` | Number | 工单的提交时间。 |
| `submitted_by` | Object | 工单的提交人。 |
| `completed_at` | Number | 工单的完成时间。 |
| `completed_by` | Object | 工单的完成人。 |
| `created_at` | Number | 工单的创建时间。 |
| `created_by` | Object | 工单的创建人。 |
| `updated_at` | Number | 工单的更新时间。 |
| `updated_by` | Object | 工单的更新人。 |
| `is_archived` | Number | 是否已归档。 |
| `is_deleted` | Number | 是否已删除。 |

**权限:** 企业令牌/用户令牌

---
### `` 工单流转记录

**路径:** `工单流转记录`

---
### `GET` 获取一个工单

**路径:** `/v1/ship/tickets/{ticket_id}`

用于查看一个工单。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `ticket_id` | String | 是 | 工单的id。 |

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `include_public_image_token` | String | 否 | 包含获取图片资源token的属性。使用','分割，最多只能20个，支持`description`和自定义多行文本类型的属性。参数示例`description,properties.prop_b`。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工单的id。 |
| `url` | String | 工单的资源地址。 |
| `product` | Object | 工单的所属产品。 |
| `identifier` | String | 工单的标识。 |
| `title` | String | 工单的标题。 |
| `short_id` | String | 工单的短id。 |
| `html_url` | String | 工单的html地址。 |
| `assignee` | Object | 工单的负责人。 |
| `state` | Object | 工单的状态。 |
| `type` | Object | 工单的类型。 |
| `customer` | Object | 工单的客户。 |
| `solution` | Object | 工单的解决方案。 |
| `priority` | Object | 工单的优先级。 |
| `channel` | Object/String | 工单的渠道。外部渠道提交的工单的渠道是Object类型，内部工单的渠道是 `internal` 字符串。 |
| `description` | String | 工单的描述。 |
| `properties` | Object | 工单的自定义属性。 |
| `properties.prop_a` | Object | 工单的自定义属性prop_a。 |
| `properties.prop_b` | Object | 工单的自定义属性prop_b。 |
| `estimated_at` | Object | 工单的预计时间。 |
| `estimated_at.from` | Number | 预计时间的开始时间。 |
| `estimated_at.to` | Number | 预计时间的结束时间。 |
| `estimated_at.granularity` | String | 预计时间的周期单位。 |
| `tags` | Object[] | 工单的标签列表。 |
| `participants` | Object[] | 工单的关注人列表。 |
| `public_image_token` | String | 工单描述和自定义多行文本类型属性里获取图片资源token。获取一个工单和获取工单列表参数`include_public_image_token`值有效时返回。 |
| `submitted_at` | Number | 工单的提交时间。 |
| `submitted_by` | Object | 工单的提交人。 |
| `completed_at` | Number | 工单的完成时间。 |
| `completed_by` | Object | 工单的完成人。 |
| `created_at` | Number | 工单的创建时间。 |
| `created_by` | Object | 工单的创建人。 |
| `updated_at` | Number | 工单的更新时间。 |
| `updated_by` | Object | 工单的更新人。 |
| `is_archived` | Number | 是否已归档。 |
| `is_deleted` | Number | 是否已删除。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一条工单流转记录

**路径:** `/v1/ship/tickets/{ticket_id}/transition_histories/{transition_history_id}`

用于查看一条工单流转记录。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `ticket_id` | String | 是 | 工单的id。 |
| `transition_history_id` | String | 是 | 工单流转记录的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工单流转记录的id。 |
| `url` | String | 工单流转记录的资源地址。 |
| `ticket` | Object | 工单的引用结构数据。 |
| `from_state` | Object | 流转前工单状态的引用结构数据。 |
| `to_state` | Object | 流转后工单状态的引用结构数据。 |
| `created_at` | Number | 创建时间，单位为秒。 |
| `created_by` | Object | 创建人的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取工单优先级列表

**路径:** `/v1/ship/ticket/priorities?product_id={product_id}`

用于查询工单优先级列表。

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 产品的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 工单优先级全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取工单列表

**路径:** `/v1/ship/tickets`

用于查询工单列表。

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 否 | 产品的id。 |
| `type_id` | String | 否 | 工单类型id。 |
| `state_id` | String | 否 | 工单状态id。 |
| `priority_id` | String | 否 | 工单优先级id。 |
| `created_between` | String | 否 | 创建时间介于的时间范围，通过','分割起始时间。 |
| `updated_between` | String | 否 | 更新时间介于的时间范围，通过','分割起始时间。 |
| `keywords` | String | 否 | 关键字。支持工单编号和工单标题。 |
| `include_public_image_token` | String | 否 | 包含获取图片资源token的属性。使用','分割，最多只能20个，支持`description`和自定义多行文本类型的属性。参数示例`description,properties.prop_b`。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 工单全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取工单属性列表

**路径:** `/v1/ship/ticket/properties?product_id={product_id}`

用于查询工单属性列表。

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 产品的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 工单属性全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取工单标签列表

**路径:** `/v1/ship/ticket/tags?product_id={product_id}`

用于查询工单标签列表。

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 产品的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 工单标签全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取工单流转记录列表

**路径:** `/v1/ship/tickets/{ticket_id}/transition_histories`

用于查询工单流转记录列表。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `ticket_id` | String | 是 | 工单的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 工单流转记录全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取工单渠道列表

**路径:** `/v1/ship/ticket/channels?product_id={product_id}`

用于查询工单渠道列表。

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 产品的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 工单渠道全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取工单状态列表

**路径:** `/v1/ship/ticket/states?product_id={product_id}`

用于查询工单状态列表。

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 产品的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 工单状态全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取工单类型列表

**路径:** `/v1/ship/ticket/types?product_id={product_id}`

用于查询工单类型列表。

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 产品的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 工单类型的全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取工单解决方案列表

**路径:** `/v1/ship/ticket/solutions?product_id={product_id}`

用于查询工单解决方案列表。

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 产品的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 工单解决方案全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `PATCH` 部分更新一个工单

**路径:** `/v1/ship/tickets/{ticket_id}`

用于部分更新一个工单。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `ticket_id` | String | 是 | 工单id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `title` | String | 否 | 工单的标题，最大长度为255。 |
| `description` | String | 否 | 工单的描述。 |
| `type_id` | String | 否 | 工单的类型id，您可以在 “获取工单类型列表” API获取。 |
| `state_id` | String | 否 | 工单的状态id，您可以在 “获取工单状态列表” API获取。 |
| `assignee_id` | String | 否 | 工单的负责人id。 |
| `submitter_id` | String | 否 | 工单的提交人id，企业授权时，该值有效；个人鉴权时，指定无效。 |
| `solution_id` | String | 否 | 工单的解决方案id，您可以在 “获取工单解决方案列表” API获取。 |
| `priority_id` | String | 否 | 工单的优先级id，您可以在 “获取工单优先级列表” API获取。 |
| `customer_id` | String | 否 | 工单的客户id，您可以在 “获取产品客户列表” API获取。 |
| `properties` | Object | 否 | 工单的自定义属性。 |
| `properties.prop_a` | Object | 否 | 工单的自定义属性`prop_a`。 |
| `properties.prop_b` | Object | 否 | 工单的自定义属性`prop_b`。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工单的id。 |
| `url` | String | 工单的资源地址。 |
| `product` | Object | 工单的所属产品。 |
| `identifier` | String | 工单的标识。 |
| `title` | String | 工单的标题。 |
| `short_id` | String | 工单的短id。 |
| `html_url` | String | 工单的html地址。 |
| `assignee` | Object | 工单的负责人。 |
| `state` | Object | 工单的状态。 |
| `type` | Object | 工单的类型。 |
| `customer` | Object | 工单的客户。 |
| `solution` | Object | 工单的解决方案。 |
| `priority` | Object | 工单的优先级。 |
| `channel` | Object/String | 工单的渠道。外部渠道提交的工单的渠道是Object类型，内部工单的渠道是 `internal` 字符串。 |
| `description` | String | 工单的描述。 |
| `properties` | Object | 工单的自定义属性。 |
| `estimated_at` | Object | 工单的预计时间。 |
| `tags` | Object[] | 工单的标签列表。 |
| `participants` | Object[] | 工单的关注人列表。 |
| `submitted_at` | Number | 工单的提交时间。 |
| `submitted_by` | Object | 工单的提交人。 |
| `completed_at` | Number | 工单的完成时间。 |
| `completed_by` | Object | 工单的完成人。 |
| `created_at` | Number | 工单的创建时间。 |
| `created_by` | Object | 工单的创建人。 |
| `updated_at` | Number | 工单的更新时间。 |
| `updated_by` | Object | 工单的更新人。 |
| `is_archived` | Number | 是否已归档。 |
| `is_deleted` | Number | 是否已删除。 |

**权限:** 企业令牌/用户令牌

---
## 工单配置

### `POST` 创建一个工单属性

**路径:** `/v1/ship/ticket_properties`

用于创建一个工单属性。

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 是 | 工单属性的名称。在一个企业中这个名称是唯一的。 |
| `type` | String | 是 | 工单属性的类型。 |
| `options` | Object[] | 否 | 选择项列表。当工单属性类型为`select,multi_select,cascade_select,cascade_multi_select`时可选填此项。 |
| `options._id` | String | 否 | 选择项id。该值在选择项中是唯一的。 |
| `options.text` | String | 是 | 选择项内容。该值在选择项中是唯一的。 |
| `options.parent_id` | String | 否 | 选择项父级id。当属性类型为`cascade_select,cascade_multi_select`时，`parent_id`参数有效，用于构建级联类型选择项之间的父子关系，最多存在4级。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工单属性的id。 |
| `url` | String | 工单属性的资源地址。 |
| `name` | String | 工单属性的名称。 |
| `type` | String | 工单属性的类型。 |
| `options` | Object[] | 下拉选项值。 |
| `is_removable` | Number | 是否允许删除。 |
| `is_name_editable` | Number | 是否允许修改名称。 |
| `is_options_editable` | Number | 是否允许修改下拉选项值。 |

**权限:** 企业令牌/用户令牌

---
### `POST` 创建一个工单状态

**路径:** `/v1/ship/ticket_states`

用于创建一个工单状态。

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 是 | 工单状态的名称，在一个企业中这个名称是唯一的。 |
| `type` | String | 是 | 工单状态的类型。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工单状态的id。 |
| `url` | String | 工单状态的资源地址。 |
| `name` | String | 工单状态的名称。 |
| `type` | String | 工单状态的类型。 |
| `color` | String | 工单状态的颜色。 |

**权限:** 企业令牌/用户令牌

---
### `POST` 向工单属性方案中添加一个工单属性

**路径:** `/v1/ship/ticket_property_plans/{property_plan_id}/ticket_properties`

用于向工单属性方案中添加一个工单属性。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `property_plan_id` | String | 是 | 工单属性方案的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `property_id` | String | 是 | 工单属性的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 属性方案中工单属性关联的id。 |
| `url` | String | 属性方案中工单属性关联的资源地址。 |
| `property_plan` | Object | 工单属性方案的引用结构数据。 |
| `property` | Object | 工单属性的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `POST` 向状态方案中添加一个工单状态

**路径:** `/v1/ship/ticket_state_plans/{state_plan_id}/ticket_states`

用于向状态方案中添加一个工单状态。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `state_plan_id` | String | 是 | 工单状态方案的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `state_id` | String | 是 | 工单状态的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 状态方案中工单状态关联的id。 |
| `url` | String | 状态方案中工单状态关联的资源地址。 |
| `state_plan` | Object | 工单状态方案的引用结构数据。 |
| `state` | Object | 工单状态的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `POST` 向状态方案中添加一个工单状态流转

**路径:** `/v1/ship/ticket_state_plans/{state_plan_id}/ticket_state_flows`

用于向状态方案中添加一个工单状态流转。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `state_plan_id` | String | 是 | 工单状态方案的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `from_state_id` | String | 是 | 起始工单状态的id。 |
| `to_state_id` | String | 是 | 可更改为的工单状态的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工单状态流转的id。 |
| `url` | String | 工单状态流转的资源地址。 |
| `state_plan` | Object | 工单状态方案的引用结构数据。 |
| `form_state` | Object | 起始工单状态的引用结构数据。 |
| `to_state` | Object | 目标工单状态的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `DELETE` 在工单属性方案中移除一个工单属性

**路径:** `/v1/ship/ticket_property_plans/{property_plan_id}/ticket_properties/{property_id}`

用于在工单属性方案中移除一个工单属性。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `property_plan_id` | String | 是 | 工单属性方案的id。 |
| `property_id` | String | 是 | 工单属性的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 属性方案中工单属性关联的id。 |
| `url` | String | 属性方案中工单属性关联的资源地址。 |
| `property_plan` | Object | 工单属性方案的引用结构数据。 |
| `property` | Object | 工单属性的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `DELETE` 在状态方案中移除一个工单状态

**路径:** `/v1/ship/ticket_state_plans/{state_plan_id}/ticket_states/{state_id}`

用于在状态方案中移除一个工单状态。  移除状态后，每种类型的状态至少存在一种，否则将无法移除。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `state_plan_id` | String | 是 | 工单状态方案的id。 |
| `state_id` | String | 是 | 工单状态的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 状态方案中工单状态关联的id。 |
| `url` | String | 状态方案中工单状态关联的资源地址。 |
| `state_plan` | Object | 工单状态方案的引用结构数据。 |
| `state` | Object | 工单状态的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `DELETE` 在状态方案中移除一个工单状态流转

**路径:** `/v1/ship/ticket_state_plans/{state_plan_id}/ticket_state_flows/{state_flow_id}`

用于在状态方案中移除一个工单状态流转。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `state_plan_id` | String | 是 | 工单状态方案的id。 |
| `state_flow_id` | String | 是 | 工单状态流转的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工单状态流转的id。 |
| `url` | String | 工单状态流转的资源地址。 |
| `state_plan` | Object | 工单状态方案的引用结构数据。 |
| `form_state` | Object | 起始工单状态的引用结构数据。 |
| `to_state` | Object | 目标工单状态的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个工单优先级

**路径:** `/v1/ship/ticket_priorities/{priority_id}`

用于查看一个工单优先级。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `priority_id` | String | 是 | 工单优先级的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工单优先级的id。 |
| `url` | String | 工单优先级的资源地址。 |
| `name` | String | 工单优先级的名称。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个工单属性

**路径:** `/v1/ship/ticket_properties/{property_id}`

用于查看一个工单属性。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `property_id` | String | 是 | 工单属性的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工单属性的id。 |
| `url` | String | 工单属性的资源地址。 |
| `name` | String | 工单属性的名称。 |
| `type` | String | 工单属性的类型。 |
| `options` | Object[] | 下拉选项值。 |
| `is_removable` | Number | 是否允许删除。 |
| `is_name_editable` | Number | 是否允许修改名称。 |
| `is_options_editable` | Number | 是否允许修改下拉选项值。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个工单属性方案

**路径:** `/v1/ship/ticket_property_plans/{property_plan_id}`

用于查看一个工单属性方案。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `property_plan_id` | String | 是 | 工单属性方案的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工单属性方案的id。 |
| `url` | String | 工单属性方案的资源地址。 |
| `product` | Object | 工单属性方案关联产品的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个工单状态

**路径:** `/v1/ship/ticket_states/{ticket_state_id}`

用于查看一个工单状态。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `ticket_state_id` | String | 是 | 工单状态的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工单状态的id。 |
| `url` | String | 工单状态的资源地址。 |
| `name` | String | 工单状态的名称。 |
| `type` | String | 工单状态的类型。 |
| `color` | String | 工单状态的颜色。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个工单状态方案

**路径:** `/v1/ship/ticket_state_plans/{state_plan_id}`

用于查看一个工单状态方案。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `state_plan_id` | String | 是 | 工单状态方案的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工单状态方案的id。 |
| `url` | String | 工单状态方案的资源地址。 |
| `product` | Object | 工单状态方案关联产品的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个工单类型

**路径:** `/v1/ship/ticket_types/{ticket_type_id}`

用于查看一个工单类型。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `ticket_type_id` | String | 是 | 工单类型的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工单类型的id。 |
| `url` | String | 工单类型的资源地址。 |
| `name` | String | 工单类型的名称。 |
| `is_system` | Number | 是否为系统内置类型。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个工单解决方案

**路径:** `/v1/ship/ticket_solutions/{ticket_solution_id}`

用于查看一个工单解决方案。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `ticket_solution_id` | String | 是 | 工单解决方案的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工单解决方案的id。 |
| `url` | String | 工单解决方案的资源地址。 |
| `name` | String | 工单解决方案的名称。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取全部工单优先级列表

**路径:** `/v1/ship/ticket_priorities`

用于查询工单优先级列表。

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 工单优先级全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取全部工单属性列表

**路径:** `/v1/ship/ticket_properties`

用于查询全部工单属性列表。

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 全部工单属性全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取全部工单状态列表

**路径:** `/v1/ship/ticket_states`

用于查询全部工单状态列表。

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 全部工单状态全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取全部工单类型列表

**路径:** `/v1/ship/ticket_types`

用于查询全部工单类型列表。

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 全部工单类型全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取全部工单解决方案列表

**路径:** `/v1/ship/ticket_solutions`

用于查询工单解决方案列表。

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 工单解决方案全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取工单属性方案中的一个工单属性

**路径:** `/v1/ship/ticket_property_plans/{property_plan_id}/ticket_properties/{property_id}`

用于查询属性方案中的一个工单属性。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `property_plan_id` | String | 是 | 工单属性方案的id。 |
| `property_id` | String | 是 | 工单属性的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 属性方案中工单属性关联的id。 |
| `url` | String | 属性方案中工单属性关联的资源地址。 |
| `property_plan` | Object | 工单属性方案的引用结构数据。 |
| `property` | Object | 工单属性的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取工单属性方案中的工单属性列表

**路径:** `/v1/ship/ticket_property_plans/{property_plan_id}/ticket_properties`

用于查询工单属性方案中的工单属性列表。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `property_plan_id` | String | 是 | 工单属性方案的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 属性方案中的工单属性全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取工单属性方案列表

**路径:** `/v1/ship/ticket_property_plans`

用于查询工单属性方案列表。

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 工单属性方案全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取工单状态方案列表

**路径:** `/v1/ship/ticket_state_plans`

用于查询工单状态方案列表。

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 工单状态方案全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取状态方案中的一个工单状态

**路径:** `/v1/ship/ticket_state_plans/{state_plan_id}/ticket_states/{state_id}`

用于查询状态方案中的一个工单状态。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `state_plan_id` | String | 是 | 工单状态方案的id。 |
| `state_id` | String | 是 | 工单状态的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 状态方案中工单状态关联的id。 |
| `url` | String | 状态方案中工单状态关联的资源地址。 |
| `state_plan` | Object | 工单状态方案的引用结构数据。 |
| `state` | Object | 工单状态的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取状态方案中的一个工单状态流转

**路径:** `/v1/ship/ticket_state_plans/{state_plan_id}/ticket_state_flows/{state_flow_id}`

用于查询状态方案中的一个工单状态流转。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `state_plan_id` | String | 是 | 工单状态方案的id。 |
| `state_flow_id` | String | 是 | 工单状态流转的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工单状态流转的id。 |
| `url` | String | 工单状态流转的资源地址。 |
| `state_plan` | Object | 工单状态方案的引用结构数据。 |
| `form_state` | Object | 起始工单状态的引用结构数据。 |
| `to_state` | Object | 目标工单状态的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取状态方案中的工单状态列表

**路径:** `/v1/ship/ticket_state_plans/{state_plan_id}/ticket_states`

用于查询状态方案中的工单状态列表。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `state_plan_id` | String | 是 | 工单状态方案的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 状态方案中的工单状态全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取状态方案中的工单状态流转列表

**路径:** `/v1/ship/ticket_state_plans/{state_plan_id}/ticket_state_flows`

用于查询状态方案中的工单状态流转列表。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `state_plan_id` | String | 是 | 工单状态方案的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 状态方案中的工单状态流转全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `PATCH` 部分更新一个工单属性

**路径:** `/v1/ship/ticket_properties/{property_id}`

用于部分更新一个工单属性。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `property_id` | String | 是 | 工单属性的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 否 | 工单属性的名称。在一个企业中这个名称是唯一的。 |
| `options` | Object[] | 否 | 选择项列表。`options`是整体更新的。 |
| `options._id` | String | 否 | 选择项id。该值在选择项中是唯一的。 |
| `options.text` | String | 是 | 选择项内容。该值在选择项中是唯一的。 |
| `options.parent_id` | String | 否 | 选择项父级id。当属性类型为`cascade_select,cascade_multi_select`时，`parent_id`参数有效，用于构建级联类型选择项之间的父子关系，最多存在4级。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工单属性的id。 |
| `url` | String | 工单属性的资源地址。 |
| `name` | String | 工单属性的名称。 |
| `type` | String | 工单属性的类型。 |
| `options` | Object[] | 下拉选项值。 |
| `is_removable` | Number | 是否允许删除。 |
| `is_name_editable` | Number | 是否允许修改名称。 |
| `is_options_editable` | Number | 是否允许修改下拉选项值。 |

**权限:** 企业令牌/用户令牌

---
### `PATCH` 部分更新一个工单状态

**路径:** `/v1/ship/ticket_states/{ticket_state_id}`

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `ticket_state_id` | String | 是 | 工单状态id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 否 | 工单状态的名称，在一个企业中这个名称是唯一的。 |
| `type` | String | 否 | 工单状态的类型。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工单状态的id。 |
| `url` | String | 工单状态的资源地址。 |
| `name` | String | 工单状态的名称。 |
| `type` | String | 工单状态的类型。 |
| `color` | String | 工单状态的颜色。 |

**权限:** 企业令牌/用户令牌

---
