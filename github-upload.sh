#!/bin/bash

# "明理"AI命理平台 - GitHub 上传脚本
# 使用令牌认证，推送到 GitHub

set -e

echo "==========================================="
echo "  GitHub 上传脚本"
echo "==========================================="
echo ""

# 检查 Git 状态
if [ ! -d ".git" ]; then
    echo "❌ 错误: 当前目录不是 Git 仓库"
    echo "请先运行: git init"
    exit 1
fi

# 配置 Git 用户信息
echo "[1/6] 配置 Git 用户信息..."
git config user.name "Mingli AI"
git config user.email "guc325@qq.com"
echo "   ✅ 用户信息已配置"

# 检查远程仓库
echo ""
echo "[2/6] 检查远程仓库..."
if git remote -v | grep -q "origin"; then
    echo "   ⚠️  远程仓库 'origin' 已存在"
    read -p "是否要重新配置? (y/n): " -n 1 -r
    echo ""
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        git remote remove origin
        echo "   ✅ 已移除旧的远程仓库"
    else
        echo "   跳过远程仓库配置"
    fi
fi

# 添加远程仓库
echo ""
echo "[3/6] 配置远程仓库..."
echo ""
echo "请在 GitHub 上创建仓库后，选择以下选项:"
echo ""
echo "1. 使用脚本自动创建仓库（推荐）"
echo "2. 我已经有仓库，复制 URL 后继续"
echo ""
read -p "请选择 (1 或 2): " choice

case $choice in
    1)
        echo ""
        echo "🔧 自动创建 GitHub 仓库..."
        read -p "请输入仓库名 (默认: mingli-ai): " repo_name
        repo_name=${repo_name:-mingli-ai}
        
        read -p "是否公开? (y/n, 默认 y): " -n 1 -r
        echo ""
        visibility="--public"
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            visibility="--private"
        fi
        
        echo ""
        echo "创建仓库: $repo_name ($visibility)"
        echo ""
        echo "⚠️  注意: 由于网络限制，建议手动在 GitHub 网页上创建仓库"
        echo ""
        echo "手动步骤:"
        echo "1. 访问: https://github.com/new"
        echo "2. Repository name: $repo_name"
        echo "3. 不要勾选 'Initialize this repository'"
        echo "4. 点击 'Create repository'"
        echo "5. 复制仓库 URL，然后回来继续"
        echo ""
        read -p "按 Enter 键继续..."
        ;;
    
    2)
        echo ""
        echo "请复制您的 GitHub 仓库 URL"
        echo "格式: https://github.com/用户名/仓库名.git"
        echo ""
        read -p "请输入仓库 URL: " repo_url
        
        if [ -z "$repo_url" ]; then
            echo "❌ 错误: URL 不能为空"
            exit 1
        fi
        
        git remote add origin "$repo_url"
        echo "   ✅ 远程仓库已添加: $repo_url"
        ;;
    
    *)
        echo ""
        echo "❌ 无效选择"
        exit 1
        ;;
esac

# 推送代码
echo ""
echo "[4/6] 推送代码到 GitHub..."
git branch -M main

echo ""
echo "正在推送代码..."
echo "请确保您有访问权限"
echo ""

# 使用令牌进行认证（如果环境变量设置了）
if [ -n "$GITHUB_TOKEN" ]; then
    echo "🔐 使用令牌认证..."
    
    # 修改 remote URL 以包含令牌
    remote_url=$(git remote get-url origin)
    if [[ $remote_url == https://* ]]; then
        # 提取用户名和仓库名
        username_repo=$(echo $remote_url | sed 's|https://||')
        new_url="https://x-access-token:${GITHUB_TOKEN}@${username_repo}"
        git remote set-url origin "$new_url"
    fi
fi

git push -u origin main

echo ""
echo "[5/6] 验证推送..."
if [ $? -eq 0 ]; then
    echo "   ✅ 推送成功!"
    
    # 显示仓库 URL
    repo_url=$(git remote get-url origin | sed 's|https://x-access-token:.*@||' | sed 's|https://||')
    echo ""
    echo "==========================================="
    echo "  🎉 上传成功!"
    echo "==========================================="
    echo ""
    echo "您的项目已上传到:"
    echo "https://github.com/${repo_url%.git}"
    echo ""
    
    echo "==========================================="
else
    echo ""
    echo "❌ 推送失败"
    echo ""
    echo "可能的原因:"
    echo "1. 仓库不存在或没有访问权限"
    echo "2. 令牌权限不足"
    echo "3. 网络连接问题"
    echo ""
    echo "请检查:"
    echo "- 仓库是否已创建"
    echo "- 令牌是否有效"
    echo "- 令牌是否有 push 权限"
fi

echo ""
echo "[6/6] 完成"
echo ""
