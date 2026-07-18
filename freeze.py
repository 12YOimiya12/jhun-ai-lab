"""
将 Flask 模板渲染为静态 HTML 文件，用于 Cloudflare Pages 部署。
运行此脚本后，所有页面会导出到 dist/ 目录。
"""
import os
import sys

# Ensure current dir is the project root
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from app import app, RESEARCH_DIRECTIONS, TEAM_MEMBERS, NEWS_ITEMS, LEARNING_RESOURCES, PUBLICATIONS, COURSES

DIST_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dist')

# 确保目录存在
os.makedirs(os.path.join(DIST_DIR, 'static', 'css'), exist_ok=True)
os.makedirs(os.path.join(DIST_DIR, 'static', 'js'), exist_ok=True)
os.makedirs(os.path.join(DIST_DIR, 'api'), exist_ok=True)

# 复制静态文件
import shutil
static_src = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
static_dst = os.path.join(DIST_DIR, 'static')
shutil.copytree(static_src, static_dst, dirs_exist_ok=True)

# 渲染所有页面
with app.test_client() as client:
    pages = [
        ('/', 'index.html'),
        ('/research', 'research.html'),
        ('/team', 'team.html'),
        ('/publications', 'publications.html'),
        ('/ai-lab', 'ai_lab.html'),
    ]

    for route, filename in pages:
        resp = client.get(route)
        if resp.status_code == 200:
            html = resp.data.decode('utf-8')
            # 修正静态资源路径：从 url_for 改为相对路径
            html = html.replace('/static/', 'static/')
            filepath = os.path.join(DIST_DIR, filename)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f'[OK] {route} -> {filename} ({len(html)} bytes)')
        else:
            print(f'[FAIL] {route} failed: {resp.status_code}')

# 创建 404 页面
with open(os.path.join(DIST_DIR, '404.html'), 'w', encoding='utf-8') as f:
    f.write('''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 - 页面未找到 | AI+冲击动力学课题组</title>
    <style>
        body { font-family: sans-serif; background: #0a0a0f; color: #e8e8f0; display: flex; align-items: center; justify-content: center; height: 100vh; margin: 0; text-align: center; }
        h1 { font-size: 6rem; color: #ff6b35; margin: 0; }
        a { color: #4a90d9; }
    </style>
    <meta http-equiv="refresh" content="3;url=/">
</head>
<body>
    <div>
        <h1>404</h1>
        <p>页面未找到，3 秒后跳转到首页...</p>
        <p><a href="/">立即返回首页</a></p>
    </div>
</body>
</html>''')

print(f'\n[DONE] All files exported to: {DIST_DIR}')
print(f'  -> Zip the {DIST_DIR}/ folder and upload to Cloudflare Pages')
