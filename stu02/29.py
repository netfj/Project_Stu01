#连接 MYSQL 统计一个表的记录数

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123",
    database="mysql"
)

mycursor=mydb.cursor()

mycursor.execute("select count(*) from user")

myresult = mycursor.fetchall()

print(myresult[0][0])

print(myresult)
for x in myresult:
    print(x)


mycursor.execute("select count(*) from user")
n=mycursor.fetchone()
print(n[0])