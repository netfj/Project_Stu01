#文件操作

#写一个文件
f=open('f1.txt','w')
f.write('This is a test by python.\n2018-10-9')
f.close()

#读一个文件
f=open('f1.txt','r')
w=f.read()
print(w)
f.close()

#追加内容
f=open('f1.txt','a+')
f.write('By Fj')
f.seek(0,0)
print(f.read())
f.close()

