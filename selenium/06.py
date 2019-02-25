#coding:utf-8
"""
info:   
author: NetFj@sina.com
file:   06.py 
time:   2019/2/24.19:53
"""

import requests
response = requests.get("https://www.xuexi.cn/index.html")
print(response.status_code)

#