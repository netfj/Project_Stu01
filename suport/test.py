#coding:utf-8
"""
Info:
@author:Netfj@sina.com  @software: PyCharm @file: test.py @time: 2018/11/3 16:56
"""

from SQLiteClass import Dbt
from Tools import *
dbt = Dbt('test01.db')
dbt.table_create('test0001')
dbt.value_insert('test0001')

dbt.table_create('t1')
dbt.value_insert('t1')

p(dbt.query_table('test0001'))
p(dbt.query_table('t1'))


