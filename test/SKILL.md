---
name: pingcode-test
description: "Use when managing PingCode test cases: test libraries, test cases, test executions, execution configurations, or test center settings."
metadata:
  qwenpaw:
    emoji: "🧪"
    requires:
      env: ["PINGCODE_CLIENT_ID", "PINGCODE_CLIENT_SECRET"]
---

# 🧪 测试管理

测试库、用例、用例执行、执行用例配置、测试中心配置。本模块包含 **70** 个 API。

## 快速调用

```bash
curl -s -H "Authorization: Bearer $TOKEN" "https://open.pingcode.com/v1/test/test_libraries"
```

## 本模块 API 列表

| 方法 | 路径 | 说明 |
|------|------|------|
| `GET` | `/v1/test/test_libraries` | 获取测试库列表 |
| `GET` | `/v1/test/test_cases` | 获取用例列表 |
| `POST` | `/v1/test/test_cases` | 创建用例 |
| `POST` | `/v1/test/test_executions` | 创建执行 |
| … | … | 共 70 个接口，详见 `APIs.md` |

完整参数表见 `APIs.md`。