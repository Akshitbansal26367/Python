import pymysql as mq

mysql = mq.connect(
    user="root",
    host="localhost",
    password="",
    database="world"
)

myCursor = mysql.cursor()
print("Total row count is ", end="")

try:
    count_row = "Select count(*) from orders"
    myCursor.execute(count_row)
    sData = myCursor.fetchall()

    for s in sData:
        print(s[0])

except mq.MySQLError as e:
    print(f"MySQL error is {e}")

except Exception as e:
    print(f"MySQL error is {e}")

finally:
    myCursor.close()
    mysql.close()
