#coding:utf-8
"""
Info:题目：求1+2!+3!+...+20!的和。
@author:Netfj@sina.com  @software: PyCharm @file: e025.py @time: 2018/11/3 22:17
"""

def jc(n):
    s=1
    for i in range(1,n+1):
        s *= i
    return s

s=0
for i in range(1,20+1):
    s += jc(i)

print(s)


n = 0
s = 0
t = 1
for n in range(1,21):
    t *= n
    s += t
print(('1! + 2! + 3! + ... + 20! = %d') % s)


print('----------------')
s = 0
l = range(1,21)
def op(x):
    r = 1
    for i in range(1,x + 1):
        r *= i
    return r
s = sum(map(op,l))
print(s)
