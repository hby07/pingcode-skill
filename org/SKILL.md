---
name: pingcode-org
description: "企业信息、成员、部门、团队、角色、职位、安全日志、全局配置 — 组织管理 相关的 PingCode REST API。需要查看具体接口参数时读取本目录 APIs.md。"
metadata:
  qwenpaw:
    emoji: "🏢"
    requires:
      bins: ["python3"]
      env: ["PINGCODE_CLIENT_ID", "PINGCODE_CLIENT_SECRET"]
---

# 🏢 PingCode 组织管理

## 概述

企业信息、成员、部门、团队、角色、职位、安全日志、全局配置

本模块包含 **50** 个 API 接口。

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
| `GET` | `/v1/myself` | 获取个人信息 |
| `POST` | `/v1/directory/users` | 创建一个企业成员 |
| `PATCH` | `/v1/directory/users/bulk` | 批量更新企业成员属性 |
| `GET` | `/v1/directory/users/{user_id}` | 获取一个企业成员 |
| `GET` | `/v1/directory/users` | 获取企业成员列表 |
| `PATCH` | `/v1/directory/users/{user_id}` | 部分更新一个企业成员 |
| `GET` | `/v1/directory/team` | 获取企业信息 |
| `` | `个人` | 个人 |
| `` | `安全` | 安全 |
| `` | `工时` | 工时 |
| `` | `组织` | 组织 |
| `` | `组织` | 组织 |
| `` | `组织` | 组织 |
| `` | `组织` | 组织 |
| `` | `组织` | 组织 |
| `` | `组织` | 组织 |
| `` | `通用` | 通用 |
| `POST` | `/v1/directory/groups` | 创建一个团队 |
| `POST` | `/v1/directory/groups/{group_id}/members` | 向团队中添加一个成员 |
| `DELETE` | `/v1/directory/groups/{group_id}/members/{member_id}` | 在团队中移除一个成员 |
| `GET` | `/v1/directory/groups/{group_id}` | 获取一个团队 |
| `GET` | `/v1/directory/groups/{group_id}/members/{member_id}` | 获取团队中的一个成员 |
| `GET` | `/v1/directory/groups/{group_id}/members` | 获取团队中的成员列表 |
| `GET` | `/v1/directory/groups` | 获取团队列表 |
| `PATCH` | `/v1/directory/groups/{group_id}` | 部分更新一个团队 |
| `` | `日志` | 日志 |
| `` | `日志` | 日志 |
| `GET` | `/v1/security/audit_logs` | 获取审计日志列表 |
| `GET` | `/v1/security/login_logs` | 获取登录日志列表 |
| `` | `URI结构` | URI结构 |
| `` | `使用方式` | 使用方式 |
| `` | `数据结构` | 数据结构 |
| `` | `欢迎使用` | 欢迎使用 |
| `` | `频率限制` | 频率限制 |
| `` | `企业` | 企业 |
| `` | `企业成员` | 企业成员 |
| `` | `团队` | 团队 |
| `` | `团队成员` | 团队成员 |
| `` | `职位` | 职位 |
| `` | `角色` | 角色 |
| `` | `部门` | 部门 |
| `GET` | `/v1/directory/jobs/{job_id}` | 获取一个职位 |
| `GET` | `/v1/directory/jobs` | 获取职位列表 |
| `GET` | `/v1/directory/roles/{role_id}` | 获取一个角色 |
| `GET` | `/v1/directory/roles` | 获取角色列表 |
| `POST` | `/v1/directory/departments` | 创建一个部门 |
| `DELETE` | `/v1/directory/departments/{department_id}` | 删除一个部门 |
| `GET` | `/v1/directory/departments/{department_id}` | 获取一个部门 |
| `GET` | `/v1/directory/departments` | 获取部门列表 |
| `PATCH` | `/v1/directory/departments/{department_id}` | 部分更新一个部门 |


## 详细参数

如需查看某个接口的完整参数表、请求体、返回字段，请阅读本目录的 **`APIs.md`**。

## 常用操作速查

- **GET 获取个人信息**: `/v1/myself` — 用于查看个人信息。
- **POST 创建一个企业成员**: `/v1/directory/users` — 用于创建一个企业成员。
- **PATCH 批量更新企业成员属性**: `/v1/directory/users/bulk` — 用于批量更新企业成员属性。
- **GET 获取一个企业成员**: `/v1/directory/users/{user_id}` — 用于查看一个企业成员。
- **GET 获取企业成员列表**: `/v1/directory/users` — 用于查询企业成员列表。
- **PATCH 部分更新一个企业成员**: `/v1/directory/users/{user_id}` — 用于部分更新一个企业成员。
- **GET 获取企业信息**: `/v1/directory/team` — 用于查看企业信息。
- ** 个人**: `个人` — 
- ** 安全**: `安全` — 
- ** 工时**: `工时` — 
- ... 共 50 个接口，详见 `APIs.md`
