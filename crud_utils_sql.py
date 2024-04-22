import mysql.connector
import csv
from mysql.connector import IntegrityError

############################################
#            STUDENTS CRUDL                #
############################################
def importStudentCSVtoDB(csv_name, db_name, host="localhost", user="root", passwd="6t9fagbussyS#1+"):
    
    # Establish database connection
    mydb = mysql.connector.connect(
        host=host,
        user=user,
        passwd=passwd,
        database=db_name
    )

    # Create a cursor object to execute SQL queries
    mycursor = mydb.cursor()

    # Read data from CSV file and insert into database
    with open(csv_name, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Process id_num to remove dash and convert to int
            id_num = int(row['id_num'].replace('-', ''))

            # Process course to handle 'NONE'
            course = None if row['course'] == 'NONE' else row['course']

            # Process status to determine isEnrolled
            isEnrolled = True if row['status'] == 'Enrolled' else False

            # Prepare SQL query
            sql = "INSERT INTO students (id_num, full_name, course, year_level, gender, isEnrolled) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (id_num, row['full_name'], course, row['yr_lvl'], row['gender'], isEnrolled)

            try:
                # Execute the SQL query
                mycursor.execute(sql, val)
                mydb.commit()
                print(f"Record inserted successfully with id_num {id_num}")
            except IntegrityError as e:
                # Ignore duplicate entry errors
                print(f"Ignoring duplicate entry for id_num {id_num}")

    # Close database connection
    mydb.close()

    print("Data insertion completed.")

# Example usage:
importStudentCSVtoDB("Students.csv", "ssisdb")

############################################
#            COURSES  CRUDL                #
############################################

import mysql.connector
import csv
from mysql.connector import IntegrityError

def importCoursesCSVtoDB(csv_name, db_name, host="localhost", user="root", passwd="6t9fagbussyS#1+"):
    """
    Imports data from a CSV file into a MySQL database table for courses.

    Args:
    - csv_name (str): The name of the CSV file containing course data.
    - db_name (str): The name of the MySQL database.
    - host (str): The host address of the MySQL server. Default is "localhost".
    - user (str): The MySQL username. Default is "root".
    - passwd (str): The MySQL password. Default is "6t9fagbussyS#1+".

    Returns:
    - None
    """

    # Establish database connection
    mydb = mysql.connector.connect(
        host=host,
        user=user,
        passwd=passwd,
        database=db_name
    )

    # Create a cursor object to execute SQL queries
    mycursor = mydb.cursor()

    # Read data from CSV file and insert into database
    with open(csv_name, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Prepare SQL query
            sql = "INSERT INTO courses (course_code, course_description) VALUES (%s, %s)"
            val = (row['course_code'], row['course_description'])

            try:
                # Execute the SQL query
                mycursor.execute(sql, val)
                mydb.commit()
                print(f"Record inserted successfully for course {row['course_code']}")
            except IntegrityError as e:
                # Ignore duplicate entry errors
                print(f"Ignoring duplicate entry for course {row['course_code']}")

    # Close database connection
    mydb.close()

    print("Data insertion completed.")

# Example usage:
importCoursesCSVtoDB("Courses.csv", "ssisdb")
