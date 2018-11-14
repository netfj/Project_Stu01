
from itertools import count
counter = count(start=100,step=3)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

#
# a=[1,2,3,4,5]
# x=iter(a)
# y=iter(a)
#
# for i in range(3):
#     print(next(x))
#
# for i in range(2):
#     print(next(y))
#
# print(type(a))
# print(type(x))
#
# next(x)
# next(x)
#
# print('----')
# next(x)