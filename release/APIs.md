# 🚀 交付与发布 — API 详细文档

> 本文档包含 42 个接口的完整参数说明。
> 来源: https://open.pingcode.com/

---

## 交付

### `` 环境

**路径:** `环境`

---
### `` 部署

**路径:** `部署`

---
## 发布

### `POST` 创建一个发布

**路径:** `/v1/pjm/projects/{project_id}/versions`

用于创建一个发布。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 是 | 项目的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 是 | 发布的名称。同一项目下该名称是唯一的。 |
| `start_at` | Number | 是 | 开始的时间。 |
| `end_at` | Number | 是 | 发布的时间。 |
| `assignee_id` | String | 是 | 负责人的id。 |
| `stage_id` | String | 否 | 发布阶段的id。 |
| `category_ids` | String[] | 否 | 发布类别id数组。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 发布的id。 |
| `url` | String | 发布的地址。 |
| `project` | Object | 发布所属项目的引用结构数据。 |
| `name` | String | 发布的名称。 |
| `start_at` | Number | 发布的开始时间。 |
| `end_at` | Number | 发布的结束时间。 |
| `stage` | Object | 发布的当前阶段。 |
| `assignee` | Object | 发布负责人的引用结构数据。 |
| `stages` | Object[] | 发布的阶段列表。 |
| `progress` | Number | 发布的进度。 |
| `changelog` | String | 发布的发布日志。 |
| `operate_at` | Number | 发布的最后操作时间。 |
| `categories` | Object[] | 发布的类别列表。 |
| `created_at` | Number | 发布的创建时间。 |
| `created_by` | Object | 发布创建人的引用结构数据。 |
| `updated_at` | Number | 发布的更新时间。 |
| `updated_by` | Object | 发布更新人的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `POST` 创建一个发布分组

**路径:** `/v1/pjm/projects/{project_id}/version_sections`

用于创建一个发布分组。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 是 | 项目的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 是 | 发布分组的名称。 |
| `description` | String | 否 | 发布分组的描述。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 发布分组的id。 |
| `url` | String | 发布分组的地址。 |
| `project` | Object | 所属项目的引用结构数据。 |
| `name` | String | 发布分组的名称。 |
| `description` | String | 发布分组的描述。 |

**权限:** 企业令牌/用户令牌

---
### `POST` 创建一个发布类别

**路径:** `/v1/pjm/projects/{project_id}/version_categories`

用于创建一个发布类别。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 是 | 项目的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 是 | 发布类别的名称。 |
| `section_id` | String | 否 | 发布类别所属发布分组。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 发布类别的id。 |
| `url` | String | 发布类别的地址。 |
| `project` | Object | 所属项目的引用结构数据。 |
| `name` | String | 发布类别的名称。 |
| `section` | Object | 所属发布分组的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `POST` 创建一个发布阶段

**路径:** `/v1/pjm/stages`

用于创建一个发布阶段。

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 是 | 发布阶段的名称。在一个企业中这个名称是唯一的。 |
| `type` | String | 是 | 发布阶段的类型。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 发布阶段的id。 |
| `url` | String | 发布阶段的地址。 |
| `name` | String | 发布阶段的名称。 |
| `type` | String | 发布阶段的类型。 |
| `color` | String | 发布阶段的颜色。 |

**权限:** 企业令牌/用户令牌

---
### `DELETE` 删除一个发布

**路径:** `/v1/pjm/projects/{project_id}/versions/{version_id}`

用于删除一个发布。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 是 | 项目的id。 |
| `version_id` | String | 是 | 发布的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 发布的id。 |
| `url` | String | 发布的地址。 |
| `project` | Object | 发布所属项目的引用结构数据。 |
| `name` | String | 发布的名称。 |
| `start_at` | Number | 发布的开始时间。 |
| `end_at` | Number | 发布的结束时间。 |
| `stage` | Object | 发布的当前阶段。 |
| `assignee` | Object | 发布负责人的引用结构数据。 |
| `stages` | Object[] | 发布的阶段列表。 |
| `progress` | Number | 发布的进度。 |
| `changelog` | String | 发布的发布日志。 |
| `operate_at` | Number | 发布的最后操作时间。 |
| `categories` | Object[] | 发布的类别列表。 |
| `created_at` | Number | 发布的创建时间。 |
| `created_by` | Object | 发布创建人的引用结构数据。 |
| `updated_at` | Number | 发布的更新时间。 |
| `updated_by` | Object | 发布更新人的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `DELETE` 删除一个发布分组

**路径:** `/v1/pjm/projects/{project_id}/version_sections/{section_id}`

用于删除一个发布分组。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 是 | 项目的id。 |
| `section_id` | String | 是 | 发布分组的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 发布分组的id。 |
| `url` | String | 发布分组的地址。 |
| `project` | Object | 所属项目的引用结构数据。 |
| `name` | String | 发布分组的名称。 |
| `description` | String | 发布分组的描述。 |

**权限:** 企业令牌/用户令牌

---
### `DELETE` 删除一个发布类别

**路径:** `/v1/pjm/projects/{project_id}/version_categories/{version_category_id}`

用于删除一个发布类别。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 是 | 项目的id。 |
| `version_category_id` | String | 是 | 发布类别的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 发布类别的id。 |
| `url` | String | 发布类别的地址。 |
| `project` | Object | 所属项目的引用结构数据。 |
| `name` | String | 发布类别的名称。 |
| `section` | Object | 所属发布分组的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `DELETE` 删除一个发布阶段

**路径:** `/v1/pjm/stages/{stage_id}`

用于删除一个发布阶段。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `stage_id` | String | 是 | 发布阶段的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `replace_id` | String | 否 | 替换的发布阶段id，如果一个发布阶段已经被发布使用，删除该发布阶段时需要提供一个替换的发布阶段。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 发布阶段的id。 |
| `url` | String | 发布阶段的地址。 |
| `name` | String | 发布阶段的名称。 |
| `type` | String | 发布阶段的类型。 |
| `color` | String | 发布阶段的颜色。 |

**权限:** 企业令牌/用户令牌

---
### `POST` 批量创建发布

**路径:** `/v1/pjm/versions/bulk`

用于批量创建发布。

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `versions` | Object[] | 是 | 需要批量创建的发布。该参数是一个对象数组（数组内对象不得超过100个）。 |
| `versions.project_id` | String | 是 | 发布所属项目的id。 |
| `versions.name` | String | 是 | 发布的名称。 |
| `versions.start_at` | Number | 是 | 发布的开始时间。 |
| `versions.end_at` | Number | 是 | 发布的时间。 |
| `versions.assignee_id` | String | 是 | 发布负责人的id。 |
| `versions.stage_id` | String | 是 | 发布的阶段id。 |
| `versions.category_ids` | String[] | 否 | 发布类别的id列表。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `state` | String | 批量创建结果的状态。 |
| `version` | Object | 发布的全量结构数据。创建成功时返回。 |

**权限:** 企业令牌

---
### `GET` 获取一个发布

**路径:** `/v1/pjm/projects/{project_id}/versions/{version_id}`

用于查看一个发布。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 是 | 项目的id。 |
| `version_id` | String | 是 | 发布的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 发布的id。 |
| `url` | String | 发布的地址。 |
| `project` | Object | 发布所属项目的引用结构数据。 |
| `name` | String | 发布的名称。 |
| `start_at` | Number | 发布的开始时间。 |
| `end_at` | Number | 发布的结束时间。 |
| `stage` | Object | 发布的当前阶段。 |
| `assignee` | Object | 发布负责人的引用结构数据。 |
| `stages` | Object[] | 发布的阶段列表。 |
| `progress` | Number | 发布的进度。 |
| `changelog` | String | 发布的发布日志。 |
| `operate_at` | Number | 发布的最后操作时间。 |
| `categories` | Object[] | 发布的类别列表。 |
| `created_at` | Number | 发布的创建时间。 |
| `created_by` | Object | 发布的创建人。 |
| `updated_at` | Number | 发布的更新时间。 |
| `updated_by` | Object | 发布的更新人。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个发布分组

**路径:** `/v1/pjm/projects/{project_id}/version_sections/{section_id}`

用于查看一个发布分组。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 是 | 项目的id。 |
| `section_id` | String | 是 | 发布分组的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 发布分组的id。 |
| `url` | String | 发布分组的地址。 |
| `project` | Object | 所属项目的引用结构数据。 |
| `name` | String | 发布分组的名称。 |
| `description` | String | 发布分组的描述。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个发布类别

**路径:** `/v1/pjm/projects/{project_id}/version_categories/{version_category_id}`

用于查看一个发布类别。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 是 | 项目的id。 |
| `version_category_id` | String | 是 | 发布类别的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 发布类别的id。 |
| `url` | String | 发布类别的地址。 |
| `project` | Object | 所属项目的引用结构数据。 |
| `name` | String | 发布类别的名称。 |
| `section` | Object | 所属发布分组的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个发布阶段

**路径:** `/v1/pjm/stages/{stage_id}`

用于查看一个发布阶段。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `stage_id` | String | 是 | 发布阶段的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 发布阶段的id。 |
| `url` | String | 发布阶段的地址。 |
| `name` | String | 发布阶段的名称。 |
| `type` | String | 发布阶段的类型。 |
| `color` | String | 发布阶段的颜色。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取发布分组列表

**路径:** `/v1/pjm/projects/{project_id}/version_sections`

用于查询发布分组列表。

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
| `values` | Object[] | 发布分组全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取发布列表

**路径:** `/v1/pjm/projects/{project_id}/versions`

用于查询发布列表。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 是 | 项目的id。 |

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 否 | 发布的名字。 |
| `status` | String | 否 | 发布的状态。 |
| `created_between` | String | 否 | 创建时间介于的时间范围，通过','分割起始时间。 |
| `updated_between` | String | 否 | 更新时间介于的时间范围，通过','分割起始时间。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 发布全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取发布类别列表

**路径:** `/v1/pjm/projects/{project_id}/version_categories`

用于查询发布类别列表。

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
| `values` | Object[] | 发布类别全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取发布阶段列表

**路径:** `/v1/pjm/stages`

用于查询发布阶段列表。

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 发布阶段的全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `PATCH` 部分更新一个发布

**路径:** `/v1/pjm/projects/{project_id}/versions/{version_id}`

用于部分更新一个发布。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 是 | 项目的id。 |
| `version_id` | String | 是 | 发布的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 否 | 发布的名称。同一项目下该名称是唯一的。 |
| `start_at` | Number | 否 | 开始的时间。 |
| `end_at` | Number | 否 | 发布的时间。 |
| `assignee_id` | String | 否 | 负责人的id。 |
| `stage_id` | String | 否 | 发布阶段的id。 |
| `operate_at` | Number | 否 | 发布阶段的日期。需要和stage_id一起传递。 |
| `category_ids` | String[] | 否 | 发布类别id数组。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 发布的id。 |
| `url` | String | 发布的地址。 |
| `project` | Object | 发布所属项目的引用结构数据。 |
| `name` | String | 发布的名称。 |
| `start_at` | Number | 发布的开始时间。 |
| `end_at` | Number | 发布的结束时间。 |
| `stage` | Object | 发布的当前阶段。 |
| `assignee` | Object | 发布负责人的引用结构数据。 |
| `stages` | Object[] | 发布的阶段列表。 |
| `progress` | Number | 发布的进度。 |
| `changelog` | String | 发布的发布日志。 |
| `operate_at` | Number | 发布的最后操作时间。 |
| `categories` | Object[] | 发布的类别列表。 |
| `created_at` | Number | 发布的创建时间。 |
| `created_by` | Object | 发布创建人的引用结构数据。 |
| `updated_at` | Number | 发布的更新时间。 |
| `updated_by` | Object | 发布更新人的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `PATCH` 部分更新一个发布分组

**路径:** `/v1/pjm/projects/{project_id}/version_sections/{section_id}`

用于部分更新一个发布分组。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 是 | 项目的id。 |
| `section_id` | String | 是 | 发布分组的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 是 | 发布分组的名称。 |
| `description` | String | 否 | 发布分组的描述。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 发布分组的id。 |
| `url` | String | 发布分组的地址。 |
| `project` | Object | 所属项目的引用结构数据。 |
| `name` | String | 发布分组的名称。 |
| `description` | String | 发布分组的描述。 |

**权限:** 企业令牌/用户令牌

---
### `PATCH` 部分更新一个发布类别

**路径:** `/v1/pjm/projects/{project_id}/version_categories/{version_category_id}`

用于部分更新一个发布类别。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 是 | 项目的id。 |
| `version_category_id` | String | 是 | 发布类别的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 否 | 发布类别的名称。 |
| `section_id` | String | 否 | 发布类别所属发布分组。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 发布类别的id。 |
| `url` | String | 发布类别的地址。 |
| `project` | Object | 所属项目的引用结构数据。 |
| `name` | String | 发布类别的名称。 |
| `section` | Object | 所属发布分组的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `PATCH` 部分更新一个发布阶段

**路径:** `/v1/pjm/stages/{stage_id}`

用于部分更新一个发布阶段。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `stage_id` | String | 是 | 发布阶段的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 否 | 发布阶段的名称。在一个企业中这个名称是唯一的。 |
| `type` | String | 否 | 发布阶段的类型。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 发布阶段的id。 |
| `url` | String | 发布阶段的地址。 |
| `name` | String | 发布阶段的名称。 |
| `type` | String | 发布阶段的类型。 |
| `color` | String | 发布阶段的颜色。 |

**权限:** 企业令牌/用户令牌

---
## 构建

### `` 构建记录

**路径:** `构建记录`

---
## 构建记录

### `PUT` 全量更新一条构建记录

**路径:** `/v1/build/builds/{build_id}`

用于全量更新一条构建记录。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `build_id` | String | 是 | 构建的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 是 | 构建的名称。 |
| `identifier` | String | 是 | 构建的编号。 |
| `job_url` | String | 否 | 构建任务的地址。如果为空，在PingCode中不显示相关跳转链接。 |
| `provider` | String | 是 | 构建工具的名称。 |
| `result_overview` | String | 否 | 构建结果的概述。 |
| `result_url` | String | 否 | 构建结果的地址。如果为空，在PingCode中不显示相关的跳转链接。 |
| `start_at` | Number | 是 | 构建开始的时间。 |
| `end_at` | Number | 是 | 构建结束的时间。 |
| `duration` | Number | 是 | 构建持续的时间。单位为秒。 |
| `status` | String | 是 | 构建的状态。 |
| `work_item_identifiers` | String[] | 否 | PingCode工作项编号的列表。通过该参数将构建与一个或多个工作项关联。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 构建记录的id。 |
| `url` | String | 构建记录的资源地址。 |
| `identifier` | String | 构建记录的编号。 |
| `name` | String | 构建记录的名称。 |
| `job_url` | String | 构建任务的地址。 |
| `provider` | String | 构建工具的名称。 |
| `result_overview` | String | 构建结果的概述。 |
| `result_url` | String | 构建结果的地址。 |
| `start_at` | Number | 构建开始的时间。 |
| `status` | String | 构建的状态。 |
| `end_at` | Number | 构建结束的时间。 |
| `duration` | Number | 构建持续的时间，单位为秒。 |
| `work_items` | Object[] | 构建关联的PingCode工作项列表。 |

**权限:** 企业令牌

---
### `POST` 创建一条构建记录

**路径:** `/v1/build/builds`

用于创建一条构建记录。  企业内实际的构建记录，用于在PingCode中显示构建的详细信息。

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 是 | 构建的名称。 |
| `identifier` | String | 是 | 构建的编号。 |
| `job_url` | String | 否 | 构建任务的地址。如果为空，在PingCode中不显示相关跳转链接。 |
| `provider` | String | 是 | 构建工具的名称。 |
| `result_overview` | String | 否 | 构建结果的概述。 |
| `result_url` | String | 否 | 构建结果的地址。如果为空，在PingCode中不显示相关的跳转链接。 |
| `start_at` | Number | 是 | 构建开始的时间。 |
| `end_at` | Number | 是 | 构建结束的时间。 |
| `duration` | Number | 是 | 构建持续的时间。单位为秒。 |
| `status` | String | 是 | 构建的状态。 |
| `work_item_identifiers` | String[] | 否 | PingCode工作项编号的列表。通过该参数将构建与一个或多个工作项关联。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 构建记录的id。 |
| `url` | String | 构建记录的资源地址。 |
| `name` | String | 构建记录的名称。 |
| `identifier` | String | 构建记录的编号。 |
| `job_url` | String | 构建任务的地址。 |
| `provider` | String | 构建工具的名称。 |
| `result_overview` | String | 构建结果的概述。 |
| `result_url` | String | 构建结果的地址。 |
| `start_at` | Number | 构建开始的时间。 |
| `status` | String | 构建的状态。 |
| `end_at` | Number | 构建结束的时间。 |
| `duration` | Number | 构建持续的时间，单位为秒。 |
| `work_items` | Object[] | 构建关联的PingCode工作项列表。 |

**权限:** 企业令牌

---
### `DEL` 删除一条构建记录

**路径:** `/v1/build/builds/{build_id}`

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `build_id` | String | 是 | 构建的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 构建记录的id。 |
| `url` | String | 构建记录的资源地址。 |
| `identifier` | String | 构建记录的编号。 |
| `name` | String | 构建记录的名称。 |
| `job_url` | String | 构建任务的地址。 |
| `provider` | String | 构建工具的名称。 |
| `result_overview` | String | 构建结果的概述。 |
| `result_url` | String | 构建结果的地址。 |
| `start_at` | Number | 构建开始的时间。 |
| `status` | String | 构建的状态。 |
| `end_at` | Number | 构建结束的时间。 |
| `duration` | Number | 构建持续的时间，单位为秒。 |
| `work_items` | Object[] | 构建关联的PingCode工作项列表。 |

**权限:** 企业令牌

---
### `GET` 获取一个构建记录

**路径:** `/v1/build/builds/{build_id}`

用于查看一个构建记录。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `build_id` | String | 是 | 构建记录的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 构建记录的id。 |
| `url` | String | 构建记录的资源地址。 |
| `identifier` | String | 构建记录的编号。 |
| `name` | String | 构建记录的名称。 |
| `job_url` | String | 构建任务的地址。 |
| `provider` | String | 构建工具的名称。 |
| `result_overview` | String | 构建结果的概述。 |
| `result_url` | String | 构建结果的地址。 |
| `start_at` | Number | 构建开始的时间。 |
| `end_at` | Number | 构建结束的时间。 |
| `status` | String | 构建的状态。 |
| `duration` | Number | 构建持续的时间，单位为秒。 |
| `work_items` | Object[] | 构建关联的PingCode的工作项列表。 |

**权限:** 企业令牌

---
### `GET` 获取构建记录列表

**路径:** `/v1/build/builds`

用于查询构建记录列表。

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 构建记录全量结构数据的数组。 |

**权限:** 企业令牌

---
### `PATCH` 部分更新一条构建记录

**路径:** `/v1/build/builds/{build_id}`

用于部分更新一条构建记录。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `build_id` | String | 是 | 构建的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 否 | 构建的名称。 |
| `identifier` | String | 否 | 构建的编号。 |
| `job_url` | String | 否 | 构建任务的地址。如果为空，在PingCode中不显示相关跳转链接。 |
| `provider` | String | 否 | 构建工具的名称。 |
| `result_overview` | String | 否 | 构建结果的概述。 |
| `result_url` | String | 否 | 构建结果的地址。如果为空，在PingCode中不显示相关的跳转链接。 |
| `start_at` | Number | 否 | 构建开始的时间。 |
| `end_at` | Number | 否 | 构建结束的时间。 |
| `status` | String | 否 | 构建的状态。 |
| `duration` | Number | 否 | 构建持续的时间。单位为秒。 |
| `work_item_identifiers` | String[] | 否 | PingCode工作项编号的列表。通过该参数将构建与一个或多个工作项关联。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 构建记录的id。 |
| `url` | String | 构建记录的资源地址。 |
| `identifier` | String | 构建记录的编号。 |
| `name` | String | 构建记录的名称。 |
| `job_url` | String | 构建任务的地址。 |
| `provider` | String | 构建工具的名称。 |
| `result_overview` | String | 构建结果的概述。 |
| `result_url` | String | 构建结果的地址。 |
| `start_at` | Number | 构建开始的时间。 |
| `status` | String | 构建的状态。 |
| `end_at` | Number | 构建结束的时间。 |
| `duration` | Number | 构建持续的时间，单位为秒。 |
| `work_items` | Object[] | 构建关联的PingCode工作项列表。 |

**权限:** 企业令牌

---
## 环境

### `PUT` 全量更新一个环境

**路径:** `/v1/release/environments/{env_id}`

用于全量更新一个环境。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `env_id` | String | 是 | 环境的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 是 | 环境的名称。同一团队内，环境的名称是唯一的。 |
| `html_url` | String | 否 | 环境的地址。如果为空，在PingCode中不显示相关跳转链接。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 环境的id。 |
| `url` | String | 环境的资源地址。 |
| `name` | String | 环境的名称。 |
| `html_url` | String | 环境的真实地址。 |

**权限:** 企业令牌

---
### `POST` 创建一个环境

**路径:** `/v1/release/environments`

用于创建一个环境。  企业内实际的部署环境，用于在PingCode中显示各个环境的部署信息。

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 是 | 环境的名称。同一团队内，环境的名称是唯一的。 |
| `html_url` | String | 否 | 环境的地址。如果为空，在PingCode中不显示相关跳转链接。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 环境的id。 |
| `url` | String | 环境的资源地址。 |
| `name` | String | 环境的名称。 |
| `html_url` | String | 环境的真实地址。 |

**权限:** 企业令牌

---
### `DELETE` 删除一个环境

**路径:** `/v1/release/environments/{env_id}`

用于删除一个环境。  删除环境之前，需要先删除与该环境关联的部署。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `env_id` | String | 是 | 环境的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 环境的id。 |
| `url` | String | 环境的资源地址。 |
| `name` | String | 环境的名称。 |
| `html_url` | String | 环境的真实地址。 |

**权限:** 企业令牌

---
### `GET` 获取一个环境

**路径:** `/v1/release/environments/{env_id}`

用于查看一个环境。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `env_id` | String | 是 | 环境的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 环境的id。 |
| `url` | String | 环境的资源地址。 |
| `name` | String | 环境的名称。 |
| `html_url` | String | 环境的真实地址。 |

**权限:** 企业令牌

---
### `GET` 获取环境列表

**路径:** `/v1/release/environments`

用于查询环境列表。

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 是 | 环境的名称。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 环境全量结构数据的数组。 |

**权限:** 企业令牌

---
### `PATCH` 部分更新一个环境

**路径:** `/v1/release/environments/{env_id}`

用于部分更新一个环境。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `env_id` | String | 是 | 环境的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 否 | 环境的名称。同一团队内，环境的名称是唯一的。 |
| `html_url` | String | 否 | 环境的地址。如果为空，在PingCode中不显示相关跳转链接。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 环境的id。 |
| `url` | String | 环境的资源地址。 |
| `name` | String | 环境的名称。 |
| `html_url` | String | 环境的真实地址。 |

**权限:** 企业令牌

---
## 部署

### `PUT` 全量更新一个部署

**路径:** `/v1/release/deploys/{deploy_id}`

用于全量更新一个部署。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `deploy_id` | String | 是 | 部署的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `status` | String | 是 | 部署的状态。 |
| `env_id` | String | 是 | 环境的id。 |
| `release_name` | String | 是 | 版本发布的名称。 |
| `release_url` | String | 否 | 版本发布的地址。如果为空，在PingCode中不显示相关跳转链接。 |
| `start_at` | Number | 是 | 部署开始的时间。 |
| `end_at` | Number | 是 | 部署结束的时间。 |
| `duration` | Number | 是 | 部署持续的时间。单位为秒。 |
| `work_item_identifiers` | String[] | 否 | PingCode工作项编号的列表。通过该参数将部署与一个或多个工作项关联。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 部署的id。 |
| `url` | String | 部署的资源地址。 |
| `status` | String | 部署的状态。 |
| `release_name` | String | 发布的名称。 |
| `environment` | Object | 环境的引用结构数据。 |
| `release_url` | String | 版本发布的地址。 |
| `start_at` | Number | 部署开始的时间。 |
| `end_at` | Number | 部署结束的时间。 |
| `duration` | Number | 部署持续的时间，单位为秒。 |
| `work_items` | Object[] | 部署关联的PingCode工作项列表。 |

**权限:** 企业令牌

---
### `POST` 创建一个部署

**路径:** `/v1/release/deploys`

用于创建一个部署。  企业内实际的部署记录，用于在PingCode中显示部署的详细信息。

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `status` | String | 是 | 部署的状态。 |
| `env_id` | String | 是 | 环境的id。 |
| `release_name` | String | 是 | 发布的名称。 |
| `release_url` | String | 否 | 版本发布的地址。如果为空，在PingCode中不显示相关跳转链接。 |
| `start_at` | Number | 是 | 部署开始的时间。 |
| `end_at` | Number | 是 | 部署结束的时间。 |
| `duration` | Number | 是 | 部署持续的时间。单位为秒。 |
| `work_item_identifiers` | String[] | 否 | PingCode工作项编号的列表。通过该参数将部署与一个或多个工作项关联。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 部署的id。 |
| `url` | String | 部署的资源地址。 |
| `status` | String | 部署的状态。 |
| `release_name` | String | 发布的名称。 |
| `environment` | Object | 环境的引用结构数据。 |
| `release_url` | String | 版本发布的地址。 |
| `start_at` | Number | 部署开始的时间。 |
| `end_at` | Number | 部署结束的时间。 |
| `duration` | Number | 部署持续的时间，单位为秒。 |
| `work_items` | Object[] | 部署关联的PingCode工作项列表。 |

**权限:** 企业令牌

---
### `DELETE` 删除一个部署

**路径:** `/v1/release/deploys/{deploy_id}`

用于删除一个部署。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `deploy_id` | String | 是 | 部署的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 部署的id。 |
| `url` | String | 部署的资源地址。 |
| `status` | String | 部署的状态。 |
| `release_name` | String | 发布的名称。 |
| `environment` | Object | 环境的引用结构数据。 |
| `release_url` | String | 版本发布的地址。 |
| `start_at` | Number | 部署开始的时间。 |
| `end_at` | Number | 部署结束的时间。 |
| `duration` | Number | 部署持续的时间，单位为秒。 |
| `work_items` | Object[] | 部署关联的PingCode工作项列表。 |

**权限:** 企业令牌

---
### `GET` 获取一个部署

**路径:** `/v1/release/deploys/{deploy_id}`

用于查看一个部署。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `deploy_id` | String | 是 | 部署的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 部署的id。 |
| `url` | String | 部署的资源地址。 |
| `status` | String | 部署的状态。 |
| `release_name` | String | 发布的名称。 |
| `environment` | Object | 发布的环境。 |
| `release_url` | String | 版本发布的地址。 |
| `start_at` | Number | 部署开始的时间。 |
| `end_at` | Number | 部署结束的时间。 |
| `duration` | Number | 部署持续的时间。单位为秒。 |
| `work_items` | Object[] | 部署关联的PingCode的工作项列表。 |

**权限:** 企业令牌

---
### `GET` 获取部署列表

**路径:** `/v1/release/deploys`

用于查询部署列表。

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `env_id` | String | 否 | 环境的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 部署的全量结构数据的数组。 |

**权限:** 企业令牌

---
### `PATCH` 部分更新一个部署

**路径:** `/v1/release/deploys/{deploy_id}`

用于部分更新一个部署。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `deploy_id` | String | 是 | 部署的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `status` | String | 否 | 部署的状态。 |
| `env_id` | String | 否 | 环境的id。 |
| `release_name` | String | 否 | 版本发布的名称。 |
| `release_url` | String | 否 | 版本发布的地址。如果为空，在PingCode中不显示相关跳转链接。 |
| `start_at` | Number | 否 | 部署开始的时间。 |
| `end_at` | Number | 否 | 部署结束的时间。 |
| `duration` | Number | 否 | 部署持续的时间。单位为秒。 |
| `work_item_identifiers` | String[] | 否 | PingCode工作项编号的列表。通过该参数将部署与一个或多个工作项关联。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 部署的id。 |
| `url` | String | 部署的资源地址。 |
| `status` | String | 部署的状态。 |
| `release_name` | String | 发布的名称。 |
| `environment` | Object | 环境的引用结构数据。 |
| `release_url` | String | 版本发布的地址。 |
| `start_at` | Number | 部署开始的时间。 |
| `end_at` | Number | 部署结束的时间。 |
| `duration` | Number | 部署持续的时间，单位为秒。 |
| `work_items` | Object[] | 部署关联的PingCode工作项列表。 |

**权限:** 企业令牌

---
