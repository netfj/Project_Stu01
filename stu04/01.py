from itertools import islice,cycle

colors = cycle(['red','blue','green',4,5,6,7,8,9])
print(colors)

a = cycle('abc')
print(a)

for n in range(10):
    print(next(colors),next(a))

b = islice(colors,0,6)
print(b)
# for n in range(4):
#     print(n)
#     print(next(b),n)

print('--->',list(b))