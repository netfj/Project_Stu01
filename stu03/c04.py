#coding:utf-8
"""
@info: 
@author:NetFj @software:PyCharm @file:c04.py @time:2018/11/6.12:25
"""

import threading, time

def music(func):
    for i in range(3):
        print('I was listening to %s . %s' % (func,time.ctime()))
        time.sleep(5)

def move(func):
    for i in range(2):
        print('I was at the %s ! %s' %(func,time.ctime()))
        time.sleep(1)

def saytime():
    while 1:
        print('--->',time.ctime())
        time.sleep(5)

threads = []
t1 = threading.Thread(target=music,args=(u'I love you !',))
threads.append(t1)
t2 = threading.Thread(target=move,args=(u'Hi, China!',))
threads.append(t2)
t3 = threading.Thread(target=saytime)
threads.append(t3)

for t in threads:
    # print(t)
    t.setDaemon(True)
    t.start()

print(threading.currentThread())
print(threading.enumerate())

# t.join()
print('Main prog over at %s' % time.ctime())



