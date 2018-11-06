import os,sys,stat
def pd():
    p=os.getcwd()
    print(p)
    return p

p=r'c:\users\test.bat'
ret = os.access(p,os.F_OK)
print(ret)
ret = os.access(p,os.R_OK)
print(ret)
ret = os.access(p,os.W_OK)
print(ret)
ret = os.access(p,os.X_OK)
print(ret)

pd()
os.chdir(r'd:\temp')
pd()

os.chmod(p,stat.S_IWOTH)
print(os.access(p,os.W_OK))
