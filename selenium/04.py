#coding:utf-8
"""
info:   键盘事件
author: NetFj@sina.com
file:   04.py 
time:   2019/2/24.18:23
"""
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
url = 'http://www.baidu.com'
brower = webdriver.Chrome()
brower.get(url)

#在输入框中输入内容
brower.find_element_by_id('kw').send_keys('python!')

#删除多输入的一个
brower.find_element_by_id('kw').send_keys(Keys.BACK_SPACE)

#继续输入
brower.find_element_by_id('kw').send_keys(Keys.SPACE)
brower.find_element_by_id('kw').send_keys('selenium')

#Ctrl+A全选
brower.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')

#Ctrl+X剪切
brower.find_element_by_id('kw').send_keys(Keys.CONTROL,'x')

#Ctrl+V粘贴
brower.find_element_by_id('kw').send_keys(Keys.CONTROL,'v')

#回车查询
brower.find_element_by_id('su').send_keys(Keys.ENTER)

time.sleep(5)

#退出
brower.quit()





