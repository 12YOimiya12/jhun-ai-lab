========================================
  阿里云 ECS 部署步骤 — 零基础手把手
========================================

## 第 0 步：购买阿里云服务器（已在会议中提到）

按照桑鸿乾老师的建议，你有两种低成本方案：

  方案A（免费试用）：阿里云新客免费试用，搜索"阿里云免费试用"
  方案B（学生优惠）：阿里云学生认证后，最低不到 10 元/月

推荐配置：
  - 系统：Ubuntu 22.04 或 CentOS 7.9
  - CPU：1 核或 2 核
  - 内存：2 GB
  - 带宽：1 Mbps（按量付费）
  - 系统盘：40 GB


## 第 1 步：登录服务器

购买后在阿里云控制台找到你的服务器公网 IP。

在你本地电脑打开 PowerShell（Win+R → 输入 powershell → 回车），输入：

  ssh root@你的服务器公网IP

首次登录会提示确认，输入 yes 回车。
密码就是买服务器时设置的 root 密码。


## 第 2 步：安装环境（登录服务器后逐条执行）

以下全部在服务器终端里粘贴执行：

  # 更新系统
  sudo apt update && sudo apt upgrade -y

  # 安装 Python 和 pip
  sudo apt install python3 python3-pip python3-venv -y

  # 安装 Nginx（Web 服务器）
  sudo apt install nginx -y

  # 安装 Git
  sudo apt install git -y


## 第 3 步：上传项目代码到服务器

方法一：从 GitHub 拉取（推荐）

  # 在服务器上克隆仓库
  cd /opt
  sudo git clone https://github.com/12YOimiya12/jhun-ai-lab.git
  cd jhun-ai-lab

方法二：从本地上传（如果不用 GitHub）

  在本机 PowerShell 里执行（不是在服务器里）：

    scp -r C:\Users\umiya\Desktop\studying_in_summer root@你的服务器IP:/opt/jhun-ai-lab


## 第 4 步：配置 Python 虚拟环境

  cd /opt/jhun-ai-lab
  python3 -m venv venv
  source venv/bin/activate
  pip install flask gunicorn


## 第 5 步：创建生产环境启动脚本

  cat > /opt/jhun-ai-lab/start.sh << 'EOF'
  #!/bin/bash
  cd /opt/jhun-ai-lab
  source venv/bin/activate
  gunicorn -w 4 -b 127.0.0.1:8000 app:app --daemon --access-logfile /var/log/jhun-lab-access.log --error-logfile /var/log/jhun-lab-error.log
  EOF

  chmod +x /opt/jhun-ai-lab/start.sh


## 第 6 步：配置 Nginx 反向代理

  sudo nano /etc/nginx/sites-available/jhun-ai-lab

将以下内容粘贴进去（把 your-domain 换成你的域名或 IP）：

  server {
      listen 80;
      server_name 你的服务器IP;    # 或者你的域名

      # 静态文件直接由 Nginx 处理
      location /static/ {
          alias /opt/jhun-ai-lab/static/;
          expires 30d;
      }

      # 其他请求转发给 Flask
      location / {
          proxy_pass http://127.0.0.1:8000;
          proxy_set_header Host $host;
          proxy_set_header X-Real-IP $remote_addr;
          proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
      }
  }

保存退出（nano: Ctrl+S 保存 → Ctrl+X 退出），然后：

  # 启用配置
  sudo ln -s /etc/nginx/sites-available/jhun-ai-lab /etc/nginx/sites-enabled/
  sudo rm /etc/nginx/sites-enabled/default   # 删除默认配置

  # 检查配置是否正确
  sudo nginx -t

  # 重启 Nginx
  sudo systemctl restart nginx


## 第 7 步：启动应用

  bash /opt/jhun-ai-lab/start.sh

现在在浏览器输入 http://你的服务器IP 就能看到网站了！


## 第 8 步（可选）：设置开机自启动

  sudo nano /etc/systemd/system/jhun-ai-lab.service

粘贴以下内容：

  [Unit]
  Description=Jianghan University AI+Impact Dynamics Lab
  After=network.target

  [Service]
  User=root
  WorkingDirectory=/opt/jhun-ai-lab
  ExecStart=/opt/jhun-ai-lab/venv/bin/gunicorn -w 4 -b 127.0.0.1:8000 app:app
  Restart=always
  RestartSec=5

  [Install]
  WantedBy=multi-user.target

然后：

  sudo systemctl daemon-reload
  sudo systemctl enable jhun-ai-lab
  sudo systemctl start jhun-ai-lab
  sudo systemctl status jhun-ai-lab   # 查看运行状态


## 第 9 步：配置安全组（阿里云控制台操作）

在阿里云控制台 → ECS → 安全组 → 配置规则 → 添加入方向规则：
  端口：80
  授权对象：0.0.0.0/0
  描述：Web服务

完成后外网才能访问你的服务器。


## 更新网站

以后修改代码后，更新步骤：

  cd /opt/jhun-ai-lab
  git pull                         # 拉取最新代码
  sudo systemctl restart jhun-ai-lab   # 重启服务


========================================
  对比 GitHub Pages vs 阿里云 ECS
========================================

| 特性           | GitHub Pages      | 阿里云 ECS        |
|---------------|-------------------|-------------------|
| 费用           | 免费              | 学生约 10 元/月    |
| 国内访问       | 部分地区不稳定    | 完全可访问         |
| 部署难度       | 上传就行          | 需要 SSH 操作      |
| Flask 后端    | 不支持            | 完整支持           |
| AI 问答 API   | 无法使用          | 可以使用           |
| 适合场景       | 展示型网站         | 完整 Web 应用      |

建议：
  - 短期展示：继续用 GitHub Pages（已经部署好了）
  - 长期使用 + AI问答功能：部署到阿里云
