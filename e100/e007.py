#coding:utf-8
"""
@info: 题目：将一个列表的数据复制到另一个列表中。
@author:NetFj @software:PyCharm @file:e007.py @time:2018/10/29.21:42
"""
def main():
    pass
if __name__ == "__main__":
    main()

import random

list0 = [random.randint(-100, x) for x in range(91,100)]

list1 = [x for x in range(10)]


list2 = list0[:]

list3 = list1[:]

print(list0)
print(list1)
print(list2)
print(list3)

