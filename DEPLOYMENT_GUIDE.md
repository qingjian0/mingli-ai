# "明理"AI命理平台 - 部署方案

## 部署架构选择

### 方案一：Cloudflare Pages + Cloudflare Workers（推荐）

```
┌─────────────────────────────────────────────┐
│           Cloudflare Pages (前端)            │
│       mingli-frontend.pages.dev             │
│         (React + Vite)                      │
└──────────────┬──────────────────────────────┘
               │ /api/*
               ▼
┌─────────────────────────────────────────────┐
│         Cloudflare Workers (后端)           │
│      mingli-backend.workers.dev             │
│       (FastAPI → Hono.js)                   │
└─────────────────────────────────────────────┘
```

### 方案二：Cloudflare Pages + 外部后端服务

```
前端: Cloudflare Pages
后端: 其他平台 (Render/Vercel/AWS/阿里云)
```

---

## 快速部署：方案一（完整 Cloudflare 栈）

### 前置准备

1. **安装 Wrangler CLI**
   ```bash
   npm install -g wrangler
   wrangler login
   ```

2. **前端部署到 Cloudflare Pages**

   #### 方式 A：使用 Cloudflare Dashboard
   - 访问: https://dash.cloudflare.com/b009d274cb9dc02032faf28b57926c4a/workers-and-pages/create/pages
   - 点击 "Upload assets"
   - 创建项目名称：`mingli-frontend`
   - 上传 `mingli-frontend/dist/` 目录下的所有文件

   #### 方式 B：使用 Wrangler CLI
   ```bash
   cd /workspace/mingli-frontend
   npm install
   npm run build
   
   # 部署到 Cloudflare Pages
   wrangler pages project create mingli-frontend --production-branch main
   wrangler pages deploy dist --project-name mingli-frontend
   ```

---

## 3. 后端部署方案

### 方案 A：使用 Cloudflare Workers + Hono.js（推荐）

由于我们当前有 Python FastAPI，我们有两个选择：

#### A1：将 Python 代码转换为 JavaScript/TypeScript（Hono.js）
创建一个简化的 API 版本：

```typescript
import { Hono } from 'hono';
import { cors } from 'hono/cors';

const app = new Hono();

app.use('/*', cors());

app.get('/', (c) => c.text('"明理"AI命理平台 API'));
app.get('/health', (c) => c.json({ status: 'ok' }));

app.post('/api/v1/chart/ziwei', async (c) => {
  // 紫微斗数排盘逻辑
  return c.json({ success: true });
});

export default app;
```

#### A2：使用 Python 部署到其他平台（如 Render）

```bash
# 使用 Render 部署后端
# 1. 访问 https://render.com/
# 2. 连接 GitHub 仓库
# 3. 配置：
#    - Build Command: pip install -r requirements.txt
#    - Start Command: uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

---

## 4. 验证部署

### 检查前端
访问你的部署 URL：
- `https://mingli-frontend.pages.dev`

### 检查 API（如果部署）
访问你的 API URL：
- `https://mingli-backend.workers.dev/health`

---

## 5. 配置自定义域名（可选）

1. 在 Cloudflare 中购买或添加你的域名
2. 在 Pages 项目设置中：
   - Settings → Custom domains
   - 点击 "Set up a custom domain"
3. 输入你的域名，如 `mingli.yourdomain.com`
4. Cloudflare 会自动配置 DNS 记录

---

## 部署检查清单

- [ ] 前端构建成功 (`npm run build`)
- [ ] `_headers` 文件已创建
- [ ] `_redirects` 文件已创建
- [ ] 部署到 Cloudflare Pages
- [ ] 检查网站可以访问
- [ ] 配置后端 API
- [ ] 测试前后端连接

---

## 故障排查

### 问题：页面刷新显示 404
**解决**：确认 `_redirects` 文件内容正确：
```
/* /index.html 200
```

### 问题：API 请求失败
**解决**：检查 CORS 配置和 API 端点

### 问题：样式丢失
**解决**：确认 `_headers` 文件存在并正确配置缓存
