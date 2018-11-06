#coding:utf-8
"""
@info: 
@author:NetFj @software:PyCharm @file:Tools.py @time:2018/11/2.11:28
"""
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

