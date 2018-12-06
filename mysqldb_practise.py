#coding:utf-8

import MySQLdb


#参数名叫做passwd  并非  password
conn = MySQLdb.connect(host='localhost',user = 'root', passwd ='', db = 'user_information',charset='utf8')

cursor = conn.cursor()



def find_data():
	sql = "SELECT * FROM client where name = %s"
	res = cursor.execute(sql,"kzk'or '1")
	print res
	print cursor.fetchall()
	return cursor.fetchall() 


def show_tables():
	res = cursor.execute("show tables")
	ress = cursor.fetchall()
	for i in ress:
		print i


if __name__ == '__main__':
	for i in find_data():
		print i