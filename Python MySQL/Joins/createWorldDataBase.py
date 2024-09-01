import pymysql as mq

mysql = mq.connect(
    host="localhost",
    user="root",
    password="",
)

myCursor = mysql.cursor()

try:
    createDatabase = "CREATE DATABASE World"
    myCursor.execute(createDatabase)
    print("DataBase Created")

except mq.MySQLError as e:
    print(f"Error while creating database is {e}")

finally:
    myCursor.close()
    mysql.close()
