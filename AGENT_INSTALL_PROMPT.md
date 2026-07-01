# Agent 自动安装提示词

将以下提示词复制并发送给你的 AI Agent，它会自动完成安装。

---

## 完整安装提示词

```
请帮我安装 pingcode-skill，这是一个 PingCode REST API 的 skill 封装。

安装步骤：
1. 克隆仓库：git clone https://github.com/hby07/pingcode-skill.git /tmp/pingcode-skill
2. 检测当前 agent 类型并确定安装目录：
   - 如果是 OpenCode：安装到 .opencode/skills/pingcode（项目级）或 ~/.config/opencode/skills/pingcode（全局）
   - 如果是 Claude Code：安装到 .claude/skills/pingcode（项目级）或 ~/.claude/skills/pingcode（全局）
   - 如果是 QwenPaw：安装到 ~/.qwenpaw/workspaces/<agent_id>/skills/pingcode
   - 如果是其他 Agent：安装到 .agents/skills/pingcode（项目级）或 ~/.agents/skills/pingcode（全局）
3. 复制 skill 目录到目标位置（保留原始仓库以便更新）
4. 检查并配置环境变量：
   - PINGCODE_CLIENT_ID（必需）
   - PINGCODE_CLIENT_SECRET（必需）
   - 如果未配置，提示用户设置
5. 验证安装：
   - 检查 SKILL.md 文件是否存在
   - 测试 API 连通性（调用 /v1/myself）
6. 告诉用户安装结果和下一步操作
```

---

## 最小安装提示词

```
安装 pingcode-skill：git clone https://github.com/hby07/pingcode-skill.git，然后按 INSTALL.md 说明安装到当前 agent 的 skills 目录。
```

---

## 仅安装（不含配置）

```
将 https://github.com/hby07/pingcode-skill 克隆到临时目录，然后复制到当前 agent 的 skills 目录。不需要配置环境变量。
```

---

## 验证安装提示词

```
验证 pingcode skill 是否安装成功：
1. 检查 skills 目录下是否有 pingcode 目录
2. 检查 SKILL.md 文件是否存在
3. 如果环境变量已配置，测试 API 连通性
```

---

## 卸载提示词

```
卸载 pingcode skill：
1. 删除 skills 目录下的 pingcode 目录
2. 清理相关的环境变量配置（如果需要）
```

---

## 使用说明

1. **选择合适的提示词**：根据你的需求选择完整版或最小版
2. **复制并粘贴**：将提示词发送给你的 AI Agent
3. **跟随指引**：Agent 会自动执行安装步骤
4. **配置凭据**：如果 Agent 提示需要配置环境变量，请按指引操作
5. **验证安装**：安装完成后，测试 API 连通性

---

## 注意事项

- 安装过程需要网络连接（克隆 GitHub 仓库）
- 需要 git 命令行工具
- 需要 Python 3（用于便捷脚本，可选）
- 环境变量配置是必需的（用于 API 认证）
