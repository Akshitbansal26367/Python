# Importing the pymysql library
import pymysql as mq

# Establishing a connection to the MySQL server
myObj = mq.connect(
    # MySQL server is hosted locally on the same machine
    host="localhost",
    # The MySQL username is 'root'
    user="root",
    # No password is set for the 'root' user; adjust if a password is needed
    password=""
)

# Creating a cursor object to interact with the MySQL database
cursorObj = myObj.cursor()

try:
    # SQL query to create a new database named 'school'
    db = "create database school"
    # Executing the SQL query using the cursor object
    cursorObj.execute(db)
    # Printing a success message if the database is created
    print("DataBase Created")

# Handling MySQL-specific errors using the pymysql.MySQLError exception
except mq.MySQLError as e:
    # Printing an error message with details about what went wrong
    print(f"DataBase Error : {e}")

finally:
    # Closing the cursor to free up resources
    cursorObj.close()
    # Closing the connection to the MySQL server to free up resources
    myObj.close()
