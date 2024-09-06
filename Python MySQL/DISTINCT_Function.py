import pymysql as mq

mysql = mq.connect(
    user="root",
    host="localhost",
    password="",
    database="world"
)

myCursor = mysql.cursor()

print("{:<20}".format("Country ID"))

try:
    # Query to select distinct country_id values from the state table
    Distinct = "Select distinct(country_id) from state"

    myCursor.execute(Distinct)

    sData = myCursor.fetchall()

    for s in sData:
        print("{:<20}".format(s[0]))

except mq.MySQLError as e:
    print(f"MySQL error is : {e}")

except Exception as e:
    print(f"General error is : {e}")

finally:
    myCursor.close()
    mysql.close()
