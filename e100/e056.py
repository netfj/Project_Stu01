#coding:utf-8
"""
Info: 题目：画图，学用circle画圆形。
@author:Netfj@sina.com  @software: PyCharm @file: e056.py @time: 2018/11/10 22:13
"""

if __name__ == '__main__':

    from tkinter import *

    canvas = Canvas(width=500, height=400, bg='yellow')
    canvas.pack(expand=YES, fill=BOTH)
    k = 1
    j = 1
    for i in range(0, 30):
        canvas.create_oval(210 - k, 200 - k, 210 + k, 200 + k, width=1)
        k += j
        j += 0.3
    mainloop()


