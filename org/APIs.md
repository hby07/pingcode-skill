# 🏢 组织管理 — API 详细文档

> 本文档包含 50 个接口的完整参数说明。
> 来源: https://open.pingcode.com/

---

## 个人

### `GET` 获取个人信息

**路径:** `/v1/myself`

用于查看个人信息。

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 个人的id。 |
| `url` | String | 个人的地址。 |
| `name` | String | 个人的名称。 |
| `display_name` | String | 个人的显示名。 |
| `avatar` | String | 个人的头像。 |
| `email` | String | 个人的邮箱。 |
| `mobile` | String | 个人的手机号。 |
| `status` | String | 个人的状态。 |
| `preferences` | Object | 个人的偏好设置。 |

**权限:** 用户令牌

---
## 企业成员

### `POST` 创建一个企业成员

**路径:** `/v1/directory/users`

用于创建一个企业成员。

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 是 | 企业成员的名称，在一个企业中这个名称是唯一的。 |
| `display_name` | String | 是 | 企业成员的显示名。 |
| `email` | String | 否 | 企业成员的邮箱地址，在一个企业中这个邮箱地址是唯一的，邮箱地址和手机号其中一个必填。 |
| `mobile` | String | 否 | 企业成员的手机号，在一个企业中这个手机号是唯一，邮箱地址和手机号其中一个必填。 |
| `password` | String | 否 | 企业成员的密码，长度为6～200的字符串(包含6和200)。 |
| `department_id` | String | 否 | 企业成员的部门id。 |
| `job_id` | String | 否 | 企业成员的职位id。 |
| `employee_number` | String | 否 | 企业成员的工号。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 企业成员的id。 |
| `url` | String | 企业成员的资源地址。 |
| `name` | String | 企业成员的名称。 |
| `display_name` | String | 企业成员的显示名。 |
| `avatar` | String | 企业成员的头像地址。 |
| `department` | Object | 企业成员的部门。 |
| `job` | Object | 企业成员的职位。 |
| `email` | String | 企业成员的邮箱地址。 |
| `mobile` | String | 企业成员的手机号。 |
| `status` | String | 企业成员的状态。 |
| `employee_number` | String | 企业成员的工号。 |

**权限:** 企业令牌/用户令牌

---
### `PATCH` 批量更新企业成员属性

**路径:** `/v1/directory/users/bulk`

用于批量更新企业成员属性。

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `user_ids` | String[] | 是 | 企业成员的id数组，不能包含自己和团队拥有者。 |
| `property_name` | String | 是 | 需要更新的企业成员属性名，目前仅支持：status（可选值为：enabled、disabled） |
| `property_value` | String | 是 | 需要更新的企业成员属性值。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `state` | String | 操作状态。 |
| `user_id` | String | 企业成员的id。 |
| `message` | String | 操作失败时的错误信息。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个企业成员

**路径:** `/v1/directory/users/{user_id}`

用于查看一个企业成员。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `user_id` | String | 是 | 企业成员的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 企业成员的id。 |
| `url` | String | 企业成员的资源地址。 |
| `name` | String | 企业成员的名称。 |
| `display_name` | String | 企业成员的显示名。 |
| `avatar` | String | 企业成员的头像地址。 |
| `department` | Object | 企业成员的部门。 |
| `job` | Object | 企业成员的职位。 |
| `email` | String | 企业成员的邮箱地址。 |
| `mobile` | String | 企业成员的手机号。 |
| `status` | String | 企业成员的状态。 |
| `employee_number` | String | 企业成员的工号。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取企业成员列表

**路径:** `/v1/directory/users`

用于查询企业成员列表。

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 否 | 企业成员的名称，在一个企业中这个名称是唯一的。 |
| `keywords` | String | 否 | 关键词模糊搜索，支持姓名、用户名。 |
| `emails` | String | 否 | 企业成员的邮箱地址，使用','分割，最多只能20个。 |
| `mobiles` | String | 否 | 企业成员的手机号，使用','分割，最多只能20个。 |
| `department_ids` | String | 否 | 企业成员的部门id，使用','分割，最多只能20个。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 企业成员全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `PATCH` 部分更新一个企业成员

**路径:** `/v1/directory/users/{user_id}`

用于部分更新一个企业成员。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `user_id` | String | 是 | 企业成员的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 否 | 企业成员的名称，在一个企业中这个名称是唯一的。 |
| `display_name` | String | 否 | 企业成员的显示名。 |
| `email` | String | 否 | 企业成员的邮箱地址，在一个企业中这个邮箱地址是唯一的。 |
| `mobile` | String | 否 | 企业成员的手机号，在一个企业中这个手机号是唯一的。 |
| `status` | String | 否 | 企业成员的状态。 |
| `employee_number` | String | 否 | 企业成员的工号。 |
| `department_id` | String | 否 | 企业成员的部门id。 |
| `job_id` | String | 否 | 企业成员的职位id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 企业成员的id。 |
| `url` | String | 企业成员的资源地址。 |
| `name` | String | 企业成员的名称。 |
| `display_name` | String | 企业成员的显示名。 |
| `avatar` | String | 企业成员的头像地址。 |
| `department` | Object | 企业成员的部门。 |
| `job` | Object | 企业成员的职位。 |
| `email` | String | 企业成员的邮箱地址。 |
| `mobile` | String | 企业成员的手机号。 |
| `status` | String | 企业成员的状态。 |
| `employee_number` | String | 企业成员的工号。 |

**权限:** 企业令牌/用户令牌

---
## 企业

### `GET` 获取企业信息

**路径:** `/v1/directory/team`

用于查看企业信息。

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 企业的id。 |
| `url` | String | 企业的地址。 |
| `name` | String | 企业的名称。 |
| `secondary_domain` | String | 企业的二级域名。 |

**权限:** 企业令牌/用户令牌

---
## 全局

### `` 个人

**路径:** `个人`

---
### `` 安全

**路径:** `安全`

---
### `` 工时

**路径:** `工时`

---
### `` 组织

**路径:** `组织`

---
### `` 组织

**路径:** `组织`

---
### `` 组织

**路径:** `组织`

---
### `` 组织

**路径:** `组织`

---
### `` 组织

**路径:** `组织`

---
### `` 组织

**路径:** `组织`

---
### `` 通用

**路径:** `通用`

---
## 团队

### `POST` 创建一个团队

**路径:** `/v1/directory/groups`

用于创建一个团队。

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 是 | 团队的名称，在一个企业中这个名称是唯一的。 |
| `visibility` | String | 否 | 团队的可见范围。 |
| `description` | String | 否 | 团队的描述。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 团队的id。 |
| `url` | String | 团队的资源地址。 |
| `name` | String | 团队的名称。 |
| `visibility` | String | 团队的可见性。 |
| `description` | String | 团队的描述。 |

**权限:** 企业令牌/用户令牌

---
### `POST` 向团队中添加一个成员

**路径:** `/v1/directory/groups/{group_id}/members`

用于向团队中添加一个成员。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `group_id` | String | 是 | 团队id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `user_id` | String | 是 | 用户id。 |
| `role` | String | 是 | 团队角色。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 团队成员的id。 |
| `url` | String | 团队成员的资源地址。 |
| `group` | Object | 所属团队的引用结构数据。 |
| `user` | Object | 成员的引用结构数据。 |
| `role` | String | 成员在团队中的角色。 |

**权限:** 企业令牌/用户令牌

---
### `DELETE` 在团队中移除一个成员

**路径:** `/v1/directory/groups/{group_id}/members/{member_id}`

用于在团队中移除一个成员。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `group_id` | String | 是 | 团队id。 |
| `member_id` | String | 是 | 团队成员的id，即用户的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 团队成员的id。 |
| `url` | String | 团队成员的资源地址。 |
| `group` | Object | 所属团队的引用结构数据。 |
| `user` | Object | 成员的引用结构数据。 |
| `role` | String | 成员在团队中的角色。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个团队

**路径:** `/v1/directory/groups/{group_id}`

用于查看一个团队。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `group_id` | String | 是 | 团队的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 团队的id。 |
| `url` | String | 团队的资源地址。 |
| `name` | String | 团队的名称。 |
| `visibility` | String | 团队的可见性。 |
| `description` | String | 团队的描述。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取团队中的一个成员

**路径:** `/v1/directory/groups/{group_id}/members/{member_id}`

用于查询团队中的一个成员。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `group_id` | String | 是 | 团队的id。 |
| `member_id` | String | 是 | 团队成员的id，即用户的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 团队成员的id。 |
| `url` | String | 团队成员的资源地址。 |
| `group` | Object | 所属团队的引用结构数据。 |
| `user` | Object | 成员的引用结构数据。 |
| `role` | String | 成员在团队中的角色。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取团队中的成员列表

**路径:** `/v1/directory/groups/{group_id}/members`

用于查询团队中的成员列表。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `group_id` | String | 是 | 团队id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 团队中的成员全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取团队列表

**路径:** `/v1/directory/groups`

用于查询团队列表。

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 团队全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `PATCH` 部分更新一个团队

**路径:** `/v1/directory/groups/{group_id}`

用于部分更新一个团队。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `group_id` | String | 是 | 团队id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 否 | 团队的名称，在一个企业中这个名称是唯一的。 |
| `visibility` | String | 否 | 团队的可见范围。 |
| `description` | String | 否 | 团队的描述。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 团队的id。 |
| `url` | String | 团队的资源地址。 |
| `name` | String | 团队的名称。 |
| `visibility` | String | 团队的可见性。 |
| `description` | String | 团队的描述。 |

**权限:** 企业令牌/用户令牌

---
## 安全

### `` 日志

**路径:** `日志`

---
### `` 日志

**路径:** `日志`

---
## 日志

### `GET` 获取审计日志列表

**路径:** `/v1/security/audit_logs`

用于查询审计日志列表。

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `operated_between` | String | 是 | 操作时间介于的时间范围，通过','分割起始时间。 |
| `operated_bys` | String | 否 | 操作人的列表，使用','分割，最多只能20个。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 审计日志的全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取登录日志列表

**路径:** `/v1/security/login_logs`

用于查询登录日志列表。

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `logged_between` | String | 是 | 登录时间介于的时间范围，通过','分割起始时间。 |
| `user_ids` | String | 否 | 成员id的列表，使用','分割，最多只能20个。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 登录日志的全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
## 概述

### `` URI结构

**路径:** `URI结构`

PingCode REST API 遵循 REST 规范，采用层级化、标准化的 URI 路径定位业务资源。路径中通过 {参数名} 标记动态路径参数，接口调用时需替换为实际业务数值。 所有接口统一遵循以下通用路径格式： https://{rest_api_root}/v1[/{area}]/{resource}[/{action}] ` 路径参数说明： - rest_api_root：API 根路径   - 公有云环境：open.pingcode.com   - 私有部署环境：{自定义域名}/open   - 其他环境：{在上下文中提供的地址} - area：资源所属子区域（可空） - resource：资源路径 - action：特殊操作（可空） ` 接口路径示例： https://open.pingcode.com/v1/myself https://open.pingcode.com/v1/ship/products https://open.pingcode.com/v1/ship/products/6422711c3f12e6c1e46d40e9/plans https://open.pingcode.com/v1/release/environments https://open.pingcode.com/v1/testhub/cases/bulk ` 另外，在下文中提到的其他路径参数： - oauth2_root：OAuth2 授权页面根路径   - 公有云环境：open.pingcode.com/oauth2   - 私有部署环境：{自定义域名}/oauth2   - 其他环境：{在上下文中提供的地址} `

---
### `` 使用方式

**路径:** `使用方式`

PingCode REST API支持 `OPTIONS`/`GET`/`PUT`/`PATCH`/`POST`/`DELETE`等标准的HTTP请求。 对于`GET`/`DELETE`请求，通过`querystring`传递参数；对于`POST`/`PUT`/`PATCH`请求，需要在`headers`中添加`&quot;content-type&quot;: &quot;application/json&quot;`，然后通过`body`传递参数。 PingCode REST API使用HTTP状态码指示已执行操作的状态； 使用`response body`传递数据。 单个资源 当创建、更新、获取、删除单个资源成功时，会返回当前操作的资源。 HTTP状态码：201 Body： {      "id": "5e05d8448f8461dada9ba29c",      "url": "https://{rest_api_root}/v1/{resource}",      "name": "资源名称",      "desc": "资源简介",      "created_at": 1578897962 } ` 分页数据 当请求多条数据时，默认每一页返回30条，最大返回100条。 通过在`querystring`中设置`page_size`和`page_index`，指定每一页的数据量和第几页的数据（`page_index`为0时，表示第一页）。 在返回的数据结构中，`page_size`表示当前每页的数据量，`page_index`表示当前在第几页，`total`表示资源总数量，`values`表示资源的数组。 HTTP状态码：200 Body： {      "page_size": 30,      "page_index": 0,      "total": 100,      "values": [          {              "id": "5e05d8448f8461dada9ba29c",              "url": "https://{rest_api_root}/v1/{resource}",              "name": "资源名称",              "desc": "资源简介",              "created_at": 1578897962          },          ...      ] } ` 错误 当请求失败时，会返回错误码和错误信息。 HTTP状态码：500 Body： {      "code": "100000",      "message": "Internal Server Error" } `

---
### `` 数据结构

**路径:** `数据结构`

PingCode REST API使用`json`作为通讯格式，所有时间均使用10位数字组成的时间戳。 PingCode REST API为每一种资源定义两种数据结构，全量结构和引用结构。 全量结构包含资源的所有属性，引用结构只包含必要属性。当获取单个资源或分页获取资源列表时，PingCode REST API将返回全量结构； 当获取其他资源引用当前资源时，PingCode REST API将返回引用结构。 全量结构 {      "id": "5e05d8448f8461dada9ba29c",      "url": "https://{rest_api_root}/v1/{resource}",      "name": "资源名称",      "desc": "资源简介",      "created_at": 1578897962 } ` 引用结构 {      "id": "5e05d8448f8461dada9ba29c",      "url": "https://{rest_api_root}/v1/{resource}",      "name": "资源名称" } `

---
### `` 欢迎使用

**路径:** `欢迎使用`

欢迎使用 PingCode Representational State Transfer APIs （简称PingCode REST API）。 PingCode REST API 基于 HTTP 协议实现与 PingCode 服务端的远程数据交互，支持对平台各类资源进行创建、修改、查询、删除等常规业务操作。

---
### `` 频率限制

**路径:** `频率限制`

PingCode REST API限制使用者的请求频率，目的是保障核心服务的可靠且响应迅速。频率限制不用于区分客户和服务级别。 具体策略 根据使用者的身份标识，PingCode REST API最多允许每位使用者每分钟请求200次，单位分钟内超出限制数量的HTTP请求将统一返回错误信息。 HTTP状态码：429 Headers： {      "x-pc-retry-after": 50 } Body： {      "code": "100038",      "message": "请求频率过高" } ` `x-pc-retry-after`指示使用者在重新请求之前必须等待的秒数。如果使用者在到期之前重新发出请求，则请求会再次失败并返回相同的HTTP状态码和`response body`。 合理请求 由于频率限制的存在，最小化请求将十分必要，一个显而易见的策略是缓存不会轻易变更的数据。 另外使用PingCode Flow中的`发送Webhook`和`发送HTTP请求`来将PingCode中发生变更的数据发送给订阅者，也可以有效降低 PingCode REST API的请求数量，从而降低遇到频率限制的风险。

---
## 组织

### `` 企业

**路径:** `企业`

---
### `` 企业成员

**路径:** `企业成员`

---
### `` 团队

**路径:** `团队`

---
### `` 团队成员

**路径:** `团队成员`

---
### `` 职位

**路径:** `职位`

---
### `` 角色

**路径:** `角色`

---
### `` 部门

**路径:** `部门`

---
## 职位

### `GET` 获取一个职位

**路径:** `/v1/directory/jobs/{job_id}`

用于查看一个职位。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `job_id` | String | 是 | 职位的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 职位的id。 |
| `url` | String | 职位的资源地址。 |
| `name` | String | 职位的名称。 |
| `is_system` | Number | 职位是否为系统内置。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取职位列表

**路径:** `/v1/directory/jobs`

用于查询职位列表。

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 职位全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
## 角色

### `GET` 获取一个角色

**路径:** `/v1/directory/roles/{role_id}`

用于查看一个角色。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `role_id` | String | 是 | 角色的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 角色的id。 |
| `url` | String | 角色的资源地址。 |
| `name` | String | 角色的名称。 |
| `is_system` | Number | 角色是否为系统内置。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取角色列表

**路径:** `/v1/directory/roles`

用于查询角色列表。

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 角色全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
## 部门

### `POST` 创建一个部门

**路径:** `/v1/directory/departments`

用于创建一个部门。

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 是 | 部门的名称，在一个企业中这个名称是唯一的。 |
| `parent_id` | String | 否 | 父部门的id。 |
| `head_id` | String | 否 | 部门负责人的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 部门的id。 |
| `url` | String | 部门的资源地址。 |
| `name` | String | 部门的名称。 |
| `head` | Object | 部门的负责人。 |
| `parent` | Object | 父部门。 |

**权限:** 企业令牌/用户令牌

---
### `DELETE` 删除一个部门

**路径:** `/v1/directory/departments/{department_id}`

用于删除一个部门。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `department_id` | String | 是 | 部门的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 部门的id。 |
| `url` | String | 部门的资源地址。 |
| `name` | String | 部门的名称。 |
| `head` | Object | 部门的负责人。 |
| `parent` | Object | 父部门。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个部门

**路径:** `/v1/directory/departments/{department_id}`

用于查看一个部门。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `department_id` | String | 是 | 部门的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 部门的id。 |
| `url` | String | 部门的资源地址。 |
| `name` | String | 部门的名称。 |
| `head` | Object | 部门的负责人。 |
| `parent` | Object | 父部门。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取部门列表

**路径:** `/v1/directory/departments`

用于查询部门列表。

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 部门全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `PATCH` 部分更新一个部门

**路径:** `/v1/directory/departments/{department_id}`

用于部分更新一个部门。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `department_id` | String | 是 | 部门的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 否 | 部门的名称，在一个企业中这个名称是唯一的。 |
| `parent_id` | String | 否 | 父部门的id。 |
| `head_id` | String | 否 | 部门负责人的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 部门的id。 |
| `url` | String | 部门的资源地址。 |
| `name` | String | 部门的名称。 |
| `head` | Object | 部门的负责人。 |
| `parent` | Object | 父部门。 |

**权限:** 企业令牌/用户令牌

---
