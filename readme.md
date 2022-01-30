# pdftools

写的一些自己可能需要用到的pdf工具，主要用的是Python的`PyMuPDF`包

## `getpath.py`

获取文件路径用的

## `pdf加书签`

功能就如这个名字

其中目录文件的格式要求为：

```
目录层级(int), 目录标题(str), 所在页码(int)
```

例如：

```
1, 一级标题, 1
2, 二级标题, 3
```

