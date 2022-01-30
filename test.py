from PyPDF2 import PdfFileReader as reader, PdfFileWriter as writer
import fitz

book = reader("test.pdf")
print(book.outlines)

pdf = writer()

for i in range(book.getNumPages()):
    pdf.addPage(book.getPage(i))
    pass
n = 10

pdf.addBookmark("目录", 7)
marks = [
    ["过程控制概论", 1],
    ["过程动态特征", 17],
    ["反馈控制", 48],
    ["前馈控制和比值控制", 65],
    ["其他典型控制系统", 85],
    ["计算机控制系统", 125],
    ["多回路控制系统分析与设计", 147],
    ["基于模型的控制方法", 167],
    ["间歇过程控制", 192],
    ["传热设备的控制", 211],
    ["精馏塔的控制", 238],
    ["化学反应过程控制", 274],
    ["参考文献", 298]
]
for mark in marks:
    pdf.addBookmark(mark[0], mark[1] + n)
    pass

with open("out.pdf", "wb") as f:
    pdf.write(f)
    # pdf.write("out.pdf")
    pass

if __name__ == '__main__':
    print("hello pdf")
