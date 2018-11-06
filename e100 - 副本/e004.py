# -*- coding: UTF-8 -*-
'''
题目：输入某年某月某日，判断这一天是这一年的第几天？
'''

import time

dt_input = '2019-12-31'

# 将输入的字符型日期，转换成日期型日期格式
dt_date = time.strptime(dt_input,"%Y-%m-%d")

# 将日期转换为时间戳
dt_stamp = int(time.mktime(dt_date))

#取得 struct_time元组
struct_time = time.localtime(dt_stamp)

#取得年、月、日
int_year = struct_time.tm_year
int_month = struct_time.tm_mon
int_day = struct_time.tm_mday
print(int_year,int_month,int_day)

#     1  2  3  4  5  6  7  8  9 10 11 12
mon=[31,28,31,30,31,30,31,31,30,31,30,31]

if int_year%4==0:   #闰年 2 月 29 天
    mon[1]=29

print('mon:',mon)

d = 0
for n in range(int_month-1):
    d += mon[n]
d += int_day

print(dt_input,'这一天是当年的第',d,'天')


print('【第2种方法】')
import calendar
d=0
for n in range(1,int_month):
    x = calendar.monthrange(int_year,n)[1]      #返回（第一个是该月的星期几，第二个是该月有几天）
    d += x
    print(n,x,d)
d += int_day
print(dt_input,'这一天是当年的第',d,'天')