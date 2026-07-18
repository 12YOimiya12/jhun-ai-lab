# 🚀 Cloudflare Pages 部署教程 — 零基础手把手

> 本教程适用于：完全没有用过 Cloudflare 的新手。
> 不需要安装任何工具，全程在浏览器中操作。

---

## 📋 准备工作（5分钟）

### 1. 注册 Cloudflare 账号

1. 打开 https://dash.cloudflare.com/sign-up
2. 输入你的邮箱地址，设置密码
3. 点击 "Sign Up" 注册
4. **不需要绑定域名**，跳过域名设置也可以继续

### 2. 准备待上传的文件

1. 打开文件管理器，进入 `dist` 文件夹：
   ```
   C:\Users\umiya\Desktop\studying_in_summer\dist\
   ```

2. 选中 `dist` 文件夹里的所有文件（5个HTML + static文件夹 + 404.html）

3. 右键 → **发送到 → 压缩(zipped)文件夹**

4. 将生成的 ZIP 文件改名为 `website.zip`

---

## 📤 上传部署（3分钟）

### 步骤 1：进入 Cloudflare Pages

1. 登录 https://dash.cloudflare.com/
2. 在左侧菜单找到 **Workers & Pages**（工人和页面）
3. 点击进入后，选择 **Pages** 标签
4. 点击蓝色按钮 **创建项目**

### 步骤 2：上传资产

1. 选择 **Upload assets**（上传资产）标签
2. 点击 **选择文件** 按钮
3. 选择刚才创建的 `website.zip` 文件
4. 项目名称填入：`jhun-ai-lab`（可以改成你喜欢的名字）
5. 点击 **创建项目** 按钮

### 步骤 3：完成！

部署大约需要 10-30 秒。完成后你会看到：

```
🎉 项目已成功部署！

你的网站地址：https://jhun-ai-lab.pages.dev
```

**点击这个地址就能看到你的网站了！**

---

## 🔧 后续更新网站（可选）

如果你之后修改了网站内容，更新很简单：

1. 重新运行 `python freeze.py` 生成新的 HTML 文件
2. 将 `dist` 文件夹重新打包成 ZIP
3. 进入 Cloudflare Pages → 你的项目 → **上传新版本**
4. 拖入新的 ZIP 文件即可

---

## ❓ 常见问题

### Q: 不需要买域名吗？

不需要。Cloudflare 会免费提供 `你的项目名.pages.dev` 格式的域名。

### Q: AI 学习助手的问答功能还能用吗？

静态部署后，`/api/ask` 接口将不可用。替代方案：
- 页面上已经有 ChatGPT、Claude Code、Gemini 等外部 AI 工具的链接
- 你可以直接使用那些工具提问

### Q: 需要付费吗？

Cloudflare Pages 免费额度：
- 每月无限次请求
- 1 个并发构建
- 500 次/月构建
- 对个人学习项目完全够用

### Q: 能用自己的域名吗？

可以。在 Cloudflare Pages 项目设置中点击 **自定义域**，按照提示添加你的域名即可。

---

## 📝 快速部署检查清单

- [ ] 注册 Cloudflare 账号 → https://dash.cloudflare.com/sign-up
- [ ] 运行 `python freeze.py` 生成静态文件
- [ ] 将 `dist` 文件夹打包成 ZIP
- [ ] 进入 Cloudflare Pages → 创建项目 → 上传资产
- [ ] 上传 ZIP 文件 → 等待部署完成
- [ ] 访问 `https://你的项目名.pages.dev` 查看网站

**总共大约 10 分钟就能完成！**
