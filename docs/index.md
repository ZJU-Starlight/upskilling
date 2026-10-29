---
title: 首页
description: 第三次社团内训资料，包括 VS Code 配置、Markdown 语法、HTML、Mermaid、LaTeX 数学公式及配套练习。
hide:
  - navigation
  - toc
  - footer
---

<div class="notebook-home">

<section class="nb-hero" aria-labelledby="home-title">
  <div class="nb-hero-copy">
    <div class="nb-eyebrow"><span class="nb-status-dot"></span> STARLIGHT NOTEBOOK <span class="nb-eyebrow-divider">/</span> 内训手册</div>
    <p class="nb-chapter">第三次社团内训 <strong>03</strong></p>
    <h1 id="home-title">社团内训资料<br><span>Markdown 文档编写</span></h1>
    <p class="nb-hero-description">本次课程介绍 VS Code 配置与 Markdown 基础语法，<br class="nb-desktop-break">以及 HTML、Mermaid 图表和 LaTeX 数学公式。</p>
    <div class="nb-actions">
      <a class="nb-button nb-button-primary" href="training/session-03/">查看第三次内训 <span aria-hidden="true">↗</span></a>
      <a class="nb-button nb-button-quiet" href="assets/downloads/session-03-homework.zip" download>下载作业包 <span aria-hidden="true">↓</span></a>
    </div>
    <div class="nb-hero-meta"><span>入门课程</span><span>建议课时 120 分钟</span><span>含配套练习</span></div>
  </div>
  <div class="nb-hero-art">
    <img src="assets/images/notebook-garden.png" width="1536" height="1024" alt="打开的笔记本与电脑，周围连接着排版卡片、流程节点和数学符号" fetchpriority="high">
    <div class="nb-art-note"><span class="nb-tiny-star" aria-hidden="true">✦</span><span>文档、流程图与数学公式</span></div>
  </div>
</section>

<div class="nb-chapter-strip">
  <span class="nb-strip-label">本期主题</span>
  <strong>Markdown 写作与排版</strong>
  <span class="nb-strip-description">文档结构 · 图表表示 · 数学排版</span>
  <a href="training/session-03/">课程总览 <span aria-hidden="true">→</span></a>
</div>

<section class="nb-learning" aria-labelledby="learning-title">
  <div class="nb-section-heading">
    <div><p class="nb-kicker">COURSE OUTLINE</p><h2 id="learning-title">课程内容与学习顺序</h2></div>
    <p>课程分为六个单元，涵盖环境配置、语法与综合练习。</p>
  </div>
  <div class="nb-learning-grid">
    <ol class="nb-path">
      <li><a href="training/session-03/setup/"><span class="nb-step-number">01</span><span class="nb-step-copy"><strong>VS Code 安装与配置</strong><span>软件下载、插件安装与预览功能</span></span><span class="nb-step-time">15 分钟</span><span class="nb-step-arrow" aria-hidden="true">↗</span></a></li>
      <li><a href="training/session-03/basics/"><span class="nb-step-number">02</span><span class="nb-step-copy"><strong>Markdown 基础语法</strong><span>标题、列表、链接、图片与代码块</span></span><span class="nb-step-time">30 分钟</span><span class="nb-step-arrow" aria-hidden="true">↗</span></a></li>
      <li><a href="training/session-03/html/"><span class="nb-step-number">03</span><span class="nb-step-copy"><strong>HTML 排版补充</strong><span>按键提示、折叠说明与图片尺寸</span></span><span class="nb-step-time">10 分钟</span><span class="nb-step-arrow" aria-hidden="true">↗</span></a></li>
      <li><a href="training/session-03/mermaid/"><span class="nb-step-number">04</span><span class="nb-step-copy"><strong>Mermaid 流程图</strong><span>节点、连线与判断分支</span></span><span class="nb-step-time">15 分钟</span><span class="nb-step-arrow" aria-hidden="true">↗</span></a></li>
      <li><a href="training/session-03/math/"><span class="nb-step-number">05</span><span class="nb-step-copy"><strong>LaTeX 数学公式</strong><span>行内公式、分式、根号与求和</span></span><span class="nb-step-time">15 分钟</span><span class="nb-step-arrow" aria-hidden="true">↗</span></a></li>
      <li><a href="training/session-03/exercises/"><span class="nb-step-number">06</span><span class="nb-step-copy"><strong>综合练习与结果检查</strong><span>完成语法填空，检查活动说明书的渲染结果</span></span><span class="nb-step-time">35 分钟</span><span class="nb-step-arrow" aria-hidden="true">↗</span></a></li>
    </ol>
    <div class="nb-demo-column">
      <div class="nb-demo" data-demo>
        <div class="nb-demo-toolbar"><span class="nb-window-dots" aria-hidden="true"><i></i><i></i><i></i></span><span class="nb-demo-filename">session-03.md</span><span class="nb-demo-language">Markdown</span></div>
        <div class="nb-demo-tabs" role="tablist" aria-label="Markdown 示例视图"><button type="button" id="demo-source-tab" role="tab" aria-selected="true" aria-controls="demo-source" tabindex="0">源码</button><button type="button" id="demo-preview-tab" role="tab" aria-selected="false" aria-controls="demo-preview" tabindex="-1">渲染结果</button></div>
        <div id="demo-source" class="nb-demo-panel" role="tabpanel" aria-labelledby="demo-source-tab" tabindex="0">
          <pre class="nb-sample-code"><code><span class="nb-code-muted" data-line="01" aria-hidden="true"></span>  <span class="nb-code-heading"># 第三次内训记录</span>
<span class="nb-code-muted" data-line="02" aria-hidden="true"></span>
<span class="nb-code-muted" data-line="03" aria-hidden="true"></span>  本次课程使用 <span class="nb-code-highlight">**Markdown**</span> 编写文档。
<span class="nb-code-muted" data-line="04" aria-hidden="true"></span>
<span class="nb-code-muted" data-line="05" aria-hidden="true"></span>  <span class="nb-code-teal">## 练习检查清单</span>
<span class="nb-code-muted" data-line="06" aria-hidden="true"></span>
<span class="nb-code-muted" data-line="07" aria-hidden="true"></span>  - [x] 完成标题与列表
<span class="nb-code-muted" data-line="08" aria-hidden="true"></span>  - [ ] 添加活动流程图
<span class="nb-code-muted" data-line="09" aria-hidden="true"></span>  - [ ] 检查公式与图片
<span class="nb-code-muted" data-line="10" aria-hidden="true"></span>
<span class="nb-code-muted" data-line="11" aria-hidden="true"></span>  <span class="nb-code-quote">&gt; 引用内容使用大于号标记。</span></code></pre>
        </div>
        <div id="demo-preview" class="nb-demo-panel nb-sample-preview" role="tabpanel" aria-labelledby="demo-preview-tab" tabindex="0" hidden>
          <h3>第三次内训记录</h3><p>本次课程使用 <strong>Markdown</strong> 编写文档。</p><h4>练习检查清单</h4><ul class="nb-preview-checklist"><li><span class="nb-check-done" aria-hidden="true">✓</span> 完成标题与列表</li><li><span class="nb-check-empty" aria-hidden="true"></span> 添加活动流程图</li><li><span class="nb-check-empty" aria-hidden="true"></span> 检查公式与图片</li></ul><blockquote>引用内容使用大于号标记。</blockquote>
        </div>
        <div class="nb-demo-bottom"><span><span class="nb-status-dot"></span> Markdown 源码与渲染结果</span><span>UTF-8</span></div>
      </div>
      <p class="nb-demo-caption"><span aria-hidden="true">↖</span> 示例提供同一段 Markdown 的源码与渲染结果。</p>
      <a class="nb-quick-reference" href="cheatsheet/"><span class="nb-reference-symbol" aria-hidden="true">Aa</span><span><strong>Markdown 语法速查</strong><span>常用语法、代码示例与兼容性说明。</span></span><span aria-hidden="true">→</span></a>
    </div>
  </div>
</section>

<section class="nb-homework" aria-labelledby="homework-title">
  <div class="nb-homework-copy"><p class="nb-kicker">PRACTICE MATERIALS</p><h2 id="homework-title">第三次内训配套作业</h2><p>作业包含 12 道填空题，覆盖本次课程的主要语法。<br>题目以社团活动通知为例，附起始文件、图片和参考答案。</p><div class="nb-homework-tags"><span>Markdown 起始文件</span><span>练习配图</span><span>独立参考答案</span></div><div class="nb-actions"><a class="nb-button nb-button-teal" href="assets/downloads/session-03-homework.zip" download>下载填空作业包 <span aria-hidden="true">↓</span></a><a class="nb-text-link" href="training/session-03/exercises/">查看作业说明 <span aria-hidden="true">→</span></a></div><p class="nb-download-note">ZIP 格式 · 使用 VS Code 编辑 · 参考答案独立存放</p></div>
  <div class="nb-homework-art"><img src="assets/images/study-desk.png" width="1672" height="941" alt="米白色的练习笔记本、靛蓝与杏橙色铅笔和学习卡片" loading="lazy"><span class="nb-homework-sticker">练习册 <strong>03</strong></span></div>
</section>

<section class="nb-bottom-links" aria-label="相关资源">
  <a href="training/"><span class="nb-bottom-icon" aria-hidden="true">▤</span><span><strong>课程资料目录</strong><span>内训课件、练习及参考资料按场次归档。</span></span><span aria-hidden="true">↗</span></a>
  <a href="contributing/"><span class="nb-bottom-icon nb-bottom-icon-teal" aria-hidden="true">✦</span><span><strong>文档维护与贡献</strong><span>内容修订、资料补充与提交规范。</span></span><span aria-hidden="true">↗</span></a>
</section>

<footer class="nb-home-footer"><span><span aria-hidden="true">✦</span> STARLIGHT</span><p>社团内训课件与技术文档归档</p><a href="https://github.com/ZJU-Starlight/upskilling">在 GitHub 查看手册 <span aria-hidden="true">↗</span></a></footer>

</div>
