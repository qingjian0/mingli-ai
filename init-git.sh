#!/bin/bash

# "明理"AI命理平台 - Git 初始化脚本
# 帮助初始化 git 仓库并推送到 GitHub

set -e

echo "==========================================="
echo "  明理 AI命理平台 - Git 初始化"
echo "==========================================="
echo ""

# 检查是否已安装 git
if ! command -v git &> /dev/null; then
    echo "❌ 错误: Git 未安装"
    echo "请先安装 Git: https://git-scm.com/"
    exit 1
fi

# 检查是否已经是 git 仓库
if [ -d ".git" ]; then
    echo "⚠️  当前目录已初始化为 Git 仓库"
    echo ""
    git status
    echo ""
    echo "如果需要重新初始化，请先删除 .git 目录"
    exit 0
fi

# 初始化 git 仓库
echo "[1/6] 初始化 Git 仓库..."
git init
echo "   ✅ 完成"

# 创建初始提交
echo ""
echo "[2/6] 添加文件..."
git add .
echo "   ✅ 完成"

echo ""
echo "[3/6] 创建初始提交..."
git commit -m "Initial commit: 明理 AI命理平台" -m "
- 完整的前端应用 (React + Vite)
- 完整的后端 API (FastAPI + Python)
- 12+ 术数系统的知识库
- 多 Agent 推理系统
- 完整的测试套件
"
echo "   ✅ 完成"

# 显示 git 状态
echo ""
echo "[4/6] Git 状态:"
git status

echo ""
echo "==========================================="
echo "  ✅ Git 仓库初始化完成！"
echo "==========================================="
echo ""
echo "接下来的步骤："
echo ""
echo "1. 在 GitHub 上创建新仓库"
echo "   访问: https://github.com/new"
echo ""
echo "2. 复制仓库的 URL，然后运行："
echo "   git remote add origin <你的仓库URL>"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
echo "或者，如果你已经有仓库，请运行："
echo "   git remote add origin https://github.com/<用户名>/<仓库名>.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
echo "提示: 如果需要取消 git init，可以删除 .git 目录"
echo ""
