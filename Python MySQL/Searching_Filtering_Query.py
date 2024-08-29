import pymysql as mq

mysql = mq.connect(
    host="localhost",
    user="root",
    password="",
    database="school"
)

myCursor = mysql.cursor()

try:
    # Prompt the user to input the student's names
    name = input("Enter the student name whose record is to be found : ")

    # Prompt the user to input the first character of the student's names
    # name = input("Enter the student name's first character whose record is to be found : ")

    class_name = input("Enter the class of the student                     : ")

    # Construct an SQL query to fetch the student record based on the provided name
    # sql = "Select * from student where st_name = '" + name + "'"
    # The query also filters results by the student's class

    """Construct an SQL query using the LIKE operator to fetch records where the student name contains the input 
    character
    
    The '%' wildcard allows matching of any sequence of characters before and after the input character"""

    sql = "Select * from student where st_name like '%" + name + "%' and st_class = '" + class_name + "'"
    myCursor.execute(sql)
    sData = myCursor.fetchall()
    print()

    print("{:<15} {:<20} {:<20} {:<20}".format("Student ID", "Student Name", "Student Class",
                                               "Student Email"))

    for s in sData:
        print("{:<15} {:<20} {:<20} {:<20}".format(s[0], s[1], s[2], s[3]))

except mq.MySQLError as e:
    print(f"MySQL error while printing is {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    myCursor.close()
    mysql.close()
