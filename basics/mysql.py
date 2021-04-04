import pymysql

conn = pymysql.connect(host='localhost',db='contacts', user='root',password='')
cursor = conn.cursor()
sql = "SELECT * FROM tbl_contacts"
cursor.execute(sql)
result = cursor.fetchall()
for row in result:
    print(row)

