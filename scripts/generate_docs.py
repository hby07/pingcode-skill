#!/usr/bin/env python3
"""
PingCode API 文档生成器
从 api_data.js 重新生成各模块的 SKILL.md 和 APIs.md

用法:
    python3 generate_docs.py <api_data.js> [--output <skill_dir>]

api_data.js 可从 https://open.pingcode.com/ 页面获取（开发者工具 Network 面板）
"""

import json
import os
import re
import sys

# ── Module mapping ──────────────────────────────────────────────────
MODULE_MAP = {
    "auth": {
        "emoji": "🔑", "name": "认证与鉴权",
        "desc": "企业令牌获取、用户授权码流程",
        "groups": ["鉴权", "客户端凭据", "授权码"],
    },
    "org": {
        "emoji": "🏢", "name": "组织管理",
        "desc": "企业信息、成员、部门、团队、角色、职位、安全日志、全局配置",
        "groups": ["全局", "个人", "企业", "企业成员", "部门", "团队",
                    "角色", "职位", "安全", "日志", "组织", "概述"],
    },
    "product": {
        "emoji": "📦", "name": "产品管理",
        "desc": "产品、产品成员、工单、客户、外部用户、标签、模块",
        "groups": ["产品", "产品管理", "工单", "工单配置"],
    },
    "workitem": {
        "emoji": "📋", "name": "工作项",
        "desc": "需求、任务、缺陷、迭代工作项、评论、附件、关注人、关联、活动记录、工时",
        "groups": ["工作项", "需求", "需求配置", "评论", "附件", "关注人",
                    "关联", "活动记录", "工时", "评审", "通用"],
    },
    "code": {
        "emoji": "💻", "name": "代码管理",
        "desc": "代码仓库、分支、提交、提交引用、拉取请求、代码评审、托管平台",
        "groups": ["代码仓库", "代码", "代码分支", "提交", "提交引用",
                    "拉取请求", "代码评审", "托管平台", "托管平台用户"],
    },
    "test": {
        "emoji": "🧪", "name": "测试管理",
        "desc": "测试库、用例、用例执行、执行用例配置、测试管理、测试配置中心",
        "groups": ["测试库", "用例", "用例配置", "执行用例配置",
                    "测试管理", "测试配置中心"],
    },
    "release": {
        "emoji": "🚀", "name": "交付与发布",
        "desc": "构建记录、部署记录、发布版本、环境管理",
        "groups": ["交付", "构建", "构建记录", "发布", "环境", "部署"],
    },
    "plan": {
        "emoji": "📅", "name": "计划管理",
        "desc": "迭代、计划、路线图",
        "groups": ["迭代", "计划", "计划配置"],
    },
    "wiki": {
        "emoji": "📚", "name": "知识库与文档",
        "desc": "知识空间、页面、评论、附件",
        "groups": ["知识管理", "空间", "页面", "评论", "附件"],
    },
    "project": {
        "emoji": "⚙️", "name": "项目管理",
        "desc": "项目、项目看板、项目配置",
        "groups": ["项目", "项目管理", "看板", "项目配置"],
    },
    "project_config": {
        "emoji": "🔧", "name": "项目配置中心",
        "desc": "工作项/工单/用例/测试 字段、状态、类型配置，自定义实体",
        "groups": ["项目配置中心", "工作项配置", "CES", "产品配置中心",
                    "DevOps_数据集成", "Storage"],
    },
}


# ── Helpers ─────────────────────────────────────────────────────────
def clean_html(text):
    if not text:
        return ""
    text = re.sub(r"<p>", "", text)
    text = re.sub(r"</p>", "", text)
    text = re.sub(r"<br\s*/?>", " ", text)
    text = re.sub(r"<code>", "`", text)
    text = re.sub(r"</code>", "`", text)
    text = re.sub(r"<strong>", "**", text)
    text = re.sub(r"</strong>", "**", text)
    text = re.sub(r"<[^>]+>", "", text)
    return text.strip()


def api_title(api):
    return (api.get("title") or "").strip() or (api.get("name") or "").strip() or "Untitled"


def render_param_table(fields):
    if not fields:
        return ""
    lines = ["| 参数名 | 类型 | 必填 | 描述 |", "| --- | --- | --- | --- |"]
    for f in fields:
        name = f.get("field", "")
        ftype = f.get("type", "")
        optional = "否" if f.get("optional") else "是"
        desc = clean_html(f.get("description", "")).replace("\n", " ")
        lines.append(f"| `{name}` | {ftype} | {optional} | {desc} |")
    return "\n".join(lines)


def render_return_table(fields):
    if not fields:
        return ""
    lines = ["| 字段名 | 类型 | 描述 |", "| --- | --- | --- |"]
    for f in fields:
        name = f.get("field", "")
        ftype = f.get("type", "")
        desc = clean_html(f.get("description", "")).replace("\n", " ")
        lines.append(f"| `{name}` | {ftype} | {desc} |")
    return "\n".join(lines)


def render_api_block(api, heading_level=3):
    prefix = "#" * heading_level
    title = api_title(api)
    method = api.get("type", "GET").upper()
    url = api.get("url", "")
    desc = clean_html(api.get("description", ""))
    perm = api.get("permission")

    lines = [f"{prefix} `{method}` {title}\n"]
    if url:
        lines.append(f"**路径:** `{url}`\n")
    if desc:
        lines.append(f"{desc}\n")

    params = api.get("parameter", {})
    if params and params.get("fields"):
        for fg, fields in params.get("fields", {}).items():
            if fields:
                lines.append(f"**参数 ({fg}):**\n")
                lines.append(render_param_table(fields))
                lines.append("")

    success = api.get("success", {})
    if success and success.get("fields"):
        for fg, fields in success.get("fields", {}).items():
            if fields:
                lines.append(f"**返回字段 ({fg}):**\n")
                lines.append(render_return_table(fields))
                lines.append("")

    if perm:
        if isinstance(perm, list):
            pstr = ", ".join(p.get("name", str(p)) for p in perm if isinstance(p, dict))
            if pstr:
                lines.append(f"**权限:** {pstr}\n")
        elif isinstance(perm, str):
            lines.append(f"**权限:** {perm}\n")

    lines.append("---\n")
    return "\n".join(lines)


def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(content)
    rel = os.path.relpath(path, os.path.dirname(os.path.dirname(path)))
    print(f"  ✅ {rel}")


# ── Main ────────────────────────────────────────────────────────────
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 generate_docs.py <api_data.js> [--output <skill_dir>]")
        sys.exit(1)

    api_data_file = sys.argv[1]
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
    if "--output" in sys.argv:
        idx = sys.argv.index("--output")
        if idx + 1 < len(sys.argv):
            output_dir = sys.argv[idx + 1]

    # Load data
    with open(api_data_file, "r") as f:
        content = f.read()
    if content.startswith("define("):
        content = content[content.index("(") + 1 : content.rindex(")")]
    apis = json.loads(content)["api"]

    # Group APIs
    module_apis = {m: [] for m in MODULE_MAP}
    for api in apis:
        g = api.get("group", "未分类")
        for mod_id, mod_cfg in MODULE_MAP.items():
            if g in mod_cfg["groups"]:
                module_apis[mod_id].append(api)
                break

    # Generate each module
    for mod_id, mod_cfg in MODULE_MAP.items():
        mod_dir = os.path.join(output_dir, mod_id)
        mod_apis = module_apis[mod_id]

        # SKILL.md
        skill_md = f"""---
name: pingcode-{mod_id}
description: "{mod_cfg['desc']} — {mod_cfg['name']} 相关的 PingCode REST API。需要查看具体接口参数时读取本目录 APIs.md。"
metadata:
  qwenpaw:
    emoji: "{mod_cfg['emoji']}"
    requires:
      bins: ["python3"]
      env: ["PINGCODE_CLIENT_ID", "PINGCODE_CLIENT_SECRET"]
---

# {mod_cfg['emoji']} PingCode {mod_cfg['name']}

## 概述

{mod_cfg['desc']}

本模块包含 **{len(mod_apis)}** 个 API 接口。

## 认证

从环境变量获取（与主模块共用）：

| 环境变量 | 说明 |
|----------|------|
| `PINGCODE_CLIENT_ID` | 应用 Client ID |
| `PINGCODE_CLIENT_SECRET` | 应用 Client Secret |
| `PINGCODE_BASE_URL` | API 根地址（可选，默认 `https://open.pingcode.com`）|

## 调用方式

```bash
python3 {{{{baseDir}}}}/../scripts/pingcode.py '{{{{"method":"GET","path":"/v1/myself"}}}}'
```

## 本模块 API 列表

| 方法 | 路径 | 说明 |
|------|------|------|
"""
        for api in mod_apis:
            method = api.get("type", "GET").upper()
            url = api.get("url", "")
            title = api_title(api)
            skill_md += f"| `{method}` | `{url}` | {title} |\n"

        skill_md += "\n## 详细参数\n\n如需查看某个接口的完整参数表，请阅读本目录的 **`APIs.md`**。\n"
        write(os.path.join(mod_dir, "SKILL.md"), skill_md)

        # APIs.md
        apis_md = f"# {mod_cfg['emoji']} {mod_cfg['name']} — API 详细文档\n\n> 本文档包含 {len(mod_apis)} 个接口的完整参数说明。\n> 来源: https://open.pingcode.com/\n\n---\n\n"
        sub_groups = {}
        for api in mod_apis:
            sg = api.get("group", "其他")
            sub_groups.setdefault(sg, []).append(api)
        for sg_name, sg_apis in sub_groups.items():
            gt = sg_apis[0].get("groupTitle", sg_name) if sg_apis else sg_name
            apis_md += f"## {gt}\n\n"
            for api in sg_apis:
                apis_md += render_api_block(api, heading_level=3)
        write(os.path.join(mod_dir, "APIs.md"), apis_md)

    print(f"\n✅ Generated {len(MODULE_MAP)} modules ({len(apis)} APIs)")


if __name__ == "__main__":
    main()
