import pymysql as mq

mysql = mq.connect(
    host="localhost",
    user="root",
    password="",
    database="world"
)

myCursor = mysql.cursor()

try:
    insertTableData = "INSERT INTO country(country_id, country_name) VALUES (%s, %s)"
    t = [(1, "India"), (2, "Sri Lanka"), (3, "Australia")]
    myCursor.executemany(insertTableData, t)
    mysql.commit()
    print("Data inserted into the table")

except mq.MySQLError as e:
    print(f"MySQL error while inserting data into table is {e}")

finally:
    myCursor.close()
    mysql.close()
