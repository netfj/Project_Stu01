#coding:utf-8
"""
Info: 题目：画图，学用rectangle画方形。
@author:Netfj@sina.com  @software: PyCharm @file: c058.py @time: 2018/11/11 22:09
"""


from tkinter import *
root = Tk()
canvas = Canvas(root)
canvas.create_rectangle(10,10,200,200)
canvas.pack()
root.mainloop()


canvas = Canvas()
canvas.pack()
mainloop()
