#coding:utf-8
"""
@info: lock 测试
@author:NetFj @software:PyCharm @file:c07.py @time:2018/11/6.17:44
"""
import threading, time

class myThread(threading.Thread):
    def __init__(self,i):
        super(myThread,self).__init__()
        self.i = i

    def run(self):
        if lock.acquire():
            for x in range(3):
                time.sleep(1)
                print('【',self.name,self.i,'】', time.ctime())
            lock.release()


a = []
for n in range(5):
    t = myThread(n)
    a.append(t)

lock = threading.RLock()
for x in a:
    x.start()

for x in a:
    x.join()

