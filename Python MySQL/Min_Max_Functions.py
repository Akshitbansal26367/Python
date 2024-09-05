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
    selectMax = "Select max(order_amount) from orders"
    myCursor.execute(selectMax)
    sMax = myCursor.fetchone()
    print((sMax[0]))

    print("Minimum Order amount in the table is", end=" ")
    selectMin = "Select min(order_amount) from orders"
    myCursor.execute(selectMin)
    sMin = myCursor.fetchone()
    print(sMin[0])

except mq.MySQLError as e:
    print(f"MySQL error while printing data is {e}")

except Exception as e:
    print(f"General error while printing data is {e}")

finally:
    myCursor.close()
    mysql.close()
