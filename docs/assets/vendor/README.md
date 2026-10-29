# 本地渲染资源

教学页面的关键脚本与站点一起分发，减少课堂中外部 CDN 的加载依赖。

- MathJax 3.2.2：`mathjax/tex-svg.js`，来自 `https://cdn.jsdelivr.net/npm/mathjax@3.2.2/es5/tex-svg.js`。SVG 输出无需外部字体，许可证见 `mathjax/LICENSE`。
- Mermaid 12.2.0：`mermaid/mermaid.min.js`，来自 `https://cdn.jsdelivr.net/npm/mermaid@12.2.0/dist/mermaid.min.js`，许可证见 `mermaid/LICENSE`。

`overrides/main.html` 按页面内容加载运行时：首页无需加载图表与公式库，课程页使用本地脚本。

升级时保留许可证，并检查公式及流程图在深浅色模式中的实际效果。
