#coding:utf-8
"""
@info: 题目：请输入星期几的第一个字母来判断一下是星期几，
            如果第一个字母一样，则继续判断第二个字母。
@author:NetFj @software:PyCharm @file:e031.py @time:2018/11/5.12:17
"""


def sel(w,n=1):
    print(w)
    s = input('输入星期的第 %d 个字母:' % n)
    a = list(filter(lambda x: x[n - 1].upper() == s.upper(), w))
    if len(a)==1:
        return a
    return sel(a,n+1)

w = ('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')
print(sel(w))



# 列表解析法
data = [-2,-1,0,1,2,3]
a = [x for x in data if x >=0 ]
print(a)