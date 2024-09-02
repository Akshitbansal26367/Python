import pymysql as mq

mysql = mq.connect(
    host="localhost",
    user="root",
    password="",
    database="world"
)

myCursor = mysql.cursor()

print("{:<15} {:<20} {:<20}".format("State ID", "State Name", "Country Name"))

try:
    # Selects the state ID, state name, and country name.
    # The INNER JOIN combines rows from the 'state' and 'country' tables
    # where the 'country_id' matches in both tables. This ensures that only
    # states that have a corresponding country in the 'country' table are included.
    selectData = ("SELECT state.state_id, state.state_name, country.country_name"
                  " FROM state INNER JOIN country ON state.country_id = country.country_id")
    myCursor.execute(selectData)
    sData = myCursor.fetchall()

    for s in sData:
        # print(s)
        print("{:<15} {:<20} {:<20}".format(s[0], s[1], s[2]))

except mq.MySQLError as e:
    print(f"The MySQL error while displaying data is {e}")

except Exception as e:
    print(f"The general error while displaying data is {e}")

finally:
    myCursor.close()
    mysql.close()
