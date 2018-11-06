#coding:utf-8
"""
@info: 题目：有一个已经排好序的数组。
            现输入一个数，要求按原来的规律将它插入数组中。
@author:NetFj @software:PyCharm @file:e040.py @time:2018/11/5.22:49
"""
import random
a=[random.randint(0,100) for x in range(10)]
a.sort()
print(a)

b=random.randint(0,100)
print(b
      )
a.append(b)
a.sort()

print(a)
