
b=[2,3]
a = 1

b.insert(0,a)
print(b)

c = [str(x) for x in b]
print(c)
print('-'.join(c))


print(b[0])
print(b[1])
print(b[2])


a = b.pop(0)
print(a,b)

a = b.pop(0)
print(a,b)

a = b.pop(0)
print(a,b)

a = b.pop(0)
print(a,b)

