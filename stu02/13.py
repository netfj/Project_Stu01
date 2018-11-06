import pickle

a={'a':[1,2,3,4],
   'b':('center','left','right'),
   'name':'Tom',
   'age':21,
   1:100,
   2:200}

f=open('data.pic','wb+')
pickle.dump(a,f,0)
f.close()

f=open('data.pic','rb')
b=pickle.load(f)
f.close()
print(b)
f=open('data2.pic','rb')
b=pickle.load(f)
f.close()
print(b)


a=100

f=open('data2.pic','wb')
pickle.dump(a,f,0)
f.close()
