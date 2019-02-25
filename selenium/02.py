#coding:utf-8
"""
info:   
author: NetFj@sina.com
file:   02.py 
time:   2019/2/24.16:33
"""

import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys

driver = Chrome()
driver.get('https://www.xuexi.cn/index.html')

ele = driver.find_element_by_link_text('十九大时间')
ele.send_keys(Keys.ENTER)


time.sleep(5)
driver.close()

print('end')