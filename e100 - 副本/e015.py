#coding:utf-8
"""
@info: 题目：利用条件运算符的嵌套来完成此题：
            学习成绩>=90分的同学用A表示，
            60-89分之间的用B表示，60分以下的用C表示。
@author:NetFj @software:PyCharm @file:e015.py @time:2018/10/31.9:28
"""
a=0
while a>=0:
    a=input('输入一个大于0的数：')
    a=int(a)
    if a>=90:
        g='A'
    elif a>=60 and a<90:
        g='B'
    elif a<60 and a>=0:
        g='C'
    print('你的成绩评定等级：',g)
