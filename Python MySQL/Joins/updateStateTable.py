import pymysql as mq

mysql = mq.connect(
    user="root",
    host="localhost",
    password="",
    database="world"
)

myCursor = mysql.cursor()

try:
    update = """UPDATE state
    SET country_id = 0
    WHERE state_id = 1"""

    myCursor.execute(update)
    mysql.commit()

    print("Data UPDATED")

except mq.MySQLError as e:
    print(f"MySQL error while updating is {e}")

finally:
    myCursor.close()
    mysql.close()
