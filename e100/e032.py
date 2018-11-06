#coding:utf-8
"""
@info: 题目：按相反的顺序输出列表的值。
@author:NetFj @software:PyCharm @file:e032.py @time:2018/11/5.21:26
"""

w = [1,2,3,4,5,6,7,8]
for n in range(len(w)-1,-1,-1):
    print(w[n])

print('-----------')
for x in reversed(w):
    print(x)

print('=========')
a=w[::-1]
print(a)

print('~~~~~~~~~~~~~~')
print(w[0:2])