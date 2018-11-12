#coding:utf-8
"""
Info:
@author:Netfj@sina.com  @software: PyCharm @file: c17.py @time: 2018/11/11 6:46
"""


def test(func):
    print('\nThis is a decorate function!\n【函数名称】'+func.__name__)
    mynum = 100000
    def inner(x,y):
        return func(x,y) + mynum
    return inner

def add(x,y):
    return x+y
def sub(m,n):
    return m-n

a = test(add)
print(a)
print(a(1,2))
print(a(100,-10))

b = test(sub)
print(b(2,1))
print(b(20,15))
