import csv
import re
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QFile, QTextStream
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QWidget, QGridLayout, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QScrollArea, QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt, QRect, QCoreApplication, QMetaObject
from widget_courseItem import Ui_CourseItem
from header_courses import Ui_HeaderCourses
from widget_studentItem import Ui_StudentItem
from widget_courseItem import Ui_CourseItem
from crud_utils import CRUD_Data
from widget_studentItemCreate import Ui_StudentCreate
from PyQt5.QtWidgets import QScrollArea
from header_students import Ui_HeaderStudents

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.CRUD_Student = CRUD_Data(csv_name='Students', key='id_num', attributes=('id_num', 'full_name', 'course', 'yr_lvl', 'gender', 'status'))
        self.CRUD_Course = CRUD_Data(csv_name='Courses', key='course_code', attributes=('course_code', 'course_description'))
        self.mode = 'Students'
        self.initGUIBeforeHeader(MainWindow)
        self.initGUIHeader(MainWindow)
        self.initGUIAfterHeader(MainWindow)
        self.initFunctionality()
        
    def initFunctionality(self):
        self.btn_addItem.clicked.connect(self.addClicked)
        self.btn_displayStudents.clicked.connect(self.displayStudents)
        self.btn_displayCourses.clicked.connect(self.displayCourses)
        self.fld_searchBar.returnPressed.connect(self.searchItem)
    
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
    
    def list(self):
        #Clear CSV First
        while self.scroll_contents_layout.count():
            child = self.scroll_contents_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        if(self.mode == 'Students'):
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
        else:
            with open(self.CRUD_Course.csv_path, 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    course_code = row['course_code']
                    course_desc = row['course_description']
                    # Call addCourse method with retrieved values
                    self.addCourse(course_code, course_desc)

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
        
    def editStudentClicked(self, id_number):
        print("Edit button clicked for student with ID:", id_number)

    def deleteStudentClicked(self, id_number):
        self.CRUD_Student.delete(id_number)
        self.list()
        
    def editCourseClicked(self, course_code):
        print("Edit button clicked for course with ID:", course_code)

    def deleteCourseClicked(self, course_code):
        self.CRUD_Course.delete(course_code)
        self.list()
        
    def addClicked(self):
        # Create an instance of Ui_StudentCreate
        student_create_widget = QtWidgets.QWidget()
        student_create_ui = Ui_StudentCreate()
        student_create_ui.setupUi(student_create_widget)
        
        student_create_ui.btn_save.clicked.connect(lambda: self.saveClicked(student_create_ui))
        # Add the widget to the vertical layout
        self.scroll_contents_layout.addWidget(student_create_widget)
        
        QtCore.QTimer.singleShot(100, self.scrollToBottom)        
        
    def scrollToBottom(self):
        scroll_bar = self.scrollArea.verticalScrollBar()
        scroll_bar.setValue(scroll_bar.maximum())
        
    def saveClicked(self, student_create_ui):
        # Get the contents of all fields and combo boxes
        id_number = student_create_ui.fld_idNum.text()
        full_name = student_create_ui.fld_fullName.text()
        course = student_create_ui.cbb_course.currentText()
        year_level = student_create_ui.cbb_yrLvl.currentText()
        gender = student_create_ui.cbb_gender.currentText()

        # Call a method with the retrieved contents as parameters
        self.saveStudentData(id_number, full_name, course, year_level, gender)
    
    def saveStudentData(self, id_number, full_name, course, year_level, gender):
        # Implement your logic here for saving student data
        print("Saving student data:")
        print("ID Number:", id_number)
        print("Full Name:", full_name)
        print("Course:", course)
        print("Year Level:", year_level)
        print("Gender:", gender)
           
    def displayStudents(self):
        self.lbl_hdr_idnum.setText("ID Number")
        self.lbl_hdr_name.setText("Full Name")
        self.lbl_hhr_course.setText("Course ")
        self.lbl_hdr_yrlvl.setText("Year Level")
        self.lbl_hdr_gender.setText("Gender")
        self.lbl_hdr_status.setText("Status")
        self.mode='Students'
        self.list()
        self.btn_addItem.setText("Add NEW STUDENT")

    def displayCourses(self):
        self.lbl_hdr_idnum.setText("Course Code")
        self.lbl_hdr_name.setText("Course Description")
        self.lbl_hhr_course.setText(" ")
        self.lbl_hdr_yrlvl.setText(" ")
        self.lbl_hdr_gender.setText(" ")
        self.lbl_hdr_status.setText(" ")
        self.mode='Courses'
        self.list()
        self.btn_addItem.setText("ADD NEW COURSE")
        
    def searchItem(self):
        print("searching...")
        query = self.fld_searchBar.text()  # Get the text from the search bar
        if query.strip():  # Check if the query is not empty after stripping whitespace
            if self.mode == 'Students':
                self.listStudentsByScore(query)
            else:
                self.listCoursesByScore(query)
        else:
            self.list()
            
    def listStudentsByScore(self,query):
        self.clearScrollContents()
        with open(self.CRUD_Student.csv_path, 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                highest_match_score = 0
                #first, ensure that we get the highest element.
                for row in reader:
                    id_number = row['id_num']
                    full_name = row['full_name']
                    course = row['course']
                    year_level = row['yr_lvl']
                    gender = row['gender']
                    status = row['status']
                    row_score = self.CRUD_Student._calculate_match_score(query=query, row=row)
                    if highest_match_score < row_score:
                        highest_match_score = row_score
                        h_id_number = row['id_num']
                        h_full_name = row['full_name']
                        h_course = row['course']
                        h_year_level = row['yr_lvl']
                        h_gender = row['gender']
                        h_status = row['status']
                        
                self.addStudent(h_id_number, h_full_name, h_course, h_year_level, h_gender, h_status)
                
                csvfile.seek(0)
                next(reader)
                
                for row in reader:
                    id_number = row['id_num']
                    full_name = row['full_name']
                    course = row['course']
                    year_level = row['yr_lvl']
                    gender = row['gender']
                    status = row['status']
                    # Call addStudent method with retrieved values
                    for i in range(0, 15):
                        if(highest_match_score-i<self.CRUD_Student._calculate_match_score(query=query, row=row) <=highest_match_score-i+1 and highest_match_score-i > 0):
                            if h_id_number != id_number:
                                self.addStudent(id_number, full_name, course, year_level, gender, status)
                                
    
    def saveClicked(self, student_create_ui):
        # Get the contents of all fields and combo boxes
        id_number = student_create_ui.fld_idNum.text()
        full_name = student_create_ui.fld_fullName.text()
        course = student_create_ui.cbb_course.currentText()
        year_level = student_create_ui.cbb_yrLvl.currentText()
        gender = student_create_ui.cbb_gender.currentText()

        # Validate the data
        if self.validateStudentData(id_number, full_name, course, year_level, gender):
            # Call a method with the retrieved contents as parameters
            self.saveStudentData(id_number, full_name, course, year_level, gender)

    # Inside the validateStudentData method
    def validateStudentData(self, id_number, full_name, course, year_level, gender):
        # Check if all fields are filled in
        if not (id_number and full_name and course and year_level and gender):
            return False
        
        # Check if ID number is in the format ####-####
        if not re.match(r'\d{4}-\d{4}', id_number):
            return False
        
        # Check if ID number already exists in the CSV
        if self.CRUD_Student._exists(id_number):
            return False
        
        return True


    def saveStudentData(self, id_number, full_name, course, year_level, gender):
        if course:
            status = 'Not Enrolled'
        else:
            status = 'Enrolled'
        self.CRUD_Student.create(id_num=id_number, full_name=full_name, course=course, yr_lvl=year_level, gender=gender, status=status)
        self.list()
                    
    def listCoursesByScore(self, query):
        self.clearScrollContents()
        with open(self.CRUD_Course.csv_path, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            highest_match_score = 0
            # First, find the highest scoring course
            for row in reader:
                course_code = row['course_code']
                course_desc = row['course_description']
                row_score = self.CRUD_Course._calculate_match_score(query=query, row=row)
                if highest_match_score < row_score:
                    highest_match_score = row_score
                    h_course_code = course_code
                    h_course_desc = course_desc

            # Add the highest scoring course to the scroll contents
            self.addCourse(h_course_code, h_course_desc)

            # Reset the file pointer to the beginning and skip header
            csvfile.seek(0)
            next(reader)

            # Iterate over other courses and add them based on their scores
            for row in reader:
                course_code = row['course_code']
                course_desc = row['course_description']
                # Call addCourse method with retrieved values for scores in a range of 0 to 15
                for i in range(0, 15):
                    if (highest_match_score - i < self.CRUD_Course._calculate_match_score(query=query, row=row) <= highest_match_score - i + 1 and highest_match_score - i > 0):
                        if h_course_code != course_code:
                            self.addCourse(course_code, course_desc)
                        
    def clearScrollContents(self):
        # Clear all widgets from the scroll area
        while self.scroll_contents_layout.count():
            child = self.scroll_contents_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
