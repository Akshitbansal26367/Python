import pymysql as mq

mysql = mq.connect(
    host="localhost",
    user="root",
    password="",
    database="world"
)

myCursor = mysql.cursor()

print("{:<15} {:<10}".format("Country ID", "Country ID Count"))
try:
    # SQL query to get the count of rows for each unique country_id in the state table
    # GROUP BY groups all rows that have the same country_id
    # COUNT(*) counts how many rows exist for each unique country_id after grouping
    GroupBy = "Select count(*), country_id FROM state group by country_id"
    myCursor.execute(GroupBy)
    sData = myCursor.fetchall()

    for s in sData:
        print("{:<15} {:<15}".format(s[1], s[0]))

except mq.MySQLError as e:
    print(f"MySQL error while printing data is {e}")

except Exception as e:
    print(f"General error while printing data is {e}")

finally:
    myCursor.close()
    mysql.close()
