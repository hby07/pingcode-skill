# 工作流模块

> 让 Agent 按照规范的工作流程与用户协作，而非自动执行。

---

## 概述

本模块定义了 Agent 与用户协作的各种工作流程。所有工作流遵循 `interactive_framework.md` 中的交互式原则。

**核心理念：** Agent 是协作者，不是执行者。每个关键步骤都需要用户确认。

---

## ⚠️ 核心流程原则

### 文档优先，写入在后

**正确流程：**
```
用户想法 → 写文档到 PingCode Wiki → 人工审核 → 创建正式需求/任务到 PingCode
```

**错误流程：**
```
用户想法 → 直接在 PingCode 创建需求/任务（❌ 跳过文档审核）
```

**为什么？**
- 文档是团队理解需求的基础
- 审核环节可以发现遗漏和问题
- 正式需求应该基于已审核的文档

### 写入 PingCode 的两种类型

| 类型 | 目的 | 时机 |
|------|------|------|
| **Wiki 文档** | 供团队阅读和审核 | 随时可以创建 |
| **工作项（需求/任务）** | 正式的需求管理 | 文档审核通过后创建 |

### 必须遵循产品开发生命周期

**所有工作流必须遵循 `LIFECYCLE.md` 中定义的产品开发生命周期，不得跳过阶段。**

完整流程：
```
Phase 1: 产品设计（PRD）→ Phase 2: 技术设计 → Phase 3: 任务拆解 → Phase 4: 开发 → Phase 5: 测试 → Phase 6: 发布
```

---

## 工作流选择指南

根据用户意图，选择对应的工作流：

| 用户意图 | 工作流 | 入口文件 |
|----------|--------|----------|
| "帮我设计产品" | 产品设计 | `design/brainstorming.md` |
| "写技术设计" | 技术设计 | `design/technical_design.md` |
| "帮我做 Sprint 计划" | Sprint 计划 | `scrum/sprint_planning.md` |
| "开始开发任务" | 每日开发 | `scrum/daily_development.md` |
| "做代码审查" | 代码审查 | `devops/code_review.md` |
| "管理缺陷" | 缺陷分诊 | `scrum/bug_triage.md` |
| "准备发布" | 发布管理 | `devops/release_management.md` |
| "生成文档" | 文档生成 | `documentation/generation_guide.md` |
| "生成报告" | 项目度量 | `scrum/metrics_report.md` |

---

## 工作流分类

### 🎨 产品设计类

- `design/brainstorming.md` — 头脑风暴与 PRD 生成
- `design/technical_design.md` — 技术设计文档生成

### 📋 项目管理类

- `scrum/sprint_planning.md` — Sprint 计划会议
- `scrum/daily_development.md` — 每日开发流程
- `scrum/bug_triage.md` — 缺陷分诊
- `scrum/metrics_report.md` — 项目度量报告
- `kanban/board_setup.md` — 看板设置

### 📄 文档生成类

- `documentation/generation_guide.md` — 文档生成指南
- `documentation/templates/` — 文档模板目录

### 🔧 DevOps 类

- `devops/code_review.md` — 代码审查流程
- `devops/release_management.md` — 发布管理流程

---

## 工作流启动流程

```
1. 读取用户意图
   ↓
2. 检查前置条件（参考 LIFECYCLE.md）
   ↓
3. 匹配工作流类型
   ↓
4. 读取对应工作流文档
   ↓
5. 展示工作流步骤
   ↓
6. 用户确认开始
   ↓
7. 按步骤执行（每步确认）
   ↓
8. 完成并引导进入下一阶段
```

---

## 注意事项

- 所有工作流都基于 `interactive_framework.md` 的交互原则
- 所有工作流必须遵循 `LIFECYCLE.md` 的生命周期
- 任何写入操作都需要用户确认
- 用户可随时输入「取消」终止工作流
- 工作流状态会保存，支持中断后恢复
- 每个阶段完成后，必须引导用户进入下一阶段
