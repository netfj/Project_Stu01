def test(a=100,b=30):
    print(a+b)
    return a+b

w = test(1,3)
print(w)
w = test('abc','123')
print(w)
w=test()
print(w)

print('-------------')


class test2():
    def __init__(self,a=10,b=2000,c=9):
        self.a=a
        self.b=b
    def do(self):
        print(self.a+self.b)
        return self.a+self.b

y=test2(1)
x=y.do()
print(x)