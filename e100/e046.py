#coding:utf-8
"""
@info: 题目：求输入数字的平方，如果平方运算后小于 50 则退出。
@author:NetFj @software:PyCharm @file:e046.py @time:2018/11/7.13:50
"""

if __name__ == "__main__":
    while 1:
        i = input('Input a number:')
        i = int(i)
        if i**2 >50:
            print('You input :',i)
            break
        else:
            print("The number's square is smaller than 50. Enter again !")



