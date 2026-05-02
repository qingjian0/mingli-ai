# "明理"AI命理平台 - Cloudflare Pages 部署指南

## 部署架构

我们将采用以下架构部署到 Cloudflare：

```
前端: Cloudflare Pages
后端: Cloudflare Workers + Workers KV (可选)
数据: Cloudflare R2 (可选)
```

---

## 第一部分：前端部署到 Cloudflare Pages

### 步骤 1：准备部署配置

首先，检查前端项目配置：

1. **构建输出目录**：`mingli-frontend/dist/` (已存在)
2. **构建命令**：`npm run build`
3. **部署目录**：`mingli-frontend/dist/`

### 步骤 2：在 Cloudflare Dashboard 上操作

登录到您的 Cloudflare 账户：
https://dash.cloudflare.com/b009d274cb9dc02032faf28b57926c4a/home/overview

#### 创建 Pages 项目

1. **进入 Workers & Pages**
   - 在左侧菜单点击 "Workers & Pages"
   - 点击 "Create application"
   - 选择 "Pages" 选项卡
   - 点击 "Upload assets" 或 "Connect to Git"

#### 方案 A：使用 Git 连接（推荐）

如果您的代码已经在 Git 上：

1. 点击 "Connect to Git"
2. 选择您的仓库
3. 配置部署设置：
   ```
   Project name: mingli-frontend
   Framework preset: Vite
   Build command: npm run build
   Build output directory: dist
   Root directory: mingli-frontend
   ```
4. 点击 "Save and Deploy"

#### 方案 B：直接上传

如果您想直接上传构建文件：

1. 点击 "Upload assets"
2. 创建项目名称：`mingli-frontend`
3. 将 `mingli-frontend/dist/` 目录下的所有文件拖拽上传
4. 点击 "Deploy site"

---

### 步骤 3：配置部署文件

我们来创建 Cloudflare Pages 所需的配置文件：

#### _headers 文件

配置安全头和缓存策略：

```
/*
  X-Frame-Options: DENY
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; font-src 'self';
  Permissions-Policy: accelerometer=(), autoplay=(), camera=(), encrypted-media=(), fullscreen=(), geolocation=(), gyroscope=(), magnetometer=(), microphone=(), midi=(), payment=(), usb=()

/assets/*
  Cache-Control: public, max-age=31536000, immutable

/index.html
  Cache-Control: public, max-age=0, must-revalidate
```

#### _redirects 文件

配置 SPA 路由：

```
/* /index.html 200
```

让我创建这些文件：
