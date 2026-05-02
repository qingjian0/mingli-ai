# GitHub 上传方案

## 📋 当前状态
- ✅ Git 仓库已初始化
- ✅ 初始提交已创建 (e7c1ba9)
- ✅ 项目文件: 244 个文件，45,000+ 行代码
- ❌ GitHub CLI (gh) 未安装在此环境中

## 🚀 方案一: 手动上传 (推荐，最简单)

### 步骤 1: 在 GitHub 上创建仓库

1. 访问: https://github.com/new
2. 填写:
   - Repository name: `mingli-ai`
   - Description: 「明理」AI命理平台
   - Public/Private: 自选
   - **不要**勾选 "Initialize this repository"
3. 点击 "Create repository"

### 步骤 2: 连接本地仓库并推送

在 **另一个可以访问 GitHub 的环境中** 或使用 GitHub Desktop：

```bash
# 如果你在本地电脑上操作
git remote add origin https://github.com/<你的用户名>/mingli-ai.git
git branch -M main
git push -u origin main
```

## 🔧 方案二: 在当前环境安装 gh-cli (如果可以)

### 安装 gh-cli

```bash
# 下载并安装 gh-cli
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
sudo apt update
sudo apt install -y gh

# 验证安装
gh --version
```

### 使用 gh-cli 创建仓库

```bash
# 1. 登录 GitHub
gh auth login

# 2. 创建仓库 (按提示操作)
gh repo create mingli-ai --public --source=. --remote=origin --push

# 3. 或者按上述方案一操作
```

## 💻 方案三: 使用 GitHub Desktop (图形界面，最容易)

1. 下载 GitHub Desktop: https://desktop.github.com/
2. 点击 "File" → "Add Local Repository"
3. 选择项目目录
4. 点击 "Publish repository"
5. 填写仓库信息并发布

## 📦 方案四: 创建项目存档

我可以为您创建一个压缩包，您可以手动下载并上传：

```bash
cd /workspace
tar -czvf mingli-ai-project.tar.gz --exclude=node_modules --exclude=.git --exclude=__pycache__ .
```

## 📖 快速参考

### 如果在本地机器上（假设已下载项目）：

```bash
# 初始化 git (如果需要)
git init
git add .
git commit -m "Initial commit: 明理 AI命理平台"

# 连接 GitHub 仓库
git remote add origin https://github.com/<你的用户名>/mingli-ai.git
git branch -M main
git push -u origin main
```

## 🔗 快速链接

- 创建仓库: https://github.com/new
- GitHub Desktop: https://desktop.github.com/
- GitHub CLI 文档: https://cli.github.com/
