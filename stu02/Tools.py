#coding:utf-8

def p(x):
    if isinstance(x, list):
        for n in x: print(n)
    else:
        print(x)

def P(x):
    p(x)



def PrintQuery(dbt,s):
    PrintList(dbt.query(s))
def pq(dbt,s):
    PrintQuery(dbt,s)
def PQ(dbt,s):
    PrintQuery(dbt,s)

