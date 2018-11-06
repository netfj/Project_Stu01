#coding:utf-8
import SQLiteClass
import Tools
from Tools import *

dbt = SQLiteClass.dbt('testgoods.db')

# P(dbt.query_table('goods'))
#
# PQ(dbt,'select * from category')

sql = 'select goods_id,cat_id,goods_name,market_price from goods ' \
      'order by goods_id desc ' \
      'group by cat_id' \
      'limit 1'

sql = 'select goods_id,cat_id,goods_name,market_price from goods ' \
      'order by cat_id '


PQ(dbt,sql)
