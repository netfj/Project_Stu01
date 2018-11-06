#coding:utf-8
"""
@info: 题目：暂停一秒输出，并格式化当前时间。
@author:NetFj @software:PyCharm @file:e010.py @time:2018/10/29.22:02
"""


def main():
    pass


if __name__ == "__main__":
    main()

import time
m=5
for n in range(m):
    a = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print('pause for %d secend, and time right now is :\n %s'
          % ((m-n),a))

    time.sleep(1)

