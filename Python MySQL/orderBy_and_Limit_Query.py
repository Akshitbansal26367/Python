import pymysql as mq

mysql = mq.connect(
    host="localhost",
    user="root",
    password="",
    database="school"
)

myCursor = mysql.cursor()
print("{:<15} {:<20} {:<20} {:<20}".format("Student ID", "Student Name", "Student Class",
                                           "Student Email"))

try:
    # Results are ordered by student name in ascending order (A to Z)
    # LIMIT 2, 3 means skipping the first 2 records and then retrieving the next 3 records
    SelectQry = "Select * from student order by st_name ASC Limit 2, 3"
    myCursor.execute(SelectQry)
    sData = myCursor.fetchall()

    for s in sData:
        print("{:<15} {:<20} {:<20} {:<20}".format(s[0], s[1], s[2], s[3]))

except mq.MySQLError as e:
    print("MySQL error while printing data is", e)
except Exception as e:
    print("Exception while printing data is", e)

finally:
    myCursor.close()
    mysql.close()
