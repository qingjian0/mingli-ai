#!/bin/bash

# ===========================================
#  明理 AI 命理平台 - Cloudflare Pages 部署脚本
#  求是思想 - 实事求是，实践出真知
# ===========================================

set -e

echo ""
echo "==========================================="
echo "  明理 AI 命理平台 - Cloudflare Pages 部署"
echo "==========================================="
echo ""

# 步骤 1: 检查必要条件
echo "[1/4] 检查部署前提条件..."

# 检查是否有 dist 目录
if [ ! -d "mingli-frontend/dist" ]; then
    echo "❌ 错误: dist 目录不存在！"
    echo "   请先运行前端构建: cd mingli-frontend && npm run build"
    exit 1
fi
echo "   ✅ dist 目录已就绪"

# 检查配置文件
if [ ! -f "mingli-frontend/dist/_headers" ] || [ ! -f "mingli-frontend/dist/_redirects" ]; then
    echo "   🔧 复制配置文件到 dist/..."
    cp mingli-frontend/_headers mingli-frontend/_redirects mingli-frontend/dist/ 2>/dev/null || true
    echo "   ✅ 配置文件已复制"
fi

# 步骤 2: 显示部署信息
echo ""
echo "[2/4] 显示部署信息..."
PROJECT_NAME="mingli-frontend"
PROJECT_PATH="mingli-frontend/dist"
FILE_SIZE=$(du -sh $PROJECT_PATH | cut -f1)

echo "   项目名: $PROJECT_NAME"
echo "   路径: $PROJECT_PATH"
echo "   文件大小: $FILE_SIZE"

# 显示文件列表
echo ""
echo "   文件列表:"
ls -lh $PROJECT_PATH/

echo ""

# 步骤 3: 部署选项
echo "[3/4] 部署选项..."
echo ""
echo "请选择部署方式:"
echo ""
echo "  方式 1: 手动上传 (推荐，最简单)"
echo "  方式 2: Wrangler CLI (需要先安装)"
echo "  方式 3: 使用 GitHub Actions (推荐)"
echo ""

read -p "请选择 (1/2/3): " deploy_choice

# 步骤 4: 执行部署
case $deploy_choice in
    1)
        # 手动上传
        echo ""
        echo "[4/4] 准备手动上传..."
        echo ""
        echo "==========================================="
        echo "  Cloudflare Pages 手动上传步骤"
        echo "==========================================="
        echo ""
        echo "1. 访问 Cloudflare Dashboard:"
        echo "   https://dash.cloudflare.com/b009d274cb9dc02032faf28b57926c4a/workers-and-pages"
        echo ""
        echo "2. 创建 Pages 项目:"
        echo "   - 点击 'Create application'"
        echo "   - 选择 'Pages' 标签"
        echo "   - 点击 'Upload assets'"
        echo ""
        echo "3. 配置项目:"
        echo "   - 项目名: $PROJECT_NAME"
        echo "   - 上传目录: $PROJECT_PATH"
        echo ""
        echo "4. 上传完成后访问项目!"
        echo ""
        
        # 创建上传包
        read -p "是否创建可下载的部署压缩包? (y/n): " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            echo "创建部署压缩包..."
            cd mingli-frontend
            mkdir -p ../deploy-packages
            tar -czf ../deploy-packages/mingli-frontend-v1.0.0.tar.gz dist/
            cd ..
            echo "✅ 压缩包已创建: deploy-packages/mingli-frontend-v1.0.0.tar.gz"
            echo ""
            ls -lh deploy-packages/
        fi
        ;;
        
    2)
        # Wrangler CLI
        echo ""
        echo "[4/4] 使用 Wrangler CLI 部署..."
        
        # 检查是否安装了 wrangler
        if ! command -v wrangler &> /dev/null; then
            echo ""
            echo "❌ Wrangler 未安装！"
            echo ""
            echo "请先安装 Wrangler:"
            echo "npm install -g wrangler"
            echo ""
            exit 1
        fi
        
        echo "准备使用 wrangler 部署..."
        echo ""
        echo "部署命令:"
        echo "cd mingli-frontend"
        echo "wrangler pages deploy dist/ --project-name $PROJECT_NAME"
        echo ""
        echo "或者在项目根目录执行:"
        echo "wrangler pages deploy mingli-frontend/dist/ --project-name $PROJECT_NAME"
        echo ""
        ;;
        
    3)
        # GitHub Actions
        echo ""
        echo "[4/4] 设置 GitHub Actions 自动部署..."
        
        # 创建 GitHub Actions 目录
        mkdir -p .github/workflows
        
        cat > .github/workflows/deploy-pages.yml << 'GHACTIONS'
name: Deploy to Cloudflare Pages

on:
  push:
    branches:
      - main
  workflow_dispatch:

jobs:
  deploy:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          
      - name: Install dependencies
        working-directory: mingli-frontend
        run: npm install
          
      - name: Build
        working-directory: mingli-frontend
        run: npm run build
          
      - name: Deploy to Cloudflare Pages
        uses: cloudflare/pages-action@v1
        with:
          apiToken: ${{ secrets.CLOUDFLARE_API_TOKEN }}
          accountId: ${{ secrets.CLOUDFLARE_ACCOUNT_ID }}
          projectName: mingli-frontend
          directory: mingli-frontend/dist
GHACTIONS
        
        echo "✅ GitHub Actions 部署配置已创建: .github/workflows/deploy-pages.yml"
        echo ""
        echo "需要配置的 Secrets:"
        echo "  - CLOUDFLARE_API_TOKEN"
        echo "  - CLOUDFLARE_ACCOUNT_ID"
        echo ""
        echo "请在 GitHub 设置中添加这些 Secrets！"
        echo ""
        ;;
        
    *)
        echo "无效选择！"
        exit 1
        ;;
esac

echo ""
echo "==========================================="
echo "  ✅ 部署准备完成！"
echo "==========================================="
echo ""
echo "后续步骤:"
echo "1. 部署前端到 Cloudflare Pages"
echo "2. 部署后端到 Render/Fly.io"
echo ""
echo "运行 'deploy-backend.sh' 配置后端部署！"
echo ""
