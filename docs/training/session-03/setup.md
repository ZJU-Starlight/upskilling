# 01 · 环境准备

**目标：** 安装 VS Code、Markdown Preview Enhanced 和 Markdown PDF，创建 Markdown 文件，完成预览与 PDF 导出。

## 下载与安装 VS Code

从 [VS Code 官方下载页](https://code.visualstudio.com/download) 选择与操作系统和处理器架构匹配的安装包。软件更新后，按钮和界面可能略有变化，以官网下载页为准。

| 系统 | 操作步骤 |
| --- | --- |
| Windows | 下载安装程序，按向导完成安装；打开 VS Code 后，选择“文件 → 打开文件夹” |
| macOS | 下载适合 Intel 或 Apple 芯片的版本，将应用拖入“应用程序”，再打开资料文件夹 |
| Linux | 按发行版选择 `.deb`、`.rpm` 或其他官方方式安装，再用 VS Code 打开资料文件夹 |

解压作业文件夹，用 VScode 打开。

## 安装课程所用插件

在 VS Code 的扩展面板中搜索以下插件，核对扩展 ID 后安装。本课程使用 Markdown Preview Enhanced 预览文档，使用 Markdown PDF 导出 PDF。

| 插件 | 扩展 ID | 课程用途 |
| --- | --- | --- |
| [Markdown Preview Enhanced](https://marketplace.visualstudio.com/items?itemName=shd101wyy.markdown-preview-enhanced) | `shd101wyy.markdown-preview-enhanced` | 预览 Markdown、HTML、Mermaid 图表和数学公式 |
| [Markdown PDF](https://marketplace.visualstudio.com/items?itemName=yzane.markdown-pdf) | `yzane.markdown-pdf` | 将 Markdown 文档导出为 PDF |

## 创建 Markdown 文件

在左侧资源管理器中新建 `practice.md`，输入：

```markdown
# 社团内训笔记

本节介绍 **Markdown** 的基础用法。

- 创建文件
- 打开预览
- 完成基础练习
```

保存文件，然后通过命令面板执行 **Markdown Preview Enhanced: Open Preview to the Side**，打开右侧预览。简体中文界面中的命令名称为 **MPE:打开侧边预览**；也可在 Markdown 编辑区右键菜单中选择该命令。

| 操作 | Windows / Linux | macOS |
| --- | --- | --- |
| 保存 | `Ctrl + S` | `⌘ + S` |
| 命令面板 | `Ctrl + Shift + P` | `⌘ + Shift + P` |
| 扩展面板 | `Ctrl + Shift + X` | `⌘ + Shift + X` |

> 源码区用于编辑文档，预览区用于检查渲染结果。修改并保存文件后，预览区会更新显示内容。

## 导出 PDF

1. 保存待导出的 `.md` 文件，并使其处于当前编辑状态。
2. 打开命令面板，执行 **Markdown PDF: Export (pdf)**；也可在 Markdown 编辑区右键菜单中选择同名命令。
3. 打开生成的 PDF，检查标题、表格、图片、图表、公式和分页结果。

## 练习要求

1. 将示例标题修改为“Markdown 基础练习”。
2. 增加一个列表项，并使用 Markdown Preview Enhanced 检查预览。
3. 分别输入 `#没有空格` 与 `# 有空格`，比较显示结果。
4. 使用 Markdown PDF 导出文档，检查 PDF 中的标题、列表和文字排版。

完成标准：能够保存 `.md` 文件，使用 Markdown Preview Enhanced 打开预览，并使用 Markdown PDF 完成导出。

[继续：Markdown 基础](basics.md)
