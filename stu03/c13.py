#coding:utf-8
"""
Info:
@author:Netfj@sina.com  @software: PyCharm @file: c13.py @time: 2018/11/9 23:52
"""


def fun():
    for i in range(20):
        x=yield i
        print('good',x)

if __name__ == '__main__':
    a=fun()
    a.__next__()
    x=a.send(5)
    print(x)


    x = a.send(11)
    print(x)