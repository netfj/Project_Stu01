#coding:utf-8
"""
Info:
@author:Netfj@sina.com  @software: PyCharm @file: 01.py @time: 2018/11/3 16:58
"""
from suport.Tools import *
from suport.SQLiteClass import *

dbt=dbt('mytest_stu03.db')
dbt.CreateTable('t1')
dbt.InsertValue('t1')
re = dbt.query_table('t1')
p(re)