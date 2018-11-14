#coding:utf-8
"""
@info: 
@author:NetFj @software:PyCharm @file:03_generator.py @time:2018/11/14.17:43
"""

from itertools import *

def fib():
    prev, curr = 0, 1
    while True:
        yield curr
        prev, curr = curr, prev + curr


f = fib()

print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))

b = fib()
c = islice(b,0,10)
d = list(c)
print(d)

