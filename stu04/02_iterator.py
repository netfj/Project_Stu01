#coding:utf-8
# 构造一个类，即是迭代器（generator），又是生成器(iterator)
from itertools import islice
class fib:
    def __init__(self):
        print('__init__')
        self.prev=0
        self.curr=1
    def __iter__(self):
        print('__iter__')
        return self
    def __next__(self):
        print('__next__')
        value = self.curr
        self.curr += self.prev
        self.prev = value
        return value

f = fib()
for i in range(5):
    print(next(f))  #iterator: 利用了fib类的迭代器性质

c = fib()
print(list(islice(c,0,4)))   # generator: 利用类fib的生成器性质




