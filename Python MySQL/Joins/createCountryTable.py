import pymysql as mq

mysql = mq.connect(
    host="localhost",
    user="root",
    password="",
    database="world"
)

myCursor = mysql.cursor()

try:
    createTable = ("CREATE TABLE Country ("
                   "country_id INT PRIMARY KEY AUTO_INCREMENT,"
                   "country_name varchar(120)"
                   ")")

    myCursor.execute(createTable)
    print("Table is created")

except mq.MySQLError as e:
    print(f"Error while creating table is {e}")

finally:
    myCursor.close()
    mysql.close()
