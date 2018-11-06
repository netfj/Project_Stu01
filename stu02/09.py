#数据结构

#列表
lb = [1,2,3]
print(lb)
print(lb[0],lb[1],lb[2])
lb[0]=['a','b',3,4,5]
lb[1]="This is a test for update!"
print(lb[0],lb[1],lb[2])

#元组
yz=(1,2,3)
print(yz)
print(yz[0],yz[1],yz[2])

#字典
zd={'name':"Tom",'age':23}
print(zd)
print(zd['name'],zd['age'])
zd['age']=zd['age']+1
print(zd)

for k,v in zd.items():
    print(k,v)


# 列表推导式
print('======')
a=[1,2,3,4,5,6]
b=[x for x in a if x>2]
print(a)
print(b)
c=[x*y for x in a for y in b]
print(c)

#集合
print('----')
a={1,1,2,2,3,4,5,7}
b={1,4,6}
print(a)    #简化
print(a-b)  #在a中，但不在b中
print(a|b)  #ab合集
print(a&b)  #ab交集
print(a^b)  #ab合集-交集：在a中或在b中，但不同时在ab中
