#coding:utf-8
"""
@info: 求s=a+aa+aaa+aaaa+……+aa...a （共有n项,最后一项是n位数）的值，其中a是一个数字。
    例如2+22+222+2222+22222(此时 n=5 a=2 )。
@author:NetFj @software:PyCharm @file:e018.py @time:2018/11/1.18:54
"""


a=4
n=6
s=[]
for i in range(1,n+1):
    s.append(int(str(a)*i))

print(s)
ttt = ''
for x in s:
    ttt+=str(x)+'+'

ttt = ttt.rstrip('+')
ttt += ' ='
print(ttt,sum(s))
