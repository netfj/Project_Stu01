# sqlite

import sqlite3

class dbt:
    def __init__(self,DatabaseName='test.db'):  #连接数据库，没有则建立
        self.connect = sqlite3.connect(DatabaseName)
        self.cursor = self.connect.cursor()
        print("Opened database successfully:", DatabaseName)

    def IsTebleExist(self,TableName):        #判断一个表是否存在
        query = "SELECT count(*) FROM sqlite_master " \
                "WHERE type='table' AND name='%s' ;" % TableName
        self.cursor.execute(query)
        n = self.cursor.fetchone()[0]  # n=0时不存在
        if n == 0:
            print('Table %s is NOT exist' % TableName)
            return False
        else:
            print('Table %s is exist' % TableName)
            return True

    # 创建一个表，示例：
    # mydbt.CreateTable('tb1',['ID Integer PRIMARY KEY autoincrement','name text','age int'])
    def CreateTable(self,
                    TableName='test_user',
                    ColumnList=['ID Integer PRIMARY KEY autoincrement','name text','age int']
                    ):
        if self.IsTebleExist(TableName) : return '文件已经存在！'
        if len(ColumnList)==0:
            print('字段参数列表不能为空！')
            return '字段参数列表不能为空'
        try:
            sql = 'create table '+TableName+' ('
            for x in ColumnList:
                sql = sql+ x +','
            sql = sql.rstrip(',') + ');'
            print(sql)
            self.cursor.execute(sql)
            self.connect.commit()
            print("Table created done")
        except:
            print("Table created error")
        if self.IsTebleExist(TableName): print('Create table successfully !')

    # 插入一条记录, 用法：mydbt.InsertValueOne('tb1',{'name':'TomOne','age':10})
    def InsertValueOne(self, TableName='test_user', InsertValue={'name':'testInserOne','age':1}):
        if self.IsTebleExist(TableName)==False:
            print('Table is NOT exist: %s' % TableName)
            return False
        if len(InsertValue)==0 : return '无数据传入'
        col,val='',''
        for k in InsertValue:
            col = col+k+','
            val = val+"'"+str(InsertValue[k])+"'"+','
        col=col.rstrip(',')
        val=val.rstrip(',')
        sql = 'insert into %s (%s) values (%s);' % (TableName, col, val)
        print(sql)
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            print('Insert values is successful.')
        except:
            print('Insert values is fail !')

    #插入多条记录
    def InsertValueMulti(self,TableName='test_user',InertValueList=[('name','age'),('testInsertValueMulti',99)]):
        print('InsertValueMulti 开始执行')
        if self.IsTebleExist(TableName)==False:
            print('Table is NOT exist: %s' % TableName)
            return False
        if len(InertValueList)==0 : return '无数据传入'
        sql_ahead ='insert into %s (' % (TableName)
        col = InertValueList[0]
        for x in col:
            sql_ahead = sql_ahead+x+','
        sql_ahead = sql_ahead.rstrip(',') + ') values ('
        for n in range(1,len(InertValueList)):
            val=InertValueList[n]
            sql = sql_ahead
            for x in val:
                sql = sql + "'" + str(x) + "',"
            sql = sql.rstrip(',') + ');'
            try:
                self.cursor.execute(sql)
                self.connect.commit()
            except:
                print('Insert values is fail !')
        print('InsertValueMulti 执行完成')

    def query(self,TableName='test_user'):      #查询一个表
        if self.IsTebleExist(TableName)==False: return '表不存在：%s' % TableName
        sql = "select * from %s " % TableName
        self.cursor.execute(sql)
        re = self.cursor.fetchall()
        return re

    def test(self):
        self.CreateTable()
        self.InsertValueOne()
        self.InsertValueMulti()
        re=self.query()
        for x in re: print(x)

#下面开始测试试用

t = dbt()
t.test()


#
# mydbt = dbt('mytest.db')
#
# mydbt.CreateTable()
#
# mydbt.InsertValueOne()
#
# import random
# c=[
#     ('name','age'),
#     ('Tom',random.randint(1,100)),
#     ('Tom', random.randint(1,100)),
#     ('Tom', 0)
# ]
# mydbt.InsertValueMulti(InertValueList=c)
#
# re = mydbt.query()
# for x in re:print(x)
#









