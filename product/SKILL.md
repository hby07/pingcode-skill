---
name: pingcode-product
description: "产品、产品成员、工单、客户、外部用户、标签、模块 — 产品管理 相关的 PingCode REST API。需要查看具体接口参数时读取本目录 APIs.md。"
metadata:
  qwenpaw:
    emoji: "📦"
    requires:
      bins: ["python3"]
      env: ["PINGCODE_CLIENT_ID", "PINGCODE_CLIENT_SECRET"]
---

# 📦 PingCode 产品管理

## 概述

产品、产品成员、工单、客户、外部用户、标签、模块

本模块包含 **85** 个 API 接口。

## 认证

从环境变量获取（与主模块共用）：

| 环境变量 | 说明 |
|----------|------|
| `PINGCODE_CLIENT_ID` | 应用 Client ID |
| `PINGCODE_CLIENT_SECRET` | 应用 Client Secret |
| `PINGCODE_BASE_URL` | API 根地址（可选，默认 `https://open.pingcode.com`）|

## 调用方式

```bash
python3 {{baseDir}}/../scripts/pingcode.py '{{"method":"GET","path":"/v1/myself"}}'
```

## 本模块 API 列表

| 方法 | 路径 | 说明 |
|------|------|------|
| `` | `产品成员` | 产品成员 |
| `POST` | `/v1/ship/products` | 创建一个产品 |
| `POST` | `/v1/ship/products/{product_id}/users` | 创建一个外部用户 |
| `POST` | `/v1/ship/products/{product_id}/customers` | 创建一个客户 |
| `DELETE` | `/v1/ship/products/{product_id}/users/{user_id}` | 删除一个外部用户 |
| `POST` | `/v1/ship/products/{product_id}/members` | 向产品中添加一个成员 |
| `POST` | `/v1/ship/products/{product_id}/tags` | 向产品中添加一个标签 |
| `POST` | `/v1/ship/products/{product_id}/suites` | 向产品中添加一个需求模块 |
| `DELETE` | `/v1/ship/products/{product_id}/members/{member_id}` | 在产品中移除一个成员 |
| `DELETE` | `/v1/ship/products/{product_id}/tags/{tag_id}` | 在产品中移除一个标签 |
| `DELETE` | `/v1/ship/products/{product_id}/suites/{suite_id}` | 在产品中移除一个需求模块 |
| `` | `外部用户` | 外部用户 |
| `` | `客户` | 客户 |
| `` | `标签` | 标签 |
| `` | `产品` | 产品 |
| `` | `` | 产品配置中心 |
| `` | `工单` | 工单 |
| `` | `需求` | 需求 |
| `GET` | `/v1/ship/products/{product_id}` | 获取一个产品 |
| `GET` | `/v1/ship/products/{product_id}/users/{user_id}` | 获取一个外部用户 |
| `GET` | `/v1/ship/products/{product_id}/customers/{customer_id}` | 获取一个客户 |
| `GET` | `/v1/ship/products/{product_id}/channels/{channel_id}` | 获取产品中的一个工单渠道 |
| `GET` | `/v1/ship/products/{product_id}/ticket_types/{ticket_type_id}` | 获取产品中的一个工单类型 |
| `GET` | `/v1/ship/products/{product_id}/members/{member_id}` | 获取产品中的一个成员 |
| `GET` | `/v1/ship/products/{product_id}/tags/{tag_id}` | 获取产品中的一个标签 |
| `GET` | `/v1/ship/products/{product_id}/plans/{plan_id}` | 获取产品中的一个需求排期 |
| `GET` | `/v1/ship/products/{product_id}/suites/{suite_id}` | 获取产品中的一个需求模块 |
| `GET` | `/v1/ship/products/{product_id}/channels` | 获取产品中的工单渠道列表 |
| `GET` | `/v1/ship/products/{product_id}/ticket_types` | 获取产品中的工单类型列表 |
| `GET` | `/v1/ship/products/{product_id}/members` | 获取产品中的成员列表 |
| `GET` | `/v1/ship/products/{product_id}/tags` | 获取产品中的标签列表 |
| `GET` | `/v1/ship/products/{product_id}/plans` | 获取产品中的需求排期列表 |
| `GET` | `/v1/ship/products/{product_id}/suites` | 获取产品中的需求模块列表 |
| `GET` | `/v1/ship/products` | 获取产品列表 |
| `GET` | `/v1/ship/products/{product_id}/users` | 获取外部用户列表 |
| `GET` | `/v1/ship/products/{product_id}/customers` | 获取客户列表 |
| `PATCH` | `/v1/ship/products/{product_id}` | 部分更新一个产品 |
| `PATCH` | `/v1/ship/products/{product_id}/users/{user_id}` | 部分更新一个外部用户 |
| `PATCH` | `/v1/ship/products/{product_id}/customers/{customer_id}` | 部分更新一个客户 |
| `` | `需求排期` | 需求排期 |
| `` | `需求模块` | 需求模块 |
| `POST` | `/v1/ship/tickets` | 创建一个工单 |
| `` | `工单流转记录` | 工单流转记录 |
| `GET` | `/v1/ship/tickets/{ticket_id}` | 获取一个工单 |
| `GET` | `/v1/ship/tickets/{ticket_id}/transition_histories/{transition_history_id}` | 获取一条工单流转记录 |
| `GET` | `/v1/ship/ticket/priorities?product_id={product_id}` | 获取工单优先级列表 |
| `GET` | `/v1/ship/tickets` | 获取工单列表 |
| `GET` | `/v1/ship/ticket/properties?product_id={product_id}` | 获取工单属性列表 |
| `GET` | `/v1/ship/ticket/tags?product_id={product_id}` | 获取工单标签列表 |
| `GET` | `/v1/ship/tickets/{ticket_id}/transition_histories` | 获取工单流转记录列表 |
| `GET` | `/v1/ship/ticket/channels?product_id={product_id}` | 获取工单渠道列表 |
| `GET` | `/v1/ship/ticket/states?product_id={product_id}` | 获取工单状态列表 |
| `GET` | `/v1/ship/ticket/types?product_id={product_id}` | 获取工单类型列表 |
| `GET` | `/v1/ship/ticket/solutions?product_id={product_id}` | 获取工单解决方案列表 |
| `PATCH` | `/v1/ship/tickets/{ticket_id}` | 部分更新一个工单 |
| `POST` | `/v1/ship/ticket_properties` | 创建一个工单属性 |
| `POST` | `/v1/ship/ticket_states` | 创建一个工单状态 |
| `POST` | `/v1/ship/ticket_property_plans/{property_plan_id}/ticket_properties` | 向工单属性方案中添加一个工单属性 |
| `POST` | `/v1/ship/ticket_state_plans/{state_plan_id}/ticket_states` | 向状态方案中添加一个工单状态 |
| `POST` | `/v1/ship/ticket_state_plans/{state_plan_id}/ticket_state_flows` | 向状态方案中添加一个工单状态流转 |
| `DELETE` | `/v1/ship/ticket_property_plans/{property_plan_id}/ticket_properties/{property_id}` | 在工单属性方案中移除一个工单属性 |
| `DELETE` | `/v1/ship/ticket_state_plans/{state_plan_id}/ticket_states/{state_id}` | 在状态方案中移除一个工单状态 |
| `DELETE` | `/v1/ship/ticket_state_plans/{state_plan_id}/ticket_state_flows/{state_flow_id}` | 在状态方案中移除一个工单状态流转 |
| `GET` | `/v1/ship/ticket_priorities/{priority_id}` | 获取一个工单优先级 |
| `GET` | `/v1/ship/ticket_properties/{property_id}` | 获取一个工单属性 |
| `GET` | `/v1/ship/ticket_property_plans/{property_plan_id}` | 获取一个工单属性方案 |
| `GET` | `/v1/ship/ticket_states/{ticket_state_id}` | 获取一个工单状态 |
| `GET` | `/v1/ship/ticket_state_plans/{state_plan_id}` | 获取一个工单状态方案 |
| `GET` | `/v1/ship/ticket_types/{ticket_type_id}` | 获取一个工单类型 |
| `GET` | `/v1/ship/ticket_solutions/{ticket_solution_id}` | 获取一个工单解决方案 |
| `GET` | `/v1/ship/ticket_priorities` | 获取全部工单优先级列表 |
| `GET` | `/v1/ship/ticket_properties` | 获取全部工单属性列表 |
| `GET` | `/v1/ship/ticket_states` | 获取全部工单状态列表 |
| `GET` | `/v1/ship/ticket_types` | 获取全部工单类型列表 |
| `GET` | `/v1/ship/ticket_solutions` | 获取全部工单解决方案列表 |
| `GET` | `/v1/ship/ticket_property_plans/{property_plan_id}/ticket_properties/{property_id}` | 获取工单属性方案中的一个工单属性 |
| `GET` | `/v1/ship/ticket_property_plans/{property_plan_id}/ticket_properties` | 获取工单属性方案中的工单属性列表 |
| `GET` | `/v1/ship/ticket_property_plans` | 获取工单属性方案列表 |
| `GET` | `/v1/ship/ticket_state_plans` | 获取工单状态方案列表 |
| `GET` | `/v1/ship/ticket_state_plans/{state_plan_id}/ticket_states/{state_id}` | 获取状态方案中的一个工单状态 |
| `GET` | `/v1/ship/ticket_state_plans/{state_plan_id}/ticket_state_flows/{state_flow_id}` | 获取状态方案中的一个工单状态流转 |
| `GET` | `/v1/ship/ticket_state_plans/{state_plan_id}/ticket_states` | 获取状态方案中的工单状态列表 |
| `GET` | `/v1/ship/ticket_state_plans/{state_plan_id}/ticket_state_flows` | 获取状态方案中的工单状态流转列表 |
| `PATCH` | `/v1/ship/ticket_properties/{property_id}` | 部分更新一个工单属性 |
| `PATCH` | `/v1/ship/ticket_states/{ticket_state_id}` | 部分更新一个工单状态 |


## 详细参数

如需查看某个接口的完整参数表、请求体、返回字段，请阅读本目录的 **`APIs.md`**。

## 常用操作速查

- ** 产品成员**: `产品成员` — 
- **POST 创建一个产品**: `/v1/ship/products` — 用于创建一个产品。
- **POST 创建一个外部用户**: `/v1/ship/products/{product_id}/users` — 用于创建一个外部用户。
- **POST 创建一个客户**: `/v1/ship/products/{product_id}/customers` — 用于创建一个客户。
- **DELETE 删除一个外部用户**: `/v1/ship/products/{product_id}/users/{user_id}` — 用于删除一个外部用户。
- **POST 向产品中添加一个成员**: `/v1/ship/products/{product_id}/members` — 用于向产品中添加一个成员。
- **POST 向产品中添加一个标签**: `/v1/ship/products/{product_id}/tags` — 用于向产品中添加一个标签。
- **POST 向产品中添加一个需求模块**: `/v1/ship/products/{product_id}/suites` — 用于向产品中添加一个需求模块。
- **DELETE 在产品中移除一个成员**: `/v1/ship/products/{product_id}/members/{member_id}` — 用于在产品中移除一个成员。
- **DELETE 在产品中移除一个标签**: `/v1/ship/products/{product_id}/tags/{tag_id}` — 用于在产品中移除一个标签。
- ... 共 85 个接口，详见 `APIs.md`
