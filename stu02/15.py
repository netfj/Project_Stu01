# Python MySQL - mysql-connector 驱动
#这是使用mysql官方驱动的示例
#安装Mysql官方提供的Python操作驱动：pip install mysql-connector-python
import mysql.connector

#连接 Mysql
conn = mysql.connector.connect(
    host='localhost',
    user='root',
     password='123')
cursor = conn.cursor()

print('【使用 SHOW DATABASES 输出所有数据库列表】')
cursor.execute('SHOW DATABASES')
for x in cursor:
    print(x)

print('【创建一个名为 runoob_db 的数据库】')
cursor.execute('SHOW DATABASES')
yn=False
for x in cursor:
    if 'runoob_db' in x :
        print('runoob_db 已经存在！')
        yn = True
        break
if yn!=True : cursor.execute('create database runoob_db')

print('【直接连接数据库】')
conn_runoob_db=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='123',
    database='runoob_db'
)
myconn=conn_runoob_db.cursor()

print('【使用 "SHOW TABLES" 语句来查看数据表】')
myconn.execute('SHOW TABLES')
for x in myconn: print(x)

print('【创建一个数据表,名为 site】')
myconn.execute('SHOW TABLES')
yn=False
for x in myconn:
    if 'site' in x:
        print('表site已经存在！')
        yn=True
        break
if yn!=True:
    print('表site不存在，下面开始创建！')
    myconn.execute(
        'CREATE TABLE site ('
        'id INT AUTO_INCREMENT PRIMARY KEY,'
        'name varchar(255) , '
        'age INT(3),'
        'url varchar (255))'
    )

# print('【创建一个主键】')
# conn_runoob_db=mysql.connector.connect(
#     host='localhost',
#     user='root',
#     passwd='123',
#     database='runoob_db'
# )
# myconn = conn_runoob_db.cursor()
# myconn.execute('SHOW TABLES')
# for x in myconn:
#     if 'site' in x:
#         print('表site已经存在！')
#         myconn.execute('ALTER TABLE site '
#                        'ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY')
#         break

print('【插入数据】')
conn_runoob_db=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='123',
    database='runoob_db'
)
myconn=conn_runoob_db.cursor()
sql='insert into site (name,age,url) values(%s,%s,%s) '
val=('Tom',25,'www.tom.com')
myconn.execute(sql,val)
conn_runoob_db.commit()    # 数据表内容有更新，必须使用到该语句

print('【批量插入数据:executemany】')
conn_runoob_db=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='123',
    database='runoob_db'
)
myconn=conn_runoob_db.cursor()
sql='insert into site (name,age,url) values(%s,%s,%s) '
val=[
    ('Jack',25,'www.jack.com'),
    ('Kite',21,'www.kite.com'),
    ('Mike',26,'www.mike.com')
]
myconn.executemany(sql,val)
conn_runoob_db.commit()    # 数据表内容有更新，必须使用到该语句

print('【查看数据表内容】')
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='123',
    database='runoob_db'
)
mycursor=mydb.cursor()
mycursor.execute('select * from site')
myresult=mycursor.fetchall()
for x in myresult:
    print(x)

print('【只读取一条记录：使用 fetchone() 方法】')
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='123',
    database='runoob_db'
)
mycursor=mydb.cursor()
mycursor.execute('select * from site')
myresult=mycursor.fetchone()
print(myresult)

print('【where 条件语句】')
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='123',
    database='runoob_db'
)
mycursor=mydb.cursor()
sql = "select * from site where name = 'Kite'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

print('【删除记录】')
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='123',
    database='runoob_db'
)
mycursor=mydb.cursor()
sql = "delete from site where name = 'Kite'"
mycursor.execute(sql)
mydb.commit()

print('【更新修改记录】')
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='123',
    database='runoob_db'
)
mycursor=mydb.cursor()
sql = "update site set name ='L.Tom' where name = 'Tom'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, " 条记录被修改")

print('【删除表】')
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='123',
    database='runoob_db'
)
mycursor=mydb.cursor()
sql = "DROP TABLE IF EXISTS site"
mycursor.execute(sql)
