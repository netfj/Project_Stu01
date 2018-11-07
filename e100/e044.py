#coding:utf-8
"""
Info: 两个 3 行 3 列的矩阵，
    现其对应位置的数据相加，并返回一个新矩阵：
@author:Netfj@sina.com  @software: PyCharm @file: e044.py @time: 2018/11/6 19:44
"""
import random
m=3
n=4
a = [[random.randint(0,10) for i in range(m)] for p in range(n)]
b = [[random.randint(0,10) for i in range(m)] for p in range(n)]
for x in a: print(x)
print('-----')
for x in b: print(x)
print('-----')

c = [
    [a[x][y]+b[x][y] for x in range(n)] for y in range(m)
]

for x in c: print(x)
print('=========')
c = [
    [c[x][y] for x in range(m)] for y in range(n)
]

for x in c: print(x)