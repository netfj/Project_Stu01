#coding:utf-8
"""
Info: 匿名函数
@author:Netfj@sina.com  @software: PyCharm @file: 01.py @time: 2018/11/3 16:58
"""


A = lambda x, y: x+y
print(A)

AB = list(map(lambda x: x**2, [1, 2, 3, 4, 5, 6, 7, 8, 9]))


def isodd(abc=0):
    '''
    :param abc: a
    :return: a
    '''
    return abc % 2 == 1
L = list(filter(isodd, range(1, 20)))
print(L)
