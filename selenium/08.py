#coding:utf-8
# @Info: 每隔 n 秒移动下鼠标
# @Author:Netfj@sina.com @File:08.py @Time:2019/2/25 17:29
import pyautogui,time
n = 3
try:
    while True:
        time.sleep(n)
        pyautogui.moveRel(100,100,duration=0.25)
except KeyboardInterrupt:
    print('\nDone.')