#迭代器

class fab():
    def __init__(self,m=100):
        self.max=m
        self.a=0
        self.b=1
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        # n=self.a+self.b
        # self.a=self.b
        # self.b=n
        if self.b>self.max:
            raise StopIteration
        return self.b

for i in fab():
    print(i)

