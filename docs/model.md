---
title: 标题
subtitle: 副标题
description: 描述
icon: material/emoticon-happy
---

!!! note "标注标题"
	标注内容   
	可用图标：
	note 笔记
	abstract 摘要
	info 信息
	tip 提示
	success 成功
	question 问题
	warning 警告
	failure 失败
	danger 危险
	bug 错误
	example 示例
	quote 引用   
	设置标题为空可以省略标题和图标

??? note "可折叠标注"
	标注内容

???+ note "默认展开的可折叠标注"
	标注内容

!!! note inline "标注标题"
	内联标注（左侧）

!!! note inline end "标注标题"
	内联标注（右侧）

附注(1)
{ .annotate }

1.  附注内容

[按钮](URL){ .md-button }

```c title="代码块名称" hl_lines="2 3" linenums="2"
代码内容
代码内容
代码内容
```

内联`#!c 代码内容`代码块

=== "选择卡名称1"
	选择卡内容1

=== "选择卡名称2"
	选择卡内容2

|表格项1|表格项1|
|-|-|
|表格内容1|表格内容2|
|表格内容3|表格内容4|

``` mermaid
---
title: 标题
---
flowchart LR
  A[Start] --> B{Error?};
  B -->|Yes| C[Hmm...];
  C --> D[Debug];
  D --> B;
  B ---->|No| E[Yay!];
```
https://mermaid.js.org/syntax/flowchart.html

脚注[^1]脚注[^2]
[^1]: 脚注内容
[^2]:
	脚注内容   
	脚注内容

{--删除--}{++添加++}{~~删除~>添加~~}{==高亮==}{>>注释<<}~下标~^上标^++ctrl+alt+d++

{==
块格式   
块格式
==}

<div class="grid cards" markdown>

- 卡片网格
- 卡片网格
- 卡片网格
- 卡片网格

</div>

<div class="grid" markdown>

通用网格

通用网格

</div>

图标：https://squidfunk.github.io/mkdocs-material/reference/icons-emojis/

![图片名称](#){ align=left }   

无序列表

+ 无序列表
* 无序列表
- 无序列表

有序列表

1. 有序列表
2. 有序列表
3. 有序列表

自定义列表

`列表名称`

: 列表内容

`列表名称`

: 列表内容

任务列表

+ [x] 任务列表
+ [ ] 任务列表

Latex

$$
\cos x=\sum_{k=0}^{\infty}\frac{(-1)^k}{(2k)!}x^{2k}
$$

当且仅当其内核只是单例集$e_G$时，同态$f$ 是单射的，因为否则$\exists a,b\in G$ 和 $a\neq b$ 使得 $f(a)=f(b)$。

[悬停提示](URL "提示内容")

[带引用的悬停提示][引用]

[引用]: URL "提示内容"

详细信息的 内容 查看 那尔斯

*[内容]: 内容的详细