#coding:utf-8
"""
Info:题目：打印出如下图案（菱形）
@author:Netfj@sina.com  @software: PyCharm @file: e023.py @time: 2018/11/3 20:52
"""

max=11
for n in range(1,max+1,2):
    print(('*'*n).center(max))
for m in range(max-2,0,-2):
    print(('*' * m).center(max))

