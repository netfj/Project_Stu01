#coding:utf-8
import SQLiteClass

dbt = SQLiteClass.dbt('TestStu.db')

def start():
    dbt.CreateTable('user',
                    ['ID Integer PRIMARY KEY autoincrement',
                     'name text',
                     'age int'])

    dbt.CreateTable('money',
                    ['ID Integer',
                     'num REAL'])

    dbt.InsertValueMulti('user', [('name','age'),('Tom', 33), ('Kite', 22), ('Jack', 26)])
    dbt.InsertValueMulti('money', [('ID','num'),(1, 100), (2, 120), (3, 110),(1,80),(3,-60)])


def st2():
    dbt.CreateTable('stu',
                    ['name text','subject text','score int'])

    dbt.InsertValueMulti('stu',
                         [('name', 'subject','score'),
                          ('张三','数学',90),
                          ('张三','语文',50),
                          ('张三','地理',40),
                          ('李四','语文',55),
                          ('李四','政治',45),
                          ('王五','政治',70),
                          ('王五','语文',80),
                          ('王五','数学',90),
                          ('王五','物理',30)])
start()
st2()

