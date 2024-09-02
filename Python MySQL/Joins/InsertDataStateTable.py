import pymysql as mq

mysql = mq.connect(
    host="localhost",
    user="root",
    password="",
    database="world"
)

myCursor = mysql.cursor()

try:
    insertData = "INSERT INTO state(state_name, country_id) VALUES (%s, %s)"
    t = [("Rajasthan", 1), ("Delhi", 1), ("Victoria", 3), ("Western Australia", 3), ("Colombo", 2),
         ("Kandy", 2)]
    myCursor.executemany(insertData, t)
    mysql.commit()
    print("Data Entered Successfully!!!")

except mq.MySQLError as e:
    print(f"Error while inserting data is {e}")

finally:
    myCursor.close()
    mysql.close()
