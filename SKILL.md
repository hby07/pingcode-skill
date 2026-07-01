---
name: pingcode
description: "PingCode REST API 全模块封装：组织管理、产品、工作项、代码、测试、发布、计划、知识库、项目管理。根据用户意图加载对应模块的 SKILL.md 和 APIs.md，通过通用脚本 pingcode.py 调用 API。"
metadata:
  qwenpaw:
    emoji: "🔗"
    requires:
      bins: ["python3"]
      env: ["PINGCODE_CLIENT_ID", "PINGCODE_CLIENT_SECRET"]
---

# PingCode API Skill

## 概述

本 Skill 封装了 [PingCode REST API](https://open.pingcode.com/) 全部接口，按业务模块拆分为 **11 个子模块**，每个模块独立维护。

**工作方式：**

1. 根据用户意图，判断需要操作哪个模块
2. 读取该模块的 `SKILL.md` 了解用法
3. 如需查看具体 API 参数，读取该模块的 `APIs.md`
4. 调用通用脚本 `{baseDir}/scripts/pingcode.py` 执行操作

**⚠️ 不要一次性加载所有模块的 APIs.md，按需加载以节省上下文。**

## 认证配置

从环境变量获取：

| 环境变量 | 说明 | 必填 |
|----------|------|------|
| `PINGCODE_CLIENT_ID` | 应用 Client ID | ✅ |
| `PINGCODE_CLIENT_SECRET` | 应用 Client Secret | ✅ |
| `PINGCODE_BASE_URL` | API 根地址 | ❌（默认 `https://open.pingcode.com`）|

首次调用时脚本会自动获取企业令牌并缓存，后续自动刷新。

## 通用脚本

```bash
python3 {baseDir}/scripts/pingcode.py '{{"method":"GET","path":"/v1/myself"}}'
```

## 模块索引

| 模块 ID | 模块名 | 说明 | API 数量 |
|---------|--------|------|----------|
| `auth` | 🔑 认证与鉴权 | 企业令牌获取、用户授权码流程 | 6 |
| `org` | 🏢 组织管理 | 企业信息、成员、部门、团队、角色、职位、安全日志、全局配置 | 50 |
| `product` | 📦 产品管理 | 产品、产品成员、工单、客户、外部用户、标签、模块 | 85 |
| `workitem` | 📋 工作项 | 需求、任务、缺陷、迭代工作项、评论、附件、关注人、关联、活动记录、工时 | 94 |
| `code` | 💻 代码管理 | 代码仓库、分支、提交、提交引用、拉取请求、代码评审、托管平台 | 44 |
| `test` | 🧪 测试管理 | 测试库、用例、用例执行、执行用例配置、测试管理、测试配置中心 | 70 |
| `release` | 🚀 交付与发布 | 构建记录、部署记录、发布版本、环境管理 | 42 |
| `plan` | 📅 计划管理 | 迭代、计划、路线图 | 34 |
| `wiki` | 📚 知识库与文档 | 知识空间、页面、评论、附件 | 21 |
| `project` | ⚙️ 项目管理 | 项目、项目看板、项目配置 | 45 |
| `project_config` | 🔧 项目配置中心 | 工作项/工单/用例/测试 字段、状态、类型配置，自定义实体 | 75 |

## 模块详细入口

### 🔑 认证与鉴权 (`auth/`)

企业令牌获取、用户授权码流程

- 用法: 读取 `auth/SKILL.md`
- API 详情: 读取 `auth/APIs.md`
- 接口数量: 6

### 🏢 组织管理 (`org/`)

企业信息、成员、部门、团队、角色、职位、安全日志、全局配置

- 用法: 读取 `org/SKILL.md`
- API 详情: 读取 `org/APIs.md`
- 接口数量: 50

### 📦 产品管理 (`product/`)

产品、产品成员、工单、客户、外部用户、标签、模块

- 用法: 读取 `product/SKILL.md`
- API 详情: 读取 `product/APIs.md`
- 接口数量: 85

### 📋 工作项 (`workitem/`)

需求、任务、缺陷、迭代工作项、评论、附件、关注人、关联、活动记录、工时

- 用法: 读取 `workitem/SKILL.md`
- API 详情: 读取 `workitem/APIs.md`
- 接口数量: 94

### 💻 代码管理 (`code/`)

代码仓库、分支、提交、提交引用、拉取请求、代码评审、托管平台

- 用法: 读取 `code/SKILL.md`
- API 详情: 读取 `code/APIs.md`
- 接口数量: 44

### 🧪 测试管理 (`test/`)

测试库、用例、用例执行、执行用例配置、测试管理、测试配置中心

- 用法: 读取 `test/SKILL.md`
- API 详情: 读取 `test/APIs.md`
- 接口数量: 70

### 🚀 交付与发布 (`release/`)

构建记录、部署记录、发布版本、环境管理

- 用法: 读取 `release/SKILL.md`
- API 详情: 读取 `release/APIs.md`
- 接口数量: 42

### 📅 计划管理 (`plan/`)

迭代、计划、路线图

- 用法: 读取 `plan/SKILL.md`
- API 详情: 读取 `plan/APIs.md`
- 接口数量: 34

### 📚 知识库与文档 (`wiki/`)

知识空间、页面、评论、附件

- 用法: 读取 `wiki/SKILL.md`
- API 详情: 读取 `wiki/APIs.md`
- 接口数量: 21

### ⚙️ 项目管理 (`project/`)

项目、项目看板、项目配置

- 用法: 读取 `project/SKILL.md`
- API 详情: 读取 `project/APIs.md`
- 接口数量: 45

### 🔧 项目配置中心 (`project_config/`)

工作项/工单/用例/测试 字段、状态、类型配置，自定义实体

- 用法: 读取 `project_config/SKILL.md`
- API 详情: 读取 `project_config/APIs.md`
- 接口数量: 75

## 工作流示例

完整的工作流编排示例见 `workflow/` 目录，包含：

- **需求实现回写**: 读取需求 → 实现 → 回写评论 → 更新状态
- **批量操作**: 批量更新工作项、批量创建记录
- **跨模块联动**: 代码提交关联工作项、部署关联发布版本

## 注意事项

- 所有时间字段使用 **10 位 Unix 时间戳**（秒级）
- 分页默认每页 30 条，最大 100 条
- 请求/响应均为 JSON 格式
- 遵循标准 HTTP 状态码约定
