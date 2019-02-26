#coding:utf-8
"""
info:   
author: NetFj@sina.com
file:   12.py 
time:   2019/2/25.22:04
"""

import time
localtime = time.localtime(time.time())
print("本地时间为 :", localtime)
print("本地时间为 :", time.asctime( time.localtime(time.time()) ))

dt = str(localtime.tm_year)+'.'+str(localtime.tm_mon)+'.'+str(localtime.tm_mday)
tm = str(localtime.tm_hour)+':'+str(localtime.tm_min)+':'+str(localtime.tm_sec)

print(dt)
print(tm)