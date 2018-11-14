#coding:utf-8
"""
Info: 题目：利用递归方法求5!。
@author:Netfj@sina.com  @software: PyCharm @file: e026.py @time: 2018/11/3 22:32
"""


m=5

def jc(n,s=1):
    if n==0: return s
    s *= n
    return jc(n-1,s)

print(jc(m))