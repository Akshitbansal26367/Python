import pymysql as mq

mysql = mq.connect(
    user="root",
    host="localhost",
    password="",
    database="world"
)

myCursor = mysql.cursor()

try:
    # Query to calculate the sum of the 'order_amount' column in the 'orders' table
    sum_elements = "Select sum(order_amount) from orders"
    myCursor.execute(sum_elements)

    sData = myCursor.fetchone()

    print("The sum of order_amount column is : {} ".format(sData[0]))

except mq.MySQLError as e:
    print(f"MySQL error is {e}")

except Exception as e:
    print(f"General error is {e}")

finally:
    myCursor.close()
    mysql.close()
