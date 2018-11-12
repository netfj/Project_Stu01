#coding:utf-8
"""
@info: 题目：打印出杨辉三角形（要求打印出10行如下图）。
            1
           1 1
          1 2 1
         1 3 3 1
        1 4 6 4 1
       1 5 10 10 5 1
      1 6 15 20 15 6 1
     1 7 21 35 35 21 7 1
    1 8 28 56 70 56 28 8 1
   1 9 36 84 126 126 84 36 9 1　
　
@author:NetFj @software:PyCharm @file:e061.py @time:2018/11/12.23:52
"""


def triangles():
    L = [1]
    while True:
        yield L
        L = [sum(i) for i in zip([0]+L, L+[0])]

# yield 使用浅析:
# http://www.runoob.com/w3cnote/python-yield-used-analysis.html



# a = [1,2,3]
# b = [4,5,6]
#
# c = zip(a,b)
# print(list(c))
#
# d1,d2 = zip(*zip(a,b))
# print(list(d1))
# print(list(d2))

