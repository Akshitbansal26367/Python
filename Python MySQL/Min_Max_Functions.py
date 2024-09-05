import pymysql as mq

mysql = mq.connect(
    user="root",
    host="localhost",
    password="",
    database="world"
)

myCursor = mysql.cursor()

try:
    print("Maximum Order amount in the table is", end=" ")
    selectQ = "Select max(order_amount) from orders"
    myCursor.execute(selectQ)
    sData = myCursor.fetchall()

    for s in sData:
        print(s[0])

except mq.MySQLError as e:
    print(f"MySQL error while printing data is {e}")

except Exception as e:
    print(f"General error while printing data is {e}")

finally:
    myCursor.close()
    mysql.close()
