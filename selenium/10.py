#coding:utf-8
"""
info:   
author: NetFj@sina.com
file:   10.py 
time:   2019/2/25.21:16
"""

def get_random(n):
    import random
    return random.randint(0, n)


for i in range(10):
    print(get_random(10))

