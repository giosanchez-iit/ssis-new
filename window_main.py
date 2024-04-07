import csv
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QFile, QTextStream
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QWidget, QGridLayout, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QScrollArea, QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt, QRect, QCoreApplication, QMetaObject
from widget_studentItem import Ui_StudentItem
from crud_utils import CRUD_Data

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.CRUD_Student = CRUD_Data(csv_name='Students', key='id_num', attributes=('id_num', 'full_name', 'course', 'yr_lvl', 'gender', 'status'))
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(626, 454)
        MainWindow.setMinimumSize(800, 400)
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
        self.btn_addStudent = QPushButton(self.centralwidget)
        self.btn_addStudent.setObjectName(u"btn_addStudent")

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)
        self.horizontalLayout_7.addWidget(self.btn_addStudent)

        self.verticalLayout_2.addLayout(self.horizontalLayout_7)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        # Add Styling
        self.loadStylesheet()
        
        # List Students
        self.scroll_contents_layout = QVBoxLayout(self.scrollAreaWidgetContents_7)
        self.scroll_contents_layout.setAlignment(Qt.AlignTop)
        
        self.listStudents()
        
        # Buttons
        self.btn_addStudent.clicked.connect(self.addStudentWindow)

    def addStudentWindow(self):
        print("ADD ME")
        
    def loadStylesheet(self):
        style_sheet_file = QFile("styles_main.qss")  # Path to your QSS file
        if style_sheet_file.open(QFile.ReadOnly | QFile.Text):
            text_stream = QTextStream(style_sheet_file)
            stylesheet = text_stream.readAll()
            QApplication.instance().setStyleSheet(stylesheet)
        else:
            print("Failed to load stylesheet.")
            
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_displayStudents.setText(QCoreApplication.translate("MainWindow", u"DISPLAY STUDENTS", None))
        self.btn_displayCourses.setText(QCoreApplication.translate("MainWindow", u"DISPLAY COURSES", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Search: ", None))
        self.lbl_hdr_idnum.setText(QCoreApplication.translate("MainWindow", u"ID Number", None))
        self.lbl_hdr_name.setText(QCoreApplication.translate("MainWindow", u"Full Name", None))
        self.lbl_hhr_course.setText(QCoreApplication.translate("MainWindow", u"Course", None))
        self.lbl_hdr_yrlvl.setText(QCoreApplication.translate("MainWindow", u"Year Level", None))
        self.lbl_hdr_gender.setText(QCoreApplication.translate("MainWindow", u"Gender", None))
        self.lbl_hdr_status.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.btn_addStudent.setText(QCoreApplication.translate("MainWindow", u"ADD NEW STUDENT", None))
    
    def listStudents(self):
        #Clear CSV First
        while self.scroll_contents_layout.count():
            child = self.scroll_contents_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
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

    def addStudent(self, id_number, full_name, course, year_level, gender, status):
        # Create a new instance of the student item with the provided details
        student_item = Ui_StudentItem()
        student_item_widget = QtWidgets.QWidget()
        student_item.setupUi(student_item_widget, id_number, full_name, course, year_level, gender, status)
        # Connect edit and delete signals to lambda functions passing id_number
        student_item.btn_edit.clicked.connect(lambda: self.editClicked(id_number))
        student_item.btn_delete.clicked.connect(lambda: self.deleteClicked(id_number))
        # Add the student item widget to the existing layout
        self.scroll_contents_layout.addWidget(student_item_widget)
        
    def editClicked(self, id_number):
        print("Edit button clicked for student with ID:", id_number)

    def deleteClicked(self, id_number):
        self.CRUD_Student.delete(id_number)
        self.listStudents()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
