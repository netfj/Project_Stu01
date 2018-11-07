#coding:utf-8
"""
Info:题目：模仿静态变量(static)另一案例。
@author:Netfj@sina.com  @software: PyCharm @file: e043.py @time: 2018/11/6 19:43
"""

class static():
    var = 0
    def get(self):
        self.var += 1
        return self.var

a = static()
b = static()
for i in range(5):
    print(a.get(),b.get())

