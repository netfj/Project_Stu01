#coding:utf-8
"""
@info:
    题目：古典问题：有一对兔子，
        从出生后第3个月起每个月都生一对兔子，
        小兔子长到第三个月后每个月又生一对兔子，
        假如兔子都不死，问每个月的兔子总数为多少？
@author:NetFj @software:PyCharm @file:e011.py @time:2018/10/29.22:12
"""

t1=1  #装 1 个月大的兔子
t2=0   #装 2 个月大的兔子
t3=0   #装 3 个月大的兔子

n=12

for x in range(1,n+1):
    print(t1+t2+t3,'<--',t1,t2,t3)
    t3 += t2
    t2=t1
    t1=t3