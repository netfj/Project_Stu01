#coding:utf-8
"""
Info:题目：给一个不多于5位的正整数，要求：
        一、求它是几位数，二、逆序打印出各位数字。
@author:Netfj@sina.com  @software: PyCharm @file: e029.py @time: 2018/11/3 22:58
"""

def g(n):
    print('它是 ',len(str(n)),' 位数')
    print('逆序：',int(str(n)[::-1]))

n=1
while n>0:
    n=int(input('Input a number:'))
    g(n)
