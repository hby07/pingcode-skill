# 💻 代码管理 — API 详细文档

> 本文档包含 44 个接口的完整参数说明。
> 来源: https://open.pingcode.com/

---

## 代码仓库

### `PUT` 全量更新一个代码仓库

**路径:** `/v1/scm/products/{product_id}/repositories/{repository_id}`

用于全量更新一个代码仓库。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 代码托管平台的id。 |
| `repository_id` | String | 是 | 代码仓库的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 是 | 代码仓库的名称。 |
| `full_name` | String | 是 | 代码仓库的全称。同一代码托管平台下，代码仓库的全称是唯一的。 |
| `description` | String | 否 | 代码仓库的简介。 |
| `is_fork` | Boolean | 否 | 是否是fork仓库。 |
| `is_private` | Boolean | 否 | 是否是私有仓库。 |
| `owner_name` | String | 否 | 代码仓库拥有者的用户名。 |
| `html_url` | String | 否 | 代码仓库在代码托管平台上的地址。如果为空，在PingCode中不显示相关跳转链接。 |
| `branches_url` | String | 否 | 代码仓库的分支地址，使用`{branch}`表示分支名。如果为空，在PingCode中不显示相关跳转链接。 |
| `commits_url` | String | 否 | 代码仓库的提交地址，使用`{sha}`表示提交的SHA值。如果为空，在PingCode中不显示相关跳转链接。 |
| `compare_url` | String | 否 | 代码仓库的分支对比地址，使用`{base}`和`{head}`表示基准分支名和需要进行对比的分支名。如果为空，在PingCode中不显示相关跳转链接。 |
| `pulls_url` | String | 否 | 代码仓库的拉取请求地址，使用`{number}`表示拉取请求的编号。如果为空，在PingCode中不显示相关跳转链接。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 代码仓库的id。 |
| `url` | String | 代码仓库的资源地址。 |
| `product` | Object | 托管平台的引用结构数据。 |
| `name` | String | 代码仓库的名称。 |
| `full_name` | String | 代码仓库的全称。 |
| `created_at` | Number | 代码仓库的创建时间。 |
| `owner` | Object | 代码仓库拥有者的引用结构数据。 |
| `is_fork` | Boolean | 代码仓库是否是fork仓库。 |
| `is_private` | Boolean | 代码仓库是否是私有仓库。 |
| `description` | String | 代码仓库的描述。 |
| `html_url` | String | 代码仓库的地址。 |
| `branches_url` | String | 代码仓库的分支地址模板。 |
| `commits_url` | String | 代码仓库的提交地址模板。 |
| `compare_url` | String | 代码仓库的分支对比地址模板。 |
| `pulls_url` | String | 代码仓库的拉取请求地址模板。 |

**权限:** 企业令牌

---
### `POST` 创建一个代码仓库

**路径:** `/v1/scm/products/{product_id}/repositories`

用于创建一个代码仓库。  代码托管平台内实际的代码仓库，用于在PingCode中显示代码仓库的详细信息。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 代码托管平台的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 是 | 代码仓库的名称。 |
| `full_name` | String | 是 | 代码仓库的全称。同一代码托管平台下，代码仓库的全称是唯一的。 |
| `description` | String | 否 | 代码仓库的简介。 |
| `is_fork` | Boolean | 否 | 是否是fork仓库。 |
| `is_private` | Boolean | 否 | 是否是私有仓库。 |
| `owner_name` | String | 否 | 代码仓库拥有者的用户名。 |
| `html_url` | String | 否 | 代码仓库的地址。如果为空，在PingCode中不显示相关跳转链接。 |
| `branches_url` | String | 否 | 代码仓库的分支地址，使用`{branch}`表示分支名。如果为空，在PingCode中不显示相关跳转链接。 |
| `commits_url` | String | 否 | 代码仓库的提交地址，使用`{sha}`表示提交的SHA值。如果为空，在PingCode中不显示相关跳转链接。 |
| `compare_url` | String | 否 | 代码仓库的分支对比地址，使用`{base}`和`{head}`表示基准分支名和需要进行对比的分支名。如果为空，在PingCode中不显示相关跳转链接。 |
| `pulls_url` | String | 否 | 代码仓库的拉取请求地址，使用`{number}`表示拉取请求的编号。如果为空，在PingCode中不显示相关跳转链接。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 代码仓库的id。 |
| `url` | String | 代码仓库的资源地址。 |
| `product` | Object | 托管平台的引用结构数据。 |
| `name` | String | 代码仓库的名称。 |
| `full_name` | String | 代码仓库的全称。 |
| `created_at` | Number | 代码仓库的创建时间。 |
| `owner` | Object | 代码仓库拥有者的引用结构数据。 |
| `is_fork` | Boolean | 代码仓库是否是fork仓库。 |
| `is_private` | Boolean | 代码仓库是否是私有仓库。 |
| `description` | String | 代码仓库的描述。 |
| `html_url` | String | 代码仓库的地址。 |
| `branches_url` | String | 代码仓库的分支地址模板。 |
| `commits_url` | String | 代码仓库的提交地址模板。 |
| `compare_url` | String | 代码仓库的分支对比地址模板。 |
| `pulls_url` | String | 代码仓库的拉取请求地址模板。 |

**权限:** 企业令牌

---
### `GET` 获取一个代码仓库

**路径:** `/v1/scm/products/{product_id}/repositories/{repository_id}`

用于查看一个代码仓库。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 托管平台的id。 |
| `repository_id` | String | 是 | 代码仓库的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 代码仓库的id。 |
| `url` | String | 代码仓库的资源地址。 |
| `product` | Object | 托管平台。 |
| `name` | String | 代码仓库的名称。 |
| `full_name` | String | 代码仓库的全称。 |
| `created_at` | Number | 代码仓库的创建时间。 |
| `owner` | Object | 代码仓库的拥有者。 |
| `is_fork` | Boolean | 代码仓库是否是fork仓库。 |
| `is_private` | Boolean | 代码仓库是否是私有仓库。 |
| `description` | String | 代码仓库的描述。 |
| `html_url` | String | 代码仓库的地址。 |
| `branches_url` | String | 代码仓库的分支地址模板，链接后面括号里的值会被替换成真实地址。 |
| `commits_url` | String | 代码仓库的提交地址模板，链接后面括号里的值会被替换成真实地址。 |
| `compare_url` | String | 代码仓库的分支对比地址模板，链接后面括号里的值会被替换成真实地址。 |
| `pulls_url` | String | 代码仓库的拉取请求地址模板，链接后面括号里的值会被替换成真实地址。 |

**权限:** 企业令牌

---
### `GET` 获取代码仓库列表

**路径:** `/v1/scm/products/{product_id}/repositories`

用于查询代码仓库列表。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 代码托管平台的id。 |

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `full_name` | String | 否 | 代码仓库的全称。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 代码仓库全量结构数据的数组。 |

**权限:** 企业令牌

---
### `PATCH` 部分更新一个代码仓库

**路径:** `/v1/scm/products/{product_id}/repositories/{repository_id}`

用于部分更新一个代码仓库。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 代码托管平台的id。 |
| `repository_id` | String | 是 | 代码仓库的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 否 | 代码仓库的名称。 |
| `full_name` | String | 否 | 代码仓库的全称。同一代码托管平台下，代码仓库的全称是唯一的。 |
| `description` | String | 否 | 代码仓库的简介。 |
| `is_fork` | Boolean | 否 | 是否是fork仓库。 |
| `is_private` | Boolean | 否 | 是否是私有仓库。 |
| `owner_name` | String | 否 | 代码仓库拥有者的用户名。 |
| `html_url` | String | 否 | 代码仓库在代码托管平台上的地址。如果为空，在PingCode中不显示相关跳转链接。 |
| `branches_url` | String | 否 | 代码仓库的分支地址，使用`{branch}`表示分支名。如果为空，在PingCode中不显示相关跳转链接。 |
| `commits_url` | String | 否 | 代码仓库的提交地址，使用`{sha}`表示提交的SHA值。如果为空，在PingCode中不显示相关跳转链接。 |
| `compare_url` | String | 否 | 代码仓库的分支对比地址，使用`{base}`和`{head}`表示基准分支名和需要进行对比的分支名。如果为空，在PingCode中不显示相关跳转链接。 |
| `pulls_url` | String | 否 | 代码仓库的拉取请求地址，使用`{number}`表示拉取请求的编号。如果为空，在PingCode中不显示相关跳转链接。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 代码仓库的id。 |
| `url` | String | 代码仓库的资源地址。 |
| `product` | Object | 托管平台的引用结构数据。 |
| `name` | String | 代码仓库的名称。 |
| `full_name` | String | 代码仓库的全称。 |
| `created_at` | Number | 代码仓库的创建时间。 |
| `owner` | Object | 代码仓库拥有者的引用结构数据。 |
| `is_fork` | Boolean | 代码仓库是否是fork仓库。 |
| `is_private` | Boolean | 代码仓库是否是私有仓库。 |
| `description` | String | 代码仓库的描述。 |
| `html_url` | String | 代码仓库的地址。 |
| `branches_url` | String | 代码仓库的分支地址模板。 |
| `commits_url` | String | 代码仓库的提交地址模板。 |
| `compare_url` | String | 代码仓库的分支对比地址模板。 |
| `pulls_url` | String | 代码仓库的拉取请求地址模板。 |

**权限:** 企业令牌

---
## 代码

### `` 代码仓库

**路径:** `代码仓库`

---
### `` 代码分支

**路径:** `代码分支`

---
### `` 代码评审

**路径:** `代码评审`

---
### `` 托管平台

**路径:** `托管平台`

---
### `` 托管平台用户

**路径:** `托管平台用户`

---
### `` 拉取请求

**路径:** `拉取请求`

---
### `` 提交

**路径:** `提交`

---
### `` 提交引用

**路径:** `提交引用`

---
## 代码分支

### `POST` 创建一个代码分支

**路径:** `/v1/scm/products/{product_id}/repositories/{repository_id}/branches`

用于创建一个代码分支。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 代码托管平台的id。 |
| `repository_id` | String | 是 | 代码仓库的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 是 | 分支的名称。同一代码仓库下，分支的名称是唯一的。 |
| `sender_name` | String | 是 | 分支创建者的用户名。 |
| `is_default` | Boolean | 否 | 是否设置为默认分支。当创建分支时，如果当前仓库的分支数为0，则新创建的分支会自动设置为该仓库的默认分支。如果创建分支时设置了该分支为默认分支，并且仓库已经有默认分支存在，那么其他分支将被取消默认属性，而该分支将被设置为新的默认分支。 |
| `work_item_identifiers` | String[] | 否 | PingCode工作项编号的列表。通过该参数将分支与一个或多个工作项关联，分支和工作项关联后，分支下所有的提交都会和该工作项关联。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 代码分支的id。 |
| `url` | String | 代码分支的资源地址。 |
| `product` | Object | 托管平台的引用结构数据。 |
| `repository` | Object | 代码仓库的引用结构数据。 |
| `name` | String | 代码分支的名称。 |
| `created_at` | Number | 代码分支的创建时间。 |
| `sender` | Object | 代码分支创建者的引用结构数据。 |
| `is_default` | Boolean | 代码分支是否为默认分支。 |
| `work_items` | Object[] | 代码分支关联的工作项列表。 |

**权限:** 企业令牌

---
### `DELETE` 删除一个代码分支

**路径:** `/v1/scm/products/{product_id}/repositories/{repository_id}/branches/{branch_id}`

用于删除一个代码分支。  删除分支后，不会移除该分支和工作项的关联历史，在关联历史中，依然可以查询到删除的分支。默认分支不能被删除。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 代码托管平台的id。 |
| `repository_id` | String | 是 | 代码仓库的id。 |
| `branch_id` | String | 是 | 分支的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 代码分支的id。 |
| `url` | String | 代码分支的资源地址。 |
| `product` | Object | 托管平台的引用结构数据。 |
| `repository` | Object | 代码仓库的引用结构数据。 |
| `name` | String | 代码分支的名称。 |
| `created_at` | Number | 代码分支的创建时间。 |
| `sender` | Object | 代码分支创建者的引用结构数据。 |
| `is_default` | Boolean | 代码分支是否为默认分支。 |
| `work_items` | Object[] | 代码分支关联的工作项列表。 |

**权限:** 企业令牌

---
### `GET` 获取一个代码分支

**路径:** `/v1/scm/products/{product_id}/repositories/{repository_id}/branches/{branch_id}`

用于查看一个代码分支。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 托管平台的id。 |
| `repository_id` | String | 是 | 代码仓库的id。 |
| `branch_id` | String | 是 | 代码分支的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 代码分支的id。 |
| `url` | String | 代码分支的资源地址。 |
| `product` | Object | 代码分支的托管平台。 |
| `repository` | Object | 代码分支的代码仓库。 |
| `name` | String | 代码分支的名称。 |
| `created_at` | Number | 代码分支的创建时间。 |
| `sender` | Object | 代码分支的创建者。 |
| `is_default` | Boolean | 代码分支是否为默认分支。 |
| `work_items` | Object[] | 代码分支关联的工作项列表。 |

**权限:** 企业令牌

---
### `GET` 获取代码分支列表

**路径:** `/v1/scm/products/{product_id}/repositories/{repository_id}/branches`

用于查询代码分支列表。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 代码托管平台的id。 |
| `repository_id` | String | 是 | 代码仓库的id。 |

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 否 | 分支的名称。 |
| `work_item_id` | String | 否 | 工作项的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 代码分支全量结构数据的数组。 |

**权限:** 企业令牌

---
### `PATCH` 部分更新一个代码分支

**路径:** `/v1/scm/products/{product_id}/repositories/{repository_id}/branches/{branch_id}`

用于部分更新一个代码分支。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 代码托管平台的id。 |
| `repository_id` | String | 是 | 代码仓库的id。 |
| `branch_id` | String | 是 | 分支的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `is_default` | Boolean | 否 | 是否设置为默认分支。该值只能是`true`，设置该分支为默认分支后将取消其他分支的默认属性。 |
| `work_item_identifiers` | String[] | 否 | PingCode工作项编号的列表。通过该参数将分支与一个或多个工作项关联，分支和工作项关联后，分支下所有的提交都会和该工作项关联。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 代码分支的id。 |
| `url` | String | 代码分支的资源地址。 |
| `product` | Object | 托管平台的引用结构数据。 |
| `repository` | Object | 代码仓库的引用结构数据。 |
| `name` | String | 代码分支的名称。 |
| `created_at` | Number | 代码分支的创建时间。 |
| `sender` | Object | 代码分支创建者的引用结构数据。 |
| `is_default` | Boolean | 代码分支是否为默认分支。 |
| `work_items` | Object[] | 代码分支关联的工作项列表。 |

**权限:** 企业令牌

---
## 代码评审

### `PUT` 全量更新一个代码评审

**路径:** `/v1/scm/products/{product_id}/repositories/{repository_id}/pull_requests/{pull_request_id}/reviews/{review_id}`

用于全量更新一个代码评审。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 代码托管平台的id。 |
| `repository_id` | String | 是 | 代码仓库的id。 |
| `pull_request_id` | String | 是 | 拉取请求的id。 |
| `review_id` | String | 是 | 代码评审的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `reviewer_name` | String | 是 | 评审人的用户名。 |
| `status` | String | 是 | 代码评审的状态。 |
| `submitted_at` | Number | 是 | 提交的时间。 |
| `description` | String | 否 | 代码评审的描述。 |
| `html_url` | String | 否 | 代码评审的地址。如果为空，在PingCode中不显示相关跳转链接。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 代码评审的id。 |
| `url` | String | 代码评审的资源地址。 |
| `product` | Object | 代码评审的托管平台。 |
| `repository` | Object | 代码评审的代码仓库。 |
| `pull_request` | Object | 代码评审的拉取请求。 |
| `reviewer` | Object | 代码评审的评审人。 |
| `status` | String | 代码评审的状态。 |
| `description` | String | 代码评审的描述。 |
| `submitted_at` | Number | 代码评审的提交时间。 |
| `html_url` | String | 代码评审的地址。 |

**权限:** 企业令牌

---
### `POST` 创建一个代码评审

**路径:** `/v1/scm/products/{product_id}/repositories/{repository_id}/pull_requests/{pull_request_id}/reviews`

用于创建一个代码评审。  拉取请求实际的代码评审记录，用于在PingCode中显示代码评审的详细信息。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 代码托管平台的id。 |
| `repository_id` | String | 是 | 代码仓库的id。 |
| `pull_request_id` | String | 是 | 拉取请求的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `status` | String | 是 | 代码评审的状态。 |
| `reviewer_name` | String | 是 | 评审人的用户名。 |
| `description` | String | 否 | 代码评审的描述。 |
| `submitted_at` | Number | 是 | 提交的时间。 |
| `html_url` | String | 否 | 代码评审的地址。如果为空，在PingCode中不显示相关跳转链接。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 代码评审的id。 |
| `url` | String | 代码评审的资源地址。 |
| `product` | Object | 代码评审的托管平台。 |
| `repository` | Object | 代码评审的代码仓库。 |
| `pull_request` | Object | 代码评审的拉取请求。 |
| `reviewer` | Object | 代码评审的评审人。 |
| `status` | String | 代码评审的状态。 |
| `description` | String | 代码评审的描述。 |
| `submitted_at` | Number | 代码评审的提交时间。 |
| `html_url` | String | 代码评审的地址。 |

**权限:** 企业令牌

---
### `GET` 获取一个代码评审

**路径:** `/v1/scm/products/{product_id}/repositories/{repository_id}/pull_requests/{pull_request_id}/reviews/{review_id}`

用于查看一个代码评审。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 代码托管平台的id。 |
| `repository_id` | String | 是 | 代码仓库的id。 |
| `pull_request_id` | String | 是 | 拉取请求的id。 |
| `review_id` | String | 是 | 代码评审的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 代码评审的id。 |
| `url` | String | 代码评审的资源地址。 |
| `product` | Object | 代码评审的托管平台。 |
| `repository` | Object | 代码评审的代码仓库。 |
| `pull_request` | Object | 代码评审的拉取请求。 |
| `reviewer` | Object | 代码评审的评审人。 |
| `status` | String | 代码评审的状态。 |
| `description` | String | 代码评审的描述。 |
| `submitted_at` | Number | 代码评审的提交时间。 |
| `html_url` | String | 代码评审的地址。 |

**权限:** 企业令牌

---
### `GET` 获取代码评审列表

**路径:** `/v1/scm/products/{product_id}/repositories/{repository_id}/pull_requests/{pull_request_id}/reviews`

用于查询代码评审列表。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 代码托管平台的id。 |
| `repository_id` | String | 是 | 代码仓库的id。 |
| `pull_request_id` | String | 是 | 拉取请求的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 代码评审全量结构数据的数组。 |

**权限:** 企业令牌

---
### `PATCH` 部分更新一个代码评审

**路径:** `/v1/scm/products/{product_id}/repositories/{repository_id}/pull_requests/{pull_request_id}/reviews/{review_id}`

用于部分更新一个代码评审。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 代码托管平台的id。 |
| `repository_id` | String | 是 | 代码仓库的id。 |
| `pull_request_id` | String | 是 | 拉取请求的id。 |
| `review_id` | String | 是 | 代码评审的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `reviewer_name` | String | 否 | 评审人的用户名。 |
| `status` | String | 否 | 代码评审的状态。 |
| `description` | String | 否 | 代码评审的描述。 |
| `submitted_at` | Number | 否 | 提交的时间。 |
| `html_url` | String | 否 | 代码评审的地址。如果为空，在PingCode中不显示相关跳转链接。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 代码评审的id。 |
| `url` | String | 代码评审的资源地址。 |
| `product` | Object | 代码评审的托管平台。 |
| `repository` | Object | 代码评审的代码仓库。 |
| `pull_request` | Object | 代码评审的拉取请求。 |
| `reviewer` | Object | 代码评审的评审人。 |
| `status` | String | 代码评审的状态。 |
| `description` | String | 代码评审的描述。 |
| `submitted_at` | Number | 代码评审的提交时间。 |
| `html_url` | String | 代码评审的地址。 |

**权限:** 企业令牌

---
## 托管平台

### `PUT` 全量更新一个托管平台

**路径:** `/v1/scm/products/{product_id}`

用于全量更新一个托管平台。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 代码托管平台的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 是 | 代码托管平台的名称，在一个企业中这个名称是唯一的。 |
| `type` | String | 是 | 代码托管平台的产品类型，主要用于显示图标。 |
| `description` | String | 否 | 代码托管平台简介。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 托管平台的id。 |
| `url` | String | 托管平台的资源地址。 |
| `name` | String | 托管平台的名称。 |
| `type` | String | 托管平台的类型。 |
| `description` | String | 托管平台的描述。 |

**权限:** 企业令牌

---
### `POST` 创建一个托管平台

**路径:** `/v1/scm/products`

用于创建一个托管平台。  企业内实际的代码托管平台，例如Github或私有部署的Gitlab。

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 是 | 代码托管平台的名称，在一个企业中这个名称是唯一的。 |
| `type` | String | 是 | 代码托管平台的产品类型，主要用于显示图标。 |
| `description` | String | 否 | 代码托管平台的简介 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 托管平台的id。 |
| `url` | String | 托管平台的资源地址。 |
| `name` | String | 托管平台的名称。 |
| `type` | String | 托管平台的类型。 |
| `description` | String | 托管平台的描述。 |

**权限:** 企业令牌

---
### `GET` 获取一个托管平台

**路径:** `/v1/scm/products/{product_id}`

用于查看一个托管平台。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 托管平台的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 托管平台的id。 |
| `url` | String | 托管平台的资源地址。 |
| `name` | String | 托管平台的名称。 |
| `type` | String | 托管平台的类型。 |
| `description` | String | 托管平台的描述。 |

**权限:** 企业令牌

---
### `GET` 获取托管平台列表

**路径:** `/v1/scm/products`

用于查询托管平台列表。

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 否 | 代码托管平台的名称。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 托管平台全量结构数据的数组。 |

**权限:** 企业令牌

---
### `PATCH` 部分更新一个托管平台

**路径:** `/v1/scm/products/{product_id}`

用于部分更新一个托管平台。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 代码托管平台的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 否 | 代码托管平台的名称，在一个企业中这个名称是唯一的。 |
| `type` | String | 否 | 代码托管平台的产品类型，主要用于显示图标。 |
| `description` | String | 否 | 代码托管平台简介。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 托管平台的id。 |
| `url` | String | 托管平台的资源地址。 |
| `name` | String | 托管平台的名称。 |
| `type` | String | 托管平台的类型。 |
| `description` | String | 托管平台的描述。 |

**权限:** 企业令牌

---
## 托管平台用户

### `PUT` 全量更新一个托管平台用户

**路径:** `/v1/scm/products/{product_id}/users/{user_id}`

用于全量更新一个托管平台用户。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 代码托管平台的id。 |
| `user_id` | String | 是 | 代码托管平台上的用户id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 是 | 代码托管平台上的用户名，同一代码托管平台下，该用户名是唯一的。 |
| `display_name` | String | 否 | 用户显示名。 |
| `html_url` | String | 否 | 代码托管平台上的用户主页地址。 |
| `avatar_url` | String | 否 | 代码托管平台上的用户头像地址。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 托管平台用户的id。 |
| `url` | String | 托管平台用户的资源地址。 |
| `product` | Object | 托管平台的引用结构数据。 |
| `name` | String | 托管平台用户的名称。 |
| `display_name` | String | 托管平台用户的显示名。 |
| `html_url` | String | 代码托管平台上的用户主页地址。 |
| `avatar_url` | String | 代码托管平台上的用户头像地址。 |

**权限:** 企业令牌

---
### `POST` 创建一个托管平台用户

**路径:** `/v1/scm/products/{product_id}/users`

用于创建一个托管平台用户。  代码托管平台内实际的用户，用于在PingCode中显示该用户在代码托管平台上的名称、头像以及主页的信息。如果没有手动创建用户，在操作代码仓库、分支、拉取请求时，将自动创建仅包含该用户名的用户。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 代码托管平台的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 是 | 代码托管平台上的用户名，同一代码托管平台下，该用户名是唯一的。 |
| `display_name` | String | 否 | 用户显示名。 |
| `html_url` | String | 否 | 代码托管平台上的用户主页地址。 |
| `avatar_url` | String | 否 | 代码托管平台上的用户头像地址。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 托管平台用户的id。 |
| `url` | String | 托管平台用户的资源地址。 |
| `product` | Object | 托管平台的引用结构数据。 |
| `name` | String | 托管平台用户的名称。 |
| `display_name` | String | 托管平台用户的显示名。 |
| `html_url` | String | 代码托管平台上的用户主页地址。 |
| `avatar_url` | String | 代码托管平台上的用户头像地址。 |

**权限:** 企业令牌

---
### `GET` 获取一个托管平台用户

**路径:** `/v1/scm/products/{product_id}/users/{user_id}`

用于查看一个托管平台用户。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 托管平台的id。 |
| `user_id` | String | 是 | 托管平台用户的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 托管平台用户的id。 |
| `url` | String | 托管平台用户的资源地址。 |
| `product` | Object | 托管平台。 |
| `name` | String | 托管平台用户的名称。 |
| `display_name` | String | 托管平台用户的显示名。 |
| `html_url` | String | 代码托管平台上的用户主页地址。 |
| `avatar_url` | String | 代码托管平台上的用户头像地址。 |

**权限:** 企业令牌

---
### `GET` 获取托管平台用户列表

**路径:** `/v1/scm/products/{product_id}/users`

用于查询托管平台用户列表。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 代码托管平台的id。 |

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 否 | 代码托管平台上的用户名。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 托管平台用户全量结构数据的数组。 |

**权限:** 企业令牌

---
### `PATCH` 部分更新一个托管平台用户

**路径:** `/v1/scm/products/{product_id}/users/{user_id}`

用于部分更新一个托管平台用户。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 代码托管平台的id。 |
| `user_id` | String | 是 | 代码托管平台上的用户id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 否 | 代码托管平台上的用户名，同一代码托管平台下，该用户名是唯一的。 |
| `display_name` | String | 否 | 用户显示名。 |
| `html_url` | String | 否 | 代码托管平台上的用户主页地址。 |
| `avatar_url` | String | 否 | 代码托管平台上的用户头像地址。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 托管平台用户的id。 |
| `url` | String | 托管平台用户的资源地址。 |
| `product` | Object | 托管平台的引用结构数据。 |
| `name` | String | 托管平台用户的名称。 |
| `display_name` | String | 托管平台用户的显示名。 |
| `html_url` | String | 代码托管平台上的用户主页地址。 |
| `avatar_url` | String | 代码托管平台上的用户头像地址。 |

**权限:** 企业令牌

---
## 拉取请求

### `PUT` 全量更新一个拉取请求

**路径:** `/v1/scm/products/{product_id}/repositories/{repository_id}/pull_requests/{pull_request_id}`

用于全量更新一个拉取请求。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 代码托管平台的id。 |
| `repository_id` | String | 是 | 代码仓库的id。 |
| `pull_request_id` | String | 是 | 拉取请求的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `title` | String | 是 | 拉取请求的标题。 |
| `creator_name` | String | 是 | 拉取请求创建者的用户名。 |
| `source_branch_id` | String | 是 | 源分支的id。 |
| `target_branch_id` | String | 是 | 目标分支的id。 |
| `status` | String | 是 | 拉取请求的状态。 |
| `description` | String | 否 | 拉取请求的描述。 |
| `merged_at` | Number | 否 | 拉取请求合并的时间。当拉取请求状态为`merged`时，该值为必填。 |
| `merged_commit_sha` | String | 否 | 源分支最后一次提交的SHA值。当拉取请求状态为`merged`时，该值为必填。 |
| `merged_by_name` | String | 否 | 拉取请求合并者的用户名。当拉取请求状态为`merged`时，该值为必填。 |
| `comments_count` | Number | 否 | 拉取请求的评论数量。 |
| `review_comments_count` | Number | 否 | 代码评审的评论数量。 |
| `commits_count` | Number | 否 | 代码的提交数量。 |
| `additions_count` | Number | 否 | 新增文件的数量。 |
| `deletions_count` | Number | 否 | 删除文件的数量。 |
| `changed_files_count` | Number | 否 | 更改文件的数量。 |
| `work_item_identifiers` | String[] | 否 | PingCode工作项编号的列表。通过该参数将拉取请求与一个或多个工作项关联。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 拉取请求的id。 |
| `url` | String | 拉取请求的资源地址。 |
| `product` | Object | 拉取请求的托管平台。 |
| `repository` | Object | 拉取请求的代码仓库。 |
| `title` | String | 拉取请求的标题。 |
| `number` | Number | 拉取请求的编号。 |
| `status` | String | 拉取请求的状态。 |
| `description` | String | 拉取请求的描述。 |
| `author` | Object | 拉取请求的创建者。 |
| `source_branch` | Object | 拉取请求的源分支。 |
| `target_branch` | Object | 拉取请求的目标分支。 |
| `created_at` | Number | 拉取请求的创建时间。 |
| `merged_at` | Number | 拉取请求的合并的时间。 |
| `merged_commit_sha` | String | 拉取请求的源分支最后一次提交的SHA值。 |
| `merged_by` | Object | 拉取请求的合并者。 |
| `comments_count` | Number | 拉取请求的评论数量。 |
| `review_comments_count` | Number | 拉取请求的代码评审评论数量。 |
| `commits_count` | Number | 拉取请求的提交数量。 |
| `additions_count` | Number | 拉取请求的新增文件数量。 |
| `deletions_count` | Number | 拉取请求的删除文件数量。 |
| `changed_files_count` | Number | 拉取请求的更改文件数量。 |
| `work_items` | Object[] | 拉取请求关联的PingCode的工作项列表。 |

**权限:** 企业令牌

---
### `POST` 创建一个拉取请求

**路径:** `/v1/scm/products/{product_id}/repositories/{repository_id}/pull_requests`

用于创建一个拉取请求。  代码仓库内实际的拉取请求，用于在PingCode中显示拉取请求的详细信息。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 代码托管平台的id。 |
| `repository_id` | String | 是 | 代码仓库的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `title` | String | 是 | 拉取请求的标题。 |
| `number` | Number | 是 | 拉取请求的编号。同一代码仓库下，该值是唯一的。 |
| `creator_name` | String | 是 | 拉取请求创建者的用户名。 |
| `source_branch_id` | String | 否 | 源分支的id。 |
| `target_branch_id` | String | 是 | 目标分支的id。 |
| `status` | String | 是 | 拉取请求的状态。 |
| `description` | String | 否 | 拉取请求的描述。 |
| `merged_at` | Number | 否 | 拉取请求合并的时间。当拉取请求状态为`merged`时，该值为必填。 |
| `merged_commit_sha` | String | 否 | 源分支最后一次提交的SHA值。当拉取请求状态为`merged`时，该值为必填。 |
| `merged_by_name` | String | 否 | 拉取请求合并者的用户名。当拉取请求状态为`merged`时，该值为必填。 |
| `comments_count` | Number | 否 | 拉取请求的评论数量。 |
| `review_comments_count` | Number | 否 | 代码评审的评论数量。 |
| `commits_count` | Number | 否 | 代码的提交数量。 |
| `additions_count` | Number | 否 | 新增文件的数量。 |
| `deletions_count` | Number | 否 | 删除文件的数量。 |
| `changed_files_count` | Number | 否 | 更改文件的数量。 |
| `work_item_identifiers` | String[] | 否 | PingCode工作项编号的列表。通过该参数将拉取请求与一个或多个工作项关联。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 拉取请求的id。 |
| `url` | String | 拉取请求的资源地址。 |
| `product` | Object | 拉取请求的托管平台。 |
| `repository` | Object | 拉取请求的代码仓库。 |
| `title` | String | 拉取请求的标题。 |
| `number` | Number | 拉取请求的编号。 |
| `status` | String | 拉取请求的状态。 |
| `description` | String | 拉取请求的描述。 |
| `author` | Object | 拉取请求的创建者。 |
| `source_branch` | Object | 拉取请求的源分支。 |
| `target_branch` | Object | 拉取请求的目标分支。 |
| `created_at` | Number | 拉取请求的创建时间。 |
| `merged_at` | Number | 拉取请求的合并的时间。 |
| `merged_commit_sha` | String | 拉取请求的源分支最后一次提交的SHA值。 |
| `merged_by` | Object | 拉取请求的合并者。 |
| `comments_count` | Number | 拉取请求的评论数量。 |
| `review_comments_count` | Number | 拉取请求的代码评审评论数量。 |
| `commits_count` | Number | 拉取请求的提交数量。 |
| `additions_count` | Number | 拉取请求的新增文件数量。 |
| `deletions_count` | Number | 拉取请求的删除文件数量。 |
| `changed_files_count` | Number | 拉取请求的更改文件数量。 |
| `work_items` | Object[] | 拉取请求关联的PingCode的工作项列表。 |

**权限:** 企业令牌

---
### `GET` 获取一个拉取请求

**路径:** `/v1/scm/products/{product_id}/repositories/{repository_id}/pull_requests/{pull_request_id}`

用于查看一个拉取请求。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 代码托管平台的id。 |
| `repository_id` | String | 是 | 代码仓库的id。 |
| `pull_request_id` | String | 是 | 拉取请求的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 拉取请求的id。 |
| `url` | String | 拉取请求的资源地址。 |
| `product` | Object | 拉取请求的托管平台。 |
| `repository` | Object | 拉取请求的代码仓库。 |
| `title` | String | 拉取请求的标题。 |
| `number` | Number | 拉取请求的编号。 |
| `status` | String | 拉取请求的状态。 |
| `description` | String | 拉取请求的描述。 |
| `author` | Object | 拉取请求的创建者。 |
| `source_branch` | Object | 拉取请求的源分支。 |
| `target_branch` | Object | 拉取请求的目标分支。 |
| `created_at` | Number | 拉取请求的创建时间。 |
| `merged_at` | Number | 拉取请求的合并的时间。 |
| `merged_commit_sha` | String | 拉取请求的源分支最后一次提交的SHA值。 |
| `merged_by` | Object | 拉取请求的合并者。 |
| `comments_count` | Number | 拉取请求的评论数量。 |
| `review_comments_count` | Number | 拉取请求的代码评审评论数量。 |
| `commits_count` | Number | 拉取请求的提交数量。 |
| `additions_count` | Number | 拉取请求的新增文件数量。 |
| `deletions_count` | Number | 拉取请求的删除文件数量。 |
| `changed_files_count` | Number | 拉取请求的更改文件数量。 |
| `work_items` | Object[] | 拉取请求关联的PingCode的工作项列表。 |

**权限:** 企业令牌

---
### `GET` 获取拉取请求列表

**路径:** `/v1/scm/products/{product_id}/repositories/{repository_id}/pull_requests`

用于查询拉取请求列表。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 代码托管平台的id。 |
| `repository_id` | String | 是 | 代码仓库的id。 |

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `number` | number | 否 | 拉取请求的编号。 |
| `work_item_id` | String | 否 | 工作项的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 拉取请求全量结构数据的数组。 |

**权限:** 企业令牌

---
### `PATCH` 部分更新一个拉取请求

**路径:** `/v1/scm/products/{product_id}/repositories/{repository_id}/pull_requests/{pull_request_id}`

用于部分更新一个拉取请求。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 代码托管平台的id。 |
| `repository_id` | String | 是 | 代码仓库的id。 |
| `pull_request_id` | String | 是 | 拉取请求的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `status` | String | 是 | 拉取请求的状态。 |
| `title` | String | 否 | 拉取请求的标题。 |
| `creator_name` | String | 否 | 拉取请求创建者的用户名。 |
| `description` | String | 否 | 拉取请求的描述。 |
| `target_branch_id` | String | 否 | 目标分支的id。 |
| `source_branch_id` | String | 否 | 源分支的id。 |
| `merged_at` | Number | 否 | 拉取请求合并的时间。当拉取请求状态为`merged`时，该值为必填。 |
| `merged_commit_sha` | String | 否 | 源分支最后一次提交的SHA值。当拉取请求状态为`merged`时，该值为必填。 |
| `merged_by_name` | String | 否 | 拉取请求合并者的用户名。当拉取请求状态为`merged`时，该值为必填。 |
| `comments_count` | Number | 否 | 拉取请求的评论数量。 |
| `review_comments_count` | Number | 否 | 代码评审的评论数量。 |
| `commits_count` | Number | 否 | 代码的提交数量。 |
| `additions_count` | Number | 否 | 新增文件的数量。 |
| `deletions_count` | Number | 否 | 删除文件的数量。 |
| `changed_files_count` | Number | 否 | 更改文件的数量。 |
| `work_item_identifiers` | String[] | 否 | PingCode工作项编号的列表。通过该参数将拉取请求与一个或多个工作项关联。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 拉取请求的id。 |
| `url` | String | 拉取请求的资源地址。 |
| `product` | Object | 拉取请求的托管平台。 |
| `repository` | Object | 拉取请求的代码仓库。 |
| `title` | String | 拉取请求的标题。 |
| `number` | Number | 拉取请求的编号。 |
| `status` | String | 拉取请求的状态。 |
| `description` | String | 拉取请求的描述。 |
| `author` | Object | 拉取请求的创建者。 |
| `source_branch` | Object | 拉取请求的源分支。 |
| `target_branch` | Object | 拉取请求的目标分支。 |
| `created_at` | Number | 拉取请求的创建时间。 |
| `merged_at` | Number | 拉取请求的合并的时间。 |
| `merged_commit_sha` | String | 拉取请求的源分支最后一次提交的SHA值。 |
| `merged_by` | Object | 拉取请求的合并者。 |
| `comments_count` | Number | 拉取请求的评论数量。 |
| `review_comments_count` | Number | 拉取请求的代码评审评论数量。 |
| `commits_count` | Number | 拉取请求的提交数量。 |
| `additions_count` | Number | 拉取请求的新增文件数量。 |
| `deletions_count` | Number | 拉取请求的删除文件数量。 |
| `changed_files_count` | Number | 拉取请求的更改文件数量。 |
| `work_items` | Object[] | 拉取请求关联的PingCode的工作项列表。 |

**权限:** 企业令牌

---
## 提交

### `POST` 创建一个提交

**路径:** `/v1/scm/commits`

用于创建一个提交。

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `sha` | String | 是 | 提交的SHA值。 |
| `message` | String | 是 | 提交的描述信息。 |
| `committer_name` | String | 是 | 提交者的用户名。 |
| `committed_at` | Number | 是 | 提交的时间。 |
| `tree_id` | String | 否 | 提交树的SHA值。 |
| `files_added` | String[] | 是 | 新增文件的文件名列表。 |
| `files_removed` | String[] | 是 | 移除文件的文件名列表。 |
| `files_modified` | String[] | 是 | 更新文件的文件名列表。 |
| `work_item_identifiers` | String[] | 否 | PingCode工作项编号的列表。通过该参数将提交与一个或多个工作项关联。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 提交的id。 |
| `url` | String | 提交的资源地址。 |
| `sha` | String | 提交的SHA值。 |
| `message` | String | 提交的描述信息。 |
| `committer_name` | String | 提交者的用户名。 |
| `committed_at` | Number | 提交的时间。 |
| `tree_id` | String | 提交树的SHA值。 |
| `files_added` | String[] | 提交新增文件的文件名列表。 |
| `files_removed` | String[] | 提交移除文件的文件名列表。 |
| `files_modified` | String[] | 提交更新文件的文件名列表。 |
| `file_changed_count` | Number | 提交更新文件数量。 |
| `work_items` | Object[] | 提交关联的PingCode工作项列表。 |

**权限:** 企业令牌

---
### `GET` 获取一个提交

**路径:** `/v1/scm/commits/{commit_id_or_sha}`

用于查看一个提交。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `commit_id_or_sha` | String | 是 | 提交的id或SHA值。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 提交的id。 |
| `url` | String | 提交的资源地址。 |
| `sha` | String | 提交的SHA值。 |
| `message` | String | 提交的描述信息。 |
| `committer_name` | String | 提交者的用户名。 |
| `committed_at` | Number | 提交的时间。 |
| `tree_id` | String | 提交树的SHA值。 |
| `files_added` | String[] | 提交新增文件的文件名列表。 |
| `files_removed` | String[] | 提交移除文件的文件名列表。 |
| `files_modified` | String[] | 提交更新文件的文件名列表。 |
| `file_changed_count` | Number | 提交更新文件数量。 |
| `work_items` | Object[] | 提交关联的PingCode的工作项列表。 |

**权限:** 企业令牌

---
### `GET` 获取提交列表

**路径:** `/v1/scm/commits`

用于查询提交列表。

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `sha` | String | 否 | 提交的SHA值。 |
| `work_item_id` | String | 否 | 工作项的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 提交全量结构数据的数组。 |

**权限:** 企业令牌

---
## 提交引用

### `POST` 创建一个提交引用

**路径:** `/v1/scm/products/{product_id}/repositories/{repository_id}/refs`

用于创建一个提交引用。  提交引用是提交与分支的一种关联关系，一个提交可以与多个分支关联，一个分支也可以与多个提交关联。当提交与分支关联后，提交会自动与由此分支发起的拉取请求关联，当拉取请求合并后，这些关联的提交将自动被标记为“已合并”状态。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 代码托管平台的id。 |
| `repository_id` | String | 是 | 代码仓库的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `sha` | String | 是 | 提交的SHA值。 |
| `meta_type` | String | 是 | 引用实体的类型。 |
| `meta_id` | String | 是 | 引用实体的id，例如：`branch_id`。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 提交引用的id。 |
| `url` | String | 提交引用的资源地址。 |
| `product` | Object | 托管平台的引用结构数据。 |
| `repository` | Object | 代码仓库的引用结构数据。 |
| `commit` | Object | 提交的引用结构数据。 |
| `meta` | Object | 提交引用实体的引用结构数据。 |

**权限:** 企业令牌

---
### `GET` 获取一个提交引用

**路径:** `/v1/scm/products/{product_id}/repositories/{repository_id}/refs/{ref_id}`

用于查看一个提交引用。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 托管平台的id。 |
| `repository_id` | String | 是 | 代码仓库的id。 |
| `ref_id` | String | 是 | 提交引用的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 提交引用的id。 |
| `url` | String | 提交引用的资源地址。 |
| `product` | Object | 提交引用的托管平台。 |
| `repository` | Object | 提交引用的代码仓库。 |
| `commit` | Object | 提交引用的代码提交。 |
| `meta` | Object | 提交引用的实体，如分支。 |

**权限:** 企业令牌

---
### `GET` 获取提交引用列表

**路径:** `/v1/scm/products/{product_id}/repositories/{repository_id}/refs`

用于查询提交引用列表。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 代码托管平台的id。 |
| `repository_id` | String | 是 | 代码仓库的id。 |

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `meta_type` | String | 是 | 引用实体的类型。 |
| `meta_id` | String | 是 | 引用实体的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 提交引用全量结构数据的数组。 |

**权限:** 企业令牌

---
