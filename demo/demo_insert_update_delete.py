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

sql_insert = "INSERT INTO user (userid, username) VALUES (10, 'name10')"
sql_update = "UPDATE user SET username='name99' WHERE userid=9"
sql_delete = "DELETE FROM user WHERE userid<3"

try:
    cursor.execute(sql_insert)
    print(cursor.rowcount)
    cursor.execute(sql_update)
    print(cursor.rowcount)
    cursor.execute(sql_delete)
    print(cursor.rowcount)

    conn.commit()
except Exception as e:
    print(e)
    conn.rollback()

cursor.close()
conn.close()
