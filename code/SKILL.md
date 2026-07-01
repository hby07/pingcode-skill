---
name: pingcode-code
description: "代码仓库、分支、提交、提交引用、拉取请求、代码评审、托管平台 — 代码管理 相关的 PingCode REST API。需要查看具体接口参数时读取本目录 APIs.md。"
metadata:
  qwenpaw:
    emoji: "💻"
    requires:
      bins: ["python3"]
      env: ["PINGCODE_CLIENT_ID", "PINGCODE_CLIENT_SECRET"]
---

# 💻 PingCode 代码管理

## 概述

代码仓库、分支、提交、提交引用、拉取请求、代码评审、托管平台

本模块包含 **44** 个 API 接口。

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
| `PUT` | `/v1/scm/products/{product_id}/repositories/{repository_id}` | 全量更新一个代码仓库 |
| `POST` | `/v1/scm/products/{product_id}/repositories` | 创建一个代码仓库 |
| `GET` | `/v1/scm/products/{product_id}/repositories/{repository_id}` | 获取一个代码仓库 |
| `GET` | `/v1/scm/products/{product_id}/repositories` | 获取代码仓库列表 |
| `PATCH` | `/v1/scm/products/{product_id}/repositories/{repository_id}` | 部分更新一个代码仓库 |
| `` | `代码仓库` | 代码仓库 |
| `` | `代码分支` | 代码分支 |
| `` | `代码评审` | 代码评审 |
| `POST` | `/v1/scm/products/{product_id}/repositories/{repository_id}/branches` | 创建一个代码分支 |
| `DELETE` | `/v1/scm/products/{product_id}/repositories/{repository_id}/branches/{branch_id}` | 删除一个代码分支 |
| `GET` | `/v1/scm/products/{product_id}/repositories/{repository_id}/branches/{branch_id}` | 获取一个代码分支 |
| `GET` | `/v1/scm/products/{product_id}/repositories/{repository_id}/branches` | 获取代码分支列表 |
| `PATCH` | `/v1/scm/products/{product_id}/repositories/{repository_id}/branches/{branch_id}` | 部分更新一个代码分支 |
| `` | `托管平台` | 托管平台 |
| `` | `托管平台用户` | 托管平台用户 |
| `` | `拉取请求` | 拉取请求 |
| `` | `提交` | 提交 |
| `` | `提交引用` | 提交引用 |
| `PUT` | `/v1/scm/products/{product_id}/repositories/{repository_id}/pull_requests/{pull_request_id}/reviews/{review_id}` | 全量更新一个代码评审 |
| `POST` | `/v1/scm/products/{product_id}/repositories/{repository_id}/pull_requests/{pull_request_id}/reviews` | 创建一个代码评审 |
| `GET` | `/v1/scm/products/{product_id}/repositories/{repository_id}/pull_requests/{pull_request_id}/reviews/{review_id}` | 获取一个代码评审 |
| `GET` | `/v1/scm/products/{product_id}/repositories/{repository_id}/pull_requests/{pull_request_id}/reviews` | 获取代码评审列表 |
| `PATCH` | `/v1/scm/products/{product_id}/repositories/{repository_id}/pull_requests/{pull_request_id}/reviews/{review_id}` | 部分更新一个代码评审 |
| `PUT` | `/v1/scm/products/{product_id}` | 全量更新一个托管平台 |
| `POST` | `/v1/scm/products` | 创建一个托管平台 |
| `PUT` | `/v1/scm/products/{product_id}/users/{user_id}` | 全量更新一个托管平台用户 |
| `POST` | `/v1/scm/products/{product_id}/users` | 创建一个托管平台用户 |
| `GET` | `/v1/scm/products/{product_id}/users/{user_id}` | 获取一个托管平台用户 |
| `GET` | `/v1/scm/products/{product_id}/users` | 获取托管平台用户列表 |
| `PATCH` | `/v1/scm/products/{product_id}/users/{user_id}` | 部分更新一个托管平台用户 |
| `GET` | `/v1/scm/products/{product_id}` | 获取一个托管平台 |
| `GET` | `/v1/scm/products` | 获取托管平台列表 |
| `PATCH` | `/v1/scm/products/{product_id}` | 部分更新一个托管平台 |
| `PUT` | `/v1/scm/products/{product_id}/repositories/{repository_id}/pull_requests/{pull_request_id}` | 全量更新一个拉取请求 |
| `POST` | `/v1/scm/products/{product_id}/repositories/{repository_id}/pull_requests` | 创建一个拉取请求 |
| `GET` | `/v1/scm/products/{product_id}/repositories/{repository_id}/pull_requests/{pull_request_id}` | 获取一个拉取请求 |
| `GET` | `/v1/scm/products/{product_id}/repositories/{repository_id}/pull_requests` | 获取拉取请求列表 |
| `PATCH` | `/v1/scm/products/{product_id}/repositories/{repository_id}/pull_requests/{pull_request_id}` | 部分更新一个拉取请求 |
| `POST` | `/v1/scm/commits` | 创建一个提交 |
| `POST` | `/v1/scm/products/{product_id}/repositories/{repository_id}/refs` | 创建一个提交引用 |
| `GET` | `/v1/scm/products/{product_id}/repositories/{repository_id}/refs/{ref_id}` | 获取一个提交引用 |
| `GET` | `/v1/scm/products/{product_id}/repositories/{repository_id}/refs` | 获取提交引用列表 |
| `GET` | `/v1/scm/commits/{commit_id_or_sha}` | 获取一个提交 |
| `GET` | `/v1/scm/commits` | 获取提交列表 |


## 详细参数

如需查看某个接口的完整参数表、请求体、返回字段，请阅读本目录的 **`APIs.md`**。

## 常用操作速查

- **PUT 全量更新一个代码仓库**: `/v1/scm/products/{product_id}/repositories/{repository_id}` — 用于全量更新一个代码仓库。
- **POST 创建一个代码仓库**: `/v1/scm/products/{product_id}/repositories` — 用于创建一个代码仓库。  代码托管平台内实际的代码仓库，用于在PingCode中显示代码仓库的详细信息。
- **GET 获取一个代码仓库**: `/v1/scm/products/{product_id}/repositories/{repository_id}` — 用于查看一个代码仓库。
- **GET 获取代码仓库列表**: `/v1/scm/products/{product_id}/repositories` — 用于查询代码仓库列表。
- **PATCH 部分更新一个代码仓库**: `/v1/scm/products/{product_id}/repositories/{repository_id}` — 用于部分更新一个代码仓库。
- ** 代码仓库**: `代码仓库` — 
- ** 代码分支**: `代码分支` — 
- ** 代码评审**: `代码评审` — 
- **POST 创建一个代码分支**: `/v1/scm/products/{product_id}/repositories/{repository_id}/branches` — 用于创建一个代码分支。
- **DELETE 删除一个代码分支**: `/v1/scm/products/{product_id}/repositories/{repository_id}/branches/{branch_id}` — 用于删除一个代码分支。  删除分支后，不会移除该分支和工作项的关联历史，在关联历史中，依然可以查询到删除的分支。默认分支不能被删除。
- ... 共 44 个接口，详见 `APIs.md`
