#coding:utf-8
import SQLiteClass

dbt = SQLiteClass.dbt('TestGoods.db')

def p(x):
    print('------')
    if x==None : return print(x)
    for n in x: print(n)
def pq(s):
    p(dbt.query(s))

p(dbt.query_table('goods'))
