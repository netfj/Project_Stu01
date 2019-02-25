#coding:utf-8
"""
info:   
author: NetFj@sina.com
file:   09.py 
time:   2019/2/25.20:24
"""

# import os
# os.system(r'"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" https://www.xuexi.cn')
#

def open_site(site_name):
    import webbrowser
    chromePath = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chromePath))
    webbrowser.get('chrome').open(site_name,new=1,autoraise=True)

site_name = 'www.baidu.com'
open_site(site_name)