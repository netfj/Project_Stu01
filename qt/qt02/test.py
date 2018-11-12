#coding:utf-8
"""
@info: 
@author:NetFj @software:PyCharm @file:test.py @time:2018/11/9.12:59
"""

from suport.SQLiteClass import *

dbt=Dbt()
dbt.database_connect('test.db')
dbt.table_create('t1')

print(dbt.tables_all())

