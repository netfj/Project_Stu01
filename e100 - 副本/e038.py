#coding:utf-8
"""
@info: 题目：求一个3*3矩阵 主 对角线元素之和。
@author:NetFj @software:PyCharm @file:e038.py @time:2018/11/5.22:08
"""
import random
# a = random.randint(-100,100)

m=3
a = [[random.randint(0,10) for n in range(m)] for n in range(m)]
for x in a: print(x)

# 主对角线
s=0
h=len(a[0])
for n in range(h):
    s += a[n][n]
print(s)


print('-------------')

# 两条对角线
s=0
h = len(a[0])
for n in range(0,h):
    print(a[n][n],a[n][h-n-1])
    s += a[n][n]
    s += a[n][h-n-1]

# 奇数时去掉中间的数
if not h%2==0:
    s0 = a[int((h-1)/2)][int((h-1)/2)]
    print('减去重复的中间数:',s0)
    s -= s0
print(s)