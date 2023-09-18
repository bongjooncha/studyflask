import pymysql

db = pymysql.connect(host="localhost",user='root',password='12345678',charset='utf8',database="member")

ak = db.cursor()
# ak.execute("CREATE DATABASE member")
ak.execute("SHOW DATABASES")

ak.execute("SHOW DATABASES")
for db in ak:
    print(db)