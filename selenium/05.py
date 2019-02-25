#coding:utf-8
"""
info:   
author: NetFj@sina.com
file:   05.py 
time:   2019/2/24.18:53
"""

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = 'https://www.xuexi.cn'
br = webdriver.Chrome()
br.get(url)

# br.find_element_by_id('C8xgl5zxg7lk00').send_keys(Keys.ENTER)
# br.find_element_by_link_text('更多头条').send_keys(Keys.ENTER)

time.sleep(5)

br.find_element_by_xpath('//*[@id="C70ngaew6trg00"]').send_keys(Keys.ENTER)


