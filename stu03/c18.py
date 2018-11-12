#coding:utf-8
"""
Info: 装饰器函数 @
@author:Netfj@sina.com  @software: PyCharm @file: c18.py @time: 2018/11/11 7:03
"""

def test(func):
    print('-1------------')
    mynub = 10000
    def inner(x,y):
        print('-2------------')
        return func(x,y)+mynub
    print('-3------------')
    return inner

@test
def add(x,y):
    print('\n= x ===========\n')
    return x+y

print(add(1,2))
