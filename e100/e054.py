#coding:utf-8
"""
@info: 题目：取一个整数a从右端开始的4〜7位。
@author:NetFj @software:PyCharm @file:e054.py @time:2018/11/8.0:29
"""

a=192803470981234

b=str(a)[-7:-3][::-1]
c=str(a)[-4:-8:-1]
e= ''.join(str(a)[i] for i in range(len(str(a))-4, 7, -1))

print(b)
print(c)

print(e)

