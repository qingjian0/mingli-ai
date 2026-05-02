#!/bin/bash

# "明理"AI命理平台 - 部署脚本
# 部署前端到 Cloudflare Pages

set -e  # 出错时停止

echo "==========================================="
echo "  明理 AI命理平台 - 部署脚本"
echo "==========================================="
echo ""

# 检查是否安装了 Node.js
if ! command -v npm &> /dev/null; then
    echo "❌ 错误: 未找到 Node.js"
    echo "请先安装 Node.js: https://nodejs.org/"
    exit 1
fi

# 检查是否安装了 Wrangler
if ! command -v wrangler &> /dev/null; then
    echo "⚠️ Wrangler CLI 未安装"
    echo "正在安装 Wrangler..."
    npm install -g wrangler
fi

# 进入前端目录
cd "$(dirname "$0")/mingli-frontend" || exit 1
echo "✅ 当前目录: $(pwd)"

# 1. 安装依赖
echo ""
echo "[1/4] 安装前端依赖..."
npm install

# 2. 构建项目
echo ""
echo "[2/4] 构建前端项目..."
npm run build

# 3. 复制配置文件到 dist
echo ""
echo "[3/4] 配置部署文件..."
if [ -f "_headers" ]; then
    cp _headers dist/
    echo "   ✅ _headers 已复制"
fi

if [ -f "_redirects" ]; then
    cp _redirects dist/
    echo "   ✅ _redirects 已复制"
fi

# 4. 部署到 Cloudflare Pages
echo ""
echo "[4/4] 部署到 Cloudflare Pages"
echo ""
echo "请选择部署方式:"
echo "1. 使用 Cloudflare Dashboard (手动上传)"
echo "2. 使用 Wrangler CLI 部署"
echo ""
read -p "请选择 (1 或 2): " choice

case $choice in
    1)
        echo ""
        echo "📋 Dashboard 部署步骤:"
        echo ""
        echo "1. 访问: https://dash.cloudflare.com/b009d274cb9dc02032faf28b57926c4a/workers-and-pages/create/pages"
        echo "2. 点击 'Upload assets'"
        echo "3. 创建项目名称: mingli-frontend"
        echo "4. 上传 dist/ 目录下的所有内容:"
        ls -la dist/
        echo ""
        echo "构建输出目录: $(pwd)/dist"
        ;;
    
    2)
        echo ""
        echo "🔧 使用 Wrangler 部署..."
        read -p "请输入项目名称 (默认: mingli-frontend): " project_name
        project_name=${project_name:-mingli-frontend}
        
        echo ""
        echo "登录到 Cloudflare..."
        wrangler login
        
        echo ""
        echo "部署项目: $project_name"
        echo ""
        
        # 检查项目是否已存在，不存在则创建
        if ! wrangler pages project list | grep -q "$project_name"; then
            echo "创建项目: $project_name"
            wrangler pages project create "$project_name" --production-branch main
        fi
        
        # 部署
        wrangler pages deploy dist --project-name "$project_name"
        
        echo ""
        echo "🎉 部署完成!"
        echo "访问: https://$project_name.pages.dev"
        ;;
    
    *)
        echo ""
        echo "❌ 无效选择"
        echo ""
        echo "提示: 构建完成，您也可以手动部署:"
        echo "构建输出目录: $(pwd)/dist"
        ;;
esac

echo ""
echo "==========================================="
echo "  部署脚本执行完毕"
echo "==========================================="
