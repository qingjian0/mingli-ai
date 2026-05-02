# 🚀 明理 AI 命理平台 - 部署总指南

**基于求是思想 - 具体问题具体分析**

---

## 📊 部署状态总览

| 任务 | 状态 | 详情 |
|------|------|------|
| ✅ GitHub 上传 | 已完成 | https://github.com/qingjian0/mingli-ai |
| ✅ 前端构建 | 已完成 | mingli-frontend/dist/ |
| ✅ 部署脚本 | 已完成 | deploy-cf-pages.sh, deploy-backend.sh |
| ⏳ Cloudflare Pages | 待完成 | 详见下文 |
| ⏳ 后端部署 | 待完成 | 详见下文 |

---

## 🎯 方案一：前端部署 (Cloudflare Pages) - 5 分钟

### 快速开始 (手动上传)

这是最简单的方式！

#### 步骤 1: 访问 Cloudflare

```
https://dash.cloudflare.com/b009d274cb9dc02032faf28b57926c4a/workers-and-pages
```

#### 步骤 2: 创建项目

1. 点击 **Create application**
2. 选择 **Pages** 标签
3. 点击 **Upload assets**
4. 项目名输入: `mingli-frontend`
5. 点击 **Create project**

#### 步骤 3: 上传文件

- 上传整个目录: `mingli-frontend/dist/`
- 等待上传完成 (通常 < 1 分钟)
- 点击 **Deploy site**

#### 步骤 4: 访问您的应用！

- Cloudflare 会分配类似: `mingli-frontend.pages.dev`
- 立即访问！

---

## 🎯 方案二：后端部署 (Render) - 10 分钟

### 使用 Render (推荐 - 有免费额度)

#### 步骤 1: 登录 Render

```
https://render.com
```

#### 步骤 2: 连接 GitHub 仓库

1. 点击 **New** → **Web Service**
2. 选择您的仓库 `mingli-ai`
3. 选择分支 `main`

#### 步骤 3: 配置部署

| 配置项 | 值 |
|---------|-----|
| **Name** | `mingli-backend` |
| **Runtime** | Python 3 |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `uvicorn app.main:app --host 0.0.0.0 --port $PORT` |
| **Plan** | Free |

点击 **Create Web Service**

#### 步骤 4: 等待部署完成！

部署成功后您会获得类似:
`https://mingli-backend.onrender.com`

---

## 🎯 使用部署脚本

### 方式 A: 使用提供的脚本

```bash
# 部署前端
./deploy-cf-pages.sh

# 部署后端
./deploy-backend.sh
```

### 方式 B: 手动操作

#### 前端手动部署

```bash
# 1. 确认前端已构建
cd mingli-frontend
npm run build
cp _headers _redirects dist/

# 2. 访问 Cloudflare 上传
# https://dash.cloudflare.com/...
```

#### 后端手动部署

```bash
# 1. 检查后端
cd mingli-backend

# 2. 在 Render 中配置部署
# 构建命令: pip install -r requirements.txt
# 启动命令: uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

---

## 📁 部署文件说明

### 前端部署包 (mingli-frontend/dist/)

```
dist/
├── index.html              # 入口页面
├── assets/
│   ├── index-XXX.js       # 应用逻辑 (157 KB)
│   └── index-XXX.css      # 样式 (39 KB)
├── _headers                # Cloudflare 安全配置
├── _redirects              # SPA 路由配置
└── vite.svg               # 图标
```

### 后端配置文件

已生成的部署配置:

| 文件 | 平台 | 说明 |
|------|------|------|
| render.yaml | Render | 一键部署配置 |
| fly.toml | Fly.io | Fly 配置 |
| Procfile | Heroku | Heroku 配置 |
| railway.json | Railway | Railway 配置 |

---

## 🔗 前后端连接

部署后配置 API 连接:

### 如果前端需要连接后端

1. 找到后端地址 (如: `https://mingli-backend.onrender.com`)
2. 在前端设置环境变量:
   ```env
   VITE_API_URL=https://mingli-backend.onrender.com
   ```
3. 重新构建前端: `npm run build`

---

## 🎉 完整部署检查清单

- [ ] 前端已构建: `mingli-frontend/dist/`
- [ ] 前端已部署到 Cloudflare Pages
- [ ] 后端已部署到 Render/Fly.io/Railway
- [ ] 前后端可以正常通信
- [ ] 测试核心功能正常
- [ ] HTTPS 正常工作
- [ ] 域名已配置（可选）

---

## 📞 获取帮助

- GitHub Issues: https://github.com/qingjian0/mingli-ai/issues
- Render 文档: https://render.com/docs
- Cloudflare Pages: https://developers.cloudflare.com/pages

---

**基于求是思想，祝您部署顺利！** 🚀
