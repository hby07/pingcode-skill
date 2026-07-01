# 工作流模块

> 让 Agent 按照规范的工作流程与用户协作，而非自动执行。

---

## 概述

本模块定义了 Agent 与用户协作的各种工作流程。所有工作流遵循 `interactive_framework.md` 中的交互式原则。

**核心理念：** Agent 是协作者，不是执行者。每个关键步骤都需要用户确认。

---

## 工作流选择指南

根据用户意图，选择对应的工作流：

| 用户意图 | 工作流 | 入口文件 |
|----------|--------|----------|
| "帮我做 Sprint 计划" | Sprint 计划 | `scrum/sprint_planning.md` |
| "开始开发任务" | 每日开发 | `scrum/daily_development.md` |
| "生成文档" | 文档生成 | `documentation/generation_guide.md` |
| "帮我设计产品" | 产品设计 | `design/brainstorming.md` |
| "做代码审查" | 代码审查 | `devops/code_review.md` |
| "管理缺陷" | 缺陷分诊 | `scrum/bug_triage.md` |
| "准备发布" | 发布管理 | `devops/release_management.md` |
| "生成报告" | 项目度量 | `scrum/metrics_report.md` |

---

## 工作流分类

### 📋 项目管理类

- `scrum/sprint_planning.md` — Sprint 计划会议
- `scrum/daily_development.md` — 每日开发流程
- `scrum/bug_triage.md` — 缺陷分诊
- `scrum/metrics_report.md` — 项目度量报告
- `kanban/board_setup.md` — 看板设置

### 📄 文档生成类

- `documentation/generation_guide.md` — 文档生成指南
- `documentation/templates/` — 文档模板目录

### 🎨 产品设计类

- `design/brainstorming.md` — 头脑风暴引导
- `design/user_story_mapping.md` — 用户故事地图
- `design/prd_generation.md` — PRD 生成

### 🔧 DevOps 类

- `devops/code_review.md` — 代码审查流程
- `devops/release_management.md` — 发布管理流程

---

## 工作流启动流程

```
1. 读取用户意图
   ↓
2. 匹配工作流类型
   ↓
3. 读取对应工作流文档
   ↓
4. 展示工作流步骤
   ↓
5. 用户确认开始
   ↓
6. 按步骤执行（每步确认）
   ↓
7. 完成并汇报
```

---

## 注意事项

- 所有工作流都基于 `interactive_framework.md` 的交互原则
- 任何写入操作都需要用户确认
- 用户可随时输入「取消」终止工作流
- 工作流状态会保存，支持中断后恢复
