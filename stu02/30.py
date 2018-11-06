#连接SQLite 01-建立库和表

import sqlite3

def IsTebleExist(cursor,TableName):
    query = "SELECT count(*) FROM sqlite_master " \
            "WHERE type='table' AND name='%s'" %TableName;
    cursor.execute(query)
    n = cursor.fetchone()[0]  # n=0时不存在
    if n==0:
        return False
    else:
        return True

conn = sqlite3.connect('test.db')   #连接数据库，没有则建立
print("Opened database successfully")
cursor = conn.cursor()

#判断表是否存在
TableName = "COMPANY"
if IsTebleExist(cursor,TableName):
    print('Table is exist!')
else:
    print('Table is not exist!')

#建表
if IsTebleExist(cursor,TableName)==False:
    try:
        sql='''
        CREATE TABLE COMPANY
        (ID INT identity PRIMARY KEY,
        NAME TEXT, 
        AGE INT, 
        ADDRESS CHAR(50), 
        SALARY REAL);
        '''
        cursor.execute(sql)
        conn.commit()
        print("Table created done")
    except:
        print("Table created error")

if IsTebleExist(cursor,TableName):
    print('Table is exist!')
else:
    print('Create table fail !')
conn.close()
