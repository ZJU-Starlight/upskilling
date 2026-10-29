# 03 · HTML 补充排版

**目标：** 用按键提示、折叠内容和图片尺寸解决三个具体的排版需求。

Markdown 可满足常见的文档排版需求，部分排版功能可通过渲染器允许的 HTML 标签实现。不同平台会过滤或限制部分标签，因此需要在目标网页中检查显示效果。

## 使用 `<kbd>` 标记按键

```html
保存文件：<kbd>Ctrl</kbd> + <kbd>S</kbd>
```

保存文件：<kbd>Ctrl</kbd> + <kbd>S</kbd>

## 使用 `<details>` 折叠补充说明

该标签可用于常见问题、说明或参考答案。`<summary>` 定义可点击的折叠标题。

```html
<details>
  <summary>参与准备事项</summary>
  <p>参与者需携带电脑，提前安装 VS Code，并下载本次练习包。</p>
</details>
```

<details>
  <summary>参与准备事项</summary>
  <p>参与者需携带电脑，提前安装 VS Code，并下载本次练习包。</p>
</details>

示例使用 `<p>` 定义内部段落。在 HTML 容器中直接混写 Markdown，可能需要额外的 `md_in_html` 配置。

## 调整图片尺寸

```html
<img src="images/study-desk.png" alt="学习桌面" width="420">
```

<img src="../../assets/images/study-desk.png" alt="学习桌面" width="420">

图片的 `alt` 描述画面，`width` 控制显示宽度。示例假设图片位于当前练习文件旁的 `images` 文件夹；实际路径需与文件目录一致。本站还会限制图片不超过正文宽度，以适应移动端显示。

## 常见错误

- 标签需要正确关闭，例如 `<summary>标题</summary>`。
- 标签属性的引号要成对出现。
- 预览没有按预期显示时，先检查平台是否允许该标签。

## 练习要求

在活动通知中添加“参与准备事项”折叠区域，并使用 `<kbd>` 标记保存文件的快捷键。

完成标准：折叠区域可以展开，内容完整，按键提示清楚。

[继续：Mermaid 流程图](mermaid.md)
