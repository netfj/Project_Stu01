#coding:utf-8
"""
Info: 题目：一个5位数，判断它是不是回文数。
        即12321是回文数，个位与万位相同，十位与千位相同。
@author:Netfj@sina.com  @software: PyCharm @file: e030.py @time: 2018/11/3 23:10
"""

a=2345432


def yn(a):
    a=str(a)
    for i in range(0,int(len(a)/2)):
        if  not  a[i] == a[-i-1] :
            return False
            break
        else:
            return True

if yn(a):
    print(a,'是回文数')
else:
    print(a, '不是回文数')



