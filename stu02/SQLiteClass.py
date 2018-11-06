#coding:utf-8
'''
名称：SQLite3 操作类 ver 0.1  2018-10-30
功能：SQLite 数据库、表的建立，记录的增删改查
作者：NetFj@sina.com
目录：
    第1部分：数据库
    第2部分：表
    第3部分：字段（列）
    第4部分：记录（1.增；2.删；3.改；4.查）
    第5部分：视图
    第6部分：索引
    第7部分：事务
'''

import sqlite3
import logging
import time

logging.basicConfig(filename='SQLiteRunInfo.log',
    level= logging.DEBUG,
    format="%(funcName)s(%(lineno)d)[%(levelname)s]%(message)s")
logging.debug(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+
              '\n模块或函数名(行号)[日志类型]日志信息: ')

class dbt:

    ###  第 1 部分：数据库  #############################

    def __init__(self,DatabaseName='test.db'):
        self.connect = sqlite3.connect(DatabaseName)    #连接数据库，没有则建立
        self.cursor = self.connect.cursor()             #取得游标
        logging.debug("Opened database successfully:%s" % DatabaseName)

    #查询数据库中的所有表，返回值：列表（性质，表名，表名，rootpage，建表命令）
    def QueryAllTables(self):
        return self.cursor.execute("SELECT * FROM sqlite_master WHERE type='table' ORDER BY name;")


    ###  第 2 部分：表   ###################

    def IsTebleExist(self,TableName):        #判断一个表是否存在
        query = "SELECT count(*) FROM sqlite_master " \
                "WHERE type='table' AND name='%s' ;" % TableName
        self.cursor.execute(query)
        n = self.cursor.fetchone()[0]  # n=0时不存在
        if n == 0:
            # logging.debug('Table %s is NOT exist' % TableName)
            return False
        else:
            # logging.debug('Table %s is exist' % TableName)
            return True

    # 删除一个表
    def DropTable(self,TableName):
        if TableName==None:
            msg = 'Reference: .DropTable(TableName)'
            logging.error('Table name is losted !\n ' + msg)
            return False
        if self.IsTebleExist(TableName) == False:
            return True
        sql_command = 'drop table %s' % TableName
        try:
            self.cursor.execute(sql_command)
            logging.debug('Drop table succesfull ! (%s)' % sql_command)
            return True
        except:
            logging.error('Drop table fail ! (%s)' % sql_command)

    # 变更表名，给表改名
    def TableRename(self,name_old,name_new):
        if name_new==None or name_old==None:
            msg = 'Reference: .TableRname(name_old,name_new)'
            logging.error('Table name is losted !\n ' + msg)
            return False
        if self.IsTebleExist(name_old) == False:
            logging.error('Table is NOT exist !')
            return False
        if self.IsTebleExist(name_new):
            logging.error('Table (new name) already is exist !')
            return False
        sql_command = 'alter table %s rename to %s' % (name_old,name_new)
        try:
            self.cursor.execute(sql_command)
            self.connect.commit()
            logging.debug('Table Rename sucessful ! (%s)' % sql_command)
            return True
        except:
            logging.error('Table Rename fail ! (%s)' % sql_command)
            return False

    # 创建一个表，示例：
    # mydbt.CreateTable('tb1',['ID Integer PRIMARY KEY autoincrement','name text','age int'])
    def CreateTable(self,
                    TableName='test_user',
                    ColumnList=['ID Integer PRIMARY KEY autoincrement','name text','age int']
                    ):
        logging.debug('开始创建表：%s' % TableName)
        if self.IsTebleExist(TableName) : return '文件已经存在！'
        if len(ColumnList)==0:
            logging.WARNING('字段参数列表不能为空！')
            return '字段参数列表不能为空'
        try:
            sql = 'create table '+TableName+' ('
            for x in ColumnList:
                sql = sql+ x +','
            sql = sql.rstrip(',') + ');'
            logging.debug(sql)
            self.cursor.execute(sql)
            self.connect.commit()
            logging.debug("Table created done")
        except:
            logging.debug("Table created error")
        if self.IsTebleExist(TableName): logging.debug('Create table successfully !')

    # 查询表的结构
    def QueryTableStructure(self,TableName=None):
        if TableName==None:
            msg='需要一个参数：表名'
            logging.error(msg)
            return [msg]
        if self.IsTebleExist(TableName) == False:
            logging.error('Table is NOT exist !("%s") '  % (TableName))
            return False
        sql='PRAGMA table_info("%s") ;'  % (TableName)
        logging.debug(sql)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    ###  第 3 部分：字段（列）   ################

    # 增加一个列
    def ColumnAdd(self,TableName='test_user',column_add='column_add_test text'):
        if self.IsTebleExist(TableName) == False:
            logging.debug('Table is NOT exist: %s' % TableName)
            return False
        sql_command = 'alter table %s ADD %s;' % (TableName,column_add)
        try:
            self.cursor.execute(sql_command)
            self.connect.commit()
            logging.debug('Add a column is succesful ! (%s)' %  sql_command)
        except:
            logging.error('Add a column is fail :\n ' + sql_command)
            logging.info("reference：\n"
                         "           .ColumnAdd(TableName,column_add)\n"
                         "           .ColumnAdd('col_test','col_test text')")


    #删除一个列(mysql中对应的语句是：alter table table_name drop column column_name)
    def ColumnDrop(self,TableName,ColumnName):
        logging.warning('SQLite目前还不支持drop column ！ 请手工处理 ！')
        return False

    # 更改字段（列）名、属性。mysql中对应的语句是：
    # alter table table_name drop column column_name
    # alter table table_name modify column_name 新属性
    def ColumnChange(self,TableName=None,ColumnNameOld=None,ColumnNameNew=None):
        if TableName==None or ColumnNameOld==None or ColumnNameNew==None:
            msg = 'Reference:\n .ColumnChange(TableName,ColumnNameOld,ColumnNameNew)'
            logging.error('Arguments is losted ! '+msg)
            return False
        msg = '与删除一列相同，在sqlite中alter同样无法重命名一列。'
        logging.warning(msg)
        return False


    ###  第 4 部分：表的记录（增删改查） -- 第 1 节：增   ######

    # 插入（增加）记录（批量插入法）, 用法：mydbt.InsertValue(表名,字段,值)
        #  表名: 要插入的表的名字, 字符串格式
        #  字段: 字段名(注意与值对应), 字符串格式, 为空时表示所有字段，注意多个时要用括号括起来
        #   值: 要插入的值, 字符串格式, 可以多条记录同时插入
        # 示例: mydbt.InsertValue('test_user',"('id','name','age')","(1,'Tom',20),(2,'Jack',21),(3,'Kite',22)")
        #   或: mydbt.InsertValue('test_user','',"(1,'Tom',20),(2,'Jack',21),(3,'Kite',22)")
    def InsertValue(self,
                    TableName="test_user",
                    Columns="('name','age')",
                    InsertValue="('Tom',20)"):
        if self.IsTebleExist(TableName) == False:
            logging.debug('Table is NOT exist: %s' % TableName)
            return False
        if len(str.rstrip(str.lstrip(InsertValue))) == 0:
            logging.debug('无插入值数据传入')
            return False
        sql = 'insert into %s %s values %s;' % (TableName, Columns, InsertValue)
        logging.debug(sql)
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            logging.debug('Insert values is successful.')
            return True
        except:
            logging.error('Insert values is fail !')
            return False

    # 插入（增加）记录（逐条插入法，以用于排查数据错误）,
        #格式 ：mydbt.InsertValue(表名,字段,值)
    def InertValueOneBYOne(self,
                           TableName='test_user',
                           Columns='',
                           InsertValue=[(1,'Tom',20),(2,'Kit',23)]):
        if self.IsTebleExist(TableName) == False:
            logging.debug('Table is NOT exist: %s' % TableName)
            return False
        if len(InsertValue) == 0:
            logging.debug('无插入值数据传入')
            return False
        for x in InsertValue:
            v = "("
            for y in x:
                v += '"' + str(y) +'",'
            v = str.rstrip(v,',') + ')'
            self.InsertValue(TableName,Columns,v)


    # 作废
    # 插入一条记录, 用法：mydbt.InsertValueOne('tb1',{'name':'TomOne','age':10})
    def InsertValueOne_old(self, TableName='test_user', InsertValue={'name':'testInserOne','age':1}):
        if self.IsTebleExist(TableName)==False:
            logging.debug('Table is NOT exist: %s' % TableName)
            return False
        if len(InsertValue)==0 : return '无数据传入'
        col,val='',''
        for k in InsertValue:
            col = col+k+','
            val = val+"'"+str(InsertValue[k])+"'"+','
        col=col.rstrip(',')
        val=val.rstrip(',')
        sql = 'insert into %s (%s) values (%s);' % (TableName, col, val)
        logging.debug(sql)
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            logging.debug('Insert values is successful.')
        except:
            logging.debug('Insert values is fail !')

    # 作废
    #插入多条记录
    def InsertValueMulti_old(self,
                         TableName='test_user',
                         InertValueList=[('name','age'),
                                         ('testInsertValueMulti1',88),
                                         ('testInsertValueMulti2',99)]):
        logging.debug('InsertValueMulti 开始执行')
        if self.IsTebleExist(TableName)==False:
            logging.debug('Table is NOT exist: %s' % TableName)
            return False
        if len(InertValueList)==0 : return '无数据传入'
        sql_ahead ='insert into %s ' % (TableName)

        # 处理字段元组
        col = InertValueList[0]
        if not '*' in col:       # 包含 '*' 时，表示所有字段
            sql_ahead += '('
            for x in col:
                sql_ahead = sql_ahead+str(x)+','
            sql_ahead = sql_ahead.rstrip(',') + ')'

        # 处理插入的值
        sql_ahead += ' values ('
        for n in range(1,len(InertValueList)):
            val=InertValueList[n]
            sql = sql_ahead
            for x in val:
                sql = sql + "'" + str(x) + "',"
            sql = sql.rstrip(',') + ');'
            try:
                self.cursor.execute(sql)
                self.connect.commit()
                logging.debug('插入数据成功：%s' % sql)
            except:
                logging.error('插入数据失败：\n  %s' % sql)
        logging.debug('InsertValueMulti 执行完成')

    # 执行一条完整的插入命令，格式：
    #  .InsterExecute("inster into test_user ('id','name','age') values (1,'Tom',23);")
    def InsterExecute(self,ExeCommand=None):
        if ExeCommand==None:
            logging.error('没有参数（命令执行语句）传递进来！')
        else:
            try:
                self.cursor.execute(ExeCommand)
                self.connect.commit()
                logging.debug('成功执行了命令: %s' % ExeCommand)
            except:
                logging.error('执行命令失败: \n  %s' % ExeCommand)
        logging.debug('执行完成')



    ###  第 4 部分：表的记录 （增删改查） -- 第 2 节：删   #####

    # 删除记录
    def RecordeDelete(self,TableName='test_user',Condition=0):
        msg = 'Reference: .RecordeDelete(TableName,Condition)'
        if self.IsTebleExist(TableName)==False:
            logging.error('Table is NOT exist: %s' % TableName)
            return False
        sql_command = 'delete from %s where %s ' % (TableName,Condition)
        logging.debug(sql_command)
        try:
            self.cursor.execute(sql_command)
            logging.debug('Delete recorde sucessful ! ' )
            return True
        except:
            logging.error('Delete recorde fail !\n %s' % (msg))
            return True

    # 清空数据（表的初始化）
    # SQLite 不支持 truncate 进行初始化。
    # 当 SQLite 数据库中包含自增列时，会自动建立一个名为 sqlite_sequence 的表。
    # 这个表包含两个列：name 和 seq。name 记录自增列所在的表，seq 记录当前序号
    # （下一条记录的编号就是当前序号加 1）。
    # 如果要将递增数归零: DELETE FROM sqlite_sequence WHERE name = 'table_name';
    # 或者：UPDATE sqlite_sequence SET seq = 0 WHERE name = 'table_name';
    def RecordeTruncate(self,TableName):
        if self.IsTebleExist(TableName)==False:
            logging.error('Table is NOT exist: %s' % TableName)
            return False
        try:
            sql_command1 = 'DELETE FROM %s;' % TableName
            sql_command2 = "DELETE FROM sqlite_sequence WHERE name = '%s';" % TableName
            self.cursor.execute(sql_command1)
            self.cursor.execute(sql_command2)
            self.connect.commit()
            logging.debug('Recorde truncate sucessful !'
                          '\n  %s\n  %s' % (sql_command1, sql_command2))
            return True
        except:
            logging.debug('Recorde truncate fail ! '
                          '\n  %s\n  %s' % (sql_command1,sql_command2))
            return False

    ###  第 4 部分：表的记录 （增删改查） -- 第 3 节：改   ######
    def RecordeUpdate(self,TableName='test_user',SetNewValue=None,Condition=True):
        msg = 'Reference: .RecordeUpdate(TableName,SetNewValue,Condition)'
        if self.IsTebleExist(TableName)==False:
            logging.error('Table is NOT exist: %s' % TableName)
            return False
        if SetNewValue==None:
            logging.error('Recorde update fail ! \n ' + msg)
            return False
        sql_command = 'update %s set %s where %s' % (TableName,SetNewValue,Condition)
        try:
            self.cursor.execute(sql_command)
            logging.debug('Update recorde sucessful ! (%s)' % sql_command)
            return True
        except:
            logging.debug('Update recorde fail ! (%s)' % sql_command)
            return False


    ###  第 4 部分：表的记录 （增删改查） -- 第 4 节：查   ######

    # 查询一个表
    def query_table(self,TableName='test_user'):
        if self.IsTebleExist(TableName)==False:
            logging.error('查询错误，表不存在：%s' % TableName)
            return ['查询错误，表不存在：%s' % TableName]
        sql = "select * from %s " % TableName
        self.cursor.execute(sql)
        re = self.cursor.fetchall()
        return re

    # 执行一条完整的查询命令,格式：
    # .query_execute("select * from test_user;")
    def query_execute(self,sql_command):
        try:
            self.cursor.execute(sql_command)
            logging.debug('查询成功：%s' % sql_command)
            return self.cursor.fetchall()
        except:
            logging.error('查询错误：%s' % sql_command)
            return ['查询错误：%s' % sql_command]

    def test(self):
        self.CreateTable()
        self.InsertValue()
        re=self.query_table()
        for x in re: print(x)



#测试试用
def test():
    t = dbt()
    t.test()
# test()









