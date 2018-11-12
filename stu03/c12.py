#coding:utf-8
"""
Info:
@author:Netfj@sina.com  @software: PyCharm @file: c12.py @time: 2018/11/9 23:35
"""

class test():
    def __enter__(self):
        print('This is test : enter')
        return 'This is test class --------> '
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('this is test: exit')
        print(exc_type, exc_val, exc_tb)

def get():
    return test()

with get() as t:
    print(t)