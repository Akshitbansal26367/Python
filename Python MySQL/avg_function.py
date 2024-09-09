import pymysql as mq

mysql = mq.connect(
    user="root",
    host="localhost",
    password="",
    database="world"
)

myCursor = mysql.cursor()
print("Order Average is ", end="")

try:
    avg_function = "Select avg(order_amount) from orders"
    myCursor.execute(avg_function)
    sData = myCursor.fetchone()

    print("{:.2f}".format(sData[0]))

except mq.MySQLError as e:
    print(f"MySQL error is {e}")

except Exception as e:
    print(f"General exception is {e}")

finally:
    myCursor.close()
    mysql.close()
