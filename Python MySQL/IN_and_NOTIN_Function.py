import pymysql as mq

mysql = mq.connect(
    host="localhost",
    user="root",
    password="",
    database="world"
)

myCursor = mysql.cursor()

print("{:<20} {:<35} {:<30}".format("Order ID", "Order Date", "Order Amount"))

try:
    # SQL query to select orders not having order_id 1 and 4
    not_in = "Select order_id, order_date, order_amount from orders where order_id not in (1,4)"
    myCursor.execute(not_in)

    sData = myCursor.fetchall()

    for s in sData:
        print("{:<20} {:<35} {:<30}".format(s[0], str(s[1]), s[2]))

except mq.MySQLError as e:
    print(f"MySQL error is {e}")

except Exception as e:
    print(f"General error is {e}")

finally:
    myCursor.close()
    mysql.close()
