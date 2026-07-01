# 📚 知识库与文档 — API 详细文档

> 本文档包含 21 个接口的完整参数说明。
> 来源: https://open.pingcode.com/

---

## 知识管理

### `` 空间

**路径:** `空间`

---
### `` 页面

**路径:** `页面`

---
## 空间

### `POST` 创建一个空间

**路径:** `/v1/wiki/spaces`

用于创建一个空间。   企业令牌不能创建`scope_type`为`user`类型的空间。

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 是 | 空间的名称（不超过32个字符）。 |
| `identifier` | String | 是 | 空间的标识。在一个企业中这个标识是唯一的。产品的标识由大写英文字母/数字/下划线/连接线组成（不超过15个字符）。 |
| `scope_type` | String | 是 | 空间的所属类型。允许值分别表示企业可见、团队可见和用户可见。 |
| `scope_id` | String | 否 | 空间的所属id。当`scope_type`为`user_group`时，该字段必填，且表示团队id；当`scope_type`为其他值时，该字段无效。 |
| `visibility` | String | 否 | 空间可见性。允许值分别表示组织全部成员可见和仅空间成员可见。 |
| `description` | String | 否 | 空间的描述。 |
| `members` | Object[] | 否 | 空间成员的列表。 |
| `members.id` | String | 是 | 企业成员或团队的`id`。 |
| `members.type` | String | 是 | 空间成员类型。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 空间的id。 |
| `url` | String | 空间的资源地址。 |
| `identifier` | String | 空间的标识。 |
| `name` | String | 空间的名称。 |
| `scope_type` | String | 空间的所属类型。 |
| `scope_id` | String | 空间的所属id。 |
| `visibility` | String | 空间的可见性。 |
| `color` | String | 空间的主题色。 |
| `description` | String | 空间的描述。 |
| `members` | Object[] | 空间的成员列表。 |
| `created_at` | Number | 创建时间，单位为秒。 |
| `created_by` | Object | 创建人的引用结构数据。 |
| `updated_at` | Number | 更新时间，单位为秒。 |
| `updated_by` | Object | 更新人的引用结构数据。 |
| `is_archived` | Number | 是否已归档。 |
| `is_deleted` | Number | 是否已删除。 |

**权限:** 企业令牌/用户令牌

---
### `DELETE` 删除一个空间

**路径:** `/v1/wiki/spaces/{space_id}`

用于删除一个空间。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `space_id` | String | 是 | 空间的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 空间的id。 |
| `url` | String | 空间的资源地址。 |
| `identifier` | String | 空间的标识。 |
| `name` | String | 空间的名称。 |
| `scope_type` | String | 空间的所属类型。 |
| `scope_id` | String | 空间的所属id。 |
| `visibility` | String | 空间的可见性。 |
| `color` | String | 空间的主题色。 |
| `description` | String | 空间的描述。 |
| `members` | Object[] | 空间的成员列表。 |
| `created_at` | Number | 创建时间，单位为秒。 |
| `created_by` | Object | 创建人的引用结构数据。 |
| `updated_at` | Number | 更新时间，单位为秒。 |
| `updated_by` | Object | 更新人的引用结构数据。 |
| `is_archived` | Number | 是否已归档。 |
| `is_deleted` | Number | 是否已删除。 |

**权限:** 企业令牌/用户令牌

---
### `POST` 向空间中添加一个成员

**路径:** `/v1/wiki/spaces/{space_id}/members`

用于向空间中添加一个成员。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `space_id` | String | 是 | 空间的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `member` | Object | 是 | 空间的成员。 |
| `member.id` | String | 是 | 企业成员或团队的id。 |
| `member.type` | String | 是 | 空间成员的类型。 |
| `role_id` | String | 否 | 角色的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 空间成员的id。 |
| `url` | String | 空间成员的资源地址。 |
| `space` | Object | 所属空间的引用结构数据。 |
| `type` | String | 空间成员的类型。 |
| `user` | Object | 企业成员的引用结构数据。当`type`为`user`时，该字段返回。 |
| `user_group` | Object | 团队的引用结构数据。当`type`为`user_group`时，该字段返回。 |
| `role` | Object | 成员角色的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `DELETE` 在空间中移除一个成员

**路径:** `/v1/wiki/spaces/{space_id}/members/{member_id}`

用于在空间中移除一个成员。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `space_id` | String | 是 | 空间的id。 |
| `member_id` | String | 是 | 企业成员或团队的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 空间成员的id。 |
| `url` | String | 空间成员的资源地址。 |
| `space` | Object | 所属空间的引用结构数据。 |
| `type` | String | 空间成员的类型。 |
| `user` | Object | 企业成员的引用结构数据。当`type`为`user`时，该字段返回。 |
| `user_group` | Object | 团队的引用结构数据。当`type`为`user_group`时，该字段返回。 |
| `role` | Object | 成员角色的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个空间

**路径:** `/v1/wiki/spaces/{space_id}`

用于查看一个空间。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `space_id` | String | 是 | 空间的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 空间的id。 |
| `url` | String | 空间的资源地址。 |
| `identifier` | String | 空间的标识。 |
| `name` | String | 空间的名称。 |
| `scope_type` | String | 空间的所属类型。允许值分别表示企业可见、团队可见和用户可见。 |
| `scope_id` | String | 空间的所属id。 |
| `visibility` | String | 空间的可见性。 |
| `color` | String | 空间的主题色。 |
| `description` | String | 空间的描述。 |
| `members` | Object[] | 空间的成员列表。 |
| `created_at` | Number | 空间的创建时间。 |
| `created_by` | Object | 空间的创建人。 |
| `updated_at` | Number | 空间的更新时间。 |
| `updated_by` | Object | 空间的更新人。 |
| `is_archived` | Number | 是否已归档。 |
| `is_deleted` | Number | 是否已删除。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取空间中的一个成员

**路径:** `/v1/wiki/spaces/{space_id}/members/{member_id}`

用于查看一个空间成员。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `space_id` | String | 是 | 空间的id。 |
| `member_id` | String | 是 | 空间成员的id，即企业成员或团队的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 空间成员的id。 |
| `url` | String | 空间成员的资源地址。 |
| `space` | Object | 所属空间的引用结构数据。 |
| `type` | String | 空间成员的类型。 |
| `user` | Object | 企业成员的引用结构数据。当`type`为`user`时，该字段返回。 |
| `user_group` | Object | 团队的引用结构数据。当`type`为`user_group`时，该字段返回。 |
| `role` | Object | 成员角色的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取空间中的成员列表

**路径:** `/v1/wiki/spaces/{space_id}/members`

用于查询空间中的成员列表。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `space_id` | String | 是 | 空间的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 空间中的成员全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取空间列表

**路径:** `/v1/wiki/spaces`

用于查询空间列表。

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `keywords` | String | 否 | 关键字。只支持`name`关键字搜索。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 空间全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `PATCH` 部分更新一个空间

**路径:** `/v1/wiki/spaces/{space_id}`

用于部分更新一个空间。  企业令牌不能更新`scope_type`为`user`类型的空间。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `space_id` | String | 是 | 空间的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 否 | 空间的名称（不超过32个字符）。 |
| `identifier` | String | 否 | 空间的标识。在一个企业中这个标识是唯一的。产品的标识由大写英文字母/数字/下划线/连接线组成（不超过15个字符）。 |
| `description` | String | 否 | 空间的描述。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 空间的id。 |
| `url` | String | 空间的资源地址。 |
| `identifier` | String | 空间的标识。 |
| `name` | String | 空间的名称。 |
| `scope_type` | String | 空间的所属类型。 |
| `scope_id` | String | 空间的所属id。 |
| `visibility` | String | 空间的可见性。 |
| `color` | String | 空间的主题色。 |
| `description` | String | 空间的描述。 |
| `members` | Object[] | 空间的成员列表。 |
| `created_at` | Number | 创建时间，单位为秒。 |
| `created_by` | Object | 创建人的引用结构数据。 |
| `updated_at` | Number | 更新时间，单位为秒。 |
| `updated_by` | Object | 更新人的引用结构数据。 |
| `is_archived` | Number | 是否已归档。 |
| `is_deleted` | Number | 是否已删除。 |

**权限:** 企业令牌/用户令牌

---
## 页面

### `POST` 创建一个页面

**路径:** `/v1/wiki/pages`

用于创建一个页面。

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `space_id` | String | 是 | 空间的id。 |
| `name` | String | 是 | 页面的名称。 |
| `parent_id` | String | 否 | 父页面的id。 |
| `content` | String | 否 | 页面的内容。 |
| `format_type` | String | 否 | 页面内容的格式。content和format_type字段必须同时传递。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 页面的id。 |
| `url` | String | 页面的资源地址。 |
| `space` | Object | 所属空间的引用结构数据。 |
| `name` | String | 页面的名称。 |
| `type` | String | 页面的类型。 |
| `short_id` | String | 页面的短id。 |
| `html_url` | String | 页面的html地址。 |
| `parent` | Object | 父页面的引用结构数据。 |
| `icon` | String | 页面的图标。 |
| `readings` | Number | 页面的阅读量。 |
| `published_at` | Number | 页面的发布时间，单位为秒。 |
| `published_by` | Object | 发布人的引用结构数据。 |
| `tags` | Object[] | 页面标签列表。 |
| `participants` | Object[] | 页面关注人列表。 |
| `position` | Number | 页面在同级中的排序位置。 |
| `created_at` | Number | 创建时间，单位为秒。 |
| `created_by` | Object | 创建人的引用结构数据。 |
| `updated_at` | Number | 更新时间，单位为秒。 |
| `updated_by` | Object | 更新人的引用结构数据。 |
| `is_locked` | Number | 是否锁定页面。 |
| `is_archived` | Number | 是否已归档。 |
| `is_deleted` | Number | 是否已删除。 |

**权限:** 企业令牌/用户令牌

---
### `DELETE` 删除一个页面

**路径:** `/v1/wiki/pages/{page_id}`

用于删除一个页面。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `page_id` | String | 是 | 页面的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 页面的id。 |
| `url` | String | 页面的资源地址。 |
| `name` | String | 页面的名称。 |
| `type` | String | 页面的类型。 |
| `short_id` | String | 页面的短id。 |
| `html_url` | String | 页面的html地址。 |
| `space` | Object | 所属空间的引用结构数据。 |
| `parent` | Object | 父页面的引用结构数据。 |
| `icon` | String | 页面的图标。 |
| `readings` | Number | 页面的阅读量。 |
| `published_at` | Number | 页面的发布时间，单位为秒。 |
| `published_by` | Object | 发布人的引用结构数据。 |
| `tags` | Object[] | 页面标签列表。 |
| `participants` | Object[] | 页面关注人列表。 |
| `position` | Number | 页面在同级中的排序位置。 |
| `created_at` | Number | 创建时间，单位为秒。 |
| `created_by` | Object | 创建人的引用结构数据。 |
| `updated_at` | Number | 更新时间，单位为秒。 |
| `updated_by` | Object | 更新人的引用结构数据。 |
| `is_locked` | Number | 是否锁定页面。 |
| `is_archived` | Number | 是否已归档。 |
| `is_deleted` | Number | 是否已删除。 |

**权限:** 企业令牌/用户令牌

---
### `POST` 恢复一个页面到指定版本

**路径:** `/v1/wiki/pages/{page_id}/versions/{version_id}/restore`

用于恢复一个页面到指定版本。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `page_id` | String | 是 | 页面的id。 |
| `version_id` | String | 是 | 页面版本的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 页面版本的id。 |
| `url` | String | 页面版本的资源地址。 |
| `page` | Object | 所属页面的引用结构数据。 |
| `name` | String | 页面版本的名称。 |
| `order` | Number | 页面版本的序号。 |
| `status` | String | 页面版本的状态。 |
| `created_at` | Number | 创建时间，单位为秒。 |
| `created_by` | Object | 创建人的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `PUT` 更新一个文档正文

**路径:** `/v1/wiki/pages/{page_id}/content`

用于更新一个文档正文。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `page_id` | String | 是 | 页面的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `content` | String | 是 | 页面的内容。 |
| `format_type` | String | 是 | 页面内容的格式。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 文档正文的id。 |
| `url` | String | 文档正文的资源地址。 |
| `format_type` | String | 正文格式。 |
| `content` | String | 正文内容。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个文档正文

**路径:** `/v1/wiki/pages/{page_id}/content`

用于查看一个文档正文。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `page_id` | String | 是 | 页面的id。 |

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `format_type` | String | 否 | 正文格式。 |
| `version_id` | String | 否 | 页面版本的id。默认值为页面当前版本的id。 |
| `include_public_image_token` | String | 否 | 包含获取图片资源token的属性。仅支持`content`，参数示例`content`。仅当`format_type`为`markdown`、`html`或`block`时有效。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 文档正文的id。 |
| `url` | String | 文档正文的资源地址。 |
| `format_type` | String | 正文格式。 |
| `content` | String | 正文内容。 |
| `public_image_token` | String | 正文内图片资源的公开预览token。传参`include_public_image_token=content`且`format_type`为`markdown`、`html`或`block`时返回。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个页面

**路径:** `/v1/wiki/pages/{page_id}`

用于查看一个页面。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `page_id` | String | 是 | 页面的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 页面的id。 |
| `url` | String | 页面的资源地址。 |
| `space` | Object | 所属空间的引用结构数据。 |
| `name` | String | 页面的名称。 |
| `type` | String | 页面的类型。 |
| `short_id` | String | 页面的短id。 |
| `html_url` | String | 页面的html地址。 |
| `parent` | Object | 父页面的引用结构数据。 |
| `icon` | String | 页面的图标。 |
| `readings` | Number | 页面的阅读量。 |
| `published_at` | Number | 页面的发布时间，单位为秒。 |
| `published_by` | Object | 发布人的引用结构数据。 |
| `tags` | Object[] | 页面标签列表。 |
| `participants` | Object[] | 页面关注人列表。 |
| `position` | Number | 页面在同级中的排序位置。 |
| `created_at` | Number | 创建时间，单位为秒。 |
| `created_by` | Object | 创建人的引用结构数据。 |
| `updated_at` | Number | 更新时间，单位为秒。 |
| `updated_by` | Object | 更新人的引用结构数据。 |
| `is_locked` | Number | 是否锁定页面。 |
| `is_archived` | Number | 是否已归档。 |
| `is_deleted` | Number | 是否已删除。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个页面版本

**路径:** `/v1/wiki/pages/{page_id}/versions/{version_id}`

用于查看一个页面版本。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `page_id` | String | 是 | 页面的id。 |
| `version_id` | String | 是 | 页面版本的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 页面版本的id。 |
| `url` | String | 页面版本的资源地址。 |
| `page` | Object | 所属页面的引用结构数据。 |
| `name` | String | 页面版本的名称。 |
| `order` | Number | 页面版本的序号。 |
| `status` | String | 页面版本的状态。 |
| `created_at` | Number | 创建时间，单位为秒。 |
| `created_by` | Object | 创建人的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个页面的版本列表

**路径:** `/v1/wiki/pages/{page_id}/versions`

用于查看一个页面的版本列表。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `page_id` | String | 是 | 页面的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 页面版本全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取页面列表

**路径:** `/v1/wiki/pages`

用于查询页面列表。

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `space_id` | String | 否 | 空间的id。 |
| `parent_id` | String | 否 | 父页面的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 页面全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `PATCH` 部分更新一个页面

**路径:** `/v1/wiki/pages/{page_id}`

用于部分更新一个页面。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `page_id` | String | 是 | 页面的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 否 | 页面的名称。 |
| `parent_id` | String | 否 | 父页面的id。 |
| `lock` | Number | 否 | 是否锁定页面。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 页面的id。 |
| `url` | String | 页面的资源地址。 |
| `space` | Object | 所属空间的引用结构数据。 |
| `name` | String | 页面的名称。 |
| `type` | String | 页面的类型。 |
| `short_id` | String | 页面的短id。 |
| `html_url` | String | 页面的html地址。 |
| `parent` | Object | 父页面的引用结构数据。 |
| `icon` | String | 页面的图标。 |
| `readings` | Number | 页面的阅读量。 |
| `published_at` | Number | 页面的发布时间，单位为秒。 |
| `published_by` | Object | 发布人的引用结构数据。 |
| `tags` | Object[] | 页面标签列表。 |
| `participants` | Object[] | 页面关注人列表。 |
| `position` | Number | 页面在同级中的排序位置。 |
| `created_at` | Number | 创建时间，单位为秒。 |
| `created_by` | Object | 创建人的引用结构数据。 |
| `updated_at` | Number | 更新时间，单位为秒。 |
| `updated_by` | Object | 更新人的引用结构数据。 |
| `is_locked` | Number | 是否锁定页面。 |
| `is_archived` | Number | 是否已归档。 |
| `is_deleted` | Number | 是否已删除。 |

**权限:** 企业令牌/用户令牌

---
