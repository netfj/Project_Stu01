#coding:utf-8
"""
Info:题目：判断101-200之间有多少个素数，并输出所有素数。
素数曾称质数。一个大于1的正整数，如果除了1和它本身以外，
不能被其他正整数整除，就叫素数。如2，3，5，7，11，13，17…。
@author:Netfj@sina.com  @software: PyCharm @file: e012.py @time: 2018/10/30 22:54
"""

s=[]
for n in range(101,200+1):
    a=[]
    print(n,'-----------')
    for x in range(2,int(n/2)+1):
        if n%x==0:
            a.append(x)
    if len(a)==0: s.append(n)
    print('因数是:',a)

print('共 %d 个---->\n' % len(s),s)

#求一个素数的所有
