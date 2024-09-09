import pymysql as mq

# Establish the connection to the MySQL database
mysql = mq.connect(
    host="localhost",
    user="root",
    password="",
    database="school"
)

# Create a cursor object using the connection
cursorObj = mysql.cursor()

# Prompt the user for student details
name = input("Enter the student name : ")
class_name = input("Enter the class name : ")
st_email = input("Enter the email : ")
st_id = input("Enter the student ID : ")

# SQL query to update the student record with the provided details
sql = "UPDATE student SET st_name=%s, st_class = %s, st_email = %s WHERE st_id = %s"
data = (name, class_name, st_email, st_id)

try:
    cursorObj.execute(sql, data)
    mysql.commit()
    print("Data Updated Successfully")

except mq.MySQLError as e:
    print(f"MySQL error is: {e}")

finally:
    cursorObj.close()
    mysql.close()
