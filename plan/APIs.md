# 📅 计划管理 — API 详细文档

> 本文档包含 34 个接口的完整参数说明。
> 来源: https://open.pingcode.com/

---

## 计划

### `PUT` 全量更新一个执行用例

**路径:** `/v1/testhub/runs/{run_id}`

用于全量更新一个执行用例。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `run_id` | String | 是 | 执行用例的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `status_id` | String | 是 | 执行用例执行结果的id。 |
| `remark` | String | 否 | 执行用例执行结果的备注。 |
| `steps` | Object[] | 是 | 执行用例步骤的列表。 |
| `steps.step_id` | String | 是 | 执行用例步骤的id。 |
| `steps.status_id` | String | 是 | 执行用例步骤执行结果的id。 |
| `steps.actual_value` | String | 否 | 执行用例步骤的实际值。 |
| `executor_id` | String | 否 | 执行人的id。不传默认执行人为空。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 执行用例的id。 |
| `url` | String | 执行用例的资源地址。 |
| `status` | String | 执行用例的执行状态。 |
| `short_id` | String | 执行用例的短id。 |
| `html_url` | String | 执行用例的html地址。 |
| `library` | Object | 所属测试库的引用结构数据。 |
| `plan` | Object | 所属测试计划的引用结构数据。 |
| `case` | Object | 关联测试用例的引用结构数据。 |
| `latest_executed_status` | Object | 最近一次执行结果的引用结构数据。 |
| `suite` | Object | 用例所属模块的引用结构数据。 |
| `remark` | String | 执行用例执行结果的备注。 |
| `executor` | Object | 执行人的引用结构数据。 |
| `steps` | Object[] | 执行用例步骤列表。 |
| `created_at` | Number | 创建时间，单位为秒。 |
| `created_by` | Object | 创建人的引用结构数据。 |
| `updated_at` | Number | 更新时间，单位为秒。 |
| `updated_by` | Object | 更新人的引用结构数据。 |
| `is_archived` | Number | 是否已归档。 |
| `is_deleted` | Number | 是否已删除。 |

**权限:** 企业令牌/用户令牌

---
### `POST` 创建一个执行用例

**路径:** `/v1/testhub/runs`

用于创建一个执行用例。

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `library_id` | String | 是 | 测试库的id。 |
| `plan_id` | String | 是 | 测试计划的id。 |
| `case_id` | String | 是 | 测试用例的id。 |
| `executor_id` | String | 否 | 执行人的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 执行用例的id。 |
| `url` | String | 执行用例的资源地址。 |
| `status` | String | 执行用例的执行状态。 |
| `short_id` | String | 执行用例的短id。 |
| `html_url` | String | 执行用例的html地址。 |
| `library` | Object | 所属测试库的引用结构数据。 |
| `plan` | Object | 所属测试计划的引用结构数据。 |
| `case` | Object | 关联测试用例的引用结构数据。 |
| `latest_executed_status` | Object | 最近一次执行结果的引用结构数据。 |
| `suite` | Object | 用例所属模块的引用结构数据。 |
| `remark` | String | 执行用例执行结果的备注。 |
| `executor` | Object | 执行人的引用结构数据。 |
| `steps` | Object[] | 执行用例步骤列表。 |
| `created_at` | Number | 创建时间，单位为秒。 |
| `created_by` | Object | 创建人的引用结构数据。 |
| `updated_at` | Number | 更新时间，单位为秒。 |
| `updated_by` | Object | 更新人的引用结构数据。 |
| `is_archived` | Number | 是否已归档。 |
| `is_deleted` | Number | 是否已删除。 |

**权限:** 企业令牌/用户令牌

---
### `POST` 创建一个计划

**路径:** `/v1/testhub/libraries/{library_id}/plans`

用于创建一个计划。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `library_id` | String | 是 | 测试库的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 是 | 测试计划的名称。名称在一个测试库里唯一。 |
| `type_id` | String | 是 | 测试计划类型的id。 |
| `start_at` | Number | 是 | 测试计划的开始时间。 |
| `end_at` | Number | 是 | 测试计划的结束时间。 |
| `assignee_id` | String | 是 | 测试计划负责人的id。 |
| `project_id` | String | 否 | 项目的id。该字段在 sprint_id 或 version_id 有值时必填。 |
| `sprint_id` | String | 否 | 迭代的id。该字段仅在 type_id 代表迭代测试时有效。 |
| `version_id` | String | 否 | 发布的id。该字段仅在 type_id 代表发布测试时有效。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 计划的id。 |
| `url` | String | 计划的资源地址。 |
| `library` | Object | 计划所属的测试库。 |
| `name` | String | 计划的名称。 |
| `state` | Object | 计划的状态。 |
| `start_at` | Number | 计划的开始时间。 |
| `end_at` | Number | 计划的结束时间。 |
| `short_id` | String | 计划的短id。 |
| `html_url` | String | 计划的html地址。 |
| `type` | Object | 计划关联的类型。 |
| `project` | Object | 计划关联的项目。 |
| `sprint` | Object | 计划关联的迭代。 |
| `version` | Object | 计划关联的发布。 |
| `assignee` | Object | 计划的负责人。 |
| `summary` | String | 计划测试报告的概要。 |
| `created_at` | Number | 计划的创建时间。 |
| `created_by` | Object | 计划的创建人。 |
| `updated_at` | Number | 计划的更新时间。 |
| `updated_by` | Object | 计划的更新人。 |

**权限:** 企业令牌/用户令牌

---
### `POST` 批量创建执行用例

**路径:** `/v1/testhub/runs/bulk`

用于批量创建执行用例。

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `runs` | Object[] | 是 | 创建单个执行用例必要参数的数组。数组长度不超过100。 |
| `runs.library_id` | String | 是 | 执行用例所属测试库的id。 |
| `runs.plan_id` | String | 是 | 执行用例所属测试计划的id。 |
| `runs.case_id` | String | 是 | 测试用例的id。 |
| `runs.executor_id` | String | 否 | 执行人的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `state` | String | 操作状态。 |
| `run` | Object | 执行用例的全量结构数据。操作成功时返回。 |
| `message` | String | 失败原因。操作失败时返回。 |

**权限:** 企业令牌/用户令牌

---
### `POST` 批量操作执行用例

**路径:** `/v1/testhub/libraries/{library_id}/plans/{plan_id}/runs/bulk`

用于批量操作执行用例。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `library_id` | String | 是 | 测试库的id。 |
| `plan_id` | String | 是 | 测试计划的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `inserts` | Object[] | 否 | 需要批量创建的执行用例。该参数是一个对象数组（数组内对象不得超过50个）。 |
| `inserts.case_id` | String | 是 | 测试用例id。 |
| `inserts.executor_id` | String | 否 | 执行人id。 |
| `updates` | Object[] | 否 | 需要批量更新的执行用例。该参数是一个对象数组（数组内对象不得超过50个）。 |
| `updates.run_id` | String | 是 | 执行用例的id。 |
| `updates.status_id` | String | 是 | 执行用例执行结果的id。 |
| `updates.steps` | Object[] | 否 | 执行用例步骤的数组。 |
| `updates.steps.step_id` | String | 是 | 执行用例步骤的id。 |
| `updates.steps.status_id` | String | 是 | 执行用例步骤执行结果的id。 |
| `updates.steps.actual_value` | String | 否 | 执行用例步骤的实际值。 |
| `updates.executor_id` | String | 否 | 执行人的id。 |
| `deletes` | String[] | 否 | 需要批量删除的执行用例。该参数是一个执行用例id的数组（数组内id不得超过50个）。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `inserts` | Number | 成功创建的执行用例数量。 |
| `updates` | Number | 成功更新的执行用例数量。 |
| `deletes` | Number | 成功删除的执行用例数量。 |

**权限:** 企业令牌/用户令牌

---
### `PATCH` 批量部分更新执行用例

**路径:** `/v1/testhub/runs/bulk`

用于批量部分更新执行用例。

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `runs` | Object[] | 是 | 部分更新单个执行用例必要参数的数组。 |
| `runs.run_id` | String | 是 | 执行用例的id。 |
| `runs.status_id` | String | 是 | 执行用例执行结果的id。 |
| `runs.remark` | String | 否 | 执行用例执行结果的备注。 |
| `runs.steps` | Object[] | 否 | 执行用例的步骤列表。 |
| `runs.steps.step_id` | String | 是 | 执行用例步骤的id。 |
| `runs.steps.status_id` | String | 是 | 执行用例步骤执行结果的id。 |
| `runs.steps.actual_value` | String | 否 | 执行用例步骤的实际值。 |
| `runs.executor_id` | String | 否 | 执行人的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `state` | String | 操作状态。 |
| `run` | Object | 执行用例的全量结构数据。操作成功时返回。 |
| `message` | String | 失败原因。操作失败时返回。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个执行用例

**路径:** `/v1/testhub/runs/{run_id}`

用于查看一个执行用例。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `run_id` | String | 是 | 执行用例的id或short_id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 执行用例的id。 |
| `url` | String | 执行用例的资源地址。 |
| `status` | String | 执行用例的执行状态。 |
| `short_id` | String | 执行用例的短id。 |
| `html_url` | String | 执行用例的html地址。 |
| `library` | Object | 所属测试库的引用结构数据。 |
| `plan` | Object | 所属测试计划的引用结构数据。 |
| `case` | Object | 关联测试用例的引用结构数据。 |
| `latest_executed_status` | Object | 最近一次执行结果的引用结构数据。 |
| `suite` | Object | 用例所属模块的引用结构数据。 |
| `remark` | String | 执行用例执行结果的备注。 |
| `executor` | Object | 执行人的引用结构数据。 |
| `steps` | Object[] | 执行用例步骤列表。 |
| `created_at` | Number | 创建时间，单位为秒。 |
| `created_by` | Object | 创建人的引用结构数据。 |
| `updated_at` | Number | 更新时间，单位为秒。 |
| `updated_by` | Object | 更新人的引用结构数据。 |
| `is_archived` | Number | 是否已归档。 |
| `is_deleted` | Number | 是否已删除。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个计划

**路径:** `/v1/testhub/libraries/{library_id}/plans/{plan_id}`

用于查看一个计划。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `library_id` | String | 是 | 测试库的id。 |
| `plan_id` | String | 是 | 测试计划的id或short_id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 计划的id。 |
| `url` | String | 计划的资源地址。 |
| `library` | Object | 计划所属的测试库。 |
| `name` | String | 计划的名称。 |
| `state` | Object | 计划的状态。 |
| `start_at` | Number | 计划的开始时间。 |
| `end_at` | Number | 计划的结束时间。 |
| `short_id` | String | 计划的短id。 |
| `html_url` | String | 计划的html地址。 |
| `type` | Object | 计划关联的类型。包括项目、发布和迭代。 |
| `project` | Object | 计划关联的项目。 |
| `sprint` | Object | 计划关联的迭代。 |
| `version` | Object | 计划关联的发布。 |
| `assignee` | Object | 计划的负责人。 |
| `summary` | String | 计划测试报告的概要。 |
| `created_at` | Number | 计划的创建时间。 |
| `created_by` | Object | 计划的创建人。 |
| `updated_at` | Number | 计划的更新时间。 |
| `updated_by` | Object | 计划的更新人。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个计划类型

**路径:** `/v1/testhub/libraries/{library_id}/plan_types/{plan_type_id}`

用于查看一个计划类型。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `library_id` | String | 是 | 测试库的id。 |
| `plan_type_id` | String | 是 | 计划类型的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 计划类型的id。 |
| `url` | String | 计划类型的资源地址。 |
| `library` | Object | 所属测试库的引用结构数据。 |
| `name` | String | 计划类型的名称。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一条执行用例的结果记录

**路径:** `/v1/testhub/runs/{run_id}/histories/{history_id}`

用于查看一条执行用例结果记录。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `run_id` | String | 是 | 执行用例的id。 |
| `history_id` | String | 是 | 执行用例结果记录的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 执行用例结果记录的id。 |
| `url` | String | 执行用例结果记录的资源地址。 |
| `run` | Object | 执行用例的引用结构数据。 |
| `library` | Object | 所属测试库的引用结构数据。 |
| `plan` | Object | 所属测试计划的引用结构数据。 |
| `case` | Object | 关联测试用例的引用结构数据。 |
| `executed_status` | Object | 执行结果的引用结构数据。 |
| `remark` | String | 执行用例执行结果的备注。 |
| `executed_at` | Number | 执行时间，单位为秒。 |
| `executed_by` | Object | 执行人的引用结构数据。 |
| `steps` | Object[] | 执行用例步骤列表。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取执行用例列表

**路径:** `/v1/testhub/runs`

用于查询执行用例列表。

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `plan_id` | String | 否 | 测试计划的id。 |
| `case_id` | String | 否 | 测试用例的id。 |
| `suite_id` | String | 否 | 测试模块的id。 |
| `status_id` | String | 否 | 执行用例执行结果的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 执行用例全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取执行用例执行结果列表

**路径:** `/v1/testhub/run/statuses?library_id={library_id}`

用于查询执行用例执行结果列表。

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
| `values` | Object[] | 执行用例执行结果全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取执行用例的结果记录列表

**路径:** `/v1/testhub/runs/{run_id}/histories`

用于查询执行用例的结果记录。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `run_id` | String | 是 | 执行用例的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 执行用例结果记录全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取计划列表

**路径:** `/v1/testhub/libraries/{library_id}/plans`

用于查询计划列表。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `library_id` | String | 是 | 测试库的id。 |

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 否 | 测试计划名称。 |
| `created_between` | String | 否 | 创建时间介于的时间范围，通过','分割起始时间。 |
| `updated_between` | String | 否 | 更新时间介于的时间范围，通过','分割起始时间。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 计划全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取计划类型列表

**路径:** `/v1/testhub/libraries/{library_id}/plan_types`

用于查询计划类型列表。

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
| `values` | Object[] | 计划类型全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `PATCH` 部分更新一个执行用例

**路径:** `/v1/testhub/runs/{run_id}`

用于部分更新一个执行用例。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `run_id` | String | 是 | 执行用例的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `status_id` | String | 是 | 执行用例执行结果的id。 |
| `remark` | String | 否 | 执行用例执行结果的备注。 |
| `steps` | Object[] | 否 | 执行用例步骤的列表。steps是整体更新的。 |
| `steps.step_id` | String | 是 | 执行用例步骤的id。 |
| `steps.status_id` | String | 是 | 执行用例步骤执行结果的id。 |
| `steps.actual_value` | String | 否 | 执行用例步骤的实际值。 |
| `executor_id` | String | 否 | 执行人的id。不传默认执行人为执行用例的创建人。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 执行用例的id。 |
| `url` | String | 执行用例的资源地址。 |
| `status` | String | 执行用例的执行状态。 |
| `short_id` | String | 执行用例的短id。 |
| `html_url` | String | 执行用例的html地址。 |
| `library` | Object | 所属测试库的引用结构数据。 |
| `plan` | Object | 所属测试计划的引用结构数据。 |
| `case` | Object | 关联测试用例的引用结构数据。 |
| `latest_executed_status` | Object | 最近一次执行结果的引用结构数据。 |
| `suite` | Object | 用例所属模块的引用结构数据。 |
| `remark` | String | 执行用例执行结果的备注。 |
| `executor` | Object | 执行人的引用结构数据。 |
| `steps` | Object[] | 执行用例步骤列表。 |
| `created_at` | Number | 创建时间，单位为秒。 |
| `created_by` | Object | 创建人的引用结构数据。 |
| `updated_at` | Number | 更新时间，单位为秒。 |
| `updated_by` | Object | 更新人的引用结构数据。 |
| `is_archived` | Number | 是否已归档。 |
| `is_deleted` | Number | 是否已删除。 |

**权限:** 企业令牌/用户令牌

---
### `PATCH` 部分更新一个计划

**路径:** `/v1/testhub/libraries/{library_id}/plans/{plan_id}`

用于部分更新一个计划。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `library_id` | String | 是 | 测试库的id。 |
| `plan_id` | String | 是 | 测试计划的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 否 | 测试计划的名称。名称在一个测试库里唯一。 |
| `type_id` | String | 否 | 测试计划类型的id。指定测试计划类型时，建议同时指定对应的 sprint_id 或 version_id。 |
| `project_id` | String | 否 | 项目的id。 |
| `sprint_id` | String | 否 | 迭代的id。该字段仅在测试计划类型为迭代测试时有效。 |
| `version_id` | String | 否 | 发布的id。该字段仅在测试计划类型为发布测试时有效。 |
| `start_at` | Number | 否 | 测试计划的开始时间。 |
| `end_at` | Number | 否 | 测试计划的结束时间。 |
| `assignee_id` | String | 否 | 测试计划负责人的id。 |
| `state_id` | String | 否 | 测试计划状态的id。 |
| `summary` | String | 否 | 测试报告的概要信息。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 计划的id。 |
| `url` | String | 计划的资源地址。 |
| `library` | Object | 计划所属的测试库。 |
| `name` | String | 计划的名称。 |
| `state` | Object | 计划的状态。 |
| `start_at` | Number | 计划的开始时间。 |
| `end_at` | Number | 计划的结束时间。 |
| `short_id` | String | 计划的短id。 |
| `html_url` | String | 计划的html地址。 |
| `type` | Object | 计划关联的类型。 |
| `project` | Object | 计划关联的项目。 |
| `sprint` | Object | 计划关联的迭代。 |
| `version` | Object | 计划关联的发布。 |
| `assignee` | Object | 计划的负责人。 |
| `summary` | String | 计划测试报告的概要。 |
| `created_at` | Number | 计划的创建时间。 |
| `created_by` | Object | 计划的创建人。 |
| `updated_at` | Number | 计划的更新时间。 |
| `updated_by` | Object | 计划的更新人。 |

**权限:** 企业令牌/用户令牌

---
## 计划配置

### `GET` 获取一个计划状态

**路径:** `/v1/testhub/plan_states/{state_id}`

用于查看一个计划状态。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `state_id` | String | 是 | 计划状态的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 计划状态的id。 |
| `url` | String | 计划状态的资源地址。 |
| `name` | String | 计划状态的名称。 |
| `type` | String | 计划状态的类型。 |
| `is_system` | Number | 是否为系统内置状态。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取全部计划状态列表

**路径:** `/v1/testhub/plan_states`

用于查询全部计划状态列表。

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_index` | Number | 页码，从0开始。 |
| `page_size` | Number | 每页条数。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 全部计划状态全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
## 迭代

### `POST` 创建一个迭代

**路径:** `/v1/pjm/projects/{project_id}/sprints`

用于创建一个迭代。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 是 | 项目的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 是 | 迭代的名称。 |
| `start_at` | Number | 是 | 迭代开始的时间。 |
| `end_at` | Number | 是 | 迭代结束的时间。 |
| `assignee_id` | String | 是 | 迭代负责人的id。 |
| `description` | String | 否 | 迭代的描述。 |
| `status` | String | 否 | 迭代的状态。 |
| `category_ids` | String[] | 否 | 迭代类别的id数组。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 迭代的id。 |
| `url` | String | 迭代的地址。 |
| `project` | Object | 迭代所属项目的引用结构数据。 |
| `name` | String | 迭代的名称。 |
| `status` | String | 迭代的状态。 |
| `assignee` | Object | 迭代负责人的引用结构数据。 |
| `start_at` | Number | 迭代的计划开始时间。 |
| `end_at` | Number | 迭代的计划结束时间。 |
| `description` | String | 迭代的描述。 |
| `started_at` | Number | 迭代的实际开始时间。 |
| `completed_at` | Number | 迭代的实际完成时间。 |
| `total_story_points` | Number | 迭代的总故事点。 |
| `started_story_points` | Number | 迭代已开始的故事点。 |
| `completed_story_points` | Number | 迭代已完成的故事点。 |
| `categories` | Object[] | 迭代关联的类别列表。 |
| `created_at` | Number | 迭代的创建时间。 |
| `created_by` | Object | 迭代创建人的引用结构数据。 |
| `updated_at` | Number | 迭代的更新时间。 |
| `updated_by` | Object | 迭代更新人的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `POST` 创建一个迭代分组

**路径:** `/v1/pjm/projects/{project_id}/sprint_sections`

用于创建一个迭代分组。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 是 | 项目的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 是 | 迭代分组的名称。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 迭代分组的id。 |
| `url` | String | 迭代分组的地址。 |
| `project` | Object | 所属项目的引用结构数据。 |
| `name` | String | 迭代分组的名称。 |

**权限:** 企业令牌/用户令牌

---
### `POST` 创建一个迭代类别

**路径:** `/v1/pjm/projects/{project_id}/sprint_categories`

用于创建一个迭代类别。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 是 | 项目的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 是 | 迭代类别的名称。 |
| `section_id` | String | 否 | 迭代类别所属迭代分组id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 迭代类别的id。 |
| `url` | String | 迭代类别的地址。 |
| `project` | Object | 所属项目的引用结构数据。 |
| `name` | String | 迭代类别的名称。 |
| `section` | Object | 所属迭代分组的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `DELETE` 删除一个迭代分组

**路径:** `/v1/pjm/projects/{project_id}/sprint_sections/{section_id}`

用于删除一个迭代分组。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 是 | 项目的id。 |
| `section_id` | String | 是 | 迭代分组的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 迭代分组的id。 |
| `url` | String | 迭代分组的地址。 |
| `project` | Object | 所属项目的引用结构数据。 |
| `name` | String | 迭代分组的名称。 |

**权限:** 企业令牌/用户令牌

---
### `DELETE` 删除一个迭代类别

**路径:** `/v1/pjm/projects/{project_id}/sprint_categories/{sprint_category_id}`

用于删除一个迭代类别。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 是 | 项目的id。 |
| `sprint_category_id` | String | 是 | 迭代类别的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 迭代类别的id。 |
| `url` | String | 迭代类别的地址。 |
| `project` | Object | 所属项目的引用结构数据。 |
| `name` | String | 迭代类别的名称。 |
| `section` | Object | 所属迭代分组的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `POST` 批量创建迭代

**路径:** `/v1/pjm/sprints/bulk`

用于批量创建迭代。

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `sprints` | Object[] | 是 | 需要批量创建的迭代。该参数是一个对象数组（数组内对象不得超过100个）。 |
| `sprints.project_id` | String | 是 | 迭代所属项目的id。 |
| `sprints.name` | String | 是 | 迭代的名称。 |
| `sprints.start_at` | Number | 是 | 迭代开始的时间。 |
| `sprints.end_at` | Number | 是 | 迭代结束的时间。 |
| `sprints.assignee_id` | String | 是 | 迭代负责人的id。 |
| `sprints.description` | String | 否 | 迭代的描述。 |
| `sprints.status` | String | 否 | 迭代的状态。 |
| `sprints.category_ids` | String[] | 否 | 迭代类别的id列表。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `state` | String | 批量创建结果的状态。 |
| `sprint` | Object | 迭代的全量结构数据。创建成功时返回。 |

**权限:** 企业令牌

---
### `GET` 获取一个迭代

**路径:** `/v1/pjm/projects/{project_id}/sprints/{sprint_id}`

用于查看一个迭代。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 是 | 项目的id。 |
| `sprint_id` | String | 是 | 迭代的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 迭代的id。 |
| `url` | String | 迭代的地址。 |
| `project` | Object | 迭代所属项目的引用结构数据。 |
| `name` | String | 迭代的名称。 |
| `status` | String | 迭代的状态。 |
| `assignee` | Object | 迭代负责人的引用结构数据。 |
| `start_at` | Number | 迭代的计划开始时间。 |
| `end_at` | Number | 迭代的计划结束时间。 |
| `description` | String | 迭代的描述。 |
| `started_at` | Number | 迭代的实际开始时间。 |
| `completed_at` | Number | 迭代的实际完成时间。 |
| `total_story_points` | Number | 迭代的总故事点。 |
| `started_story_points` | Number | 迭代已开始的故事点。 |
| `completed_story_points` | Number | 迭代已完成的故事点。 |
| `categories` | Object[] | 迭代关联的类别列表。 |
| `created_at` | Number | 迭代的创建时间。 |
| `created_by` | Object | 迭代的创建人。 |
| `updated_at` | Number | 迭代的更新时间。 |
| `updated_by` | Object | 迭代的更新人。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个迭代分组

**路径:** `/v1/pjm/projects/{project_id}/sprint_sections/{section_id}`

用于查看一个迭代分组。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 是 | 项目的id。 |
| `section_id` | String | 是 | 迭代分组的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 迭代分组的id。 |
| `url` | String | 迭代分组的地址。 |
| `project` | Object | 所属项目的引用结构数据。 |
| `name` | String | 迭代分组的名称。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个迭代类别

**路径:** `/v1/pjm/projects/{project_id}/sprint_categories/{sprint_category_id}`

用于查看一个迭代类别。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 是 | 项目的id。 |
| `sprint_category_id` | String | 是 | 迭代类别的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 迭代类别的id。 |
| `url` | String | 迭代类别的地址。 |
| `project` | Object | 所属项目的引用结构数据。 |
| `name` | String | 迭代类别的名称。 |
| `section` | Object | 所属迭代分组的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取迭代分组列表

**路径:** `/v1/pjm/projects/{project_id}/sprint_sections`

用于查询迭代分组列表。

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
| `values` | Object[] | 迭代分组全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取迭代列表

**路径:** `/v1/pjm/projects/{project_id}/sprints`

用于查询迭代列表。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 是 | 项目的id。 |

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 否 | 迭代的名称。 |
| `status` | String | 否 | 迭代的状态。 |
| `created_between` | String | 否 | 创建时间介于的时间范围，通过','分割起始时间。 |
| `updated_between` | String | 否 | 更新时间介于的时间范围，通过','分割起始时间。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 迭代全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取迭代类别列表

**路径:** `/v1/pjm/projects/{project_id}/sprint_categories`

用于查询迭代类别列表。

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
| `values` | Object[] | 迭代类别的全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `PATCH` 部分更新一个迭代

**路径:** `/v1/pjm/projects/{project_id}/sprints/{sprint_id}`

用于部分更新一个迭代。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 是 | 项目的id。 |
| `sprint_id` | String | 是 | 迭代的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 否 | 迭代的名称。 |
| `start_at` | Number | 否 | 迭代开始的时间。 |
| `end_at` | Number | 否 | 迭代结束的时间。 |
| `assignee_id` | String | 否 | 迭代负责人的id。 |
| `description` | String | 否 | 迭代的描述。 |
| `status` | String | 否 | 迭代的状态。 |
| `category_ids` | String[] | 否 | 迭代类别的id列表。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 迭代的id。 |
| `url` | String | 迭代的地址。 |
| `project` | Object | 迭代所属项目的引用结构数据。 |
| `name` | String | 迭代的名称。 |
| `status` | String | 迭代的状态。 |
| `assignee` | Object | 迭代负责人的引用结构数据。 |
| `start_at` | Number | 迭代的计划开始时间。 |
| `end_at` | Number | 迭代的计划结束时间。 |
| `description` | String | 迭代的描述。 |
| `started_at` | Number | 迭代的实际开始时间。 |
| `completed_at` | Number | 迭代的实际完成时间。 |
| `total_story_points` | Number | 迭代的总故事点。 |
| `started_story_points` | Number | 迭代已开始的故事点。 |
| `completed_story_points` | Number | 迭代已完成的故事点。 |
| `categories` | Object[] | 迭代关联的类别列表。 |
| `created_at` | Number | 迭代的创建时间。 |
| `created_by` | Object | 迭代创建人的引用结构数据。 |
| `updated_at` | Number | 迭代的更新时间。 |
| `updated_by` | Object | 迭代更新人的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `PATCH` 部分更新一个迭代分组

**路径:** `/v1/pjm/projects/{project_id}/sprint_sections/{section_id}`

用于部分更新一个迭代分组。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 是 | 项目的id。 |
| `section_id` | String | 是 | 迭代分组的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 是 | 迭代分组的名称。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 迭代分组的id。 |
| `url` | String | 迭代分组的地址。 |
| `project` | Object | 所属项目的引用结构数据。 |
| `name` | String | 迭代分组的名称。 |

**权限:** 企业令牌/用户令牌

---
### `PATCH` 部分更新一个迭代类别

**路径:** `/v1/pjm/projects/{project_id}/sprint_categories/{sprint_category_id}`

用于部分更新一个迭代类别。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 是 | 项目的id。 |
| `sprint_category_id` | String | 是 | 迭代类别的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 否 | 迭代类别的名称。 |
| `section_id` | String | 否 | 迭代类别所属迭代分组id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 迭代类别的id。 |
| `url` | String | 迭代类别的地址。 |
| `project` | Object | 所属项目的引用结构数据。 |
| `name` | String | 迭代类别的名称。 |
| `section` | Object | 所属迭代分组的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
