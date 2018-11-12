#coding:utf-8
"""
Info: 写一个可以测量
@author:Netfj@sina.com  @software: PyCharm @file: c19.py @time: 2018/11/11 7:32
"""

def test(func):
    print('-1------------')
    mynub = 10000
    def inner(x,y):
        print('-2------------')
        return func(x,y)+mynub
    print('-3------------')
    return inner

def add(x,y):
    print('\n= y ===========\n')
    return x+y

new_func = test(add)

print(new_func(1,2))