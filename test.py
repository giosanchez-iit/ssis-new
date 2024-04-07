import csv
from crud_utils import CRUD_Data

if __name__ == "__main__":
    # Initialize CRUD_Data for courses
    Courses = CRUD_Data(csv_name='Courses', key='course_code', attributes=('course_code', 'course_description'))

    # Populate with 10 courses
    courses_data = [
        ("BSCS", "Bachelor of Science in Computer Studies"),
        ("BAFil", "Bachelor of Arts in Filipino"),
        ("BSEng", "Bachelor of Science in Engineering"),
        ("BSChe", "Bachelor of Science in Chemistry"),
        ("BSEco", "Bachelor of Science in Economics"),
        ("BSBio", "Bachelor of Science in Biology"),
        ("BSPsy", "Bachelor of Science in Psychology"),
        ("BSMath", "Bachelor of Science in Mathematics"),
        ("BSAcc", "Bachelor of Science in Accountancy"),
        ("BSEdu", "Bachelor of Science in Education")
        # Add more courses here
    ]

    for course_code, course_name in courses_data:
        Courses.create(course_code=course_code, course_name=course_name)

    # Example usage: Print all courses
    print("All Courses:")
    all_courses = Courses.retrieve_all()
    for course in all_courses:
        print(course)

    # Example usage: Update course
    Courses.update("BSCS", course_name="Bachelor of Science in Computer Science")

    #
