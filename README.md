# 明理 AI命理平台

> A comprehensive AI-powered Chinese metaphysics platform built with modern technologies.

## 项目简介

「明理」是一个基于古籍原典的 AI 命理智能推演平台，提供紫微斗数、子平八字、奇门遁甲、梅花易数等多种术数的排盘与分析功能。

## 项目结构

```
/workspace/
├── mingli-backend/           # 后端服务 (FastAPI + Python)
│   ├── app/
│   │   ├── agents/          # AI Agents
│   │   ├── api/             # API 路由
│   │   ├── engine/          # 排盘引擎
│   │   ├── knowledge/       # 知识库系统
│   │   ├── models/          # 数据模型
│   │   ├── reasoning/       # 推理引擎
│   │   └── services/        # 业务服务
│   ├── tests/               # 测试套件
│   └── requirements.txt
│
├── mingli-frontend/          # 前端应用 (React + Vite + TypeScript)
│   ├── src/
│   │   ├── components/      # UI 组件
│   │   └── App.tsx
│   └── package.json
│
├── docs/                    # 文档 (可选)
├── DEPLOYMENT_SUMMARY.md    # 部署总结
└── README.md               # 本文件
```

## 核心功能

### 📊 术数系统
- **紫微斗数** - 完整的星曜排盘与分析
- **子平八字** - 四柱八字、大运流年
- **奇门遁甲** - 起局与八门九星分析
- **梅花易数** - 灵活起卦与外应
- **易经 64 卦** - 完整卦辞与爻辞
- **更多系统** - 大衍、邵子、皇极等

### 🧠 AI 系统
- **多 Agent 协作** - 专家级 Agent 协同工作
- **推理引擎** - 基于古籍的可信推理
- **知识图谱** - 结构化的术数知识库
- **置信度评分** - 透明的分析可信度

### 🏗️ 系统特性
- **纯净知识库** - 源于古籍，经过严格验证
- **多维度评分** - 科学评估各术数系统
- **来源可追溯** - 每条知识标注原始出处

## 快速开始

### 前置要求

- **Node.js** >= 18
- **Python** >= 3.10
- **Git**

### 后端启动

```bash
cd mingli-backend
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
.\venv\Scripts\activate  # Windows

pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

### 前端启动

```bash
cd mingli-frontend
npm install
npm run dev
```

访问：http://localhost:3000

## 部署

### Cloudflare Pages (前端)

详细部署指南请查看：
- [快速部署指南](QUICK_DEPLOY.md)
- [Cloudflare 部署完整指南](CLOUDFLARE_DEPLOY_GUIDE.md)
- [部署总结](DEPLOYMENT_SUMMARY.md)

快速部署：
1. 访问 https://dash.cloudflare.com/
2. 创建 Pages 项目
3. 上传 `mingli-frontend/dist/`

### 后端部署

推荐使用：
- **Render** (Python 友好)
- **Vercel Functions** (Serverless)
- **Cloudflare Workers** (需要转 TS)

## 技术栈

### 后端
- **Framework**: FastAPI
- **Language**: Python 3.11
- **Database**: SQLAlchemy (SQLite/PostgreSQL)
- **Testing**: pytest

### 前端
- **Framework**: React 18
- **Build Tool**: Vite 5
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **State Management**: Zustand

### DevOps
- **Frontend Hosting**: Cloudflare Pages
- **CI/CD**: GitHub Actions

## 知识库

知识库特点：
- **古籍原典** - 源于《紫微斗数全书》、《渊海子平》等经典
- **严格验证** - 多轮校验确保内容准确
- **来源追溯** - 每条知识标注出处
- **持续更新** - 不断完善的知识体系

包含的术数系统：
- 紫微斗数 (Ziwei)
- 八字命理 (Bazi)
- 奇门遁甲 (Qimen)
- 梅花易数 (Meihua)
- 易经 (Yijing)
- 六爻纳甲 (Liuyao)
- 大衍筮法 (Dayan)
- 邵子易数 (Shaozi)
- 皇极数 (Huangji)
- 小成图 (Xiaocheng)
- 神易术 (Shenyi)
- 大定数 (Dading)

## 项目文档

| 文档 | 说明 |
|------|------|
| [QUICK_DEPLOY.md](QUICK_DEPLOY.md) | 快速部署指南 |
| [DEPLOYMENT_SUMMARY.md](DEPLOYMENT_SUMMARY.md) | 部署总结 |
| [CLOUDFLARE_DEPLOY_GUIDE.md](CLOUDFLARE_DEPLOY_GUIDE.md) | Cloudflare 完整指南 |
| [SANDBOX_TEST_REPORT.md](SANDBOX_TEST_REPORT.md) | 沙箱测试报告 |
| [SYSTEM_SELECTION_SUMMARY.md](SYSTEM_SELECTION_SUMMARY.md) | 系统评分与对比 |
| [KNOWLEDGE_COMPLETION_SUMMARY.md](KNOWLEDGE_COMPLETION_SUMMARY.md) | 知识库完成总结 |

## 开发指南

### 测试

```bash
# 后端测试
cd mingli-backend
pytest tests/
```

### 代码规范

- 遵循 PEP 8 (Python)
- 遵循 ESLint (TypeScript)
- 代码审查前请运行测试

## 贡献

欢迎贡献！请遵循以下流程：

1. Fork 项目
2. 创建特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 开启 Pull Request

## 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE)

## 联系方式

- 项目地址: https://github.com/your-username/mingli-ai
- 问题反馈: Issues

## 致谢

感谢所有贡献者和古籍原典作者！

---

**明理 AI命理平台** - 让传统智慧触手可及 ✨
