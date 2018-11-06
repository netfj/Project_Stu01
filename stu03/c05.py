#coding:utf-8
"""
@info: threading  join
@author:NetFj @software:PyCharm @file:c05.py @time:2018/11/6.15:43
"""

import threading, time
class MyThread(threading.Thread):
    def __init__(self,id):
        threading.Thread.__init__(self)
        self.id = id

    def run(self):
        time.sleep(5)
        print('子线程结束: ',self.id)

if __name__ == '__main__':
    t = MyThread(999999)
    t.setDaemon(False)   # True: 主线程结束即结束；
                        # Flase: 不结束子线程
                        #       但主线程不等候子线程（各执行各的，相当于两个线程）
    t.start()
    t.join()        #守候，等子线程完结，再进行后面的

    for i in range(5):
        print(i)
    print('父线程结束！')
