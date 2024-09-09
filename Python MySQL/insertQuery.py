import pymysql as mq

mysql = mq.connect(
    host="localhost",
    user="root",
    password="",
    database="school"
)

mysqlCursor = mysql.cursor()

try:
    # SQL command to insert data into the student table
    ins = "INSERT INTO student (st_name, st_class, st_email) VALUES(%s, %s, %s)"

    # Tuple with data to be inserted
    # t = ("Ravi", "12th", "ravi@gmail.com")

    t = [("rajesh", "10th", "raj@gmail.com"), ('testing', "10th", "testing@gmail.com"),
         ("aarav", "6th", "aarav@gmail.com"), ("sunil", "12th", "mtqasunilbansal@yahoo.in"),
         ("warner", "10th", "warner310706@gmail.com")]

    # Executing the insert command
    # mysqlCursor.execute(ins, t)

    mysqlCursor.executemany(ins, t)

    mysql.commit()
    print("Record Inserted Successfully")

except mq.MySQLError as e:
    # Handling any MySQL errors that occur
    print(f"Error Occurred : {e}")

finally:
    # Ensuring that resources are closed in the final block
    mysqlCursor.close()
    mysql.close()
