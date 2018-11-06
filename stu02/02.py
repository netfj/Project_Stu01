#创建一个迭代器

class fab(n,a=0,b=1):
    print(n,a,b)
    def __init__(self):
        self.a=a
        self.b=b
    def __iter__(self):
        return self
    def __next__(self,n):
        while True:
            if self.a>n:
                self.a , self.b = self.b, self.a+self.b
                return self.a



f = fab(10)

