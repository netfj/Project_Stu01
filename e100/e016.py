#coding:utf-8
"""
@info: 输出指定格式的日期。
@author:NetFj @software:PyCharm @file:e016.py @time:2018/11/1.11:44
"""

import time

print('\n时间戳(timestamp)'
      '【时间戳是指格林威治时间'
      '1970年01月01日00时00分00秒'
      '(北京时间1970年01月01日08时00分00秒)'
      '起至现在的总秒数】\n  '
      ' time.time() =',time.time())

print('\n时间戳-->元组\n time.localtime(time.time())=')
t = time.localtime(time.time())
print(t)
print('年 tm_year = ',t[0],t.tm_year)
print('月 tm_mon =',t[1],t.tm_mon)
print('日 tm_mday = ',t[2],t.tm_mday)
print('时 tm_hour = ',t[3],t.tm_hour)
print('分 tm_min = ',t[4],t.tm_min)
print('秒 tm_sec = ',t[5],t.tm_sec)
print('周 tm_wday = ',t[6],t.tm_wday)
print('一年的第几日 tm_wday = ',t[7],t.tm_yday)
print('夏令时 tm_isdst = ',t[8],t.tm_isdst)

print('\n--- 格式化输出时间  --------')
print('time.asctime() =',time.asctime())

print('\ntime.strftime("%Y-%m-%d %H:%M:%S", time.localtime())=')
print(time.strftime("%Y-%m-%d %H:%M:%S %A", time.localtime()))
text='''
python中时间日期格式化符号：
● %y 两位数的年份表示（00-99）
● %Y 四位数的年份表示（000-9999）
● %m 月份（01-12）
● %d 月内中的一天（0-31）
● %H 24小时制小时数（0-23）
● %I 12小时制小时数（01-12）
● %M 分钟数（00=59）
● %S 秒（00-59）
● %a 本地简化星期名称
● %A 本地完整星期名称
● %b 本地简化的月份名称
● %B 本地完整的月份名称
● %c 本地相应的日期表示和时间表示
● %j 年内的一天（001-366）
● %p 本地A.M.或P.M.的等价符
● %U 一年中的星期数（00-53）星期天为星期的开始
● %w 星期（0-6），星期天为星期的开始
● %W 一年中的星期数（00-53）星期一为星期的开始
● %x 本地相应的日期表示
● %X 本地相应的时间表示
● %Z 当前时区的名称
● %% %号本身'''
print(text)

print('--- 时间格式间转换 ---')

print('\n字符串 -- strptime --> 时间元组 ')
print("time.strptime('2018-12-12','%Y-%m-%d') =")
print( time.strptime('2018-12-12','%Y-%m-%d') )

print('\n时间元组 --  mktime --> 时间戳 ')
print("time.mktime(time.strptime('2018-12-12','%Y-%m-%d')) =")
print(time.mktime(time.strptime('2018-12-12','%Y-%m-%d')))
