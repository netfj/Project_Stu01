
def test(x=['a',1]):
    print(x)
    for i in x:
        print(i)
user_names = ['id int ','name char(30)','age int']
test(user_names)
test()


def greet_users(names):
    for name in names:
        msg = "hello, " + name.title() + "!"
        print(msg)

user_names = ['a张三', '赵四', '王二']
greet_users(user_names)


def CreateTable(TableName='test_user',
                ColumnList=['ID int identity primary key','name text']
                ):
    print(TableName,ColumnList)

CreateTable('ttt',['a','b'])
CreateTable()