# 🔄 PingCode 工作流示例

## 流程一：需求实现 → 结果回写

这是最核心的工作流：Agent 从 PingCode 读取需求，实现后回写结果。

### Step 1: 获取产品列表（product/）

```bash
python3 {baseDir}/../scripts/pingcode.py '{"method":"GET","path":"/v1/ship/products","params":{"page":1,"size":20}}'
```

### Step 2: 获取需求列表（workitem/）

```bash
python3 {baseDir}/../scripts/pingcode.py '{"method":"GET","path":"/v1/ship/products/{product_id}/work_items","params":{"page":1,"size":20}}'
```

### Step 3: 获取需求详情（workitem/）

```bash
python3 {baseDir}/../scripts/pingcode.py '{"method":"GET","path":"/v1/ship/work_items/{work_item_id}"}'
```

### Step 4: Agent 实现需求

根据需求描述，使用自身能力完成开发任务。

### Step 5: 回写评论（workitem/）

```bash
python3 {baseDir}/../scripts/pingcode.py '{"method":"POST","path":"/v1/ship/work_items/{work_item_id}/comments","body":{"content":"已实现需求，代码已提交到分支 feature/xxx"}}'
```

### Step 6: 上传附件（workitem/）

```bash
python3 {baseDir}/../scripts/pingcode.py '{"method":"POST","path":"/v1/ship/work_items/{work_item_id}/attachments","body":{...}}'
```

### Step 7: 更新状态（workitem/）

```bash
python3 {baseDir}/../scripts/pingcode.py '{"method":"PATCH","path":"/v1/ship/work_items/{work_item_id}","body":{"status":"已完成"}}'
```

---

## 流程二：代码提交关联工作项

### Step 1: 创建分支（code/）

```bash
python3 {baseDir}/../scripts/pingcode.py '{"method":"POST","path":"/v1/ship/products/{product_id}/repositories/{repo_id}/branches","body":{"name":"feature/work-item-xxx","ref":"main"}}'
```

### Step 2: 关联提交引用（code/）

```bash
python3 {baseDir}/../scripts/pingcode.py '{"method":"POST","path":"/v1/ship/work_items/{work_item_id}/commit_references","body":{"commit_sha":"abc123","repository_id":"xxx"}}'
```

### Step 3: 创建拉取请求（code/）

```bash
python3 {baseDir}/../scripts/pingcode.py '{"method":"POST","path":"/v1/ship/products/{product_id}/repositories/{repo_id}/pull_requests","body":{"title":"feat: xxx","head_branch":"feature/xxx","base_branch":"main"}}'
```

---

## 流程三：部署与发布

### Step 1: 获取环境列表（release/）

```bash
python3 {baseDir}/../scripts/pingcode.py '{"method":"GET","path":"/v1/release/environments","params":{"product_id":"xxx"}}'
```

### Step 2: 获取构建记录（release/）

```bash
python3 {baseDir}/../scripts/pingcode.py '{"method":"GET","path":"/v1/release/products/{product_id}/builds","params":{"page":1,"size":10}}'
```

### Step 3: 创建部署记录（release/）

```bash
python3 {baseDir}/../scripts/pingcode.py '{"method":"POST","path":"/v1/release/products/{product_id}/deployments","body":{"build_id":"xxx","environment_id":"xxx"}}'
```

### Step 4: 创建发布版本（release/）

```bash
python3 {baseDir}/../scripts/pingcode.py '{"method":"POST","path":"/v1/release/products/{product_id}/releases","body":{"name":"v1.0.0","description":"首次发布"}}'
```

---

## 流程四：批量操作

### 批量更新工作项属性（workitem/）

```bash
python3 {baseDir}/../scripts/pingcode.py '{"method":"POST","path":"/v1/ship/work_items/bulk","body":{"work_item_ids":["id1","id2"],"properties":{"status":"已完成"}}}'
```

### 批量获取（通用）

```bash
python3 {baseDir}/../scripts/pingcode.py '{"method":"GET","path":"/v1/ship/work_items","params":{"product_id":"xxx","ids":"id1,id2,id3"}}'
```

---

## 注意事项

1. **令牌自动管理**: 脚本自动获取和刷新企业令牌，无需手动处理
2. **分页处理**: 默认每页 30 条，最大 100 条，注意翻页获取全量数据
3. **错误处理**: 脚本返回 JSON，包含 `code` 和 `error` 字段
4. **速率限制**: 注意 `X-RateLimit-Remaining` 响应头，避免触发限流
