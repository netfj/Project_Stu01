#coding:utf-8
"""
Info:
@author:Netfj@sina.com  @software: PyCharm @file: c14.py @time: 2018/11/10 0:10
"""

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def apply(func,x,y):
    return func(x,y)

print(apply(add,2,1))
print(apply(sub,2,1))


