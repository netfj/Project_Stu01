#coding:utf-8
"""
@info:题目：按逗号分隔列表。
@author:NetFj @software:PyCharm @file:e033.py @time:2018/11/5.21:37
"""


w = [1,2,3,4,5,6]

a = ','.join(str(n) for n in w)
print(a)

