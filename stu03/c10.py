#coding:utf-8
"""
@info: 
@author:NetFj @software:PyCharm @file:c10.py @time:2018/11/8.23:44
"""


def count():
    a = 1
    b = 1
    def sum():
        c = 1
        return a + c  # a - 自由变量
    return sum

a=100
print(list(count()))
