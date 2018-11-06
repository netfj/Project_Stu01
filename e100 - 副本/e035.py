#coding:utf-8
"""
@info: 题目：文本颜色设置。
@author:NetFj @software:PyCharm @file:e034.py @time:2018/11/5.21:41
"""



class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print(bcolors.WARNING + "警告的颜色字体?" + bcolors.ENDC)

print(bcolors)

'''
数值表示的参数含义：
显示方式: 0（默认值）、1（高亮）、22（非粗体）、4（下划线）、
        24（非下划线）、 5（闪烁）、25（非闪烁）、7（反显）、27（非反显）
前景色: 30（黑色）、31（红色）、32（绿色）、 33（黄色）、
        34（蓝色）、35（洋红）、36（青色）、37（白色）
背景色: 40（黑色）、41（红色）、42（绿色）、 43（黄色）、
        44（蓝色）、45（洋红）、46（青色）、47（白色）
'''

# 红色字体
print('\033[1;31m')
print('*' * 10)
print('hello world！')
print('*' * 10)
print('\033[0m')

# 绿色字体
print('\033[1;32m' + 'green' + '\033[0m')

# 蓝色字体
print('\033[1;34m' + 'blue' + '\033[0m')

# 黄字下划线
print('\033[4;33m' + 'yellow' + '\033[0m')

# 红底黑字
print('\033[1;30;41m' + 'black' + '\033[0m')

# 白底黑字
print('\033[1;30;47m' + 'white' + '\033[0m')

print('normal')
