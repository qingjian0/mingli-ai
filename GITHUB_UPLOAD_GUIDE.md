# GitHub 上传指南

## ✅ 当前状态

Git 仓库已初始化并创建了初始提交！
- 提交: e7c1ba9
- 分支: master (或 main)
- 文件: 244 个文件，45,000+ 行代码

## 🚀 步骤 1: 在 GitHub 上创建仓库

1. 访问 https://github.com/new
2. 填写仓库信息：
   - Repository name: `mingli-ai` (或你喜欢的名字)
   - Description: 「明理」AI命理平台
   - Public/Private: 自行选择
   - **不要**勾选 "Initialize this repository" (我们已有代码)

3. 点击 "Create repository"

## 📤 步骤 2: 连接并推送到 GitHub

在你创建仓库后，GitHub 会显示命令指引。运行以下命令：

```bash
# 进入项目目录 (已在 workspace 中)
cd /workspace

# 1. 添加远程仓库
git remote add origin https://github.com/<你的用户名>/<你的仓库名>.git

# 2. 重命名分支为 main (推荐)
git branch -M main

# 3. 推送到 GitHub
git push -u origin main
```

### 示例 (假设用户名是 "zhangsan"，仓库名是 "mingli-ai")：
```bash
git remote add origin https://github.com/zhangsan/mingli-ai.git
git branch -M main
git push -u origin main
```

## 🔐 使用 SSH (可选)

如果你使用 SSH 而不是 HTTPS：

```bash
git remote add origin git@github.com:<你的用户名>/<你的仓库名>.git
git branch -M main
git push -u origin main
```

## 📋 验证推送是否成功

推送成功后，访问你的 GitHub 仓库：
https://github.com/<你的用户名>/<你的仓库名>

你应该能看到：
- 所有项目文件
- README.md 内容
- Git 提交记录

## 🎯 后续：启用 GitHub Pages (可选)

如果你想用 GitHub Pages 托管前端：

1. 进入仓库 Settings → Pages
2. Source: Deploy from a branch
3. Branch: 选择包含构建文件的分支 (或使用 GitHub Actions 自动构建)
4. 点击 Save

更推荐使用 **Cloudflare Pages** (已在 `QUICK_DEPLOY.md` 中有详细说明)

## 📁 项目结构预览

上传到 GitHub 后，你的仓库会有以下结构：
```
mingli-ai/
├── mingli-backend/      # 后端服务
├── mingli-frontend/     # 前端应用
├── docs/               # 文档 (可选)
├── README.md           # 项目说明
├── .gitignore          # Git 忽略规则
└── ...其他文档
```

## 🔧 常见问题

### Q: 提示 "remote origin already exists"
A: 先删除旧的 origin，再重新添加：
```bash
git remote remove origin
git remote add origin https://github.com/...
```

### Q: 提示 "Authentication failed"
A: 需要配置 GitHub 访问权限：
1. 使用 Personal Access Token (推荐)
2. 或使用 SSH 密钥

### Q: 如何更改提交的用户名/邮箱？
A: 在当前仓库：
```bash
git config user.name "你的名字"
git config user.email "你的邮箱"
```

全局设置（所有仓库）：
```bash
git config --global user.name "你的名字"
git config --global user.email "你的邮箱"
```

## 📚 更多资源

- Git 官方文档: https://git-scm.com/doc
- GitHub 入门指南: https://guides.github.com/
- GitHub Pages 文档: https://pages.github.com/

---

**祝你上传成功！** ✨
