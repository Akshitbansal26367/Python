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
    eqi_join = """Select state.state_id, state.state_name, country.country_name
    from state, country WHERE state.country_id = country.country_id"""
    myCursor.execute(eqi_join)
    sData = myCursor.fetchall()

    for s in sData:
        print("{:<15} {:<20} {:<20}".format(s[0], s[1], s[2]))

except mq.MySQLError as e:
    print(f"MySQL error is {e}")

except Exception as e:
    print(f"General error is {e}")

finally:
    myCursor.close()
    mysql.close()
