import csv
import re
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QFile, QTextStream, QTimer
from PyQt5.QtWidgets import QApplication, QFrame, QWidget, QGridLayout, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QScrollArea, QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt, QRect, QCoreApplication, QMetaObject
from widget_courseItem import Ui_CourseItem
from widget_studentItem import Ui_StudentItem
from widget_courseItemCreate import Ui_CourseCreate
from widget_courseItemEdit import Ui_CourseEdit
from crud_utils import CRUD_Data
from widget_studentItemCreate import Ui_StudentCreate
from PyQt5.QtWidgets import QScrollArea, QMessageBox
from widget_studentItemEdit import Ui_StudentEdit

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.CRUD_Student = CRUD_Data(csv_name='Students', key='id_num', attributes=('id_num', 'full_name', 'course', 'yr_lvl', 'gender', 'status'))
        self.CRUD_Course = CRUD_Data(csv_name='Courses', key='course_code', attributes=('course_code', 'course_description'))
        self.mode = 'Students'
        self.initGUIBeforeHeader(MainWindow)
        self.initGUIHeader(MainWindow)
        self.initGUIAfterHeader(MainWindow)
        self.initFunctionality()
    
    # GUI FUNCTIONALITY    
    def initFunctionality(self):
        self.btn_addItem.clicked.connect(self.addClicked)
        self.btn_displayStudents.clicked.connect(self.displayStudents)
        self.btn_displayCourses.clicked.connect(self.displayCourses)
        self.fld_searchBar.textChanged.connect(self.searchItem)
    
    # GUI APPEARANCE
    def initGUIBeforeHeader(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowTitle("Simple Student Information System")
        MainWindow.resize(626, 454)
        MainWindow.setMinimumSize(840, 420)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.btn_displayStudents = QPushButton(self.centralwidget)
        self.btn_displayStudents.setObjectName(u"btn_displayStudents")

        self.horizontalLayout_5.addWidget(self.btn_displayStudents)

        self.btn_displayCourses = QPushButton(self.centralwidget)
        self.btn_displayCourses.setObjectName(u"btn_displayCourses")

        self.horizontalLayout_5.addWidget(self.btn_displayCourses)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label)

        self.fld_searchBar = QLineEdit(self.centralwidget)
        self.fld_searchBar.setObjectName(u"fld_searchBar")

        self.horizontalLayout_5.addWidget(self.fld_searchBar)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.divider = QFrame(self.centralwidget)
        self.divider.setObjectName(u"divider")
        self.divider.setFrameShape(QFrame.HLine)
        self.divider.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.divider)

        self.horizontalLayout_2 = QHBoxLayout()      
    def initGUIHeader(self, MainWindow):
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(18, -1, 45, -1)
        self.lbl_hdr_idnum = QLabel(self.centralwidget)
        self.lbl_hdr_idnum.setObjectName(u"lbl_hdr_idnum")
        self.horizontalLayout_2.addWidget(self.lbl_hdr_idnum)

        self.lbl_hdr_name = QLabel(self.centralwidget)
        self.lbl_hdr_name.setObjectName(u"lbl_hdr_name")
        self.horizontalLayout_2.addWidget(self.lbl_hdr_name)

        self.lbl_hhr_course = QLabel(self.centralwidget)
        self.lbl_hhr_course.setObjectName(u"lbl_hhr_course")
        self.horizontalLayout_2.addWidget(self.lbl_hhr_course)

        self.lbl_hdr_yrlvl = QLabel(self.centralwidget)
        self.lbl_hdr_yrlvl.setObjectName(u"lbl_hdr_yrlvl")
        self.horizontalLayout_2.addWidget(self.lbl_hdr_yrlvl)

        self.lbl_hdr_gender = QLabel(self.centralwidget)
        self.lbl_hdr_gender.setObjectName(u"lbl_hdr_gender")
        self.horizontalLayout_2.addWidget(self.lbl_hdr_gender)

        self.lbl_hdr_status = QLabel(self.centralwidget)
        self.lbl_hdr_status.setObjectName(u"lbl_hdr_status")
        self.horizontalLayout_2.addWidget(self.lbl_hdr_status)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(1, 5)
        self.horizontalLayout_2.setStretch(2, 2)
        self.horizontalLayout_2.setStretch(3, 2)
        self.horizontalLayout_2.setStretch(4, 2)
        self.horizontalLayout_2.setStretch(5, 2)
        self.horizontalLayout_2.setStretch(6, 4)
        
        # Set labels text for students mode
        self.lbl_hdr_idnum.setText("ID Number")
        self.lbl_hdr_name.setText("Full Name")
        self.lbl_hhr_course.setText("Course")
        self.lbl_hdr_yrlvl.setText("Year Level")
        self.lbl_hdr_gender.setText("Gender")
        self.lbl_hdr_status.setText("Status")    
    def initGUIAfterHeader(self,MainWindow):
        
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 604, 313))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_7)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.btn_addItem = QPushButton(self.centralwidget)
        self.btn_addItem.setObjectName(u"btn_addItem")

        self.operation_status = QLabel(self.centralwidget)
        self.operation_status.setObjectName(u"operation_status")
        self.operation_status.setText("...")
        self.operation_status.setStyleSheet("padding-left: 11px;")
        self.horizontalLayout_7.addWidget(self.operation_status)
        
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)
        self.horizontalLayout_7.addWidget(self.btn_addItem)

        self.verticalLayout_2.addLayout(self.horizontalLayout_7)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.lbl_courseCode = QLabel(self.centralwidget)
        self.lbl_courseDescription = QLabel(self.centralwidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        # Add Styling
        self.loadStylesheet()
        
        # List Students
        self.scroll_contents_layout = QVBoxLayout(self.scrollAreaWidgetContents_7)
        self.scroll_contents_layout.setAlignment(Qt.AlignTop)
        
        self.list() 
    def loadStylesheet(self):
        style_sheet_file = QFile("styles_main.qss")  # Path to your QSS file
        if style_sheet_file.open(QFile.ReadOnly | QFile.Text):
            text_stream = QTextStream(style_sheet_file)
            stylesheet = text_stream.readAll()
            QApplication.instance().setStyleSheet(stylesheet)
        else:
            print("Failed to load stylesheet.")       
    def retranslateUi(self, MainWindow):
        self.btn_displayStudents.setText(QCoreApplication.translate("MainWindow", u"DISPLAY STUDENTS", None))
        self.btn_displayCourses.setText(QCoreApplication.translate("MainWindow", u"DISPLAY COURSES", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Search: ", None))
        self.lbl_hdr_idnum.setText(QCoreApplication.translate("MainWindow", u"ID Number", None))
        self.lbl_hdr_name.setText(QCoreApplication.translate("MainWindow", u"Full Name", None))
        self.lbl_hhr_course.setText(QCoreApplication.translate("MainWindow", u"Course", None))
        self.lbl_hdr_yrlvl.setText(QCoreApplication.translate("MainWindow", u"Year Level", None))
        self.lbl_hdr_gender.setText(QCoreApplication.translate("MainWindow", u"Gender", None))
        self.lbl_hdr_status.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.btn_addItem.setText(QCoreApplication.translate("MainWindow", u"ADD NEW STUDENT", None))

    ##############################################
    #                  CREATE                    #
    ##############################################
    
    def addClicked(self):
        self.clearScrollContents()
        self.list()
        if self.mode == 'Students':
            self.prompt("Add a student.")
            # Create an instance of Ui_StudentCreate
            student_create_widget = QtWidgets.QWidget()
            student_create_ui = Ui_StudentCreate()
            student_create_ui.setupUi(student_create_widget)
            
            student_create_ui.btn_save.clicked.connect(lambda: self.saveStudentClicked(student_create_ui))
            student_create_ui.btn_cancel.clicked.connect(self.list)
            # Add the widget to the vertical layout
            self.scroll_contents_layout.addWidget(student_create_widget)
        elif self.mode == 'Courses':
            self.prompt("Add a course.")
            # Create an instance of Ui_CourseCreate
            course_create_widget = QtWidgets.QWidget()
            course_create_ui = Ui_CourseCreate()
            course_create_ui.setupUi(course_create_widget)
            
            course_create_ui.btn_save.clicked.connect(lambda: self.saveCourseClicked(course_create_ui.line_courseCode, course_create_ui.line_courseDescription))
            course_create_ui.btn_cancel.clicked.connect(self.list)
            # Add the widget to the vertical layout
            self.scroll_contents_layout.addWidget(course_create_widget)
        
        
        QtCore.QTimer.singleShot(100, self.scrollToBottom)        
    
    def saveStudentClicked(self, student_create_ui):
        # Get the contents of the line edits and combo boxes
        student_id = student_create_ui.fld_idNum.text()
        student_name = student_create_ui.fld_fullName.text()
        course = student_create_ui.cbb_course.currentText()
        year_level = student_create_ui.cbb_yrLvl.currentText()
        gender = student_create_ui.cbb_gender.currentText()
        if course == 'NONE' or course == '':
            status = 'Not Enrolled'
        else:
            status = 'Enrolled'
        # Validate the data
        if self.validateStudentData(student_id, student_name, course, year_level, gender):
            # Perform CRUD operation to save the student
            self.CRUD_Student.create(id_num=student_id, full_name=student_name, course=course, yr_lvl=year_level, gender=gender, status=status)
            self.list()
        else:
            pass
    
    def addStudent(self, id_number, full_name, course, year_level, gender, status):
        # Create a new instance of the student item with the provided details
        student_item = Ui_StudentItem()
        student_item_widget = QtWidgets.QWidget()
        student_item.setupUi(student_item_widget, id_number, full_name, course, year_level, gender, status)
        # Connect edit and delete signals to lambda functions passing id_number
        student_item.btn_edit.clicked.connect(lambda: self.editStudentClicked(id_number))
        student_item.btn_delete.clicked.connect(lambda: self.deleteStudentClicked(id_number))
        # Add the student item widget to the existing layout
        self.scroll_contents_layout.addWidget(student_item_widget)
    
    def saveCourseClicked(self, line_courseCode, line_courseDescription):
        # Get the contents of the line edits
        course_code = line_courseCode.text()
        course_description = line_courseDescription.text()

        # Validate the data
        if self.validateCourseData(course_code, course_description):
            self.CRUD_Course.create(course_code=course_code, course_description=course_description)
            self.list()
        else:
            pass
    
    def addCourse(self, course_code, course_desc):
        # Create a new instance of the student item with the provided details
        course_item = Ui_CourseItem()
        course_item_widget = QtWidgets.QWidget()
        course_item.setupUi(course_item_widget, course_code, course_desc)
        # Connect edit and delete signals to lambda functions passing id_number
        course_item.btn_edit.clicked.connect(lambda: self.editCourseClicked(course_code))
        course_item.btn_delete.clicked.connect(lambda: self.deleteCourseClicked(course_code))
        # Add the student item widget to the existing layout
        self.scroll_contents_layout.addWidget(course_item_widget)

    ##############################################
    #                  UPDATE                    #
    ##############################################  
    
    def editStudentClicked(self, id_number):
        self.clearScrollContents()
        self.fld_searchBar.setText = ""
        student_edit_widget = QtWidgets.QWidget()
        student_edit_ui = Ui_StudentEdit()

        # Initialize variables to hold the details of the found student
        found_student = None
        rows_total = row_of_element = 0
                
        # Find the student with the given id_number and skip it during listing
        with open(self.CRUD_Student.csv_path, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['id_num'] != id_number:
                    # If the current student is not the one being edited, add it to the list
                    id_num = row['id_num']
                    full_name = row['full_name']
                    course = row['course']
                    year_level = row['yr_lvl']
                    gender = row['gender']
                    status = row['status']
                    self.addStudent(id_num, full_name, course, year_level, gender, status)
                    rows_total += 1
                else:
                    # If the current student matches the one being edited, save its details
                    found_student = {
                        'id_number': id_number,
                        'full_name': row['full_name'],
                        'course': row['course'],
                        'year_level': row['yr_lvl'],
                        'gender': row['gender'],
                        'status': row['status']
                    }
                    prompt = ("Now Editing Student %s, %s." % (found_student["id_number"], found_student["full_name"]))
                    student_edit_ui.setupUi(student_edit_widget, found_student['id_number'], found_student['full_name'],
                                            found_student['course'], found_student['year_level'], found_student['gender'],
                                            found_student['status'])

                    # Connect save and cancel signals to appropriate methods
                    student_edit_ui.btn_save.clicked.connect(
                        lambda: self.saveEditedStudent(found_student['id_number'], student_edit_widget))
                    student_edit_ui.btn_cancel.clicked.connect(self.list)

                    # Add the student edit form widget to the existing layout
                    self.scroll_contents_layout.addWidget(student_edit_widget)
                    row_of_element = rows_total

            self.prompt(prompt)
            scroll_bar = self.scrollArea.verticalScrollBar()

            if rows_total > 0:
                # Calculate the value for the desired percentage
                percentage = float(row_of_element) / float(rows_total)
                print(percentage)
                scroll_value = int(75*row_of_element)
                print(scroll_value)
                # Set the scroll bar's value to the calculated value if search bar populated
                QTimer.singleShot(100, lambda: scroll_bar.setSliderPosition(scroll_value))   
    
    def saveEditedStudent(self, id_number, student_edit_widget):
        # Access child widgets from student_edit_widget
        fld_fullName = student_edit_widget.findChild(QtWidgets.QLineEdit, "fld_fullName")
        cbb_course = student_edit_widget.findChild(QtWidgets.QComboBox, "cbb_course")
        cbb_yrLvl = student_edit_widget.findChild(QtWidgets.QComboBox, "cbb_yrLvl")
        cbb_gender = student_edit_widget.findChild(QtWidgets.QComboBox, "cbb_gender")

        # Get the updated information from the widgets
        if cbb_course.currentText() == 'NONE':
            status = 'Not Enrolled'
        else:
            status = 'Enrolled'

        updated_info = {
            'id_num': id_number,
            'full_name': fld_fullName.text(),
            'course': cbb_course.currentText(),
            'yr_lvl': cbb_yrLvl.currentText(),
            'gender': cbb_gender.currentText(),
            'status': status
        }

        # Save the updated information to the CSV
        print(updated_info['id_num'])
        self.CRUD_Student.update(id_number, **updated_info)
        
        # Re-list the students
        self.list()
        self.prompt("Changes to Student %s, %s saved!" %(id_number, updated_info["full_name"]))

        # Get the contents of all fields and combo boxes
        full_name = fld_fullName.text()
        course = cbb_course.currentText()
        year_level = cbb_yrLvl.currentText()
        gender = cbb_gender.currentText()

        # Validate the data
        if self.validateStudentData(id_number, full_name, course, year_level, gender):
            # Call a method with the retrieved contents as parameters
            self.saveStudentData(id_number, full_name, course, year_level, gender)
            self.prompt("Student %s, %s Created!" %(id_number, full_name))
    
    def saveStudentData(self, id_number, full_name, course, year_level, gender):
        if course:
            status = 'Enrolled'
        else:
            status = 'Not Enrolled'
        self.CRUD_Student.create(id_num=id_number, full_name=full_name, course=course, yr_lvl=year_level, gender=gender, status=status)
        self.list()  # Re-list the students after saving
        self.prompt("Student %s saved successfully." % id_number)        
    
    def editCourseClicked(self, course_code):
        self.clearScrollContents()
        self.fld_searchBar.setText = ''
        found_course = None
        rows_total = row_of_element = 0

        with open(self.CRUD_Course.csv_path, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['course_code'] == course_code:
                    found_course = {
                        'course_code': course_code,
                        'course_description': row['course_description']
                    }
                    break  # Exit the loop after finding the course

        # List all courses
        with open(self.CRUD_Course.csv_path, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                course_code = row['course_code']
                course_description = row['course_description']
                if found_course is not None and course_code == found_course['course_code']:
                    # If the course to be edited is found, add the edit widget
                    course_edit_widget = QtWidgets.QWidget()
                    course_edit_ui = Ui_CourseEdit()
                    course_edit_ui.setupUi(course_edit_widget, found_course['course_code'],
                                            found_course['course_description'])
                    course_edit_ui.btn_save.clicked.connect(
                        lambda: self.saveEditedCourse(found_course['course_code'], course_edit_widget))
                    course_edit_ui.btn_cancel.clicked.connect(self.list)
                    self.scroll_contents_layout.addWidget(course_edit_widget)
                    row_of_element = rows_total
                    self.prompt("Now Editing Course "+ course_code + ".")
                else:
                    # Otherwise, add the course item
                    self.addCourse(course_code, course_description)
                    rows_total += 1

        # Scroll to the position of the edited course if found
        if rows_total > 0:
            # Calculate the value for the desired percentage
            percentage = float(row_of_element) / float(rows_total)

            # Set the scroll bar's value to the calculated value after a delay
            QTimer.singleShot(100, lambda: self.scrollToPercentage(percentage))
    
    def saveEditedCourse(self, course_code, course_edit_widget):
        # Access child widgets from course_edit_widget
        line_courseCode = course_edit_widget.findChild(QtWidgets.QLabel, "lbl_courseCode")
        line_courseDescription = course_edit_widget.findChild(QtWidgets.QLineEdit, "line_courseDescription")

        # Get the updated information from the widgets
        updated_info = {
            'course_code': line_courseCode.text(),
            'course_description': line_courseDescription.text()
        }

        # Save the updated information to the CSV
        self.CRUD_Course.update(course_code, **updated_info)
        
        # Re-list the courses or perform any other necessary action
        self.list()
        self.prompt("Changes to Course %s saved!" % course_code)      
    
    ##############################################
    #                  DELETE                    #
    ##############################################  
    
    def deleteStudentClicked(self, id_number):
        # Creating a confirmation dialog
        confirmation = QMessageBox.question(MainWindow, 'Confirmation', 
                                            "Are you sure you want to delete student %s?" % id_number, 
                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        
        if confirmation == QMessageBox.Yes:
            # Proceed with deletion if confirmed
            self.CRUD_Student.delete(id_number)
            self.list()
            self.prompt("Student %s deleted." % id_number)
        else:
            # Cancel deletion if not confirmed
            self.prompt("Deletion cancelled.")
    
        
    def deleteCourseClicked(self, course_code):
        # Creating a confirmation dialog
        confirmation = QMessageBox.question(MainWindow, 'Confirmation', 
                                            "Are you sure you want to delete course %s?" % course_code, 
                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        
        if confirmation == QMessageBox.Yes:
            # Update the course code to 'NONE' and status to 'Not Enrolled' for all students with the specified course code
            with open(self.CRUD_Student.csv_path, 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                updated_students = []
                for row in reader:
                    if row['course'] == course_code:
                        row['course'] = 'NONE'
                        row['status'] = 'Not Enrolled'
                    updated_students.append(row)
            # Write back the updated data to the CSV file
            with open(self.CRUD_Student.csv_path, 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=self.CRUD_Student.attributes)
                writer.writeheader()
                writer.writerows(updated_students)
                
            self.CRUD_Course.delete(course_code)
            self.list()
            self.prompt("Course %s deleted." % course_code)
        else:
            # Cancel deletion if not confirmed
            self.prompt("Deletion cancelled.")
  
    ##############################################
    #                   LIST                     #
    ##############################################  
     
    def displayStudents(self):
        self.fld_searchBar.clear()
        self.lbl_hdr_idnum.setText("ID Number")
        self.lbl_hdr_name.setText("Full Name")
        self.lbl_hhr_course.setText("Course ")
        self.lbl_hdr_yrlvl.setText("Year Level")
        self.lbl_hdr_gender.setText("Gender")
        self.lbl_hdr_status.setText("Status")
        self.mode='Students'
        self.list()
        self.btn_addItem.setText("ADD NEW STUDENT")

    def displayCourses(self):
        self.fld_searchBar.clear()
        self.lbl_hdr_idnum.setText("Course Code")
        self.lbl_hdr_name.setText("Course Description")
        self.lbl_hhr_course.setText(" ")
        self.lbl_hdr_yrlvl.setText(" ")
        self.lbl_hdr_gender.setText(" ")
        self.lbl_hdr_status.setText(" ")
        self.mode='Courses'
        self.list()
        self.btn_addItem.setText("ADD NEW COURSE")
        self.prompt("Now displaying Courses.")
 
    def list(self):
            #Clear CSV and Field
            self.fld_searchBar.clear()
            while self.scroll_contents_layout.count():
                child = self.scroll_contents_layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()
            if(self.mode == 'Students'):
                self.prompt("Listing Students...")
                with open(self.CRUD_Student.csv_path, 'r', newline='') as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        id_number = row['id_num']
                        full_name = row['full_name']
                        course = row['course']
                        year_level = row['yr_lvl']
                        gender = row['gender']
                        status = row['status']
                        # Call addStudent method with retrieved values
                        self.addStudent(id_number, full_name, course, year_level, gender, status)
                self.prompt("Now displaying Students.")
            else:
                self.prompt("Listing Courses...")
                with open(self.CRUD_Course.csv_path, 'r', newline='') as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        course_code = row['course_code']
                        course_desc = row['course_description']
                        # Call addCourse method with retrieved values
                        self.addCourse(course_code, course_desc)
                                    
    def listStudentsByScore(self, query):
        self.clearScrollContents()
        
        # Define variables to store the highest match score and its corresponding student details
        highest_match_score = 0
        highest_match_student = None
        
        with open(self.CRUD_Student.csv_path, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            
            # Iterate through each row in the CSV
            for row in reader:
                # Calculate match score for the current row
                row_score = self.CRUD_Student._calculate_match_score(query=query, row=row)
                
                # Check if the current row has a higher match score than the highest match score so far
                if row_score > highest_match_score:
                    highest_match_score = row_score
                    highest_match_student = row
            
            # Add the highest match student to the UI (assuming self.addStudent method adds a student to the UI)
            if highest_match_student is not None:
                self.addStudent(highest_match_student['id_num'], highest_match_student['full_name'], highest_match_student['course'], highest_match_student['yr_lvl'], highest_match_student['gender'], highest_match_student['status'])
            
            # Reset the file pointer to read from the beginning of the file
            csvfile.seek(0)
            next(reader)  # Skip the header
            
            # Iterate through the remaining rows in the CSV
            for row in reader:
                # Calculate match score for the current row
                row_score = self.CRUD_Student._calculate_match_score(query=query, row=row)
                
                # Check if the row score is within a certain range of the highest match score
                if highest_match_score - 15 < row_score <= highest_match_score:
                    # Skip adding the highest match student again
                    if row != highest_match_student:
                        self.addStudent(row['id_num'], row['full_name'], row['course'], row['yr_lvl'], row['gender'], row['status'])
                        
        # Print a message indicating the closest match score
        if highest_match_student is not None:
            self.prompt("Students matching '%s' listed. (CLOSEST MATCH: %d%%)" % (query, highest_match_score))

    def listCoursesByScore(self, query):
        self.clearScrollContents()
        with open(self.CRUD_Course.csv_path, 'r', newline='') as csvfile:
            self.prompt("Reading File.")
            reader = csv.DictReader(csvfile)
            highest_match_score = 0
            highest_match_course = None
            
            # First, find the highest scoring course
            for row in reader:
                course_code = row['course_code']
                course_desc = row['course_description']
                row_score = self.CRUD_Course._calculate_match_score(query=query, row=row)
                if row_score > highest_match_score:
                    highest_match_score = row_score
                    highest_match_course = row
            
            # Add the highest scoring course to the scroll contents
            if highest_match_course is not None:
                self.addCourse(highest_match_course['course_code'], highest_match_course['course_description'])

            # Reset the file pointer to the beginning and skip header
            csvfile.seek(0)
            next(reader)

            # Iterate over other courses and add them based on their scores
            self.prompt("Adding Course Items.")
            for row in reader:
                course_code = row['course_code']
                course_desc = row['course_description']
                # Calculate match score for the current row
                row_score = self.CRUD_Course._calculate_match_score(query=query, row=row)
                # Check if the row score is within a certain range of the highest match score
                if highest_match_score - 15 < row_score <= highest_match_score:
                    # Skip adding the highest scoring course again
                    if course_code != highest_match_course['course_code']:
                        self.addCourse(course_code, course_desc)
                        
        self.prompt("Courses matching '%s' listed. (CLOSEST MATCH: %d%%)" % (query, highest_match_score))


            
    ##############################################
    #              HELPER METHODS                #
    ############################################## 
     
    def validateCourseData(self, course_code, course_description):
        print(course_code, course_description)
        if (course_code=="" or course_description==""):
            self.prompt("Error: Course code and description are required.")
            return False

        # Check if the course code is unique
        if self.CRUD_Course._exists(course_code):
            self.prompt("Course %s already exists." %(course_code))
            return False

        # If validation passes, print a success message
        print("Course data is valid.")
        return True    
    
    def scrollToBottom(self):
        scroll_bar = self.scrollArea.verticalScrollBar()
        scroll_bar.setValue(scroll_bar.maximum())
    
    def scrollToPercentage(self, percentage):
        scroll_bar = self.scrollArea.verticalScrollBar()
        scroll_value = int(scroll_bar.maximum() * percentage)
        scroll_bar.setSliderPosition(scroll_value)
                     
    def searchItem(self):
        try:
            query = str(self.fld_searchBar.text())  # Get the text from the search bar and convert it to a string
        except:
            query = ""
        
        if query.strip():  # Check if the query is not empty after stripping whitespace
            try:
                if self.mode == 'Students':
                    self.listStudentsByScore(query)
                else:
                    self.listCoursesByScore(query)
            except:
                # Handle any exceptions that might occur during the search
                self.list()
        else:
            self.list()

    def validateStudentData(self, id_number, full_name, course, year_level, gender):
        # Check if all fields are filled in
        if not (id_number and full_name and course and year_level and gender):
            self.prompt("Fields must not be left blank.")
            return False
            
        # Check if ID number is in the format ####-####
        if not re.match(r'^\d{4}-\d{4}$', id_number):
            self.prompt("ID Number must be in the format ####-####")
            return False
            
        # Check if ID number already exists in the CSV
        if self.CRUD_Student._exists(id_number):
            return False

        return True                    
    
    def clearScrollContents(self):
        # Clear all widgets from the scroll area
        while self.scroll_contents_layout.count():
            child = self.scroll_contents_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
                
    def prompt(self, message):
        self.operation_status.setText(message)
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
