import pymysql as mq

mysql = mq.connect(
    user="root",
    host="localhost",
    password="",
    database="world"
)

myCursor = mysql.cursor()

print("{:<15} {:<20} {:<20}".format("State ID", "Country Name", "Country ID"))

try:
    # SQL query to select records where state_id is between 2 and 5 (inclusive)
    # The BETWEEN operator is used to filter the rows based on a range of values.
    # In this case, it will return rows where 'state_id' is 2, 3, 4, or 5.
    BETWEEN_opr = "Select * from state WHERE state_id between 2 and 5"
    myCursor.execute(BETWEEN_opr)
    sData = myCursor.fetchall()

    for s in sData:
        print("{:<15} {:<20} {:<20}".format(s[0], s[1], s[2]))

except mq.MySQLError as e:
    print(f"MySQL error while displaying data is {e}")

except Exception as e:
    print(f"General error while displaying data is {e}")

finally:
    myCursor.close()
    mysql.close()
