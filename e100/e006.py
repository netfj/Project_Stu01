#coding:utf-8
"""
@author: NetFj
@contact: netfj@sina.com
@software: PyCharm
@file: e006.py
@time: 2018/10/29 20:19
"""
'''
题目：斐波那契数列。
程序分析：斐波那契数列（Fibonacci sequence），
    又称黄金分割数列，指的是这样一个数列：
    0、1、1、2、3、5、8、13、21、34、……。
在数学上，费波那契数列是以递归的方法来定义：
'''

def main():
    pass


if __name__ == "__main__":
    main()

#终止数
def fb_out_max(a=0,b=1,max_out=100,l=[]):
    if len(l)==0:
        l.append(a)
    if a+b>=max_out:
        return l
    a, b = b, a + b
    l.append(b)
    return fb_out_max(a, b, max_out, l)

#个数
def fb_n(a=0,b=1,n=10,l=[]):
    if len(l)==0:
        l.append(a)
    if len(l)>=n:
       return l
    a,b=b,a+b
    l.append(b)
    return fb_n(a,b,n,l)


print(fb_out_max(0,1,100))

print(fb_n(0,1,8))

