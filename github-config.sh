#!/bin/bash

# "明理"AI命理平台 - GitHub CLI 配置脚本
# 使用 gh-cli 配置 GitHub 账户并上传项目

set -e

echo "==========================================="
echo "  GitHub CLI 配置脚本"
echo "==========================================="
echo ""

# 检查是否安装了 gh
if ! command -v gh &> /dev/null; then
    echo "⚠️  GitHub CLI 未安装"
    echo ""
    echo "正在尝试安装..."
    
    if command -v apt-get &> /dev/null; then
        echo "使用 apt 安装..."
        curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
        echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
        sudo apt update
        sudo apt install gh -y
    elif command -v brew &> /dev/null; then
        echo "使用 Homebrew 安装..."
        brew install gh
    elif command -v yum &> /dev/null; then
        echo "使用 yum 安装..."
        sudo yum install gh -y
    else
        echo "❌ 无法自动安装 gh"
        echo ""
        echo "请手动安装:"
        echo "- macOS: brew install gh"
        echo "- Linux: https://github.com/cli/cli#installation"
        echo "- Windows: winget install GitHub.cli"
        echo ""
        exit 1
    fi
    
    # 验证安装
    if ! command -v gh &> /dev/null; then
        echo "❌ 安装失败"
        exit 1
    fi
fi

echo "✅ GitHub CLI 已安装"
gh --version
echo ""

# 配置 GitHub 账户
echo "==========================================="
echo "  配置 GitHub 账户"
echo "==========================================="
echo ""

# 使用令牌登录
echo "[1/5] 登录 GitHub..."
echo ""
echo "请选择登录方式:"
echo "1. 使用 Personal Access Token (推荐)"
echo "2. Web 浏览器登录"
echo "3. 直接使用令牌 (无需交互)"
echo ""
read -p "请选择 (1, 2 或 3): " login_choice

case $login_choice in
    1)
        echo ""
        echo "请在 GitHub 上创建 Personal Access Token:"
        echo "Settings → Developer settings → Personal access tokens → Tokens (classic)"
        echo "需要的权限: repo, workflow, read:org"
        echo ""
        gh auth login -p
        ;;
    
    2)
        echo ""
        echo "打开浏览器进行交互式登录..."
        gh auth login -w
        ;;
    
    3)
        echo ""
        read -p "请输入 Personal Access Token: " token
        if [ -z "$token" ]; then
            echo "❌ 令牌不能为空"
            exit 1
        fi
        
        echo "$token" | gh auth login --hostname github.com --with-token
        ;;
    
    *)
        echo "❌ 无效选择"
        exit 1
        ;;
esac

echo ""
echo "[2/5] 验证登录状态..."
gh auth status

# 配置 git
echo ""
echo "[3/5] 配置 git 集成..."
gh auth setup-git

# 创建仓库
echo ""
echo "[4/5] 创建 GitHub 仓库..."
echo ""

# 检查远程仓库
if git remote -v | grep -q "origin"; then
    echo "⚠️  远程仓库 'origin' 已存在"
    echo "仓库将被推送到现有远程仓库"
else
    read -p "请输入仓库名 (默认: mingli-ai): " repo_name
    repo_name=${repo_name:-mingli-ai}
    
    read -p "仓库描述 (可选): " repo_description
    repo_description=${repo_description:-"明理 AI命理平台 - 基于古籍原典的AI命理智能推演系统"}
    
    # 创建仓库（不初始化，因为已有代码）
    gh repo create "$repo_name" \
        --description "$repo_description" \
        --source=. \
        --remote=origin \
        --push \
        --public
fi

echo ""
echo "[5/5] 推送完成！"
echo ""

# 显示仓库信息
echo "==========================================="
echo "  ✅ 配置完成！"
echo "==========================================="
echo ""

repo_info=$(gh repo view --json name,url,description -q '{name,url,description}')
echo "仓库信息:"
echo "$repo_info" | jq -r '.name + "\nURL: " + .url + "\n描述: " + .description'

echo ""
echo "==========================================="
