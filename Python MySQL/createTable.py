import pymysql as mq

# Establishing a connection to the MySQL database
conn = mq.connect(
    host="localhost",
    user="root",
    password="",
    database="school"
)

# Creating a cursor object to interact with the database
mySqlCursor = conn.cursor()

# SQL command to create a new table called 'student'
tc = """CREATE TABLE student (
        st_id INT primary key auto_increment,
        st_name varchar(50),
        st_class varchar(10),
        st_email varchar(50)
        )"""

# Attempt to execute the SQL command within a try block
try:
    mySqlCursor.execute(tc)
    # Commit the transaction
    conn.commit()
    print("Table Created Successfully.")

# Catch any MySQL errors that occur
except mq.MySQLError as e:
    print(f"Error Occurred : {e}")

# Ensure that resources are closed in the final block
finally:
    mySqlCursor.close()
    conn.close()
