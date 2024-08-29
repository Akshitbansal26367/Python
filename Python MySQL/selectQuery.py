# Import the pymysql module and alias it as 'mq'
import pymysql as mq

# Establish a connection to the MySQL database
mysql = mq.connect(
    host="localhost",
    user="root",
    password="",
    database="school"
)

# Create a cursor object to interact with the database
myCursor = mysql.cursor()

# Print the table headers for the output in a formatted way
# print("{:<15} {:<20}".format("Student ID", "Student Name"))

# Print the table headers for the output in a formatted way
print("{:<15} {:<20} {:<20} {:<10}".format("Student ID", "Student Name", "Student Email", "Student Class"))

try:
    # SQL query to select student ID and name from the student table
    # sql = "Select st_id, st_name from student"

    # Query to select all columns from the student table
    sql = "Select * from student"

    # Execute the SQL query
    myCursor.execute(sql)

    # Fetch all the results of the executed query
    sData = myCursor.fetchall()

    # Loop through the fetched data and print each student's ID and name
    for s in sData:
        print("{:<15} {:<20} {:<20} {:<10}".format(s[0], s[1], s[2], s[3]))
        # print("{:<15} {:<20}".format(s[0], s[1]))

except mq.MySQLError as e:
    # Handle any MySQL-specific errors
    print(f"The MySQL error is {e}")

except Exception as e:
    # Handle any other general exceptions
    print(f"An error occurred: {e}")

finally:
    # Close the cursor and the database connection
    myCursor.close()
    mysql.close()
