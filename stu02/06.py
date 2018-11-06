# 生成器示例1
def fab(m):
    n,a,b=1,0,1
    while n<=m:
        w=[n,b]
        yield w
        a,b=b,a+b
        n=n+1
    return 'Game is over...'

f=fab(10)
while True:
    try:
        x=next(f)
        print(x)
    except StopIteration as t:
        print(t)
        break


# 生成器示例2
def test(n):
    for i in range(n):
        yield i
for x in test(10):
    print(x)

#生成器表达式
print('生成器表达式示例：')
q=[x*3 for x in range(10)]  #返回的是列表
print(q)

p=(x*3 for x in range(10))  #返回的是对象：是一个迭代生成器对象
for r in p:
    print(r)

a=input('回车退出')
print('exit.....',a)