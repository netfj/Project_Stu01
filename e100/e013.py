#coding:utf-8
"""
Info:题目：打印出所有的"水仙花数"，
所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
@author:Netfj@sina.com  @software: PyCharm @file: e013.py @time: 2018/10/30 23:14
"""

for n in range(100,1000):
    a=int(str(n)[0:1])
    b=int(str(n)[1:2])
    c=int(str(n)[2:3])
    if a**3+b**3+c**3==n:
        print(n)