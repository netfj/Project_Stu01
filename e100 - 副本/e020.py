#coding:utf-8
"""
@info: 题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；
            再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
@author:NetFj @software:PyCharm @file:e20.py @time:2018/11/1.21:06
"""

h=100
n=10
s=0
for i in range(1,n+1):
    s1=h
    h /= 2
    s += s1 + h
    if h>0:
        print('第 %s 次反弹的高度：%s ; 经过行程： %s' % (i,h,s))


print('-----------------')
tour = []
height = []

hei = 100.0  # 起始高度
tim = 10  # 次数

for i in range(1, tim + 1):
    # 从第二次开始，落地时的距离应该是反弹高度乘以2（弹到最高点再落下）
    if i == 1:
        tour.append(hei)
    else:
        tour.append(2 * hei)
    hei /= 2
    height.append(hei)

print(tour)
print(sum(tour))
print('第10次反弹高度：height = {0}'.format(height[-1]))
print('总高度：tour = {0}'.format(sum(tour)))

'''
第10次反弹高度：height = 0.09765625
总高度：tour = 299.609375
'''