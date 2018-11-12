#coding:utf-8
"""
Info:
@author:Netfj@sina.com  @software: PyCharm @file: c15.py @time: 2018/11/10 0:29
"""

def decorate(func):
    def inner(a,b):
        ret =func(a,b)
        return abs(ret)
    return inner
def sub(a,b):
    return a-b

print(sub(3,4))

s = decorate(sub)
print(s(3,4))

