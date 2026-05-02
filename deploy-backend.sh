#!/bin/bash

# ===========================================
#  明理 AI 命理平台 - 后端部署脚本
#  求是思想 - 具体问题具体分析
# ===========================================

set -e

echo ""
echo "==========================================="
echo "  明理 AI 命理平台 - 后端部署"
echo "==========================================="
echo ""

echo "[1/4] 检查后端状态..."

# 检查 requirements.txt
if [ ! -f "mingli-backend/requirements.txt" ]; then
    echo "❌ 错误: 找不到 requirements.txt!"
    exit 1
fi
echo "   ✅ requirements.txt 已就绪"

# 检查主应用
if [ ! -f "mingli-backend/app/main.py" ]; then
    echo "❌ 错误: 找不到 main.py!"
    exit 1
fi
echo "   ✅ FastAPI 应用已就绪"

echo ""
echo "[2/4] 选择部署平台..."
echo ""
echo "请选择后端部署平台:"
echo ""
echo "  1. Render (推荐 - 免费额度，最易用)"
echo "  2. Fly.io"
echo "  3. Railway"
echo "  4. Heroku"
echo "  5. 生成部署配置（所有平台）"
echo ""

read -p "请选择 (1/2/3/4/5): " platform_choice

echo ""
echo "[3/4] 创建部署配置..."
cd mingli-backend

case $platform_choice in
    1)
        # Render
        echo "创建 Render 配置..."
        
        # 创建 render.yaml
        cat > render.yaml << 'RENDERYAML'
services:
  - type: web
    name: mingli-backend
    env: python
    plan: free
    buildCommand: pip install -r requirements.txt
    startCommand: uvicorn app.main:app --host 0.0.0.0 --port $PORT
    envVars:
      - key: PYTHON_VERSION
        value: 3.11
RENDERYAML
        
        # 创建部署说明
        cat > RENDER_DEPLOY.md << 'RENDERDEPLOY'
# Render 部署指南

## 方式 1: 手动部署（推荐）

1. 登录 https://render.com
2. 连接你的 GitHub 仓库
3. 点击 "New" → "Web Service"
4. 选择仓库和分支
5. 配置部署:
   - 构建命令: `pip install -r requirements.txt`
   - 启动命令: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
   - Python 版本: 3.11
6. 点击 "Create Web Service"
7. 等待部署完成，获得访问地址！

## 方式 2: 使用 Blueprint (render.yaml)

1. 将 render.yaml 提交到仓库
2. 在 Render 中选择 "Blueprints"
3. 按照提示完成设置
RENDERDEPLOY
        
        echo "✅ Render 配置已创建!"
        echo ""
        echo "文件:"
        echo "  - render.yaml"
        echo "  - RENDER_DEPLOY.md"
        ;;
        
    2)
        # Fly.io
        echo "创建 Fly.io 配置..."
        
        # 创建 fly.toml
        cat > fly.toml << 'FLYTOML'
app = 'mingli-backend'
primary_region = 'hkg'

[build]

[env]
  PYTHON_VERSION = "3.11"

[http_service]
  internal_port = 8000
  force_https = true
  auto_stop_machines = true
  auto_start_machines = true
  min_machines_running = 0
FLYTOML
        
        # 创建部署说明
        cat > FLY_DEPLOY.md << 'FLYDEPLOY'
# Fly.io 部署指南

## 部署步骤

1. 安装 Fly CLI: https://fly.io/docs/hands-on/install-flyctl
2. 登录: `fly auth login`
3. 部署: `fly deploy`
4. 访问应用: `fly open`

## 本地测试

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```
FLYDEPLOY
        
        echo "✅ Fly.io 配置已创建!"
        ;;
        
    3)
        # Railway
        echo "创建 Railway 配置..."
        
        # 创建 railway.json
        cat > railway.json << 'RAILWAYJSON'
{
  "$schema": "https://railway.app/railway.schema.json",
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "uvicorn app.main:app --host 0.0.0.0 --port $PORT",
    "healthcheckPath": "/"
  }
}
RAILWAYJSON
        
        echo "✅ Railway 配置已创建!"
        ;;
        
    4)
        # Heroku
        echo "创建 Heroku 配置..."
        
        # 创建 Procfile
        echo "web: uvicorn app.main:app --host 0.0.0.0 --port \$PORT" > Procfile
        
        echo "✅ Heroku 配置已创建!"
        ;;
        
    5)
        # 所有平台
        echo "创建所有平台配置..."
        
        # Render
        cat > render.yaml << 'RENDERYAML'
services:
  - type: web
    name: mingli-backend
    env: python
    plan: free
    buildCommand: pip install -r requirements.txt
    startCommand: uvicorn app.main:app --host 0.0.0.0 --port $PORT
RENDERYAML
        
        # Fly
        cat > fly.toml << 'FLYTOML'
app = 'mingli-backend'
primary_region = 'hkg'

[build]

[http_service]
  internal_port = 8000
FLYTOML
        
        # Procfile
        echo "web: uvicorn app.main:app --host 0.0.0.0 --port \$PORT" > Procfile
        
        echo "✅ 所有平台配置已创建!"
        ;;
esac

cd ..
echo ""
echo "[4/4] 创建完整部署说明..."

# 创建完整的部署文档
cat > FULL_DEPLOY_GUIDE.md << 'DEPLOYGUIDE'
# 明理 AI 命理平台 - 完整部署指南

## 整体架构

```
┌─────────────────────────────────────────┐
│         用户访问 (浏览器)            │
└────────────────┬────────────────────────┘
                 │
         ┌───────┴────────┐
         │                │
    ┌────▼─────┐   ┌────▼─────┐
    │ 前端    │   │ 后端    │
    │ (CF)    │   │ (Render) │
    └──────────┘   └──────────┘
```

## 1. 前端部署 (Cloudflare Pages)

### 方式 A: 手动上传（最简单）

1. 访问 Cloudflare Dashboard:
   https://dash.cloudflare.com/b009d274cb9dc02032faf28b57926c4a/workers-and-pages

2. 创建 Pages 项目:
   - 点击 "Create application" → "Pages"
   - 选择 "Upload assets"
   - 项目名: `mingli-frontend`

3. 上传 `mingli-frontend/dist/` 目录

### 方式 B: 使用 wrangler CLI

```bash
npm install -g wrangler
cd mingli-frontend
wrangler pages deploy dist/ --project-name mingli-frontend
```

## 2. 后端部署 (Render)

### 部署步骤

1. 登录 https://render.com
2. 连接 GitHub 仓库
3. 创建 Web Service:
   - 构建命令: `pip install -r requirements.txt`
   - 启动命令: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
   - 环境: Python 3.11

## 3. 环境变量配置

### 前端 (.env)

```env
VITE_API_URL=https://your-render-app.onrender.com
```

### 后端 (.env)

```env
DATABASE_URL=sqlite:///./mingli.db
CORS_ORIGINS=https://mingli-frontend.pages.dev,http://localhost:3000
```

## 4. 域名配置（可选）

### 自定义域名

1. 在 Cloudflare Pages 设置中添加自定义域名
2. 在 Render 设置中添加自定义域名
3. 配置 DNS 记录

## 部署检查清单

- [ ] 前端构建成功
- [ ] Cloudflare Pages 部署成功
- [ ] 后端 Render 部署成功
- [ ] 前后端连接正常
- [ ] 自定义域名配置（可选）
- [ ] HTTPS 正常
- [ ] 测试所有功能
DEPLOYGUIDE

echo ""
echo "==========================================="
echo "  ✅ 后端部署配置已完成！"
echo "==========================================="
echo ""
echo "部署说明已保存到: mingli-backend/ 和 FULL_DEPLOY_GUIDE.md"
echo ""
echo "推荐部署方案:"
echo "  前端: Cloudflare Pages"
echo "  后端: Render (免费额度)"
echo ""
echo "运行 'deploy-cf-pages.sh' 部署前端！"
echo ""
