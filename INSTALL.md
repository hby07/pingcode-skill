# PingCode Skill 安装指南

## 🚀 快速安装（推荐）

### 方法一：Agent 自动安装（最简单）

将以下提示词发送给你的 AI Agent，它会自动完成安装：

```
请帮我安装 pingcode-skill：
1. 从 https://github.com/hby07/pingcode-skill 克隆仓库
2. 检测当前 agent 类型（OpenCode / Claude Code / QwenPaw / 其他）
3. 将 skill 目录复制到正确的 skills 目录：
   - OpenCode: .opencode/skills/ 或 ~/.config/opencode/skills/
   - Claude Code: .claude/skills/ 或 ~/.claude/skills/
   - QwenPaw: ~/.qwenpaw/workspaces/<agent_id>/skills/
   - 通用: .agents/skills/ 或 ~/.agents/skills/
4. 配置环境变量 PINGCODE_CLIENT_ID 和 PINGCODE_CLIENT_SECRET
5. 验证安装成功（测试 API 连通性）
```

### 方法二：手动安装

#### 步骤 1：克隆仓库

```bash
git clone https://github.com/hby07/pingcode-skill.git
cd pingcode-skill
```

#### 步骤 2：根据你的 Agent 选择安装位置

---

## 📦 各 Agent 安装方式

### OpenCode

**项目级安装（推荐）：**
```bash
# 复制到项目目录
cp -r pingcode-skill .opencode/skills/pingcode

# 或者创建符号链接（推荐，便于更新）
ln -s $(pwd)/pingcode-skill .opencode/skills/pingcode
```

**全局安装：**
```bash
mkdir -p ~/.config/opencode/skills
ln -s $(pwd)/pingcode-skill ~/.config/opencode/skills/pingcode
```

**验证安装：**
```
在 OpenCode 中输入：使用 skill 工具列出所有 skills
应该能看到 pingcode skill
```

---

### Claude Code

**项目级安装：**
```bash
# 复制到 Claude Code 目录
cp -r pingcode-skill .claude/skills/pingcode

# 或创建符号链接
ln -s $(pwd)/pingcode-skill .claude/skills/pingcode
```

**全局安装：**
```bash
mkdir -p ~/.claude/skills
ln -s $(pwd)/pingcode-skill ~/.claude/skills/pingcode
```

**验证安装：**
```
在 Claude Code 中输入：/skills
应该能看到 pingcode skill
```

---

### QwenPaw

**工作区安装：**
```bash
# 找到你的 agent 工作区目录
WORKSPACE_DIR=~/.qwenpaw/workspaces/<your_agent_id>

# 复制 skill
cp -r pingcode-skill $WORKSPACE_DIR/skills/pingcode

# 或创建符号链接
ln -s $(pwd)/pingcode-skill $WORKSPACE_DIR/skills/pingcode
```

**验证安装：**
```
在 QwenPaw 中询问：你有哪些 skills？
应该能看到 pingcode skill
```

---

### 通用安装（任何 Agent）

大多数 Agent 都支持以下目录格式：

```bash
# 项目级
mkdir -p .agents/skills
ln -s $(pwd)/pingcode-skill .agents/skills/pingcode

# 全局
mkdir -p ~/.agents/skills
ln -s $(pwd)/pingcode-skill ~/.agents/skills/pingcode
```

---

## 🔑 配置认证

### 环境变量方式

```bash
# 添加到 ~/.bashrc 或 ~/.zshrc
export PINGCODE_CLIENT_ID="your_client_id_here"
export PINGCODE_CLIENT_SECRET="your_client_secret_here"

# 可选：自定义 API 地址
# export PINGCODE_BASE_URL="https://your-custom-domain.com"
```

### .env 文件方式

在 skill 目录下创建 `.env` 文件：

```bash
cd pingcode-skill
cp scripts/.env.example scripts/.env
# 编辑 scripts/.env 填入你的凭据
```

---

## ✅ 验证安装

### 测试 API 连通性

```bash
# 使用 Python 脚本
python3 pingcode-skill/scripts/pingcode.py '{"method":"GET","path":"/v1/myself"}'

# 或使用 curl
curl -H "Authorization: Bearer $TOKEN" https://open.pingcode.com/v1/myself
```

### 在 Agent 中测试

```
请帮我测试 pingcode skill：
1. 获取当前用户信息
2. 列出我参与的项目
3. 查看第一个项目的前 5 个工作项
```

---

## 🔄 更新

### Git 方式（推荐）

```bash
cd pingcode-skill
git pull origin main
```

### 重新安装

```bash
# 删除旧版本
rm -rf .opencode/skills/pingcode  # 或对应目录

# 重新克隆
git clone https://github.com/hby07/pingcode-skill.git
# 按上述步骤重新安装
```

---

## ❓ 常见问题

### Q: 安装后 Agent 找不到 skill？

**A:** 检查目录结构：
```bash
# OpenCode 应该看到
.opencode/skills/pingcode/SKILL.md

# Claude Code 应该看到
.claude/skills/pingcode/SKILL.md
```

### Q: API 调用返回 401 未授权？

**A:** 检查凭据配置：
```bash
echo $PINGCODE_CLIENT_ID
echo $PINGCODE_CLIENT_SECRET
# 确保环境变量已设置且正确
```

### Q: 如何获取 Client ID 和 Secret？

**A:** 
1. 登录 [PingCode 开放平台](https://open.pingcode.com/)
2. 创建应用或使用已有应用
3. 复制 Client ID 和 Client Secret

### Q: 支持哪些 Agent？

**A:** 
- ✅ OpenCode（原生支持）
- ✅ Claude Code（原生支持）
- ✅ QwenPaw（原生支持）
- ✅ 任何支持 skills 目录的 Agent
- ✅ Cursor（通过 .cursorrules 手动配置）

---

## 📁 目录结构说明

```
pingcode-skill/
├── SKILL.md              # 主入口（Agent 读取此文件开始）
├── auth/                 # 认证模块
│   ├── SKILL.md
│   └── APIs.md
├── org/                  # 组织管理
├── product/              # 产品管理
├── workitem/             # 工作项
├── code/                 # 代码管理
├── test/                 # 测试管理
├── release/              # 交付发布
├── plan/                 # 计划管理
├── wiki/                 # 知识库
├── project/              # 项目管理
├── project_config/       # 项目配置
├── scripts/              # 便捷脚本
│   ├── pingcode.py
│   └── .env.example
└── workflow/             # 工作流示例
```

---

## 🤝 贡献

欢迎贡献！请查看 [GitHub 仓库](https://github.com/hby07/pingcode-skill) 了解详情。
