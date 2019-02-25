#coding:utf-8
"""
info:   
author: NetFj@sina.com
file:   01.py 
time:   2019/2/24.15:34
"""


import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys

driver = Chrome()
driver.get("http://www.baidu.com")

assert "百度一下" in driver.title , '这不是百度的!'

# element = driver.find_element_by_id('kw')
# element.clear()
# element.send_keys('天气')
# element.send_keys(Keys.RETURN)


driver.find_element_by_id('kw').send_keys('天气')
x = driver.find_element_by_id('su')
x.click()

# time.sleep(5)
# driver.close()
# driver.quit()

print('end!')