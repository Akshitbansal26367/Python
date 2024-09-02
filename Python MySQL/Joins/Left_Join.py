import pymysql as mq

mysql = mq.connect(
    host="localhost",
    user="root",
    password="",
    database="world"
)

myCursor = mysql.cursor()
print("{:<15} {:<20} {:<15}".format("State ID", "State Name", "Country Name"))

try:
    selectData = ("SELECT state.state_id, state.state_name, country.country_name"
                  " FROM state LEFT JOIN country ON state.country_id = country.country_id")
    myCursor.execute(selectData)
    sData = myCursor.fetchall()

    for s in sData:
        print("{:<15} {:<20} {:<15}".format(s[0], s[1], str(s[2])))

except mq.MySQLError as e:
    print(f"MySQL error while displaying data is {e}")

except Exception as e:
    print(f"General error while displaying data is {e}")

finally:
    myCursor.close()
    mysql.close()
