# Starlight · 社团内训手册

面向社团成员的 Markdown 学习与内训资料站。首版包含第三次内训课件、语法速查和可下载的填空作业包。

站点使用 Zensical 构建，采用 `mkdocs.yml` 配置与 Material 风格主题。GitHub Actions 负责检查、打包和发布。

## 本地运行

需要 Python 3.11 或更新版本；CI 使用 Python 3.14。在仓库根目录执行：

```powershell
python -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
.venv\Scripts\python scripts/package_homework.py
.venv\Scripts\zensical serve
```

macOS / Linux 对应命令：

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python scripts/package_homework.py
.venv/bin/zensical serve
```

打开终端打印的本地预览地址。源码首页是 `docs/index.md`；预览完整站点应使用上面的服务器，避免通过 `file://` 打开构建页面导致搜索或脚本无法加载。

本课使用 Markdown Preview Enhanced（`shd101wyy.markdown-preview-enhanced`）打开预览，使用 Markdown PDF（`yzane.markdown-pdf`）导出。站点发布效果以 Zensical 生成的页面为准。

## 构建与检查

```powershell
.venv\Scripts\python scripts/package_homework.py
.venv\Scripts\zensical build --clean --strict
.venv\Scripts\python scripts/check_site.py
```

静态输出位于 `site/`。链接检查仅访问本地文件，检查页面、图片、脚本和下载附件是否存在，并验证 GitHub Pages 的 `/upskilling/` 路径前缀。

作业源文件位于 `homework/session-03/`，打包脚本将其与配图合并为 `docs/assets/downloads/session-03-homework.zip`。修改题目、答案或配图后重新运行打包命令。

## 发布到 GitHub Pages

1. 将本仓库内容推送到 GitHub 仓库的 `main` 分支。
2. 在仓库 **Settings → Pages → Build and deployment → Source** 选择 **GitHub Actions**。
3. 查看 **Actions → Build and publish handbook**，确认构建和部署任务成功。
4. 通过工作流部署结果里的地址访问网站。按当前配置，地址为 `https://zju-starlight.github.io/upskilling/`。

PR 会检查作业打包、严格构建与本地链接；`main` 更新或在 `main` 手动运行工作流后发布。发布使用 Pages artifact，无需维护生成文件分支，也无需配置个人访问令牌。

迁移仓库或绑定域名时，应同步更新 `mkdocs.yml` 的 `site_url` 与链接检查的 `--base-path`。站内图片和附件使用相对路径。

## 目录

```text
docs/                         网页内容与静态资源
  training/session-03/        第三次内训课件
  assets/downloads/           下载材料
  assets/images/              网站与练习配图
homework/session-03/          填空作业及参考答案源文件
scripts/package_homework.py   作业打包
scripts/check_site.py         构建后链接检查
.github/workflows/pages.yml  检查与发布工作流
mkdocs.yml                   导航、主题和 Markdown 扩展配置
```

新增课程时，建立新的 `docs/training/session-XX/` 目录，并更新 `mkdocs.yml` 中的导航和课程索引。编写约定见 [贡献指南](docs/contributing.md)。

## 技术资料

- [Zensical 构建与严格模式](https://zensical.org/docs/usage/build/)
- [Zensical 发布指南](https://zensical.org/docs/publish-your-site/)
- [GitHub Pages 自定义工作流](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)

依赖固定为官方 PyPI 的 `zensical==0.0.73`。Actions 固定到已核验的官方 release commit，更新时同时检查兼容性与构建结果。
