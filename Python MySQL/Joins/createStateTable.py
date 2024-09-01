import pymysql as mq

mysql = mq.connect(
    user="root",
    host="localhost",
    password="",
    database="world"
)

myCursor = mysql.cursor()

try:
    createTable = ("CREATE TABLE State ("
                   "state_id INT PRIMARY KEY AUTO_INCREMENT,"
                   "state_name varchar(30),"
                   "country_id INT"
                   ")")

    myCursor.execute(createTable)
    mysql.commit()
    print("Table Created")

except mq.MySQLError as e:
    print(f"Error while creating table is {e}")

finally:
    myCursor.close()
    mysql.close()
