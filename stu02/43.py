
import sqlite3
con = sqlite3.connect('test.db')
cur = con.cursor()
# cur.execute('select * from t1')
# re = cur.fetchall()
# print(re)
#
#
# sql = "insert into t1 ('id','name','age') values (1,'Tom',20),(2,'Jack',21),(3,'Kite',22);"
# cur.execute(sql)
# con.commit()

#
# cur.execute('select * from t1')
# re = cur.fetchall()
# print(re)
#
# alter table record drop column name;
# alter table t1     drop column ct01;
print(cur.execute('alter table t1 drop column name;'))
print(con.commit())

a=cur.execute("PRAGMA table_info('t1');")
print(a)
