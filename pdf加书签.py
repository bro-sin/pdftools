import fitz
from getpath import *

n = int(input("请输入该电子书第一页的pdf页码：")) - 1
tocpath = getopenpath("选择书签的txt文件")
with open(tocpath, encoding="utf-8") as f:
    tocs_text = f.readlines()
    tocs = []
    for i in range(len(tocs_text)):
        temps = tocs_text[i].split(", ")
        tocs.append([int(temps[0]), temps[1], int(temps[2]) + n])
        # tocs[i]分别为level(int), title(str), page(int)
        pass  # 将文本文件转换成书签要求的格式

pdfpath = getopenpath("选择要添加书签的pdf文件")
doc = fitz.open(pdfpath)
# doc.delete_pages([doc.page_count-1])#删除最后一页
doc.set_toc(tocs)
doc.save(getsavepath("选择添加书签后pdf的输出目录"))
doc.close()
