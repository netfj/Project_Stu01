#coding:utf-8
"""
Info:题目：两个乒乓球队进行比赛，各出三人。
        甲队为a,b,c三人，乙队为x,y,z三人。
        已抽签决定比赛名单。有人向队员打听比赛的名单。
        a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。
@author:Netfj@sina.com  @software: PyCharm @file: e022.py @time: 2018/11/3 17:09
"""
import itertools
team1=('a','b','c')
team2=[]
notuse=['ax','cx','cz']
pl = itertools.permutations('xyz',3)
for i in pl:
    x = [team1[0]+i[0],team1[1]+i[1],team1[2]+i[2]]
    y = list(set(x).intersection(set(notuse)))
    if len(y)==0:
        team2.append(i)

print('对阵顺序是：')
print('甲队：',team1)
print('乙队：')
for i in team2: print(i)
