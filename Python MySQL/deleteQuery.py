# SQL has the delete command that is used to delete data from a table. The DELETE command delete a row in the table

# commit() is required to make the changes, otherwise no changes are made to the table

import pymysql as mq

# Establish the connection to the MySQL database
mysql = mq.connect(
    host="localhost",
    user="root",
    password="",
    database="school"
)

# Create a cursor object using the connection
myCursor = mysql.cursor()

# Take student ID as input
st_id = input("Enter the student id to be deleted : ")

# SQL query to delete the student with the provided ID
sql = "Delete from student where st_id = %s"

try:
    # Execute the SQL query with the student ID as a parameter
    myCursor.execute(sql, (st_id,))

    # Commit the transaction to make the changes permanent
    mysql.commit()

    print("Student is deleted")

except mq.MySQLError as e:
    # Print any MySQL error that occurs
    print("My SQL error is :", e)

finally:
    # Close the cursor and the connection
    myCursor.close()
    mysql.close()
