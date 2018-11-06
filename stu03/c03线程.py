#coding:utf-8
"""
Info:
@author:Netfj@sina.com  @software: PyCharm @file: 03线程.py @time: 2018/11/3 22:00
"""
#
# import _thread,time
# def print_time(threading_name,delay):
#     count=0
#     while count<5:
#         time.sleep(delay)
#         count+=1
#         print(threading_name,time.ctime(time.time()))
#
# try:
#     # _thread.start_new_thread(print_time('thread-1', 1))
#     _thread.start_new_thread(print_time,('thread-2', 3))
#     _thread.start_new_thread(print_time,('thread-3', 5))
# except:
#     print('erroe: Can not start threading')
#


print('---')

# 使用 threading 模块创建线程
import threading,time
def pt(delay=2):
    count = 0
    while count<5:
        time.sleep(delay)
        count += 1
        print(trname, delay)

try:
    th = threading.Thread(target=pt)
    th.setName('xxxx')
    th.start()
    th.join()
except:
    print('threading error...')
