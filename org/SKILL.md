---
name: pingcode-org
description: "Use when managing PingCode organization structure: members, departments, teams, roles, positions, or security logs."
metadata:
  qwenpaw:
    emoji: "🏢"
    requires:
      env: ["PINGCODE_CLIENT_ID", "PINGCODE_CLIENT_SECRET"]
---

# 🏢 组织管理

企业、成员、部门、团队、角色、职位、安全日志。本模块包含 **50** 个 API。

## 快速调用

```bash
curl -s -H "Authorization: Bearer $TOKEN" "https://open.pingcode.com/v1/myself"
curl -s -H "Authorization: Bearer $TOKEN" "https://open.pingcode.com/v1/departments"
```

## ⚠️ 注意事项

- 部门/团队有层级结构，获取全部时留意 `parent_id` 参数
- 成员状态（active/inactive）筛选通过查询参数 `status` 控制

## 本模块 API 列表

| 方法 | 路径 | 说明 |
|------|------|------|
| `GET` | `/v1/myself` | 获取当前用户 |
| `GET` | `/v1/departments` | 获取部门列表 |
| `POST` | `/v1/departments` | 创建部门 |
| `GET` | `/v1/departments/{dept_id}` | 获取部门详情 |
| `PATCH` | `/v1/departments/{dept_id}` | 更新部门 |
| `DELETE` | `/v1/departments/{dept_id}` | 删除部门 |
| `GET` | `/v1/departments/{dept_id}/members` | 部门成员列表 |
| `POST` | `/v1/departments/{dept_id}/members` | 添加部门成员 |
| `DELETE` | `/v1/departments/{dept_id}/members/{member_id}` | 移除部门成员 |
| … | … | 共 50 个接口，详见 `APIs.md` |

完整参数表、请求体、返回字段见 `APIs.md`。