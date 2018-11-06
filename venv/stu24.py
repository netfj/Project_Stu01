#coding:utf-8
"""
@info: 
@author:NetFj @software:PyCharm @file:stu24.py @time:2018/11/2.8:08
"""

import re


text = r'cat mat hat sat'
key = r'[cmh]at'
a=re.compile(key).findall(text)
print(a)

key2=r'[^m]at'
a=re.compile(key2).findall(text)
print(a)


# key=r'https://www.baidu.com;http://sina.com.cn'
# p1='https*://'
# a=re.compile(p1).findall(key)
# print(a)



# key='2180934skdlfjklasjnetfj@sina.comalksdjf123'
# p1='netfj@sina\.com'
# parttern1=re.compile(p1)
# a=parttern1.findall(key)
# print(a)

# key = r"<h1>hollo word<h1>"
# p1 = r"<h1>.+<h1>"
# pattren1=re.compile(p1)
# print(pattren1.findall(key))


# key = r"<html><body><h1>hello world<h1></body></html>"
# p1 = r"(?<=<h1>).+?(?=<h1>)"
# com = re.compile(p1)
# sea = re.search(com,key)
# print(sea.group(0))


#
# key = r'abcdefghin'
# p1 = 'de'
# pattern1=re.compile(p1)
# matcher1=re.search(pattern1,key)
# print(matcher1.group(0))
#
# # key = r"<html><body><h1>hello world<h1></body></html>"#这段是你要匹配的文本
# # p1 = r"(?<=<h1>).+?(?=<h1>)"#这是我们写的正则表达式规则，你现在可以不理解啥意思
# # pattern1 = re.compile(p1)#我们在编译这段正则表达式
# # matcher1 = re.search(pattern1,key)#在源文本中搜索符合正则表达式的部分
# # print(matcher1.group(0))    #打印出来
# #
# #
# key = r"I am a boy , and I have a boy name."
# p1 = r"boy"
# pattern1 = re.compile(p1)
# matcher1 = re.search(pattern1,key)
# print(matcher1.group(0))
# #
# # key = r"javapythonhtmlvhdl"
# # p1 = r"python"
# pattern1 = re.compile(p1)#同样是编译
# matcher1 = re.search(pattern1,key)#同样是查询
# print(matcher1.group())