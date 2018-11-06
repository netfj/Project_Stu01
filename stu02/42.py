from Tools import *
from SQLiteClass import *
mydbt = dbt('test.db')

mydbt.DropTable('t1')
                          # INTEGER PRIMARY KEY AUTOINCREMENT
mydbt.CreateTable('t1',['id Integer primary key autoincrement','name text','age integer default 0'])
mydbt.InsertValue('t1',"('id','name','age')","(1,'Tom',20),(2,'Jack',21),(3,'Kite',22)")
mydbt.InertValueOneBYOne('t1',"('id','name','age')",[(4,'Tom',20),(5,'Jack',21),(6,'Kite',22)])
mydbt.InsertValue('t1',"('id','name')","(7,'Tom'),(8,'Jack'),(9,'Kite')")
p(mydbt.query_table('t1'))
print('---------')
mydbt.RecordeTruncate('t1')


mydbt.InsertValue('t1',"('id','name','age')","(1,'Tom',20),(2,'Jack',21),(3,'Kite',22)")

p(mydbt.query_table('t1'))