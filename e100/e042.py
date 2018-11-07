#coding:utf-8
"""
Info: 题目：学习使用auto定义变量的用法。
@author:Netfj@sina.com  @software: PyCharm @file: e042.py @time: 2018/11/6 19:12
"""

def autoadd(n=0):
    if not 'autoadd_variable' in globals():
        global autoadd_variable
        autoadd_variable = n
    autoadd_variable += 1
    return autoadd_variable




if __name__ == "__main__":
    a = autoadd(100)
    print(a)
    a = autoadd()
    print(a)
    a = autoadd()
    print(a)

    del autoadd_variable
    a = autoadd()
    print(a)
    a = autoadd()
    print(a)
    a = autoadd()
    print(a)

