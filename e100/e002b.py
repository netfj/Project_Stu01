# -*- coding: UTF-8 -*-
for n in range(79,83):
    jj1 = 0
    je1 = n
    jf1=[0,0,0,0,0,0]
    jf1[0] = max((je1-100),0)*0.01
    jf1[1] = min(max((je1-60),0),40)*0.015
    jf1[2] = min(max((je1-40),0),20)*0.03
    jf1[3] = min(max((je1 - 20), 0), 20) * 0.05
    jf1[4] = min(max((je1 - 10), 0), 10) * 0.075
    jf1[5] = min(max((je1 - 0), 0), 10) * 0.10
    jj1 = jf1[0]+jf1[1]+jf1[2]+jf1[3]+jf1[4]+jf1[5]

    # print('方法2:' ,end='')
    ar=[100,60,40,20,10,0]
    rat=[0.01,0.015,0.03,0.05,0.075,0.10]
    jj2=0
    je2 = n
    jf2=[0,0,0,0,0,0]
    for i in range(0,6):
        if je2>ar[i]:
            jf2[i] = (je2-ar[i])*rat[i]
            jj2 += jf2[i]
            je2=ar[i]

    print('----------------------------')
    if not jj1 == jj2: print('X :')
    print(n,round(jj1,3),round(jj2,3))
    print(jf1[0],jf1[1],jf1[2],jf1[3],jf1[4],jf1[5])
    print(jf2[0],jf2[1],jf2[2],jf2[3],jf2[4],jf2[5])

    jj2 = jf2[0] + jf2[1] + jf2[2] + jf2[3] + jf2[4] + jf2[5]
    print(jj1,jj2)



#当输入81万，不同，待排错 : OK!!!