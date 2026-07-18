# 江汉大学 AI+冲击动力学 课题组门户网站
# 部署到 Cloudflare 的说明

## 项目结构

```
studying_in_summer/
├── app.py                    # Flask 后端应用
├── worker.py                 # Cloudflare Worker 入口
├── wrangler.toml             # Cloudflare 部署配置
├── requirements.txt          # Python 依赖
├── templates/                # Jinja2 模板
│   ├── base.html             # 基础模板（导航、页脚）
│   ├── index.html            # 首页
│   ├── research.html         # 研究方向
│   ├── team.html             # 团队成员
│   ├── publications.html     # 学术成果
│   └── ai_lab.html           # AI学习实验室
├── static/
│   ├── css/
│   │   └── style.css         # 主样式表
│   └── js/
│       └── main.js           # 交互脚本
└── README.md
```

## 功能页面

| 页面 | 路由 | 说明 |
|------|------|------|
| 首页 | `/` | Hero区 + 研究方向预览 + 团队成员 + 新闻动态 + 加入我们 |
| 研究方向 | `/research` | 6个研究方向的详细介绍 + 全链条研究范式 |
| 团队成员 | `/team` | 高矗老师 & 桑鸿乾老师完整资料 |
| 学术成果 | `/publications` | 代表性论文 + 主讲课程 + 成果统计 |
| AI实验室 | `/ai-lab` | 4阶段学习路径 + 资源推荐 + AI学习助手 |

## 本地运行

```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 运行应用
python app.py

# 3. 浏览器访问
# http://localhost:5000
```

## 部署到 Cloudflare

### 方案一：Cloudflare Workers (推荐 - 全栈部署)

Cloudflare Workers 支持 Python 运行时，可以完整部署 Flask 应用：

```bash
# 1. 安装 Wrangler CLI
npm install -g wrangler

# 2. 登录 Cloudflare
wrangler login

# 3. 部署
wrangler deploy
```

### 方案二：Cloudflare Pages (静态前端) + Workers (API)

适合前后端分离部署：

1. **Cloudflare Pages** 部署静态文件（HTML/CSS/JS）
2. **Cloudflare Workers** 部署 API 路由（`/api/ask`, `/api/contact`）

步骤：
1. 将 `templates/` 编译为静态 HTML
2. 将 `static/` 上传到 Cloudflare Pages
3. 单独部署 `worker.py` 作为 API Worker

### 方案三：阿里云 ECS (传统部署)

按照桑鸿乾老师的建议，在阿里云学生服务器上部署：

```bash
# 1. SSH 连接到云服务器
ssh root@your-server-ip

# 2. 安装 Python 环境
apt update && apt install python3 python3-pip nginx

# 3. 克隆项目
git clone <your-repo-url> /var/www/jhun-ai-lab

# 4. 安装依赖
cd /var/www/jhun-ai-lab
pip install -r requirements.txt

# 5. 使用 Gunicorn 运行
pip install gunicorn
gunicorn -w 4 -b 127.0.0.1:8000 app:app

# 6. 配置 Nginx 反向代理
# 编辑 /etc/nginx/sites-available/jhun-ai-lab
# 配置 server_name 和 proxy_pass http://127.0.0.1:8000

# 7. 重启 Nginx
systemctl restart nginx
```

## 技术栈

- **前端**: HTML5 + CSS3 (Custom Properties, Grid, Flexbox, Animations) + Vanilla JavaScript
- **后端**: Python 3 + Flask + Jinja2
- **部署**: Cloudflare Workers / Pages, 阿里云 ECS
- **设计**: 暗色主题 + 渐变色彩 + 微交互动效 + 响应式布局
