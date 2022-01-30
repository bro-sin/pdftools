import tkinter.filedialog as tf


def getopenpath(title):
    path = tf.askopenfilename(title=title, filetypes=[("pdf", "*.pdf"), ("txt", "*.txt"), ("所有", "*.*")])
    # print(path)
    return path


def getsavepath(title):
    path = tf.asksaveasfilename(title=title, filetypes=[("pdf", "*.pdf"), ("所有", "*.*")])
    # print(path)
    return path
