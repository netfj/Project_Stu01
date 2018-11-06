#coding:utf-8
"""
@info: 题目：将一个正整数，分解质因数。例如：输入90,打印出90=2*3*3*5。
@author:NetFj @software:PyCharm @file:e014.py @time:2018/10/31.9:14
"""

#使用递归的方法

def ys(n,lt=[]):
    for x in range(2,int(n/2)):
        if n%x==0:
            lt.append(x)
            return ys(n/x,lt)
    lt.append(int(n))
    return lt

print(ys(761))