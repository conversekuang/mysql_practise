#coding:utf-8
"""                  
MySQLdb只支持Py2    
pymysql 支持3和2    
Mysqldb 和 pymysql 在cursor.execute()只能接受一个参数
因此，不存在    

sql = '语句','参数'
cursor.execute(sql)  #报错，

因此含有变量的写法有两种：

方式1
cursor.execute(sql,参数)


方式2
sql = '语句'%'参数'  #字符串的拼接,其实是一个参数
cursor.execute(sql)

***方式1能够有效的转换特殊字符防止注入，而方式2不能，存在风险

***pymysql 中存在cursor.mogrify()方法，可以打印最后执行的mysql语句

关于pymysql默认select获取的数据是tuple类型，如果想要字典类型的数据，有两种方式

"""
import pymysql.cursors
#安装pymysql
# Connect to the database
# 博客        http://www.cnblogs.com/wt11/p/6141225.html
#datasheet    https://pymysql.readthedocs.io/en/latest/user/index.html
#用法
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='user_information',
                             charset='utf8',
                            )#cursorclass = pymysql.cursors.DictCursor

cursor = connection.cursor()

def create_table():
    sql = """CREATE TABLE client(
             client_id int auto_increment,
             name varchar(20),
             age int,
             phone char(11),
             PRIMARY KEY(client_id)
             )
          """
    cursor.execute(sql)

def insert_data():
    #传递参数的形式
    sql = "INSERT INTO client(name,age,phone)VALUES(%s,%d,%s)"
    cursor.execute(sql,('kzk',28,'13110209659'))

    #
    #sql = "INSERT INTO client(name,age,phone)VALUES('%s','%d','%s')%('kzk',28,'13110209659')
    #cursor.execute(sql)
    

def select_data_paras():
    #方式1#传入参数
    sql = "SELECT * FROM client where name = %s"
    res = cursor.execute(sql, "kzk'or'1")

    print cursor.mogrify(sql, "kzk'or'1")
    #打印出来实际对MYSQL执行的sql语句

    print res
    results = cursor.fetchall()
    print results
    for i in results:
        print i


def select_data_cat():
    #方式2#拼接式导致的SQL注入
    sql = "SELECT * FROM client where name = '%s'"%("kzk'or'1") 
    res = cursor.execute(sql)
    print res
    results = cursor.fetchall()
    for i in results:
        print i
    




if __name__ == '__main__':
    #create_table()
    #insert_data()
    select_data_paras()