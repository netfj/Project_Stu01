# 一个继承类的例子

class animal():
    def __init__(self,eye=2,foot=2):
        self.eye = eye
        self.foot = foot

class cat(animal):
    def __init__(self):
        super().__init__()
        self.foot=4
    def cry(self):
        return  'miao~~~~~ '

c1 = cat()
print(c1.eye)
print(c1.foot)
print(c1.cry())