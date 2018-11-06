#coding:utf-8
"""
@info: 题目：暂停一秒输出。
@author:NetFj @software:PyCharm @file:e009.py @time:2018/10/29.21:59
"""


def main():
    pass


if __name__ == "__main__":
    main()


import time
m=5
for n in range(m):
    print('pause for %d secend...' % (m-n))
    time.sleep(1)