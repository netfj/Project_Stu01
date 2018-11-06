#coding:utf-8
"""
@info: 题目：求100之内的素数。
        质数（prime number）又称素数，有无限个。
        质数定义为在大于1的自然数中，除了1和它本身以外不再有其他因数。
@author:NetFj @software:PyCharm @file:e035.py @time:2018/11/5.21:54
"""


def ss(n):
    for x in range(2,int(n/2)+1):
        if n%x==0:
            return False
    return True

a=[]
for i in range(1,101):
    if ss(i)==True:
        a.append(i)

print(a)

