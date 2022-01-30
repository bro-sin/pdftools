import fitz

mainpath = "D:/Chem/大三下/自动控制原理/优化/"
fname = "test.pdf"
doc = fitz.open(mainpath + fname)
for page in doc:
    pix = page.get_pixmap()
    pix.save(mainpath + "out%d.png" % page.number)
    print(page.number)
