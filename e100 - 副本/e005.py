#coding:utf-8
"""
@author: NetFj
@contact: netfj@sina.com
@software: PyCharm
@file: e005.py
@time: 2018/10/29 20:19
"""
'''
题目：输入三个整数x,y,z，请把这三个数由小到大输出。
'''

def main():
    pass


if __name__ == "__main__":
    main()

l=[]
while True:
    a=input('输入一个数（直接回车结束）：')
    if a=='':
        break
    l.append(a)
    print(l)

l.sort()

print(l)