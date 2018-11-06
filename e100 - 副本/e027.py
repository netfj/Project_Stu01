#coding:utf-8
"""
Info:题目：利用递归函数调用方式，
        将所输入的5个字符，以相反顺序打印出来。
@author:Netfj@sina.com  @software: PyCharm @file: e027.py @time: 2018/11/3 22:38
"""

st = '12345'

def out(st,bk=''):
    if len(st)==0: return bk
    bk+=st[-1]
    st=st[0:-1]
    return out(st,bk)

print(out(st))

