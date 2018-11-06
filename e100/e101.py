#coding:utf-8
"""
Info:需求： 在你的面前有一个n阶的台阶，
        你一步只能上1级或者2级，
        请计算出你可以采用多少种不同的方法爬完这个楼梯？
        输入一个正整数表示这个台阶的级数，
        输出一个正整数表示有多少种方法爬完这个楼梯。
    分析：提炼出题干的意思：用1和2产生不同组合，
        使得他们的和等于台阶的级数，输出有多少种组合方式。
@author:Netfj@sina.com  @software: PyCharm @file: e101.py @time: 2018/11/3 17:19
"""

import itertools

print('product 笛卡尔积（有放回抽样排列）')
for i in itertools.product('xyz', repeat=3):
    print(i)

print('permutations 排列（不放回抽样排列）')
for i in itertools.permutations('xyz', 3):
    print(i)

print('combinations 组合,没有重复（不放回抽样组合）')
for i in itertools.combinations('xyz', 2):
    print(i)

print('combinations_with_replacement 组合,有重复（有放回抽样组合）')
for i in itertools.combinations_with_replacement('xyz', 2):
    print(i)
