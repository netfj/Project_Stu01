#coding:utf-8
"""
@info: 题目：输出 9*9 乘法口诀表。
@author:NetFj @software:PyCharm @file:e008.py @time:2018/10/29.21:54
"""


def main():
    pass


if __name__ == "__main__":
    main()

for n in range(1,10):
    for m in range (1,n+1):
        print('%d*%d=%d' % (m,n,n*m),end='  ')
    print('\n')