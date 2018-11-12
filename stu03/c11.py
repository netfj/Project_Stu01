#coding:utf-8
"""
@info: with
@author:NetFj @software:PyCharm @file:c11.py @time:2018/11/9.12:47
"""


class Sample:
    def __enter__(self):
        print('enter')
        return self

    def __exit__(self, type, value, trace):
        print('exit')
        print("type:", type)
        print("value:", value)
        print("trace:", trace)

    def do_something(self):
        bar = 1/0
        return bar + 10


with Sample() as sample:
    a = sample.do_something()
    print(a)
