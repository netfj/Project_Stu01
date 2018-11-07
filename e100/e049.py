#coding:utf-8
"""
@info: 题目：使用lambda来创建匿名函数。
@author:NetFj @software:PyCharm @file:e049.py @time:2018/11/7.14:01
"""

# lambda 典型应用
from functools import reduce
lt = [-1,-2,-3,0,1000,200,30,6]
# 1.过滤 filter
a = list(filter(lambda x: x>0, lt))
# 2.映射 map
b = list(map(lambda x: x*2, lt))
# 3.累积 reduce
c = reduce(lambda x,y: x+y, lt )
# 4.排序 sorted 用于指定对列表中所有元素进行排序的准则
d=sorted(lt, key=lambda x: abs(0-x))   #将列表按照元素与0距离从小到大进行排序
print(a)
print(b)
print(c)
print(d)
