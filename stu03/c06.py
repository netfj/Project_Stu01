#coding:utf-8
"""
@info: 线程启动方法： threading
@author:NetFj @software:PyCharm @file:c06.py @time:2018/11/6.16:49
"""

import threading, time

print('方法一： 将要执行的方法作为参数传递给Thread的构造方法')
def action(arg):
    time.sleep(1)
    print(threading.currentThread(),
          '[1]: {}\n'.format(arg))

for i in range(5):
    t = threading.Thread(target=action,args=(i,))
    t.start()
print('main thread end!')
t.join()


print('方法二：从 Thread 继承，并重写 run()')
class MyThread(threading.Thread):
    def __init__(self,arg):
        super(MyThread,self).__init__()
        self.arg = arg
    def run(self):
        time.sleep(1)
        print('[2]',threading.Thread.getName(self),self.arg)

for i in range(5):
    t = MyThread(i)
    t.start()
print('Main is over!')
t.join()

