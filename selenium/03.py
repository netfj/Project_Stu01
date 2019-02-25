#coding:utf-8
"""
info:   鼠标事件
author: NetFj@sina.com
file:   03.py 
time:   2019/2/24.18:02
"""

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

url = 'http://www.baidu.com'
brower = webdriver.Firefox()
brower.get(url)

above = brower.find_element_by_link_text('设置')
ActionChains(brower).move_to_element(above).perform()
