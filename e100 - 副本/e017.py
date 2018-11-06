#coding:utf-8
"""
@info: 题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
@author:NetFj @software:PyCharm @file:e017.py @time:2018/11/1.16:45
"""
# c='0'
# while c != '':
# c = input('Input a string:')

c='abc1 2 3 4 5 6[(@#$)]'
y,k,s,q =0,0,0,0
for x in c:
    if x.isalpha():y+=1
    elif x.isspace():k+=1
    elif x.isdigit(): s += 1
    else: q+=1
print(y,k,s,q)

y,k,s,q =0,0,0,0
for n in range(0,len(c)):
    if c[n].isalpha():
        y += 1
    elif c[n].isspace():
        k += 1
    elif c[n].isdigit():
        s += 1
    else:
        q += 1
print(y, k, s, q)