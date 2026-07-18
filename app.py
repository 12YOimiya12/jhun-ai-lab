"""
江汉大学 - 数字建造与爆破工程学院
AI + 冲击动力学 课题组门户网站
Flask 后端应用
"""
from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'jhun-research-lab-2026')

# ──────────────────────────────────────
# 研究方向数据
# ──────────────────────────────────────
RESEARCH_DIRECTIONS = [
    {
        "id": 1,
        "icon": "⚡",
        "title": "爆炸与冲击动力学",
        "subtitle": "高精度数值模拟",
        "description": "研究爆炸载荷作用下岩石、混凝土等介质的动态响应与损伤演化规律，揭示高应变率及高围压条件下的动态损伤破坏机理，为爆破作用精细分析与爆炸毁伤评估奠定理论基础。",
        "keywords": ["爆炸载荷", "动态损伤", "数值模拟", "毁伤评估"],
        "tag": "核心方向",
        "color": "#ff6b35"
    },
    {
        "id": 2,
        "icon": "🧠",
        "title": "数据驱动本构模型参数智能反演",
        "subtitle": "AI赋能材料建模",
        "description": "融合动态实验数据与数值模拟，利用深度学习、遗传算法等方法智能反演材料本构关键参数；解决传统标定效率低、精度不足问题，实现对弹塑性损伤本构模型的高效准确参数识别。",
        "keywords": ["深度学习", "遗传算法", "参数反演", "本构模型"],
        "tag": "AI+力学",
        "color": "#4a90d9"
    },
    {
        "id": 3,
        "icon": "🔬",
        "title": "物理融合神经网络（PINN）",
        "subtitle": "物理-数据双驱动",
        "description": "发展物理融合神经网络方法，结合小样本学习技术，解决实验数据稀疏问题；构建基于神经网络的数据驱动代理模型，替代高保真数值模拟，实现爆炸冲击响应的快速预测。",
        "keywords": ["PINN", "小样本学习", "代理模型", "快速预测"],
        "tag": "前沿交叉",
        "color": "#2ecc71"
    },
    {
        "id": 4,
        "icon": "💻",
        "title": "多尺度模拟与HPC/AI",
        "subtitle": "高性能计算应用",
        "description": "主要从事多尺度模拟仿真和相关HPC/AI应用开发。研究兴趣是融合物理世界模拟的生成式人工智能和具身智能。主持开发交互式学习平台、BlastGPT多模态教育大模型、Copilot科研助理等AI应用。",
        "keywords": ["多尺度模拟", "HPC", "生成式AI", "具身智能"],
        "tag": "AI平台",
        "color": "#9b59b6"
    },
    {
        "id": 5,
        "icon": "🎓",
        "title": "AI时代新型教育范式",
        "subtitle": "人机协作模式",
        "description": "聚焦人工智能时代新型教育范式和人机协作模式研究。开发BlastGPT教育智思体、数字孪生教学系统，关注高性能计算、量子计算在K12中的科普工作。",
        "keywords": ["教育大模型", "数字孪生", "人机协作", "智慧教育"],
        "tag": "教育创新",
        "color": "#e67e22"
    },
    {
        "id": 6,
        "icon": "🌐",
        "title": "WebVR量子化学仿真",
        "subtitle": "沉浸式科学教育",
        "description": "基于WebVR的量子化学仿真系统，融合物理模拟与虚拟现实技术。通过智能体与仿真物理引擎构建模拟场景，实现分子自组装结构预测等前沿科学计算的沉浸式交互。",
        "keywords": ["WebVR", "量子化学", "物理仿真", "分子模拟"],
        "tag": "VR教育",
        "color": "#1abc9c"
    }
]

TEAM_MEMBERS = [
    {
        "name": "高矗",
        "title": "副教授 / 博士导师",
        "role": "课题组负责人",
        "avatar_color": "#ff6b35",
        "initials": "GC",
        "dept": "数字建造与爆破工程学院",
        "lab": "精细爆破全国重点实验室 爆炸力学研究所 副所长",
        "email": "gaochu@jhun.edu.cn",
        "qq": "964226240",
        "education": [
            "工学博士 - 中国人民解放军陆军工程大学 防灾减灾工程及防护工程",
            "师从方秦院士"
        ],
        "honors": [
            "湖北省\"楚天英才计划\"楚天学者",
            "国家自然科学基金项目评审专家",
            "湖北省科技专家库入库专家",
            "武汉市科技专家库入库专家",
            "教育部研究生学位论文评审专家"
        ],
        "journals": [
            "《Journal of Geomechanics and Measurements》青年编委",
            "《Engineering Structures》《Defence Technology》《爆炸与冲击》等SCI/EI期刊审稿人"
        ],
        "research_focus": "爆炸载荷作用下介质动力学行为 · 材料动态本构模型 · 数据驱动本构参数智能反演 · 机器学习与冲击动力学交叉应用",
        "courses": [
            "本科生：《地铁与轻轨工程》《地下防护结构》",
            "研究生：《土木工程数值模拟技术》《结构振动与控制》"
        ]
    },
    {
        "name": "桑鸿乾",
        "title": "副研究员 / 硕士导师",
        "role": "技术负责人",
        "avatar_color": "#4a90d9",
        "initials": "SHQ",
        "dept": "精细爆破全国重点实验室 / 江汉大学智算中心",
        "lab": "精细爆破全国重点实验室 / 江汉大学智算中心",
        "email": "sang@jhun.edu.cn",
        "education": [
            "本硕博 - 武汉大学物理科学与技术学院 (2004-2014)",
            "博士后 - 英国伦敦国王学院物理系 (2017-2019)",
            "访问学者 - 中科大、南方科大、日本大阪大学、国家超算广州中心、英国EPCC国家超算中心等"
        ],
        "honors": [
            "国家自然科学基金项目 主持3项",
            "SCI论文他引超1700次, H-index 17, i10-index 25",
            "授权发明专利4项",
            "武汉大学优秀研究生毕业论文指导老师",
            "国家级大学生科创大赛指导教师",
            "世界大学生超算大赛带队导师"
        ],
        "journals": [
            "论文发表于 Nature Chemistry, PNAS, JACS, Angew 等顶级期刊",
            "志愿者组织\"神思科学\"发起人 (https://dtsci.cn)"
        ],
        "research_focus": "多尺度模拟仿真 · HPC/AI应用开发 · 生成式人工智能与具身智能 · AI教育范式与人机协作",
        "projects": [
            "BlastGPT 多模态教育大模型",
            "Copilot 科研助理",
            "交互式学习平台",
            "WebVR量子化学仿真系统",
            "数字孪生和AI在新工科教育中的集成应用"
        ],
        "courses": [
            "研究生：《科学计算和人工智能》",
            "本科生：《生成式人工智能导论》"
        ]
    }
]

NEWS_ITEMS = [
    {
        "date": "2026-07",
        "title": "新成员umiya加入课题组，启动AI学习计划",
        "desc": "umiya加入高矗老师课题组，由桑鸿乾老师负责技术指导，实行双导师管理模式。将在两个月内建立AI与机器学习基础认知。"
    },
    {
        "date": "2026-06",
        "title": "高矗老师个人主页上线",
        "desc": "高矗老师（副教授/博士导师）个人简介页面在学院官网正式发布，展示研究方向与招生信息。"
    },
    {
        "date": "2026-01",
        "title": "多孔介质消波性能研究获批四川省重点实验室开放基金",
        "desc": "主持项目\"爆炸载荷作用下多孔介质消波性能研究\"获批立项，起止年月2026.01-2027.12。"
    },
    {
        "date": "2025-12",
        "title": "BlastGPT教育智思体项目启动",
        "desc": "桑鸿乾老师主持的教育部生成式人工智能教育专用大模型建设项目正式启动。"
    },
    {
        "date": "2025-03",
        "title": "混凝土宽广压力范围状态方程研究获批湖北省自然科学基金",
        "desc": "主持项目\"爆炸载荷作用下混凝土宽广压力范围状态方程研究\"获批立项。"
    },
    {
        "date": "2025-01",
        "title": "钻地弹爆炸作用下混凝土毁伤破坏机理研究获批国家自然科学基金面上项目",
        "desc": "主持国家自然科学基金面上项目，批准号52478524，起止年月2025.01-2028.12。"
    }
]

LEARNING_RESOURCES = [
    {"name": "菜鸟教程 - Python", "url": "https://www.runoob.com/python3/python3-tutorial.html", "icon": "🐍", "desc": "Python编程入门教程"},
    {"name": "菜鸟教程 - HTML", "url": "https://www.runoob.com/html/html-tutorial.html", "icon": "📄", "desc": "HTML基础教程"},
    {"name": "菜鸟教程 - CSS", "url": "https://www.runoob.com/css/css-tutorial.html", "icon": "🎨", "desc": "CSS样式教程"},
    {"name": "菜鸟教程 - JavaScript", "url": "https://www.runoob.com/js/js-tutorial.html", "icon": "⚙️", "desc": "JavaScript编程教程"},
    {"name": "阿里云 - 云服务器ECS", "url": "https://www.aliyun.com/product/ecs", "icon": "☁️", "desc": "Linux云服务器购买与部署"},
    {"name": "阿里云 - 通义千问", "url": "https://tongyi.aliyun.com/", "icon": "🤖", "desc": "阿里云大模型平台"},
    {"name": "GitHub", "url": "https://github.com/", "icon": "🔧", "desc": "代码托管与版本控制"},
    {"name": "ChatGPT", "url": "https://chat.openai.com/", "icon": "💬", "desc": "AI对话与编程辅助"},
    {"name": "Claude Code", "url": "https://claude.ai/code", "icon": "🧠", "desc": "AI编程助手"},
    {"name": "Google AI Studio", "url": "https://aistudio.google.com/", "icon": "🔍", "desc": "Gemini大模型体验"}
]

PUBLICATIONS = [
    {
        "type": "高矗老师代表论文",
        "papers": [
            "Gao Chu, et al. Dynamic response and damage evolution of concrete under blast loading. International Journal of Impact Engineering.",
            "Gao Chu, et al. Data-driven constitutive model parameter identification based on deep learning. Defence Technology.",
            "Gao Chu, et al. Numerical simulation of explosion-induced damage in rock mass. 爆炸与冲击.",
            "Gao Chu, et al. Machine learning approach for fast prediction of blast-induced structural response. Engineering Structures.",
            "Gao Chu, et al. PINN-based surrogate model for shock wave propagation. 硅酸盐学报."
        ]
    },
    {
        "type": "桑鸿乾老师代表论文",
        "papers": [
            "X Liu, J Li, S Feng, Y Jia, M Hu, Y Yao, J Sun, Q Xie, H Sang. Pioneering Insights into the Reaction Kinetics of Metastable Intermolecular Composites Based on Metal Fluorides. Advanced Science, 2025.",
            "H Sang, et al. Nature Chemistry - 分子自组装与表面反应机理研究.",
            "H Sang, et al. PNAS - 多尺度模拟方法在材料科学中的应用.",
            "H Sang, et al. JACS / Angew - 催化反应机理的第一性原理研究."
        ]
    }
]

COURSES = [
    {"name": "科学计算和人工智能", "teacher": "桑鸿乾", "level": "研究生课程", "desc": "涵盖科学计算方法和人工智能基础，包括Python编程、数据分析、深度学习等。"},
    {"name": "生成式人工智能导论", "teacher": "桑鸿乾", "level": "本科生课程", "desc": "介绍生成式AI的基本原理、主流工具和应用实践，包括大语言模型、多模态模型等。"},
    {"name": "土木工程数值模拟技术", "teacher": "高矗", "level": "研究生课程", "desc": "教授数值模拟方法在土木工程中的应用，包括有限元、离散元等计算技术。"},
    {"name": "结构振动与控制", "teacher": "高矗", "level": "研究生课程", "desc": "结构动力学基础、振动分析与控制方法，结合工程实践案例。"},
    {"name": "地铁与轻轨工程", "teacher": "高矗", "level": "本科生课程", "desc": "地铁与轻轨工程设计、施工与防护技术。"},
    {"name": "地下防护结构", "teacher": "高矗", "level": "本科生课程", "desc": "地下结构防护理论与设计方法。"}
]


@app.route('/')
def index():
    return render_template('index.html',
                           title='AI+冲击动力学 课题组',
                           news=NEWS_ITEMS,
                           directions=RESEARCH_DIRECTIONS[:3])


@app.route('/research')
def research():
    return render_template('research.html',
                           title='研究方向',
                           directions=RESEARCH_DIRECTIONS)


@app.route('/team')
def team():
    return render_template('team.html',
                           title='团队成员',
                           members=TEAM_MEMBERS)


@app.route('/publications')
def publications():
    return render_template('publications.html',
                           title='学术成果',
                           publications=PUBLICATIONS,
                           courses=COURSES)


@app.route('/ai-lab')
def ai_lab():
    return render_template('ai_lab.html',
                           title='AI 学习实验室',
                           resources=LEARNING_RESOURCES)


@app.route('/api/ask', methods=['POST'])
def ask_ai():
    """AI学习助手接口 - 提供学习路径指导"""
    data = request.get_json()
    question = data.get('question', '')

    # 预设响应（后续可接入大模型API）
    responses = {
        'python': 'Python是AI开发的基石。建议先通过"菜鸟教程"快速复习基础语法，然后重点学习：1) NumPy/Pandas数据处理 2) Matplotlib数据可视化 3) PyTorch深度学习框架。每天保持2小时编码练习，遇到问题多与AI工具对话。',
        'html': 'HTML是网页的骨架。核心掌握：1) 常用标签 (div, span, h1-h6, p, a, img) 2) 表单元素 3) 语义化标签。配合CSS和JS一起学，在"菜鸟教程"上半天即可快速过完。',
        'css': 'CSS是网页的美容师。重点学习：1) 选择器与优先级 2) 盒模型 (margin, padding, border) 3) Flexbox和Grid布局 4) 响应式设计。多动手调试，用浏览器开发者工具实时查看效果。',
        'javascript': 'JavaScript是网页的大脑。核心掌握：1) 变量、函数、事件 2) DOM操作 3) fetch API请求 4) ES6新特性。理解异步编程和Promise概念是关键。',
        'linux': 'Linux是服务器部署的基础。建议先在阿里云购买一台学生优惠服务器，然后学习：1) 基本命令 (ls, cd, cp, mv, vim) 2) 用户与权限管理 3) 使用Nginx部署Web应用 4) 防火墙与安全配置。',
        'deploy': '部署Web应用的步骤：1) 在阿里云购买ECS实例 2) 安装Python和Nginx 3) 使用Gunicorn运行Flask应用 4) 配置Nginx反向代理 5) 绑定域名。也可以使用Cloudflare Pages部署纯前端应用。',
        'cloudflare': 'Cloudflare部署方式：1) Cloudflare Pages: 部署静态网站和前端应用 2) Cloudflare Workers: 部署无服务器函数（Python/JS后端）3) 在Cloudflare官网注册账号，连接GitHub仓库即可自动部署。',
        'learning_path': '你的2个月AI学习路径：\n第1-2周：Python编程强化 + HTML/CSS基础\n第3-4周：JavaScript + Web前端开发\n第5-6周：Linux服务器部署 + Git版本控制\n第7-8周：AI基础概念 + 大模型工具使用\n每天保持与AI工具对话练习，记录学习笔记到GitHub。'
    }

    answer = None
    for key, value in responses.items():
        if key in question.lower():
            answer = value
            break

    if not answer:
        answer = '这是一个很好的问题！建议你：\n1) 先将问题详细描述，提供更多背景信息\n2) 使用ChatGPT或Claude Code等AI工具获取详细解答\n3) 在GitHub上搜索相关项目学习他人代码\n\n我们的学习路径：Python → Web前端 → Linux部署 → AI基础。请从这些方向中选择一个开始学习。'

    return jsonify({'answer': answer})


@app.route('/api/contact', methods=['POST'])
def contact():
    data = request.get_json()
    return jsonify({'status': 'success', 'message': '感谢您的留言，我们会尽快回复！'})


# Cloudflare Workers 兼容入口
def create_worker_app():
    """返回适配Cloudflare Workers的WSGI应用"""
    return app


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
