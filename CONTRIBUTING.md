# 贡献指南

感谢你对 PingCode Skill 的关注！

## 如何贡献

### 报告问题

在 [Issues](../../issues) 中提交 Bug 报告，请包含：

- 问题描述
- 复现步骤
- 期望行为 vs 实际行为
- 你的环境（OS、Python 版本、Agent 类型）

### 提交 PR

1. Fork 本仓库
2. 创建特性分支：`git checkout -b feature/your-feature`
3. 修改代码
4. 测试通过
5. 提交：`git commit -m 'feat: add xxx'`
6. 推送：`git push origin feature/your-feature`
7. 创建 Pull Request

### PR 规范

- 标题格式：`feat:` / `fix:` / `docs:` / `refactor:` / `test:`
- 一个 PR 只做一件事
- 更新相关文档

## 项目结构

```
├── SKILL.md              # 路由入口（勿轻易修改）
├── scripts/
│   ├── pingcode.py       # 通用调用脚本
│   └── .env.example      # 凭据模板
├── <module>/
│   ├── SKILL.md          # 模块说明
│   └── APIs.md           # API 详细文档
└── workflow/
    └── apis.md           # 工作流示例
```

## 开发指南

### 添加新模块

1. 创建 `<module>/SKILL.md` 和 `<module>/APIs.md`
2. 在顶层 `SKILL.md` 的模块索引中添加条目
3. 在 `scripts/pingcode.py` 中无需修改（通用脚本）

### 更新 API 文档

如果有 PingCode API 更新，可以用以下脚本重新生成：

```bash
# 需要先下载最新的 api_data.js
# 从 https://open.pingcode.com/ 页面获取
python3 scripts/generate_docs.py api_data.js
```

### 修改通用脚本

`scripts/pingcode.py` 是所有模块共用的调用脚本，修改时请注意：

- 保持向后兼容
- 不要引入第三方依赖（保持零依赖）
- 错误信息要清晰

## 代码风格

- Python 3.10+ 语法
- 类型注解
- 清晰的函数文档
- 错误处理完善

## 问题反馈

- GitHub Issues: [提交 Issue](../../issues)
- 邮件: （请在 PR 中留下联系方式）

再次感谢你的贡献！🎉
