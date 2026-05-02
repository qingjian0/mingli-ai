# "明理"AI命理平台 - 快速部署指南

## 🚀 最快部署方式（推荐）

### 步骤 1：部署前端到 Cloudflare Pages

#### 方式 A：手动上传（5分钟）

1. **打开 Cloudflare Dashboard**
   - 访问: https://dash.cloudflare.com/b009d274cb9dc02032faf28b57926c4a/workers-and-pages

2. **创建 Pages 项目**
   - 点击 "Create application"
   - 选择 "Pages" 选项卡
   - 点击 "Upload assets"

3. **配置项目**
   - 项目名称：`mingli-frontend`
   - 上传文件夹：选择 `/workspace/mingli-frontend/dist/`

4. **完成部署**
   - 点击 "Deploy site"
   - 访问你的网站：`https://mingli-frontend.pages.dev`

---

## 📦 文件清单

### 前端已准备好部署

| 文件/目录 | 说明 |
|-----------|------|
| `mingli-frontend/dist/` | ✅ 构建完成的部署文件 |
| `mingli-frontend/_headers` | ✅ 安全头和缓存配置 |
| `mingli-frontend/_redirects` | ✅ SPA 路由配置 |

### 部署文件位置

```
/workspace/mingli-frontend/dist/
├── index.html
├── assets/
│   ├── index-DsLr21RP.css
│   └── index-qxSpkAUV.js
├── _headers
└── _redirects
```

---

## 🎯 后端部署选项

由于我们有 Python FastAPI 后端，您有以下选项：

### 选项 A：使用 Render 部署（推荐给 Python）

1. 访问 https://render.com/
2. 连接您的代码仓库
3. 配置：
   - Runtime: Python 3.11
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`

### 选项 B：使用 Vercel/其他平台

类似配置，具体参考各平台文档。

---

## 📝 详细文档

更多详细信息请查看：

- [Cloudflare 部署完整指南](file:///workspace/CLOUDFLARE_DEPLOY_GUIDE.md)
- [部署方案对比](file:///workspace/DEPLOYMENT_GUIDE.md)
- [自动部署脚本](file:///workspace/deploy.sh)

---

## ✅ 检查清单

部署前确认：

- [ ] 前端已构建 (`npm run build`)
- [ ] `_headers` 配置文件存在
- [ ] `_redirects` 配置文件存在
- [ ] 配置文件已复制到 `dist/` 目录

部署后确认：

- [ ] 网站可以正常访问
- [ ] 路由刷新不会出现 404
- [ ] 静态资源加载正常

---

## 🔧 故障排查

### 问题 1：刷新页面出现 404

**解决**：检查 `_redirects` 文件是否正确部署
```
/* /index.html 200
```

### 问题 2：样式加载失败

**解决**：确认 `_headers` 配置正确

### 问题 3：API 请求失败

**解决**：检查后端 API 是否部署并配置了 CORS

---

## 📞 需要帮助？

查看完整文档或使用部署脚本：
```bash
cd /workspace
chmod +x deploy.sh
./deploy.sh
```
