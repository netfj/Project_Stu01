#coding:utf-8
"""
Info:题目：有一分数序列：
        2/1，3/2，5/3，8/5，13/8，21/13...
        求出这个数列的前20项之和。
@author:Netfj@sina.com  @software: PyCharm @file: e024.py @time: 2018/11/3 21:12
"""

a,b=1,2
l=[]
for n in range(20):
    print(b,a)
    l.append(b/a)
    a,b=b,a+b
print(sum(l))