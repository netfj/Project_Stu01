#coding:utf-8
"""
Info:
@author:Netfj@sina.com  @software: PyCharm @file: c16.py @time: 2018/11/10 0:45
"""

def outer():
    x=1
    def inner():
        print(x)
    return inner

foo = outer()
print(foo)
print(foo())
