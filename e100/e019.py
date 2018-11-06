#coding:utf-8
"""
@info: 题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。
            例如6=1＋2＋3.编程找出1000以内的所有完数。
@author:NetFj @software:PyCharm @file:e019.py @time:2018/11/1.19:53
"""

def ys(n,x,lt):
    for i in range(x,int(n/2)+1):
        if n%i==0:
            lt.append(i)
            return ys(n,i+1,lt)
    return [1]+lt

for x in range(2,1001):
    y = ys(x,2,[])
    if sum(y)==x:
        print(x,end=' --> ')
        print(y)