#coding:utf-8
"""
@info: 题目：模仿静态变量的用法。
@author:NetFj @software:PyCharm @file:e041.py @time:2018/11/6.0:05
"""

class static_variable():
    def __init__(self,n=0):
        self.var = n
    def set_var(self,n):
        self.var = n
    def get_var(self):
        return self.var




if __name__ == "__main__":
    a = static_variable(100)
    b = static_variable(200)
    c = static_variable('test')
    print(a.get_var())
    print(b.get_var())
    print(c.get_var())

    a.set_var(0)
    b.set_var(0)
    c.set_var('')

    print(a.get_var())
    print(b.get_var())
    print(c.get_var())


print('-----------')
class static():
    var = 0
    def get(self):
        self.var += 1
        return self.var

a = static()
b = static()
for i in range(5):
    print(a.get(),b.get())