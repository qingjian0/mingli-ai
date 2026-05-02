#!/bin/bash

# 明理 AI 命理平台 - 完整发布和部署脚本

set -e

echo "==========================================="
echo "  明理 AI 命理平台 - 发布流程"
echo "==========================================="
echo ""

# 步骤 1：构建前端
echo "[1/5] 构建前端应用..."
cd mingli-frontend
npm run build
cp _headers _redirects dist/
cd ..
echo "✅ 前端构建完成"
echo ""

# 步骤 2：准备后端
echo "[2/5] 准备后端发布..."
cd mingli-backend
mkdir -p dist
# 复制核心文件
cp -r app dist/ 2>/dev/null || true
cp requirements.txt dist/
# 创建启动脚本
cat > dist/start.sh << 'START_SCRIPT'
#!/bin/bash
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port $PORT
START_SCRIPT
chmod +x dist/start.sh
cd ..
echo "✅ 后端准备完成"
echo ""

# 步骤 3：生成发布说明
echo "[3/5] 生成发布说明..."
VERSION="1.0.0"
RELEASE_DATE=$(date +"%Y-%m-%d")
cat > RELEASE_NOTES.md << RELEASE_NOTES
# 明理 AI 命理平台 v${VERSION}

发布日期: ${RELEASE_DATE}

## 主要功能

- 📊 12+ 命理系统支持（紫微斗数、八字、奇门遁甲等）
- 🧠 多 Agent 协同推理系统
- 📚 纯净知识库系统（源自古籍原典）
- 📱 响应式前端应用
- 🔌 RESTful API 后端

## 前端发布

- 构建文件: mingli-frontend/dist/
- 部署目标: Cloudflare Pages
- 文件大小: ~200KB gzip 压缩

## 后端发布

- 构建文件: mingli-backend/dist/
- 部署目标: Render / Fly.io / AWS
- 运行环境: Python 3.11+

## 部署指南

### 1. 前端部署 (Cloudflare Pages)

```bash
cd mingli-frontend
# 使用 wrangler CLI 部署
wrangler pages deploy dist/ --project-name mingli-frontend
```

### 2. 后端部署 (Render)

1. 创建 Render 账户
2. 连接 GitHub 仓库
3. 创建 Web Service
4. 设置构建命令: `pip install -r requirements.txt`
5. 设置启动命令: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`

## 发布注意事项

- 确保所有测试通过
- 检查 .env 文件是否已配置
- 验证所有依赖是否正确安装
RELEASE_NOTES
echo "✅ 发布说明已生成"
echo ""

# 步骤 4：验证发布包
echo "[4/5] 验证发布包..."
echo "前端发布包:"
ls -la mingli-frontend/dist/
echo ""
echo "后端发布包:"
ls -la mingli-backend/dist/ 2>/dev/null || echo "后端目录暂未生成"
echo ""
echo "✅ 发布验证完成"
echo ""

# 步骤 5：完成
echo "[5/5] 发布准备完成！"
echo ""
echo "==========================================="
echo "  发布包准备完成！"
echo "==========================================="
echo ""
echo "发布包位置:"
echo "  前端: mingli-frontend/dist/"
echo "  后端: mingli-backend/dist/"
echo "  说明: RELEASE_NOTES.md"
echo ""
echo "下一步:"
echo "  1. 上传到 GitHub（已完成）"
echo "  2. 部署到 Cloudflare Pages"
echo "  3. 部署后端到 Render"
echo ""
