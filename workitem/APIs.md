# 📋 工作项 — API 详细文档

> 本文档包含 94 个接口的完整参数说明。
> 来源: https://open.pingcode.com/

---

## 关注人

### `POST` 添加一个关注人

**路径:** `/v1/participants`

用于添加一个关注人。

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `principal_type` | String | 是 | 关注人主体的类型。 在 `principal_type` 为 `work_item` 时，要求 `scopes` 包括 `pcp:write:pjm:workitem`;  在 `principal_type` 为 `test_case` 时，要求 `scopes` 包括 `pcp:write:testhub:testcase`;  在 `principal_type` 为 `idea` 时，要求 `scopes` 包括 `pcp:write:ship:idea`;  在 `principal_type` 为 `ticket` 时，要求 `scopes` 包括 `pcp:write:ship:ticket`;  在 `principal_type` 为 `page` 时，要求 `scopes` 包括 `pcp:write:wiki:page`; |
| `principal_id` | String | 否 | 关注人主体的id。 |
| `review_id` | String | 否 | 关注人评审主体的id。`principal_id`和`review_id`至少存在一个，若同时存在，则忽略`review_id`。 |
| `type` | String | 是 | 关注人的类型。 |
| `participant_id` | String | 是 | 关注人的id。用户的id或者团队的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 关注人的id。 |
| `url` | String | 关注人的资源地址。 |
| `type` | String | 关注人的类型。 |
| `user` | Object | 关注的用户。当 `type` 为 `user` 时返回。 |
| `user_group` | Object | 关注的团队。当 `type` 为 `user_group` 时返回。 |

**权限:** 企业令牌/用户令牌

---
### `DELETE` 移除一个关注人

**路径:** `/v1/participants/{participant_id}?principal_type={principal_type}&principal_id={principal_id}`

用于移除一个关注人。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `participant_id` | String | 是 | 关注人的id。用户的id或者团队的id。 |

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `principal_type` | String | 是 | 关注人主体的类型。 在 `principal_type` 为 `work_item` 时，要求 `scopes` 包括 `pcp:write:pjm:workitem`;  在 `principal_type` 为 `test_case` 时，要求 `scopes` 包括 `pcp:write:testhub:testcase`;  在 `principal_type` 为 `idea` 时，要求 `scopes` 包括 `pcp:write:ship:idea`;  在 `principal_type` 为 `ticket` 时，要求 `scopes` 包括 `pcp:write:ship:ticket`;  在 `principal_type` 为 `page` 时，要求 `scopes` 包括 `pcp:write:wiki:page`; |
| `principal_id` | String | 否 | 关注人主体的id。 |
| `review_id` | String | 否 | 注人评审主体的id。`principal_id`和`review_id`至少存在一个，若同时存在，则忽略`review_id`。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 关注人的id。 |
| `url` | String | 关注人的资源地址。 |
| `type` | String | 关注人的类型。 |
| `user` | Object | 关注的用户。当 `type` 为 `user` 时返回。 |
| `user_group` | Object | 关注的团队。当 `type` 为 `user_group` 时返回。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个关注人

**路径:** `/v1/participants/{participant_id}`

用于查看一个关注人。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `participant_id` | String | 是 | 关注人的id。 |

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `principal_type` | String | 是 | 关注人主体的类型。 在 `principal_type` 为 `work_item` 时，要求 `scopes` 包括 `pcp:read:pjm:workitem`;  在 `principal_type` 为 `test_case` 时，要求 `scopes` 包括 `pcp:read:testhub:testcase`;  在 `principal_type` 为 `idea` 时，要求 `scopes` 包括 `pcp:read:ship:idea`;  在 `principal_type` 为 `ticket` 时，要求 `scopes` 包括 `pcp:read:ship:ticket`;  在 `principal_type` 为 `page` 时，要求 `scopes` 包括 `pcp:read:wiki:page`; |
| `principal_id` | String | 否 | 关注人主体的id。 |
| `review_id` | String | 否 | 关注人评审主体的id。`principal_id`和`review_id`至少存在一个，若同时存在，则忽略`review_id`。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 关注人的id。 |
| `url` | String | 关注人的资源地址。 |
| `type` | String | 关注人的类型。 |
| `user` | Object | 关注的用户。当`type`为`user`时，该字段返回。 |
| `user_group` | Object | 关注的团队。当`type`为`user_group`时，该字段返回。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取关注人列表

**路径:** `/v1/participants?principal_type={principal_type}&principal_id={principal_id}`

用于查询关注人列表。

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `principal_type` | String | 是 | 关注人主体的类型。 在 `principal_type` 为 `work_item` 时，要求 `scopes` 包括 `pcp:read:pjm:workitem`;  在 `principal_type` 为 `test_case` 时，要求 `scopes` 包括 `pcp:read:testhub:testcase`;  在 `principal_type` 为 `idea` 时，要求 `scopes` 包括 `pcp:read:ship:idea`;  在 `principal_type` 为 `ticket` 时，要求 `scopes` 包括 `pcp:read:ship:ticket`;  在 `principal_type` 为 `page` 时，要求 `scopes` 包括 `pcp:read:wiki:page`; |
| `principal_id` | String | 否 | 关注人主体的id。 |
| `review_id` | String | 否 | 关注人评审主体的id。`principal_id`和`review_id`至少存在一个，若同时存在，则忽略`review_id`。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 关注人全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
## 关联

### `POST` 创建一个关联

**路径:** `/v1/relations`

用于创建一个关联。

**参数 (请求参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `principal_type` | String | 是 | 关联主体的类型。关联主体的类型和关联的目标类型需要搭配使用，比如： `需求关联工单`，principal_type为`idea`，target_type为`ticket`，要求 `scopes` 包括 `pcp:write:ship:idea`、`pcp:write:ship:ticket`； `需求关联工作项`，principal_type为`idea`，target_type为`work_item`，要求 `scopes` 包括 `pcp:write:ship:idea`、`pcp:write:pjm:workitem`； `需求关联测试用例`，principal_type为`idea`，target_type为`test_case`，要求 `scopes` 包括 `pcp:write:ship:idea`、`pcp:write:testhub:testcase`； `需求关联需求`，principal_type为`idea`，target_type为`idea`，要求 `scopes` 包括 `pcp:write:ship:idea`； `需求关联页面`，principal_type为`idea`，target_type为`page`，要求 `scopes` 包括 `pcp:write:ship:idea`、`pcp:write:wiki:page`； `工单关联需求`，principal_type为`ticket`，target_type为`idea`，要求 `scopes` 包括 `pcp:write:ship:ticket`、`pcp:write:ship:idea`； `工单关联工作项`，principal_type为`ticket`，target_type为`work_item`，要求 `scopes` 包括 `pcp:write:ship:ticket`、`pcp:write:pjm:workitem`； `工单关联工单`，principal_type为`ticket`，target_type为`ticket`，要求 `scopes` 包括 `pcp:write:ship:ticket`； `工单关联页面`，principal_type为`ticket`，target_type为`page`，要求 `scopes` 包括 `pcp:write:ship:ticket`、`pcp:write:wiki:page`； `工作项关联测试用例`，principal_type为`work_item`，target_type为`test_case`，要求 `scopes` 包括 `pcp:write:pjm:workitem`、`pcp:write:testhub:testcase`； `工作项关联需求`，principal_type为`work_item`，target_type为`idea`，要求 `scopes` 包括 `pcp:write:pjm:workitem`、`pcp:write:ship:idea`； `工作项关联工单`，principal_type为`work_item`，target_type为`ticket`，要求 `scopes` 包括 `pcp:write:pjm:workitem`、`pcp:write:ship:ticket`； `工作项关联页面`，principal_type为`work_item`，target_type为`page`，要求 `scopes` 包括 `pcp:write:pjm:workitem`、`pcp:write:wiki:page`； `测试计划关联缺陷`，principal_type为`test_plan`，target_type为`work_item`，要求 `scopes` 包括 `pcp:write:testhub:testplan`、`pcp:write:pjm:workitem`； `执行用例关联缺陷`，principal_type为`test_run`，target_type为`work_item`，要求 `scopes` 包括 `pcp:write:testhub:testplan`、`pcp:write:pjm:workitem`； `测试用例关联需求`，principal_type为`test_case`，target_type为`idea`，要求 `scopes` 包括 `pcp:write:testhub:testcase`、`pcp:write:ship:idea`； `测试用例关联工作项`，principal_type为`test_case`，target_type为`work_item`，要求 `scopes` 包括 `pcp:write:testhub:testcase`、`pcp:write:pjm:workitem`； `测试用例关联页面`，principal_type为`test_case`，target_type为`page`，要求 `scopes` 包括 `pcp:write:testhub:testcase`、`pcp:write:wiki:page`； `页面关联需求`，暂不开放； `页面关联工单`，暂不开放； `页面关联工作项`，暂不开放； `页面关联测试用例`，暂不开放； |
| `principal_id` | String | 是 | 关联主体的id。 |
| `target_type` | String | 是 | 关联的目标类型。 |
| `target_id` | String | 是 | 关联的目标id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 关联的id。 |
| `url` | String | 关联的资源地址。 |
| `principal_type` | String | 关联主体的类型。 |
| `principal` | Object | 关联的主体。 |
| `target_type` | String | 关联的目标类型。 |
| `target` | Object | 关联的目标。 |

**权限:** 企业令牌/用户令牌

---
### `DELETE` 删除一个关联

**路径:** `/v1/relations/{relation_id}`

用于删除一个关联。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `relation_id` | String | 是 | 关联的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 关联的id。 |
| `url` | String | 关联的资源地址。 |
| `principal_type` | String | 关联主体的类型。 |
| `principal` | Object | 关联的主体。 |
| `target_type` | String | 关联的目标类型。 |
| `target` | Object | 关联的目标。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个关联

**路径:** `/v1/relations/{relation_id}`

用于查看一个关联。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `relation_id` | String | 是 | 关联的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 关联的id。 |
| `url` | String | 关联的资源地址。 |
| `principal_type` | String | 关联主体的类型。 |
| `principal` | Object | 关联的主体。 |
| `target_type` | String | 关联的目标类型。 |
| `target` | Object | 关联的目标。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取关联列表

**路径:** `/v1/relations?principal_type={principal_type}&principal_id={principal_id}&target_type={target_type}`

用于查询关联列表。

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `principal_type` | String | 是 | 关联主体的类型。关联主体的类型和关联的目标类型需要搭配使用，比如： `需求关联工单`，principal_type为`idea`，target_type为`ticket`，要求 `scopes` 包括 `pcp:read:ship:idea`、`pcp:read:ship:ticket`； `需求关联工作项`，principal_type为`idea`，target_type为`work_item`，要求 `scopes` 包括 `pcp:read:ship:idea`、`pcp:read:pjm:workitem`； `需求关联测试用例`，principal_type为`idea`，target_type为`test_case`，要求 `scopes` 包括 `pcp:read:ship:idea`、`pcp:read:testhub:testcase`； `需求关联需求`，principal_type为`idea`，target_type为`idea`，要求 `scopes` 包括 `pcp:read:ship:idea`； `需求关联页面`，principal_type为`idea`，target_type为`page`，要求 `scopes` 包括 `pcp:read:ship:idea`、`pcp:read:wiki:page`； `工单关联需求`，principal_type为`ticket`，target_type为`idea`，要求 `scopes` 包括 `pcp:read:ship:ticket`、`pcp:read:ship:idea`； `工单关联工作项`，principal_type为`ticket`，target_type为`work_item`，要求 `scopes` 包括 `pcp:read:ship:ticket`、`pcp:read:pjm:workitem`； `工单关联工单`，principal_type为`ticket`，target_type为`ticket`，要求 `scopes` 包括 `pcp:read:ship:ticket`； `工单关联页面`，principal_type为`ticket`，target_type为`page`，要求 `scopes` 包括 `pcp:read:ship:ticket`、`pcp:read:wiki:page`； `工作项关联测试用例`，principal_type为`work_item`，target_type为`test_case`，要求 `scopes` 包括 `pcp:read:pjm:workitem`、`pcp:read:testhub:testcase`； `工作项关联需求`，principal_type为`work_item`，target_type为`idea`，要求 `scopes` 包括 `pcp:read:pjm:workitem`、`pcp:read:ship:idea`； `工作项关联工单`，principal_type为`work_item`，target_type为`ticket`，要求 `scopes` 包括 `pcp:read:pjm:workitem`、`pcp:read:ship:ticket`； `工作项关联页面`，principal_type为`work_item`，target_type为`page`，要求 `scopes` 包括 `pcp:read:pjm:workitem`、`pcp:read:wiki:page`； `测试计划关联缺陷`，principal_type为`test_plan`，target_type为`work_item`，要求 `scopes` 包括 `pcp:read:testhub:testplan`、`pcp:read:pjm:workitem`； `执行用例关联缺陷`，principal_type为`test_run`，target_type为`work_item`，要求 `scopes` 包括 `pcp:read:testhub:testplan`、`pcp:read:pjm:workitem`； `测试用例关联需求`，principal_type为`test_case`，target_type为`idea`，要求 `scopes` 包括 `pcp:read:testhub:testcase`、`pcp:read:ship:idea`； `测试用例关联工作项`，principal_type为`test_case`，target_type为`work_item`，要求 `scopes` 包括 `pcp:read:testhub:testcase`、`pcp:read:pjm:workitem`； `测试用例关联页面`，principal_type为`test_case`，target_type为`page`，要求 `scopes` 包括 `pcp:read:testhub:testcase`、`pcp:read:wiki:page`； `页面关联需求`，principal_type为`page`，target_type为`idea`，要求 `scopes` 包括 `pcp:read:wiki:page`、`pcp:read:ship:idea`； `页面关联工单`，principal_type为`page`，target_type为`ticket`，要求 `scopes` 包括 `pcp:read:wiki:page`、`pcp:read:ship:ticket`； `页面关联工作项`，principal_type为`page`，target_type为`work_item`，要求 `scopes` 包括 `pcp:read:wiki:page`、`pcp:read:pjm:workitem`； `页面关联测试用例`，principal_type为`page`，target_type为`test_case`，要求 `scopes` 包括 `pcp:read:wiki:page`、`pcp:read:testhub:testcase`； |
| `principal_id` | String | 是 | 关联主体的id。 |
| `target_type` | String | 是 | 关联的目标类型。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 关联全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
## 工作项

### `POST` 关联一个工作项

**路径:** `/v1/pjm/work_items/{work_item_id}/relations`

用于关联一个工作项。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `work_item_id` | String | 是 | 工作项的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `target_work_item_id` | String | 是 | 目标工作项的id。 |
| `relation_type` | String | 是 | 关联的类型。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工作项关联的id。 |
| `url` | String | 工作项关联的地址。 |
| `relation_type` | String | 关联的类型。 |
| `origin_work_item` | Object | 源工作项的引用结构数据。 |
| `target_work_item` | Object | 目标工作项的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `POST` 创建一个工作项

**路径:** `/v1/pjm/work_items`

用于创建一个工作项。

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 是 | 项目的id。 |
| `type_id` | String | 是 | 工作项类型的id。工作项类型分为9种系统类型和一些自定义类型。系统类型包括：史诗、特性、用户故事、阶段、里程碑、需求、任务、缺陷和事务。可以通过`获取全部工作项类型列表`获得。 |
| `title` | String | 是 | 工作项的标题。 |
| `description` | String | 否 | 工作项的描述。 |
| `start_at` | Number | 否 | 工作项的开始时间。当工作项类型为里程碑时，该参数无效。 |
| `end_at` | Number | 否 | 工作项的截止时间。 |
| `priority_id` | String | 否 | 工作项优先级的id。 |
| `state_id` | String | 否 | 工作项状态的id。工作项状态的id在设置时必须同时满足工作项类型的工作项状态方案和工作项状态流转的状态值才能成功完成设置。工作项状态方案可以通过`获取工作项状态方案列表`获取。工作项状态流转则可以通过`获取状态方案中的工作项状态流转列表`获取。 |
| `assignee_id` | String | 否 | 工作项负责人的id。 |
| `parent_id` | String | 否 | 工作项的父工作项的id。当前工作项类型支持的父工作类型包含`parent_id`对应的工作项类型时，该参数有效。具体配置见属性与视图子工作项配置。 |
| `sprint_id` | String | 否 | 所属迭代id。该字段只有项目类型为`scrum`和`hybrid`时有效。 |
| `version_ids` | String[] | 否 | 所属发布的id列表。 |
| `board_id` | String | 否 | 看板的id。该字段只有项目类型为`kanban`和`hybrid`时有效。 |
| `entry_id` | String | 否 | 看板栏的id。该字段只有项目类型为`kanban`和`hybrid`时有效。 |
| `swimlane_id` | String | 否 | 泳道的id。该字段只有项目类型为`kanban`和`hybrid`时有效。 |
| `story_points` | Number | 否 | 工作项的故事点。当工作项的属性在视图中配置了故事点属性时，该参数生效。故事点数值必须是大于等于0的整数或最多包含一位小数的正数。 |
| `estimated_workload` | Number | 否 | 工作项的预估工时。 |
| `remaining_workload` | Number | 否 | 工作项的剩余工时。 |
| `properties` | Object | 否 | 工作项属性的键值对集合，需要注意的是，当前工作项类型对应的工作项属性方案需要包含这些工作项属性，例如工作项属性方案中包含`prop_a`和`prop_b`。 |
| `properties.prop_a` | Object | 否 | 工作项属性`prop_a`。 |
| `properties.prop_b` | Object | 否 | 工作项属性`prop_b`。 |
| `participant_ids` | String[] | 否 | 工作项关注人的id列表。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工作项的id。 |
| `url` | String | 工作项的地址。 |
| `project` | Object | 所属项目的引用结构数据。 |
| `identifier` | String | 工作项的标识。 |
| `title` | String | 工作项的标题。 |
| `type` | String | 工作项的类型。 |
| `start_at` | Number | 工作项的开始时间。 |
| `end_at` | Number | 工作项的结束时间。 |
| `parent_id` | String | 工作项的父工作项id。 |
| `short_id` | String | 工作项的短id。 |
| `html_url` | String | 工作项的html地址。 |
| `parent` | Object | 父工作项的引用结构数据。 |
| `assignee` | Object | 负责人的引用结构数据。 |
| `state` | Object | 工作项状态的引用结构数据。 |
| `priority` | Object | 工作项优先级的引用结构数据。 |
| `versions` | Object[] | 所属发布的引用结构数据列表。 |
| `sprint` | Object | 所属迭代的引用结构数据。 |
| `board` | Object | 所属看板的引用结构数据。 |
| `entry` | Object | 所属看板栏的引用结构数据。 |
| `swimlane` | Object | 所属泳道的引用结构数据。 |
| `phase` | Object | 所属计划的引用结构数据。 |
| `description` | String | 工作项的描述。 |
| `completed_at` | Number | 工作项的完成时间。 |
| `story_points` | Number | 工作项的故事点。 |
| `estimated_workload` | Number | 工作项的预估工时。 |
| `remaining_workload` | Number | 工作项的剩余工时。 |
| `properties` | Object | 工作项自定义属性的键值对集合。 |
| `tags` | Object[] | 工作项标签的引用结构数据列表。 |
| `participants` | Object[] | 工作项关注人的引用结构数据列表。 |
| `created_at` | Number | 工作项的创建时间。 |
| `created_by` | Object | 创建人的引用结构数据。 |
| `updated_at` | Number | 工作项的更新时间。 |
| `updated_by` | Object | 更新人的引用结构数据。 |
| `is_archived` | Number | 是否已归档。 |
| `is_deleted` | Number | 是否已删除。 |

**权限:** 企业令牌/用户令牌

---
### `POST` 创建一个工作项交付目标

**路径:** `/v1/pjm/deliverables`

用于创建一个工作项交付目标。

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `work_item_id` | String | 是 | 工作项的id。工作项所属项目类型必须为`waterfall`或`hybrid`。 |
| `name` | String | 是 | 工作项交付目标的名称。 |
| `content_type` | String | 否 | 工作项交付物的类型。工作项交付物的类型。只支持`link`。`attachment`类型的交付物通过`向交付目标中上传一个文件`接口上传附件。 |
| `content` | String | 否 | 工作项交付物。当工作项交付物的类型是`link`时，工作项交付物为包含name和href的对象，例如：`{ &quot;name&quot;: &quot;链接工作项交付目标&quot;,  &quot;href&quot;: &quot;https://{rest_api_root}/wiki/spaces/public/pages/6472e6f2f1968d3fdb0aba15&quot; }`。当工作项交付物不为空时，参数必须包含交付物类型。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工作项交付目标的id。 |
| `url` | String | 工作项交付目标的地址。 |
| `name` | String | 工作项交付目标的名称。 |
| `content_type` | String | 工作项交付物的类型。 |
| `content` | Object | 工作项交付物的引用结构数据。 |
| `project` | Object | 所属项目的引用结构数据。 |
| `work_item` | Object | 所属工作项的引用结构数据。 |
| `created_at` | Number | 工作项交付目标的创建时间。 |
| `created_by` | Object | 创建人的引用结构数据。 |
| `updated_at` | Number | 工作项交付目标的更新时间。 |
| `updated_by` | Object | 更新人的引用结构数据。 |
| `is_archived` | Number | 是否已归档。 |
| `is_deleted` | Number | 是否已删除。 |

**权限:** 企业令牌/用户令牌

---
### `DELETE` 删除一个工作项

**路径:** `/v1/pjm/work_items/{work_item_id}`

用于删除一个工作项。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `work_item_id` | String | 是 | 工作项的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工作项的id。 |
| `url` | String | 工作项的地址。 |
| `project` | Object | 所属项目的引用结构数据。 |
| `identifier` | String | 工作项的标识。 |
| `title` | String | 工作项的标题。 |
| `type` | String | 工作项的类型。 |
| `start_at` | Number | 工作项的开始时间。 |
| `end_at` | Number | 工作项的结束时间。 |
| `short_id` | String | 工作项的短id。 |
| `html_url` | String | 工作项的html地址。 |
| `assignee` | Object | 负责人的引用结构数据。 |
| `state` | Object | 工作项状态的引用结构数据。 |
| `priority` | Object | 工作项优先级的引用结构数据。 |
| `versions` | Object[] | 所属发布的引用结构数据列表。 |
| `sprint` | Object | 所属迭代的引用结构数据。 |
| `board` | Object | 所属看板的引用结构数据。 |
| `entry` | Object | 所属看板栏的引用结构数据。 |
| `swimlane` | Object | 所属泳道的引用结构数据。 |
| `phase` | Object | 所属计划的引用结构数据。 |
| `description` | String | 工作项的描述。 |
| `completed_at` | Number | 工作项的完成时间。 |
| `story_points` | Number | 工作项的故事点。 |
| `estimated_workload` | Number | 工作项的预估工时。 |
| `remaining_workload` | Number | 工作项的剩余工时。 |
| `properties` | Object | 工作项自定义属性的键值对集合。 |
| `tags` | Object[] | 工作项标签的引用结构数据列表。 |
| `participants` | Object[] | 工作项关注人的引用结构数据列表。 |
| `created_at` | Number | 工作项的创建时间。 |
| `created_by` | Object | 创建人的引用结构数据。 |
| `updated_at` | Number | 工作项的更新时间。 |
| `updated_by` | Object | 更新人的引用结构数据。 |
| `is_archived` | Number | 是否已归档。 |
| `is_deleted` | Number | 是否已删除。 |

**权限:** 企业令牌/用户令牌

---
### `DELETE` 删除一个工作项交付目标

**路径:** `/v1/pjm/deliverables/{deliverable_target_id}`

用于删除一个工作项交付目标。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `deliverable_target_id` | String | 是 | 工作项交付目标的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工作项交付目标的id。 |
| `url` | String | 工作项交付目标的地址。 |
| `name` | String | 工作项交付目标的名称。 |
| `content_type` | String | 工作项交付物的类型。 |
| `content` | Object | 工作项交付物的引用结构数据。 |
| `project` | Object | 所属项目的引用结构数据。 |
| `work_item` | Object | 所属工作项的引用结构数据。 |
| `created_at` | Number | 工作项交付目标的创建时间。 |
| `created_by` | Object | 创建人的引用结构数据。 |
| `updated_at` | Number | 工作项交付目标的更新时间。 |
| `updated_by` | Object | 更新人的引用结构数据。 |
| `is_archived` | Number | 是否已归档。 |
| `is_deleted` | Number | 是否已删除。 |

**权限:** 企业令牌/用户令牌

---
### `DELETE` 取消关联一个工作项

**路径:** `/v1/pjm/work_items/{work_item_id}/relations/{relation_id}`

用于取消关联一个工作项。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `work_item_id` | String | 是 | 工作项的id。 |
| `relation_id` | String | 是 | 工作项关联的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工作项关联的id。 |
| `url` | String | 工作项关联的地址。 |
| `relation_type` | String | 关联的类型。 |
| `origin_work_item` | Object | 源工作项的引用结构数据。 |
| `target_work_item` | Object | 目标工作项的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `POST` 向工作项中添加一个标签

**路径:** `/v1/pjm/work_items/{work_item_id}/tags`

用于向工作项中添加一个标签。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `work_item_id` | String | 是 | 工作项的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `tag_id` | String | 是 | 标签的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工作项标签的id。 |
| `url` | String | 工作项标签的地址。 |
| `work_item` | Object | 工作项的引用结构数据。 |
| `tag` | Object | 标签的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `DELETE` 在工作项中移除一个标签

**路径:** `/v1/pjm/work_items/{work_item_id}/tags/{tag_id}`

用于在工作项中移除一个标签。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `work_item_id` | String | 是 | 工作项的id。 |
| `tag_id` | String | 是 | 标签的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工作项标签的id。 |
| `url` | String | 工作项标签的地址。 |
| `work_item` | Object | 工作项的引用结构数据。 |
| `tag` | Object | 标签的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `PATCH` 批量部分更新工作项属性

**路径:** `/v1/pjm/work_items`

用于批量部分更新工作项属性。

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `ids` | String[] | 是 | 需要更新的工作项的id列表。最多可以批量更新100个工作项。 |
| `property_name` | String | 是 | 需要更新的工作项属性名。 |
| `property_value` | String | 否 | 需要更新的工作项属性值。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `inserts` | Number | 新增条数。 |
| `updates` | Number | 更新条数。 |
| `deletes` | Number | 删除条数。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个工作项

**路径:** `/v1/pjm/work_items/{work_item_id}`

用于查看一个工作项。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `work_item_id` | String | 是 | 工作项的id或short_id。 |

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `include_public_image_token` | String | 否 | 包含获取图片资源token的属性。使用','分割，最多只能20个，支持`description`和自定义多行文本类型的属性。参数示例`description,properties.prop_b`。 |
| `include_deleted` | Boolean | 否 | 是否包含已删除的工作项。该值默认为`false`。 |
| `include_archived` | Boolean | 否 | 是否包含已归档的工作项。该值默认为`false`。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工作项的id。 |
| `url` | String | 工作项的地址。 |
| `project` | Object | 工作项所属的项目。 |
| `identifier` | String | 工作项的标识。 |
| `title` | String | 工作项的标题。 |
| `type` | String | 工作项的类型。工作项类型分为9种系统类型和一些自定义类型。系统类型包括：史诗、特性、用户故事、阶段、里程碑、需求、任务、缺陷和事务。 |
| `start_at` | Number | 工作项的开始时间。 |
| `end_at` | Number | 工作项的结束时间。 |
| `parent_id` | String | 工作项的父工作项id。 |
| `short_id` | String | 工作项的短id。 |
| `html_url` | String | 工作项的html地址。 |
| `parent` | Object | 工作项的父工作项。 |
| `assignee` | Object | 工作项的负责人。 |
| `state` | Object | 工作项的状态。 |
| `priority` | Object | 工作项的优先级。 |
| `version` | Object | 工作项属的发布。 |
| `sprint` | Object | 工作项所属的迭代。 |
| `board` | Object | 工作项所属的看板。 |
| `entry` | Object | 工作项所属的看板栏。 |
| `swimlane` | Object | 工作项的所属的泳道。 |
| `phase` | Object | 工作项的所属计划。 |
| `description` | String | 工作项的描述。 |
| `completed_at` | Number | 工作项的完成时间。 |
| `story_points` | Number | 工作项的故事点。 |
| `estimated_workload` | Number | 工作项的预估工时。 |
| `remaining_workload` | Number | 工作项的剩余工时。 |
| `properties` | Object | 工作项的自定义属性。自定义属性包括用户自定义的属性和一些系统内置的属性。用户自定义的属性例如`prop_a`和`prop_b`。系统内置的属性例如`bug_type`、`solution`和`risk`等。 |
| `tags` | Object[] | 工作项的标签列表。 |
| `participants` | Object[] | 工作项的关注人列表。 |
| `public_image_token` | String | 工作项描述和自定义多行文本类型属性里获取图片资源token。获取一个工作项和获取工作项列表参数`include_public_image_token`值有效时返回。 |
| `created_at` | Number | 工作项的创建时间。 |
| `created_by` | Object | 工作项的创建人。 |
| `updated_at` | Number | 工作项的更新时间。 |
| `updated_by` | Object | 工作项的更新人。 |
| `is_archived` | Number | 是否已归档。 |
| `is_deleted` | Number | 是否已删除。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个工作项交付目标

**路径:** `/v1/pjm/deliverables/{deliverable_target_id}`

用于查看一个工作项交付目标。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `deliverable_target_id` | String | 是 | 工作项交付目标的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工作项交付目标的id。 |
| `url` | String | 工作项交付目标的地址。 |
| `name` | String | 工作项交付目标的名称。 |
| `content_type` | String | 工作项交付物的类型。 |
| `content` | Object | 工作项交付物的引用结构数据。 |
| `project` | Object | 所属项目的引用结构数据。 |
| `work_item` | Object | 所属工作项的引用结构数据。 |
| `created_at` | Number | 工作项交付目标的创建时间。 |
| `created_by` | Object | 创建人的引用结构数据。 |
| `updated_at` | Number | 工作项交付目标的更新时间。 |
| `updated_by` | Object | 更新人的引用结构数据。 |
| `is_archived` | Number | 是否已归档。 |
| `is_deleted` | Number | 是否已删除。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个工作项关联

**路径:** `/v1/pjm/work_items/{work_item_id}/relations/{relation_id}`

用于查看一个工作项关联。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `work_item_id` | String | 是 | 工作项的id。 |
| `relation_id` | String | 是 | 工作项关联的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工作项关联的id。 |
| `url` | String | 工作项关联的地址。 |
| `relation_type` | String | 关联的类型。 |
| `origin_work_item` | Object | 源工作项的引用结构数据。 |
| `target_work_item` | Object | 目标工作项的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个工作项关联类型

**路径:** `/v1/pjm/work_item_relation_types/{relation_type_id}`

用于查看一个工作项关联类型。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `relation_type_id` | String | 是 | 工作项关联类型的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工作项关联类型的id。 |
| `url` | String | 工作项关联类型的地址。 |
| `name` | String | 工作项关联类型的名称。 |
| `category` | String | 关联类型分类。 |
| `is_system` | Number | 是否为系统预设类型。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个工作项流转记录

**路径:** `/v1/pjm/work_items/{work_item_id}/transition_histories/{transition_history_id}`

用于查看一个工作项流转记录。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `work_item_id` | String | 是 | 工作项的id。 |
| `transition_history_id` | String | 是 | 工作项流转记录的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工作项流转记录的id。 |
| `url` | String | 工作项流转记录的地址。 |
| `work_item` | Object | 工作项的引用结构数据。 |
| `from_state` | Object | 流转前状态的引用结构数据。 |
| `to_state` | Object | 流转后状态的引用结构数据。 |
| `created_at` | Number | 流转记录的创建时间。 |
| `created_by` | Object | 创建人的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取关联的工作项列表

**路径:** `/v1/pjm/work_items/{work_item_id}/relations`

用于查询关联的工作项列表。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `work_item_id` | String | 是 | 工作项的id。 |

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `relation_type` | String | 否 | 关联的类型。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 关联的工作项全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取工作项中的一个标签

**路径:** `/v1/pjm/work_items/{work_item_id}/tags/{tag_id}`

用于查询工作项中的一个标签。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `work_item_id` | String | 是 | 工作项的id。 |
| `tag_id` | String | 是 | 标签的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工作项标签的id。 |
| `url` | String | 工作项标签的地址。 |
| `work_item` | Object | 工作项的引用结构数据。 |
| `tag` | Object | 标签的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取工作项交付目标列表

**路径:** `/v1/pjm/deliverables`

用于查询工作项交付目标列表。

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 否 | 项目的id。项目类型必须为`waterfall`或`hybrid`。 |
| `work_item_id` | String | 否 | 工作项的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 工作项交付目标全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取工作项优先级列表

**路径:** `/v1/pjm/work_item/priorities?project_id={project_id}`

用于查询工作项优先级列表。

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 是 | 项目的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 工作项优先级全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取工作项关联类型列表

**路径:** `/v1/pjm/work_item/relation_types`

用于查询工作项关联类型列表。

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_index` | Number | 页码，从0开始。 |
| `page_size` | Number | 每页条数。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 工作项关联类型的全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取工作项列表

**路径:** `/v1/pjm/work_items`

用于查询工作项列表。

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `identifier` | String | 否 | 工作项编号。 |
| `project_ids` | String | 否 | 项目的id，使用','分割，最多只能20个。 |
| `type_ids` | String | 否 | 工作项类型的id。工作项类型分为9种系统类型和一些自定义类型。系统类型包括：史诗、特性、用户故事、阶段、里程碑、需求、任务、缺陷和事务。可以通过`获取全部工作项类型列表`获得。最多只能20个。 |
| `parent_ids` | String | 否 | 父工作项的id，使用','分割，最多只能20个。 |
| `assignee_ids` | String | 否 | 工作项负责人的id，使用','分割，最多只能20个。 |
| `state_ids` | String | 否 | 工作项状态的id，使用','分割，最多只能20个。 |
| `start_between` | String | 否 | 开始时间介于的时间范围，通过','分割起始时间。比如`1580000000,1590000000`表示开始时间介于两个时间之间；`,1590000000`表示开始时间小于该时间；`1580000000`表示开始时间大于该时间。 |
| `end_between` | String | 否 | 结束时间介于的时间范围，通过','分割起始时间。使用方式参考开始时间。 |
| `priority_ids` | String | 否 | 工作项优先级的id，使用','分割，最多只能20个。 |
| `bug_type_ids` | String | 否 | 缺陷类别的id，使用','分割，最多只能20个。 |
| `tag_ids` | String | 否 | 工作项标签的id，使用','分割，最多只能20个。 |
| `sprint_ids` | String | 否 | 迭代的id，使用','分割，最多只能20个。 |
| `board_ids` | String | 否 | 看板的id，使用','分割，最多只能20个。 |
| `entry_ids` | String | 否 | 看板栏的id，使用','分割，最多只能20个。 |
| `swimlane_ids` | String | 否 | 泳道的id，使用','分割，最多只能20个。 |
| `phase_ids` | String | 否 | 所属计划的id，使用','分割，最多只能20个。 |
| `version_ids` | String | 否 | 发布的id，使用','分割，最多只能20个。 |
| `created_by_ids` | String | 否 | 创建人的id，使用','分割，最多只能20个。 |
| `created_between` | String | 否 | 创建时间介于的时间范围，通过','分割起始时间。使用方式参考开始时间。 |
| `updated_between` | String | 否 | 更新时间介于的时间范围，通过','分割起始时间。使用方式参考开始时间。 |
| `participant_id` | String | 否 | 工作项关注人的id。 |
| `keywords` | String | 否 | 关键字。支持工作项编号和工作项标题。 |
| `include_public_image_token` | String | 否 | 包含获取图片资源token的属性。使用','分割，最多只能20个，支持`description`和自定义多行文本类型的属性。参数示例`description,properties.prop_b`。 |
| `include_deleted` | Boolean | 否 | 是否查询已删除的工作项。该值默认为`false`。 |
| `include_archived` | Boolean | 否 | 是否查询已归档的工作项。该值默认为`false`。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 工作项全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取工作项属性列表

**路径:** `/v1/pjm/work_item/properties?project_id={project_id}&work_item_type_id={work_item_type_id}`

用于查询工作项属性列表。

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 是 | 项目的id。 |
| `work_item_type_id` | String | 是 | 工作项类型的id。工作项类型分为9种系统类型和一些自定义类型。系统类型包括：史诗、特性、用户故事、阶段、里程碑、需求、任务、缺陷和事务。可以通过`获取全部工作项类型列表`获得。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 工作项属性全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取工作项标签列表

**路径:** `/v1/pjm/work_item/tags`

用于查询工作项标签列表。

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 是 | 项目的id。 |
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
### `GET` 获取工作项流转记录列表

**路径:** `/v1/pjm/work_items/{work_item_id}/transition_histories`

用于查询工作项流转记录列表。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `work_item_id` | String | 是 | 工作项的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 工作项流转记录的全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取工作项状态列表

**路径:** `/v1/pjm/work_item/states?project_id={project_id}&work_item_type_id={work_item_type_id}`

用于查询工作项状态列表。

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 是 | 项目的id。 |
| `work_item_type_id` | String | 是 | 工作项类型的id。工作项类型分为9种系统类型和一些自定义类型。系统类型包括：史诗、特性、用户故事、阶段、里程碑、需求、任务、缺陷和事务。可以通过`获取全部工作项类型列表`获得。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 工作项状态的全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取工作项类型列表

**路径:** `/v1/pjm/work_item/types?project_id={project_id}`

用于查询工作项类型列表。

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `project_id` | String | 是 | 项目的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 工作项类型全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `PATCH` 部分更新一个工作项

**路径:** `/v1/pjm/work_items/{work_item_id}`

用于部分更新一个工作项。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `work_item_id` | String | 是 | 工作项的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `title` | String | 否 | 工作项的标题。 |
| `description` | String | 否 | 工作项的描述。 |
| `start_at` | Number | 否 | 工作项的开始时间。当工作项类型为里程碑时，该参数无效。 |
| `end_at` | Number | 否 | 工作项的截止时间。 |
| `priority_id` | String | 否 | 工作项优先级的id。 |
| `state_id` | String | 否 | 工作项状态的id。工作项状态的id在设置时必须同时满足工作项类型的工作项状态方案和工作项状态流转的状态值才能成功完成设置。工作项状态方案可以通过`获取工作项状态方案列表`获取。工作项状态流转则可以通过`获取状态方案中的工作项状态流转列表`获取。 |
| `assignee_id` | String | 否 | 工作项负责人的id。 |
| `parent_id` | String | 否 | 工作项的父工作项的id。当前工作项类型支持的父工作类型包含`parent_id`对应的工作项类型时，该参数有效。具体配置见属性与视图子工作项配置。 |
| `version_ids` | String[] | 否 | 所属发布的id列表。 |
| `board_id` | String | 否 | 看板的id。该字段只有项目类型为`kanban`和`hybrid`时有效。 |
| `entry_id` | String | 否 | 看板栏的id。该字段只有项目类型为`kanban`和`hybrid`时有效。 |
| `swimlane_id` | String | 否 | 泳道的id。该字段只有项目类型为`kanban`和`hybrid`时有效。 |
| `phase_id` | String | 否 | 所属计划的id。该字段只有项目类型为`waterfall`和`hybrid`时有效。 |
| `story_points` | Number | 否 | 工作项的故事点。当工作项的属性在视图中配置了故事点属性时，该参数生效。故事点数值必须是大于等于0的整数或最多包含一位小数的正数。 |
| `estimated_workload` | Number | 否 | 工作项的预估工时。 |
| `remaining_workload` | Number | 否 | 工作项的剩余工时。 |
| `properties` | Object | 否 | 工作项属性的键值对集合，需要注意的是，当前工作项类型对应的工作项属性方案需要包含这些工作项属性，例如工作项属性方案中包含`prop_a`和`prop_b`。 |
| `properties.prop_a` | Object | 否 | 工作项属性`prop_a`。 |
| `properties.prop_b` | Object | 否 | 工作项属性`prop_b`。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工作项的id。 |
| `url` | String | 工作项的地址。 |
| `project` | Object | 所属项目的引用结构数据。 |
| `identifier` | String | 工作项的标识。 |
| `title` | String | 工作项的标题。 |
| `type` | String | 工作项的类型。 |
| `start_at` | Number | 工作项的开始时间。 |
| `end_at` | Number | 工作项的结束时间。 |
| `parent_id` | String | 工作项的父工作项id。 |
| `short_id` | String | 工作项的短id。 |
| `html_url` | String | 工作项的html地址。 |
| `parent` | Object | 父工作项的引用结构数据。 |
| `assignee` | Object | 负责人的引用结构数据。 |
| `state` | Object | 工作项状态的引用结构数据。 |
| `priority` | Object | 工作项优先级的引用结构数据。 |
| `versions` | Object[] | 所属发布的引用结构数据列表。 |
| `sprint` | Object | 所属迭代的引用结构数据。 |
| `board` | Object | 所属看板的引用结构数据。 |
| `entry` | Object | 所属看板栏的引用结构数据。 |
| `swimlane` | Object | 所属泳道的引用结构数据。 |
| `phase` | Object | 所属计划的引用结构数据。 |
| `description` | String | 工作项的描述。 |
| `completed_at` | Number | 工作项的完成时间。 |
| `story_points` | Number | 工作项的故事点。 |
| `estimated_workload` | Number | 工作项的预估工时。 |
| `remaining_workload` | Number | 工作项的剩余工时。 |
| `properties` | Object | 工作项自定义属性的键值对集合。 |
| `tags` | Object[] | 工作项标签的引用结构数据列表。 |
| `participants` | Object[] | 工作项关注人的引用结构数据列表。 |
| `created_at` | Number | 工作项的创建时间。 |
| `created_by` | Object | 创建人的引用结构数据。 |
| `updated_at` | Number | 工作项的更新时间。 |
| `updated_by` | Object | 更新人的引用结构数据。 |
| `is_archived` | Number | 是否已归档。 |
| `is_deleted` | Number | 是否已删除。 |

**权限:** 企业令牌/用户令牌

---
### `PATCH` 部分更新一个工作项交付目标

**路径:** `/v1/pjm/deliverables/{deliverable_target_id}`

用于部分更新一个工作项交付目标。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `deliverable_target_id` | String | 是 | 工作项交付目标id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `work_item_id` | String | 否 | 工作项的id。 |
| `name` | String | 否 | 工作项交付目标的名称。 |
| `content_type` | String | 否 | 工作项交付物的类型。只支持`link`。`attachment`类型的交付物通过`向交付目标中上传一个文件`接口上传附件。 |
| `content` | String | 否 | 工作项交付物。当工作项交付物的类型是`link`时，工作项交付物为包含name和href的对象，例如：`{ &quot;name&quot;: &quot;链接工作项交付目标&quot;,  &quot;href&quot;: &quot;https://{rest_api_root}/wiki/spaces/public/pages/6472e6f2f1968d3fdb0aba15&quot; }`。当工作项交付物不为空时，参数必须包含交付物类型。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工作项交付目标的id。 |
| `url` | String | 工作项交付目标的地址。 |
| `name` | String | 工作项交付目标的名称。 |
| `content_type` | String | 工作项交付物的类型。 |
| `content` | Object | 工作项交付物的引用结构数据。 |
| `project` | Object | 所属项目的引用结构数据。 |
| `work_item` | Object | 所属工作项的引用结构数据。 |
| `created_at` | Number | 工作项交付目标的创建时间。 |
| `created_by` | Object | 创建人的引用结构数据。 |
| `updated_at` | Number | 工作项交付目标的更新时间。 |
| `updated_by` | Object | 更新人的引用结构数据。 |
| `is_archived` | Number | 是否已归档。 |
| `is_deleted` | Number | 是否已删除。 |

**权限:** 企业令牌/用户令牌

---
## 工时

### `POST` 创建一个工时

**路径:** `/v1/workloads`

用于创建一个工时。

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `principal_type` | String | 是 | 工时主体的类型。 在 `principal_type` 为 `work_item` 时，要求 `scopes` 包括 `pcp:write:pjm:workitem`;  在 `principal_type` 为 `idea` 时，要求 `scopes` 包括 `pcp:write:ship:idea`;  在 `principal_type` 为 `test_case` 时，要求 `scopes` 包括 `pcp:write:testhub:testcase`; |
| `principal_id` | String | 是 | 工时主体的id。 |
| `type_id` | String | 否 | 工时类型的id。 |
| `duration` | Number | 是 | 工时的时长。单位是小时，数值可以是为0-24之间，最多包含一位小数的正数。 |
| `report_at` | Number | 是 | 工时的登记日期。该值为十位数字组成的时间戳，会被转换为该时间当天的零点零分零秒。 |
| `report_by_id` | String | 否 | 工时的登记人，企业鉴权时必填。个人鉴权时不需要传递，即使传递了也会被忽略。 |
| `recorded_at` | String | 否 | 工时的登记时间，默认是当前时间。 |
| `description` | String | 否 | 工时的说明。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工时的id。 |
| `url` | String | 工时的资源地址。 |
| `principal_type` | String | 工时主体的类型。 |
| `principal` | Object | 工时的主体。 |
| `type` | Object | 工时的类型。 |
| `duration` | Number | 工时的时长。单位是小时，数值可以是为0-24之间，最多包含一位小数的正数。 |
| `review_state` | String | 工时的评审状态。 |
| `description` | String | 工时的说明。 |
| `report_at` | Number | 工时的登记日期。该值为十位数字组成的时间戳，会被转换为该时间当天的零点零分零秒。 |
| `report_by` | Object | 工时的登记人。 |
| `created_at` | Number | 工时的创建日期。该值为十位数字组成的时间戳。 |
| `created_by` | Object | 工时的创建人。 |

**权限:** 企业令牌/用户令牌

---
### `DELETE` 删除一个工时

**路径:** `/v1/workloads/{workload_id}`

用于删除一个工时。  用户令牌只能删除用户自己登记的工时记录。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `workload_id` | String | 是 | 工时的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工时的id。 |
| `url` | String | 工时的资源地址。 |
| `principal_type` | String | 工时主体的类型。 |
| `principal` | Object | 工时的主体。 |
| `type` | Object | 工时的类型。 |
| `duration` | Number | 工时的时长。单位是小时，数值可以是为0-24之间，最多包含一位小数的正数。 |
| `review_state` | String | 工时的评审状态。 |
| `description` | String | 工时的说明。 |
| `report_at` | Number | 工时的登记日期。该值为十位数字组成的时间戳，会被转换为该时间当天的零点零分零秒。 |
| `report_by` | Object | 工时的登记人。 |
| `created_at` | Number | 工时的创建日期。该值为十位数字组成的时间戳。 |
| `created_by` | Object | 工时的创建人。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个工时

**路径:** `/v1/workloads/{workload_id}`

用于查看一个工时。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `workload_id` | String | 是 | 工时的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工时的id。 |
| `url` | String | 工时的资源地址。 |
| `principal_type` | String | 工时主体的类型。 |
| `principal` | Object | 工时的主体。 |
| `type` | Object | 工时的类型。 |
| `duration` | Number | 工时的时长。单位是小时，数值可以是为0-24之间，最多包含一位小数的正数。 |
| `review_state` | String | 工时的评审状态。 |
| `description` | String | 工时的说明。 |
| `report_at` | Number | 工时的登记日期。该值为十位数字组成的时间戳，会被转换为该时间当天的零点零分零秒。 |
| `report_by` | Object | 工时的登记人。 |
| `created_at` | Number | 工时的创建日期。该值为十位数字组成的时间戳。 |
| `created_by` | Object | 工时的创建人。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个工时类型

**路径:** `/v1/workload_types/{type_id}`

用于查看一个工时类型。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `type_id` | String | 是 | 工时类型的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工时类型的id。 |
| `url` | String | 工时类型的资源地址。 |
| `name` | String | 工时类型的名称。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取工时列表

**路径:** `/v1/workloads`

用于查询工时列表。

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `principal_type` | String | 否 | 工时主体的类型。当查询参数含有pilot_id或principal_id时，principal_type参数必填。 在 `principal_type` 为 `work_item` 时，要求 `scopes` 包括 `pcp:write:pjm:workitem`;  在 `principal_type` 为 `idea` 时，要求 `scopes` 包括 `pcp:write:ship:idea`;  在 `principal_type` 为 `test_case` 时，要求 `scopes` 包括 `pcp:write:testhub:testcase`;  当不传`principal_type`时，要求 `scopes` 包括 `pcp:write:pjm:workitem`, `pcp:write:ship:idea`, `pcp:write:testhub:testcase`。 |
| `pilot_id` | String | 否 | 工时主体所在产品、项目或测试库的id。使用该参数过滤数据时，登记日期查询的起始时间和登记日期查询的结束时间的跨度最大为3个月。 |
| `principal_id` | String | 否 | 工时主体的id。 |
| `start_at` | Number | 否 | 登记日期查询的起始时间。开始时间会转换为对应日期的开始时间点。开始时间和结束时间须同时存在。 |
| `end_at` | Number | 否 | 登记日期查询的结束时间。结束时间会转换为对应日期的结束时间点。 |
| `report_by_id` | String | 否 | 登记人的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 工时全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取工时类型列表

**路径:** `/v1/workload_types`

用于查询工时类型列表。

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 工时类型的全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `PATCH` 部分更新一个工时

**路径:** `/v1/workloads/{workload_id}`

用于部分更新一个工时。  用户令牌只能更新属于用户自己登记的工时记录。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `workload_id` | String | 是 | 工时的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `type_id` | String | 否 | 工时类型的id。 |
| `duration` | Number | 否 | 工时的时长。单位是小时，数值可以是为0-24之间，最多包含一位小数的正数。 |
| `report_at` | Number | 否 | 工时的登记日期。该值为十位数字组成的时间戳，会被转换为该时间当天的零点零分零秒。 |
| `description` | String | 否 | 工时的说明。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 工时的id。 |
| `url` | String | 工时的资源地址。 |
| `principal_type` | String | 工时主体的类型。 |
| `principal` | Object | 工时的主体。 |
| `type` | Object | 工时的类型。 |
| `duration` | Number | 工时的时长。单位是小时，数值可以是为0-24之间，最多包含一位小数的正数。 |
| `review_state` | String | 工时的评审状态。 |
| `description` | String | 工时的说明。 |
| `report_at` | Number | 工时的登记日期。该值为十位数字组成的时间戳，会被转换为该时间当天的零点零分零秒。 |
| `report_by` | Object | 工时的登记人。 |
| `created_at` | Number | 工时的创建日期。该值为十位数字组成的时间戳。 |
| `created_by` | Object | 工时的创建人。 |

**权限:** 企业令牌/用户令牌

---
## 活动记录

### `GET` 获取一个活动记录

**路径:** `/v1/activities/{activity_id}`

用于查看一个活动记录。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `activity_id` | String | 是 | 活动记录的id。 |

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `principal_type` | String | 是 | 主体的类型。 在 `principal_type` 为 `work_item` 时，要求 `scopes` 包括 `pcp:read:pjm:workitem`;  在 `principal_type` 为 `test_case` 时，要求 `scopes` 包括 `pcp:read:testhub:testcase`;  在 `principal_type` 为 `test_run` 时，要求 `scopes` 包括 `pcp:read:testhub:testplan`;  在 `principal_type` 为 `idea` 时，要求 `scopes` 包括 `pcp:read:ship:idea`;  在 `principal_type` 为 `ticket` 时，要求 `scopes` 包括 `pcp:read:ship:ticket`; |
| `principal_id` | String | 是 | 主体的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 活动记录的id。 |
| `url` | String | 活动记录的资源地址。 |
| `template` | String | 活动记录的模板。 |
| `type` | String | 活动记录的操作类型。 |
| `summary` | String | 活动记录的摘要。 |
| `content` | Object | 活动记录的内容。 |
| `client` | String | 活动记录的客户端。 |
| `created_at` | Number | 活动记录的创建时间。 |
| `created_by` | Object | 活动记录的创建者。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取活动记录列表

**路径:** `/v1/activities?principal_type={principal_type}&principal_id={principal_id}`

用于查询活动记录列表。

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `principal_type` | String | 是 | 主体的类型。 在 `principal_type` 为 `work_item` 时，要求 `scopes` 包括 `pcp:read:pjm:workitem`;  在 `principal_type` 为 `test_case` 时，要求 `scopes` 包括 `pcp:read:testhub:testcase`;  在 `principal_type` 为 `test_run` 时，要求 `scopes` 包括 `pcp:read:testhub:testplan`;  在 `principal_type` 为 `idea` 时，要求 `scopes` 包括 `pcp:read:ship:idea`;  在 `principal_type` 为 `ticket` 时，要求 `scopes` 包括 `pcp:read:ship:ticket`; |
| `principal_id` | String | 是 | 主体的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_index` | Number | 页码，从0开始。 |
| `page_size` | Number | 每页条数。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 活动记录全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
## 评审

### `POST` 创建一个评审

**路径:** `/v1/reviews`

用于创建一个评审。

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `title` | String | 是 | 评审的标题。 |
| `pilot_id` | String | 是 | 评审主体所在产品、项目或测试库的id。 |
| `principal_type` | String | 是 | 评审主体的类型。 在 `principal_type` 为 `work_item` 时，要求 `scopes` 包括 `pcp:write:pjm:project`;  在 `principal_type` 为 `test_case` 时，要求 `scopes` 包括 `pcp:write:testhub:library`;  在 `principal_type` 为 `idea` 时，要求 `scopes` 包括 `pcp:write:ship:product`; |
| `description` | String | 否 | 评审的描述。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 评审的id。 |
| `url` | String | 评审的资源地址。 |
| `identifier` | String | 评审的标识符。 |
| `title` | String | 评审的标题。 |
| `status` | String | 评审的状态。 |
| `principal_type` | String | 评审主体的类型。 |
| `short_id` | String | 评审的短id。 |
| `html_url` | String | 评审的html地址。 |
| `pilot` | Object | 评审所在的产品、项目或测试库。 |
| `description` | String | 评审的描述。 |
| `participants` | Object[] | 评审的关注人列表。 |
| `submitted_at` | Number | 评审的提交时间。 |
| `submitted_by` | Object | 评审的提交人。 |
| `completed_at` | Number | 评审的完成时间。 |
| `completed_by` | Object | 评审的完成人。 |
| `created_at` | Number | 评审的创建时间。 |
| `created_by` | Object | 评审的创建人。 |
| `updated_at` | Number | 评审的更新时间。 |
| `updated_by` | Object | 评审的更新人。 |

**权限:** 企业令牌/用户令牌

---
### `DELETE` 删除一个评审

**路径:** `/v1/reviews/{review_id}?principal_type={principal_type}`

用于删除一个评审。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `review_id` | String | 是 | 评审的id。 |

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `principal_type` | String | 是 | 评审主体的类型。 在 `principal_type` 为 `work_item` 时，要求 `scopes` 包括 `pcp:write:pjm:project`;  在 `principal_type` 为 `test_case` 时，要求 `scopes` 包括 `pcp:write:testhub:library`;  在 `principal_type` 为 `idea` 时，要求 `scopes` 包括 `pcp:write:ship:product`; |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 评审的id。 |
| `url` | String | 评审的资源地址。 |
| `identifier` | String | 评审的标识符。 |
| `title` | String | 评审的标题。 |
| `status` | String | 评审的状态。 |
| `principal_type` | String | 评审主体的类型。 |
| `short_id` | String | 评审的短id。 |
| `html_url` | String | 评审的html地址。 |
| `pilot` | Object | 评审所在的产品、项目或测试库。 |
| `description` | String | 评审的描述。 |
| `participants` | Object[] | 评审的关注人列表。 |
| `submitted_at` | Number | 评审的提交时间。 |
| `submitted_by` | Object | 评审的提交人。 |
| `completed_at` | Number | 评审的完成时间。 |
| `completed_by` | Object | 评审的完成人。 |
| `created_at` | Number | 评审的创建时间。 |
| `created_by` | Object | 评审的创建人。 |
| `updated_at` | Number | 评审的更新时间。 |
| `updated_by` | Object | 评审的更新人。 |

**权限:** 企业令牌/用户令牌

---
### `POST` 向评审中添加一个评审内容

**路径:** `/v1/reviews/{review_id}/principals`

用于向评审中添加一个评审内容。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `review_id` | String | 是 | 评审的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `principal_id` | String | 是 | 评审内容的id。 |
| `principal_type` | String | 是 | 评审主体的类型。 在 `principal_type` 为 `work_item` 时，要求 `scopes` 包括 `pcp:write:pjm:project`;  在 `principal_type` 为 `test_case` 时，要求 `scopes` 包括 `pcp:write:testhub:library`;  在 `principal_type` 为 `idea` 时，要求 `scopes` 包括 `pcp:write:ship:product`; |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 评审内容的id。 |
| `url` | String | 评审内容的资源地址。 |
| `review` | Object | 所属评审的引用结构数据。 |
| `principal_type` | String | 评审内容的类型。 |
| `principal` | Object | 评审内容的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `DELETE` 在评审中移除一个评审内容

**路径:** `/v1/reviews/{review_id}/principals/{principal_id}?principal_type={principal_type}`

用于在评审中移除一个评审内容。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `review_id` | String | 是 | 评审的id。 |
| `principal_id` | String | 是 | 评审内容的id。 |

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `principal_type` | String | 是 | 评审主体的类型。 在 `principal_type` 为 `work_item` 时，要求 `scopes` 包括 `pcp:write:pjm:project`;  在 `principal_type` 为 `test_case` 时，要求 `scopes` 包括 `pcp:write:testhub:library`;  在 `principal_type` 为 `idea` 时，要求 `scopes` 包括 `pcp:write:ship:product`; |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 评审内容的id。 |
| `url` | String | 评审内容的资源地址。 |
| `review` | Object | 所属评审的引用结构数据。 |
| `principal_type` | String | 评审内容的类型。 |
| `principal` | Object | 评审内容的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个评审

**路径:** `/v1/reviews/{review_id}`

用于查看一个评审。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `review_id` | String | 是 | 评审的id。 |

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `principal_type` | String | 是 | 评审主体的类型。 在 `principal_type` 为 `work_item` 时，要求 `scopes` 包括 `pcp:read:pjm:project`;  在 `principal_type` 为 `test_case` 时，要求 `scopes` 包括 `pcp:read:testhub:library`;  在 `principal_type` 为 `idea` 时，要求 `scopes` 包括 `pcp:read:ship:product`; |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 评审的id。 |
| `url` | String | 评审的资源地址。 |
| `identifier` | String | 评审的标识符。 |
| `title` | String | 评审的标题。 |
| `status` | String | 评审状态。 |
| `principal_type` | String | 评审主体的类型。 |
| `short_id` | String | 评审的短id。 |
| `html_url` | String | 评审的html地址。 |
| `pilot` | Object | 评审所在的产品、项目或测试库。 |
| `description` | String | 评审的描述。 |
| `participants` | Object[] | 评审的关注人列表。 |
| `submitted_at` | Number | 评审的提交时间。 |
| `submitted_by` | Object | 评审的提交人。 |
| `completed_at` | Number | 评审的完成时间。 |
| `completed_by` | Object | 评审的完成人。 |
| `created_at` | Number | 评审的创建时间。 |
| `created_by` | Object | 评审的创建人。 |
| `updated_at` | Number | 评审的更新时间。 |
| `updated_by` | Object | 评审的更新人。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个评审内容

**路径:** `/v1/reviews/{review_id}/principals/{principal_id}?principal_type={principal_type}`

用于查看一个评审内容。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `review_id` | String | 是 | 评审的id。 |
| `principal_id` | String | 是 | 评审内容的id。 |

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `principal_type` | String | 是 | 评审主体的类型。 在 `principal_type` 为 `work_item` 时，要求 `scopes` 包括 `pcp:read:pjm:project`;  在 `principal_type` 为 `test_case` 时，要求 `scopes` 包括 `pcp:read:testhub:library`;  在 `principal_type` 为 `idea` 时，要求 `scopes` 包括 `pcp:read:ship:product`; |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 评审内容的id。 |
| `url` | String | 评审内容的资源地址。 |
| `review` | Object | 所属评审的引用结构数据。 |
| `principal_type` | String | 评审内容的类型。 |
| `principal` | Object | 评审内容的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取评审内容列表

**路径:** `/v1/reviews/{review_id}/principals?principal_type={principal_type}`

用于查询评审内容列表。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `review_id` | String | 是 | 评审的id。 |

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `principal_type` | String | 是 | 评审主体的类型。 在 `principal_type` 为 `work_item` 时，要求 `scopes` 包括 `pcp:read:pjm:project`;  在 `principal_type` 为 `test_case` 时，要求 `scopes` 包括 `pcp:read:testhub:library`;  在 `principal_type` 为 `idea` 时，要求 `scopes` 包括 `pcp:read:ship:product`; |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 评审内容全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取评审列表

**路径:** `/v1/reviews?principal_type={principal_type}&pilot_id={pilot_id}`

用于查询评审列表。

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `principal_type` | String | 是 | 评审主体的类型。 在 `principal_type` 为 `work_item` 时，要求 `scopes` 包括 `pcp:read:pjm:project`;  在 `principal_type` 为 `test_case` 时，要求 `scopes` 包括 `pcp:read:testhub:library`;  在 `principal_type` 为 `idea` 时，要求 `scopes` 包括 `pcp:read:ship:product`; |
| `pilot_id` | String | 是 | 评审主体所在产品、项目或测试库的id。 |
| `status` | String | 否 | 评审的状态。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 评审全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
## 评论

### `POST` 创建一个评论

**路径:** `/v1/comments`

用于创建一个评论。

**参数 (请求参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `principal_type` | String | 是 | 评论主体的类型。 在 `principal_type` 为 `work_item` 时，要求 `scopes` 包括 `pcp:write:pjm:workitem`;  在 `principal_type` 为 `test_case` 时，要求 `scopes` 包括 `pcp:write:testhub:testcase`;  在 `principal_type` 为 `test_run` 时，要求 `scopes` 包括 `pcp:write:testhub:testplan`;  在 `principal_type` 为 `idea` 时，要求 `scopes` 包括 `pcp:write:ship:idea`;  在 `principal_type` 为 `ticket` 时，要求 `scopes` 包括 `pcp:write:ship:ticket`;  在 `principal_type` 为 `page` 时，要求 `scopes` 包括 `pcp:write:wiki:page`; |
| `principal_id` | String | 否 | 评论主体的id。 |
| `review_id` | String | 否 | 评论评审的id。`principal_id`和`review_id`至少存在一个，若同时存在，则忽略`review_id`。 |
| `content` | String | 是 | 评论的内容。 |
| `reply_comment_id` | String | 否 | 被回复评论的id。 |
| `created_at` | Number | 否 | 评论的创建时间。 |
| `created_by` | String | 否 | 评论的创建人。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 评论的id。 |
| `url` | String | 评论的资源地址。 |
| `content` | String | 评论的内容。 |
| `attachment_count` | Number | 评论的附件数量。 |
| `attachments` | Object[] | 评论的附件列表。 |
| `is_reply_comment` | Number | 是否是回复评论。 |
| `replied_comment` | Object | 被回复的评论。 |
| `created_at` | Number | 评论的创建时间。 |
| `created_by` | Object | 评论的创建人。 |
| `is_deleted` | Number | 评论是否被删除。 |

**权限:** 企业令牌/用户令牌

---
### `DELETE` 删除一个评论

**路径:** `/v1/comments/{comment_id}?principal_type={principal_type}&principal_id={principal_id}`

用于删除一个评论。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `comment_id` | String | 是 | 评论的id。 |

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `principal_type` | String | 是 | 评论主体的类型。 在 `principal_type` 为 `work_item` 时，要求 `scopes` 包括 `pcp:write:pjm:workitem`;  在 `principal_type` 为 `test_case` 时，要求 `scopes` 包括 `pcp:write:testhub:testcase`;  在 `principal_type` 为 `test_run` 时，要求 `scopes` 包括 `pcp:write:testhub:testplan`;  在 `principal_type` 为 `idea` 时，要求 `scopes` 包括 `pcp:write:ship:idea`;  在 `principal_type` 为 `ticket` 时，要求 `scopes` 包括 `pcp:write:ship:ticket`;  在 `principal_type` 为 `page` 时，要求 `scopes` 包括 `pcp:write:wiki:page`; |
| `principal_id` | String | 否 | 评论主体的id。 |
| `review_id` | String | 否 | 评论评审的id。`principal_id`和`review_id`至少存在一个，若同时存在，则忽略`review_id`。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 评论的id。 |
| `url` | String | 评论的资源地址。 |
| `content` | String | 评论的内容。被删除后为空字符串。 |
| `attachment_count` | Number | 评论的附件数量。 |
| `attachments` | Object[] | 评论的附件列表。 |
| `is_reply_comment` | Number | 是否是回复评论。 |
| `replied_comment` | Object | 被回复的评论。 |
| `created_at` | Number | 评论的创建时间。 |
| `created_by` | Object | 评论的创建人。 |
| `is_deleted` | Number | 评论是否被删除。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个评论

**路径:** `/v1/comments/{comment_id}`

用于查看一个评论。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `comment_id` | String | 是 | 评论的id。 |

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `principal_type` | String | 是 | 评论主体的类型。 在 `principal_type` 为 `work_item` 时，要求 `scopes` 包括 `pcp:read:pjm:workitem`;  在 `principal_type` 为 `test_case` 时，要求 `scopes` 包括 `pcp:read:testhub:testcase`;  在 `principal_type` 为 `test_run` 时，要求 `scopes` 包括 `pcp:read:testhub:testplan`;  在 `principal_type` 为 `idea` 时，要求 `scopes` 包括 `pcp:read:ship:idea`;  在 `principal_type` 为 `ticket` 时，要求 `scopes` 包括 `pcp:read:ship:ticket`;  在 `principal_type` 为 `page` 时，要求 `scopes` 包括 `pcp:read:wiki:page`; |
| `principal_id` | String | 否 | 评论主体的id。 |
| `review_id` | String | 否 | 评论评审的id。`principal_id`和`review_id`至少存在一个，若同时存在，则忽略`review_id`。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 评论的id。 |
| `url` | String | 评论的资源地址。 |
| `content` | String | 评论的内容。被删除的评论content字段会被置空，is_deleted字段为1。 |
| `attachment_count` | Number | 评论的附件数量。 |
| `attachments` | Object[] | 评论的附件列表。 |
| `is_reply_comment` | Number | 是否是回复评论。 |
| `replied_comment` | Object | 被回复的评论。 |
| `created_at` | Number | 评论的创建时间。 |
| `created_by` | Object | 评论的创建人。 |
| `is_deleted` | Number | 评论是否被删除。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取评论列表

**路径:** `/v1/comments?principal_type={principal_type}&principal_id={principal_id}`

用于查询评论列表。

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `principal_type` | String | 是 | 评论主体的类型。 在 `principal_type` 为 `work_item` 时，要求 `scopes` 包括 `pcp:read:pjm:workitem`;  在 `principal_type` 为 `test_case` 时，要求 `scopes` 包括 `pcp:read:testhub:testcase`;  在 `principal_type` 为 `test_run` 时，要求 `scopes` 包括 `pcp:read:testhub:testplan`;  在 `principal_type` 为 `idea` 时，要求 `scopes` 包括 `pcp:read:ship:idea`;  在 `principal_type` 为 `ticket` 时，要求 `scopes` 包括 `pcp:read:ship:ticket`;  在 `principal_type` 为 `page` 时，要求 `scopes` 包括 `pcp:read:wiki:page`; |
| `principal_id` | String | 否 | 评论主体的id。 |
| `review_id` | String | 否 | 评论评审的id。`principal_id`和`review_id`至少存在一个，若同时存在，则忽略`review_id`。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 评论全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
## 通用

### `` 关注人

**路径:** `关注人`

---
### `` 关联

**路径:** `关联`

---
### `` 活动记录

**路径:** `活动记录`

---
### `` 评审

**路径:** `评审`

---
### `` 评论

**路径:** `评论`

---
### `` 附件

**路径:** `附件`

---
## 附件

### `POST` 上传一个代码段

**路径:** `/v1/attachments`

用于上传一个代码段。

**参数 (请求参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `principal_type` | String | 是 | 附件主体的类型。  在 `principal_type` 为 `work_item` 时，要求 `scopes` 包括 `pcp:write:pjm:workitem`;  在 `principal_type` 为 `test_case` 时，要求 `scopes` 包括 `pcp:write:testhub:testcase`;  在 `principal_type` 为 `test_run` 时，要求 `scopes` 包括 `pcp:write:testhub:testplan`;  在 `principal_type` 为 `idea` 时，要求 `scopes` 包括 `pcp:write:ship:idea`;  在 `principal_type` 为 `ticket` 时，要求 `scopes` 包括 `pcp:write:ship:ticket`;  在 `principal_type` 为 `page` 时，要求 `scopes` 包括 `pcp:write:wiki:page`; |
| `principal_id` | String | 是 | 附件主体的id。 |
| `comment_id` | String | 否 | 附件主体的评论id。当需要向附件主体的评论上传文件或者代码段时，需要传入该参数。 |
| `title` | String | 是 | 代码段的标题。 |
| `format` | String | 是 | 代码段的语言。 |
| `content` | String | 是 | 代码段的内容。 |

**权限:** 企业令牌/用户令牌

---
### `POST` 上传一个文件

**路径:** `/v1/attachments?principal_type={principal_type}&principal_id={principal_id}`

用于上传一个文件。

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `principal_type` | String | 是 | 附件主体的类型。 在 `principal_type` 为 `work_item`, `work_item_deliverable` 时，要求 `scopes` 包括 `pcp:write:pjm:workitem`;  在 `principal_type` 为 `test_case` 时，要求 `scopes` 包括 `pcp:write:testhub:testcase`;  在 `principal_type` 为 `test_run` 时，要求 `scopes` 包括 `pcp:write:testhub:testplan`;  在 `principal_type` 为 `idea` 时，要求 `scopes` 包括 `pcp:write:ship:idea`;  在 `principal_type` 为 `ticket` 时，要求 `scopes` 包括 `pcp:write:ship:ticket`;  在 `principal_type` 为 `page` 时，要求 `scopes` 包括 `pcp:write:wiki:page`; |
| `principal_id` | String | 是 | 附件主体的id。 |
| `comment_id` | String | 否 | 附件主体的评论id。当需要向附件主体的评论上传文件或者代码段时，需要传入该参数。 |

**参数 (请求参数 form-data):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `title` | String | 是 | 这是一个图片类型的附件.png |
| `file` | File | 是 | /Users/ping-code/这是一个图片类型的附件.png |

**权限:** 企业令牌/用户令牌

---
### `DELETE` 删除一个附件

**路径:** `/v1/attachments/{attachment_id}?principal_type={principal_type}&principal_id={principal_id}`

用于删除一个附件。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `attachment_id` | String | 是 | 附件的id。 |

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `principal_type` | String | 是 | 附件主体的类型。 在 `principal_type` 为 `work_item`, `work_item_deliverable` 时，要求 `scopes` 包括 `pcp:write:pjm:workitem`;  在 `principal_type` 为 `test_run` 时，要求 `scopes` 包括 `pcp:write:testhub:testcase`;  在 `principal_type` 为 `test_run` 时，要求 `scopes` 包括 `pcp:write:testhub:testplan`;  在 `principal_type` 为 `idea` 时，要求 `scopes` 包括 `pcp:write:ship:idea`;  在 `principal_type` 为 `ticket` 时，要求 `scopes` 包括 `pcp:write:ship:ticket`;  在 `principal_type` 为 `page` 时，要求 `scopes` 包括 `pcp:write:wiki:page`; |
| `principal_id` | String | 是 | 附件主体的id。 |
| `comment_id` | String | 否 | 附件主体的评论id。当需要删除评论附件时，需要传入该参数。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 附件的id。 |
| `url` | String | 附件的资源地址。 |
| `title` | String | 附件的标题。 |
| `size` | Number | 附件的大小。 |
| `type` | String | 附件的类型。 |
| `file_type` | String | 文件的类型。 |
| `ext` | String | 文件的扩展名。 |
| `download_url` | String | 文件的下载地址。 |
| `created_at` | Number | 附件的创建时间。 |
| `created_by` | Object | 附件的创建人。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个附件

**路径:** `/v1/attachments/{attachment_id}`

用于查看一个附件。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `attachment_id` | String | 是 | 附件的id。 |

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `principal_type` | String | 是 | 附件主体的类型。 在 `principal_type` 为 `work_item`, `work_item_deliverable` 时，要求 `scopes` 包括 `pcp:read:pjm:workitem`;  在 `principal_type` 为 `test_case` 时，要求 `scopes` 包括 `pcp:read:testhub:testcase`;  在 `principal_type` 为 `test_run` 时，要求 `scopes` 包括 `pcp:read:testhub:testplan`;  在 `principal_type` 为 `idea` 时，要求 `scopes` 包括 `pcp:read:ship:idea`;  在 `principal_type` 为 `ticket` 时，要求 `scopes` 包括 `pcp:read:ship:ticket`;  在 `principal_type` 为 `page` 时，要求 `scopes` 包括 `pcp:read:wiki:page`; |
| `principal_id` | String | 是 | 附件主体的id。 |
| `comment_id` | String | 否 | 附件主体的评论id。当需要获取评论附件时，需要传入该参数。 |
| `review_id` | String | 否 | 附件主体的评审id。当需要获取评审附件时，需要传入该参数。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 附件的id。 |
| `url` | String | 附件的资源地址。 |
| `title` | String | 附件的标题。 |
| `size` | Number | 附件的大小。 |
| `type` | String | 附件的类型。 |
| `file_type` | String | 文件的类型。当附件的类型为 `file` 时返回。 |
| `ext` | String | 文件的扩展名。当附件的类型为 `file` 时返回。 |
| `download_url` | String | 文件的下载地址。当附件的类型为 `file` 时返回。 |
| `format` | String | 代码的格式。当附件的类型为 `snippet` 时返回。 |
| `content` | String | 代码的内容。当附件的类型为 `snippet` 时返回。 |
| `line` | Number | 代码的行数。当附件的类型为 `snippet` 时返回。 |
| `created_at` | Number | 附件的创建时间。 |
| `created_by` | Object | 附件的创建人。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取附件列表

**路径:** `/v1/attachments?principal_type={principal_type}&principal_id={principal_id}`

用于查询附件列表。

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `principal_type` | String | 是 | 附件主体的类型。 在 `principal_type` 为 `work_item`, `work_item_deliverable` 时，要求 `scopes` 包括 `pcp:read:pjm:workitem`;  在 `principal_type` 为 `test_case` 时，要求 `scopes` 包括 `pcp:read:testhub:testcase`;  在 `principal_type` 为 `test_run` 时，要求 `scopes` 包括 `pcp:read:testhub:testplan`;  在 `principal_type` 为 `idea` 时，要求 `scopes` 包括 `pcp:read:ship:idea`;  在 `principal_type` 为 `ticket` 时，要求 `scopes` 包括 `pcp:read:ship:ticket`;  在 `principal_type` 为 `page` 时，要求 `scopes` 包括 `pcp:read:wiki:page`; |
| `principal_id` | String | 是 | 附件主体的id。 |
| `comment_id` | String | 否 | 附件主体的评论id。当需要获取评论附件时，需要传入该参数。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 附件全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
## 需求

### `POST` 创建一个需求

**路径:** `/v1/ship/ideas`

用于创建一个需求。

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 是 | 需求的产品id。 |
| `title` | String | 是 | 需求的标题，最大长度为255。 |
| `assignee_id` | String | 否 | 需求负责人的id。 |
| `description` | String | 否 | 需求的描述。 |
| `suite_id` | String | 否 | 需求的产品模块id。 |
| `priority_id` | String | 否 | 需求优先级的id，您可以在 `获取需求优先级列表` API获取。 |
| `properties` | Object | 否 | 需求属性的键值对集合。要注意的是，当前产品的需求属性视图需要包含这些需求属性，例如需求属性视图中包含`prop_a`和`prop_b`。 |
| `properties.prop_a` | Object | 否 | 需求项属性`prop_a`。 |
| `properties.prop_b` | Object | 否 | 需求项属性`prop_b`。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个需求

**路径:** `/v1/ship/ideas/{idea_id}`

用于查看一个需求。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `idea_id` | String | 是 | 需求的id。 |

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `include_public_image_token` | String | 否 | 包含获取图片资源token的属性。使用','分割，最多只能20个，支持`description`和自定义多行文本类型的属性。参数示例`description,properties.xxx`。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 需求的id。 |
| `url` | String | 需求的资源地址。 |
| `product` | Object | 需求的所属产品。 |
| `identifier` | String | 需求的标识。 |
| `title` | String | 需求的标题。 |
| `short_id` | String | 需求的短id。 |
| `html_url` | String | 需求的html地址。 |
| `assignee` | Object | 需求的负责人。 |
| `state` | Object | 需求的状态。 |
| `priority` | Object | 需求的优先级。 |
| `plan` | Object | 需求的计划。 |
| `suite` | Object | 需求的模块。 |
| `plan_at` | Object | 需求的计划时间范围。 |
| `plan_at.from` | Number | 需求的计划开始时间。 |
| `plan_at.to` | Number | 需求的计划结束时间。 |
| `plan_at.granularity` | String | 需求的计划时间周期单位。 |
| `real_at` | Object | 需求的实际时间范围。 |
| `real_at.from` | Number | 需求的实际开始时间。 |
| `real_at.to` | Number | 需求的实际结束时间。 |
| `real_at.granularity` | String | 需求的计划时间周期单位。 |
| `score` | Number | 需求的分数。 |
| `progress` | Number | 需求的进度。 |
| `description` | String | 需求的描述。 |
| `properties` | Object | 需求的自定义属性。 |
| `properties.prop_a` | Object | 需求的自定义属性prop_a。 |
| `properties.prop_b` | Object | 需求的自定义属性prop_b。 |
| `participants` | Object[] | 需求的关注人列表。 |
| `public_image_token` | String | 需求描述和自定义多行文本类型属性里获取图片资源token。获取一个需求和获取需求列表参数`include_public_image_token`值有效时返回。 |
| `completed_at` | Number | 需求的完成时间。 |
| `completed_by` | Object | 需求的完成人。 |
| `created_at` | Number | 需求的创建时间。 |
| `created_by` | Object | 需求的创建人。 |
| `updated_at` | Number | 需求的更新时间。 |
| `updated_by` | Object | 需求的更新人。 |
| `is_archived` | Number | 是否已归档。 |
| `is_deleted` | Number | 是否已删除。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一条需求流转记录

**路径:** `/v1/ship/ideas/{idea_id}/transition_histories/{transition_history_id}`

用于查看一条需求流转记录。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `idea_id` | String | 是 | 需求的id。 |
| `transition_history_id` | String | 是 | 需求流转记录的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 需求流转记录的id。 |
| `url` | String | 需求流转记录的资源地址。 |
| `idea` | Object | 需求的引用结构数据。 |
| `from_state` | Object | 流转前需求状态的引用结构数据。 |
| `to_state` | Object | 流转后需求状态的引用结构数据。 |
| `created_at` | Number | 创建时间，单位为秒。 |
| `created_by` | Object | 创建人的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取需求优先级列表

**路径:** `/v1/ship/idea/priorities?product_id={product_id}`

用于查询需求优先级列表。

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
| `values` | Object[] | 需求优先级全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取需求列表

**路径:** `/v1/ship/ideas`

用于查询需求列表。

**参数 (查询参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `product_id` | String | 否 | 产品的id。 |
| `state_id` | String | 否 | 需求状态id。 |
| `priority_id` | String | 否 | 需求优先级id。 |
| `created_between` | String | 否 | 创建时间介于的时间范围，通过','分割起始时间。 |
| `updated_between` | String | 否 | 更新时间介于的时间范围，通过','分割起始时间。 |
| `keywords` | String | 否 | 搜索关键字。支持需求编号和需求标题。 |
| `include_public_image_token` | String | 否 | 包含获取图片资源token的属性。使用','分割，最多只能20个，支持`description`和自定义多行文本类型的属性。参数示例`description,properties.xxx`。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取需求属性列表

**路径:** `/v1/ship/idea/properties?product_id={product_id}`

用于查询需求属性列表。

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
| `values` | Object[] | 需求属性全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取需求排期列表

**路径:** `/v1/ship/idea/plans?product_id={product_id}`

用于查询需求排期列表。

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
| `values` | Object[] | 需求排期全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取需求模块列表

**路径:** `/v1/ship/idea/suites?product_id={product_id}`

用于查询需求模块列表。

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
| `values` | Object[] | 需求模块全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取需求流转记录列表

**路径:** `/v1/ship/ideas/{idea_id}/transition_histories`

用于查询需求流转记录列表。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `idea_id` | String | 是 | 需求的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 需求流转记录全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取需求状态列表

**路径:** `/v1/ship/idea/states?product_id={product_id}`

用于查询需求状态列表。

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
| `values` | Object[] | 需求状态全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `PATCH` 部分更新一个需求

**路径:** `/v1/ship/ideas/{idea_id}`

用于部分更新一个需求。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `idea_id` | String | 是 | 需求id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `title` | String | 否 | 需求的标题，最大长度为255。 |
| `description` | String | 否 | 需求的描述。 |
| `state_id` | String | 否 | 需求状态的id，您可以在 `获取需求状态列表` API获取。 |
| `priority_id` | String | 否 | 需求优先级的id，您可以在 `获取需求优先级列表` API获取。 |
| `assignee_id` | String | 否 | 需求负责人的id。 |
| `progress` | Number | 否 | 需求的进度，取值范围为：0到1的两位小数。 |
| `plan_at` | Object | 否 | 需求的计划时间。plan_at是整体更新的，其中包含`from`、`to`、`granularity`三个属性，均为必填。 |
| `plan_at.from` | Number | 是 | 需求的计划开始时间。为秒级时间戳。 |
| `plan_at.to` | Number | 是 | 需求的计划结束时间。为秒级时间戳。 |
| `plan_at.granularity` | String | 是 | 需求的计划时间周期单位。 |
| `real_at` | Object | 否 | 需求的实际时间，参数格式同`plan_at`。 |
| `plan_id` | String | 否 | 产品排期的id，您可以在 `获取产品排期列表` API获取。 |
| `suite_id` | String | 否 | 产品模块的id，您可以在 `获取产品模块列表` API获取。 |
| `properties` | Object | 否 | 需求的自定义属性。 |
| `properties.prop_a` | Object | 否 | 需求的自定义属性`prop_a`。 |
| `properties.prop_b` | Object | 否 | 需求的自定义属性`prop_b`。 |

**权限:** 企业令牌/用户令牌

---
### `` 需求模块

**路径:** `需求模块`

---
### `` 需求流转记录

**路径:** `需求流转记录`

---
## 需求配置

### `POST` 创建一个需求属性

**路径:** `/v1/ship/idea_properties`

用于创建一个需求属性。

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 是 | 需求属性的名称。在一个企业中这个名称是唯一的。 |
| `type` | String | 是 | 需求属性的类型。 |
| `options` | Object[] | 否 | 选择项列表。当需求属性类型为`select,multi_select,cascade_select,cascade_multi_select`时可选填此项。 |
| `options._id` | String | 否 | 选择项id。该值在选择项中是唯一的。 |
| `options.text` | String | 是 | 选择项内容。该值在选择项中是唯一的。 |
| `options.parent_id` | String | 否 | 选择项父级id。当属性类型为`cascade_select,cascade_multi_select`时，`parent_id`参数有效，用于构建级联类型选择项之间的父子关系，最多存在4级。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 需求属性的id。 |
| `url` | String | 需求属性的资源地址。 |
| `name` | String | 需求属性的名称。 |
| `type` | String | 需求属性的类型。 |
| `options` | Object[] | 下拉选项值。 |
| `is_removable` | Number | 是否允许删除。 |
| `is_name_editable` | Number | 是否允许修改名称。 |
| `is_options_editable` | Number | 是否允许修改下拉选项值。 |
| `select_all_level` | Boolean | 级联选择时是否允许选择全部层级。 |
| `display_all_level` | Boolean | 级联选择时是否展示全部层级。 |
| `display_separator` | String | 级联选择时的层级分隔符。 |

**权限:** 企业令牌/用户令牌

---
### `POST` 向需求属性方案中添加一个需求属性

**路径:** `/v1/ship/idea_property_plans/{property_plan_id}/idea_properties`

用于向需求属性方案中添加一个需求属性。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `property_plan_id` | String | 是 | 需求属性方案的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `property_id` | String | 是 | 需求属性的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 属性方案中需求属性关联的id。 |
| `url` | String | 属性方案中需求属性关联的资源地址。 |
| `property_plan` | Object | 需求属性方案的引用结构数据。 |
| `property` | Object | 需求属性的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `DELETE` 在需求属性方案中移除一个需求属性

**路径:** `/v1/ship/idea_property_plans/{property_plan_id}/idea_properties/{property_id}`

用于在需求属性方案中移除一个需求属性。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `property_plan_id` | String | 是 | 需求属性方案的id。 |
| `property_id` | String | 是 | 需求属性的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 属性方案中需求属性关联的id。 |
| `url` | String | 属性方案中需求属性关联的资源地址。 |
| `property_plan` | Object | 需求属性方案的引用结构数据。 |
| `property` | Object | 需求属性的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个需求优先级

**路径:** `/v1/ship/idea_priorities/{priority_id}`

用于查看一个需求优先级。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `priority_id` | String | 是 | 需求优先级的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 需求优先级的id。 |
| `url` | String | 需求优先级的资源地址。 |
| `name` | String | 需求优先级的名称。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个需求属性

**路径:** `/v1/ship/idea_properties/{property_id}`

用于查看一个需求属性。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `property_id` | String | 是 | 需求属性的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 需求属性的id。 |
| `url` | String | 需求属性的资源地址。 |
| `name` | String | 需求属性的名称。 |
| `type` | String | 需求属性的类型。 |
| `options` | Object[] | 下拉选项值。 |
| `is_removable` | Number | 是否允许删除。 |
| `is_name_editable` | Number | 是否允许修改名称。 |
| `is_options_editable` | Number | 是否允许修改下拉选项值。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个需求属性方案

**路径:** `/v1/ship/idea_property_plans/{property_plan_id}`

用于查看一个需求属性方案。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `property_plan_id` | String | 是 | 需求属性方案的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 需求属性方案的id。 |
| `url` | String | 需求属性方案的资源地址。 |
| `product` | Object | 需求属性方案关联产品的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取一个需求状态

**路径:** `/v1/ship/idea_states/{idea_state_id}`

用于查看一个需求状态。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `idea_state_id` | String | 是 | 需求状态的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 需求状态的id。 |
| `url` | String | 需求状态的资源地址。 |
| `name` | String | 需求状态的名称。 |
| `type` | String | 需求状态的类型。 |
| `color` | String | 需求状态的颜色。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取全部需求优先级列表

**路径:** `/v1/ship/idea_priorities`

用于查询需求优先级列表。

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 需求优先级的全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取全部需求属性列表

**路径:** `/v1/ship/idea_properties`

用于查询全部需求属性列表。

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 全部需求属性的全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取全部需求状态列表

**路径:** `/v1/ship/idea_states`

用于查询全部需求状态列表。

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 全部需求状态的全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取需求属性方案中的一个需求属性

**路径:** `/v1/ship/idea_property_plans/{property_plan_id}/idea_properties/{property_id}`

用于查询属性方案中的一个需求属性。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `property_plan_id` | String | 是 | 需求属性方案的id。 |
| `property_id` | String | 是 | 需求属性的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 属性方案中需求属性关联的id。 |
| `url` | String | 属性方案中需求属性关联的资源地址。 |
| `property_plan` | Object | 需求属性方案的引用结构数据。 |
| `property` | Object | 需求属性的引用结构数据。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取需求属性方案中的需求属性列表

**路径:** `/v1/ship/idea_property_plans/{property_plan_id}/idea_properties`

用于查询需求属性方案中的需求属性列表。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `property_plan_id` | String | 是 | 需求属性方案的id。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 属性方案中的需求属性全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `GET` 获取需求属性方案列表

**路径:** `/v1/ship/idea_property_plans`

用于查询需求属性方案列表。

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `page_size` | Number | 每页条数。 |
| `page_index` | Number | 页码，从0开始。 |
| `total` | Number | 总条数。 |
| `values` | Object[] | 需求属性方案全量结构数据的数组。 |

**权限:** 企业令牌/用户令牌

---
### `PATCH` 部分更新一个需求属性

**路径:** `/v1/ship/idea_properties/{property_id}`

用于部分更新一个需求属性。

**参数 (路径参数):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `property_id` | String | 是 | 需求属性的id。 |

**参数 (Parameter):**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| `name` | String | 否 | 需求属性的名称。在一个企业中这个名称是唯一的。 |
| `options` | Object[] | 否 | 选择项列表。`options`是整体更新的。 |
| `options._id` | String | 否 | 选择项id。该值在选择项中是唯一的。 |
| `options.text` | String | 是 | 选择项内容。该值在选择项中是唯一的。 |
| `options.parent_id` | String | 否 | 选择项父级id。当属性类型为`cascade_select,cascade_multi_select`时，`parent_id`参数有效，用于构建级联类型选择项之间的父子关系，最多存在4级。 |

**返回字段 (资源属性):**

| 字段名 | 类型 | 描述 |
| --- | --- | --- |
| `id` | String | 需求属性的id。 |
| `url` | String | 需求属性的资源地址。 |
| `name` | String | 需求属性的名称。 |
| `type` | String | 需求属性的类型。 |
| `options` | Object[] | 下拉选项值。 |
| `is_removable` | Number | 是否允许删除。 |
| `is_name_editable` | Number | 是否允许修改名称。 |
| `is_options_editable` | Number | 是否允许修改下拉选项值。 |
| `select_all_level` | Boolean | 级联选择时是否允许选择全部层级。 |
| `display_all_level` | Boolean | 级联选择时是否展示全部层级。 |
| `display_separator` | String | 级联选择时的层级分隔符。 |

**权限:** 企业令牌/用户令牌

---
