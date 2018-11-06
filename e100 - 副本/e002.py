# -*- coding: UTF-8 -*-
'''
http://www.runoob.com/python/python-100-examples.html
http://www.runoob.com/python/python-exercise-example2.html
题目：企业发放的奖金根据利润提成。
利润(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；
40万到60万之间时高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%，
高于100万元时，超过100万元的部分按1%提成，
从键盘输入当月利润I，求应发放奖金总数？

程序分析：请利用数轴来分界，定位。注意定义时需把奖金定义成长整型。
'''


for n in range(75,85):
    # je = int(input('Input Your shouru(万元):'))

    # print('方法1:',end='')
    jj1 = 0
    je1 = n
    jj1 = max((je1-100),0)*0.01 +\
        min(max((je1-60),0),40)*0.015+\
        min(max((je1-40),0),20)*0.03+ \
         min(max((je1 - 20), 0), 20) * 0.05+ \
         min(max((je1 - 10), 0), 10) * 0.075+\
        min(max((je1 - 0), 0), 10) * 0.10

    # print('方法2:' ,end='')
    ar=[100,60,40,20,10,0]
    rat=[0.01,0.015,0.03,0.05,0.075,0.10]
    jj2=0
    je2 = n
    for i in range(0,6):
        if je2>ar[i]:
            jj2 += (je2-ar[i])*rat[i]
            je2=ar[i]

    if not jj1 == jj2: print('X',end='')
    print(n,round(jj1,2),round(jj2,2))


#当输入81万，不同，待排错 : OK!!!