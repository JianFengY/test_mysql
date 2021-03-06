"""
Created on 2018/2/18
@Author: Jeff Yang
"""
import pymysql

conn = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123456',
    db='pymysql',
    charset='utf8'  # 注意不是utf-8!
)

cursor = conn.cursor()

sql = "SELECT * FROM user"
cursor.execute(sql)

print(cursor.rowcount)

rs = cursor.fetchone()
print(rs)

rs = cursor.fetchmany(3)
print(rs)

rs = cursor.fetchall()
print(rs)

cursor.close()
conn.close()
