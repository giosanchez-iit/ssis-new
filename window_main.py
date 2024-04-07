# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QFile, QTextStream
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame
from widget_studentItem import Ui_StudentItem


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(800, 400)
        MainWindow.resize(855, 454)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btn_displayStudents = QtWidgets.QPushButton(self.centralwidget)
        self.btn_displayStudents.setObjectName("btn_displayStudents")
        self.horizontalLayout_5.addWidget(self.btn_displayStudents)
        self.btn_displayCourses = QtWidgets.QPushButton(self.centralwidget)
        self.btn_displayCourses.setObjectName("btn_displayCourses")
        self.horizontalLayout_5.addWidget(self.btn_displayCourses)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.fld_searchBar = QtWidgets.QLineEdit(self.centralwidget)
        self.fld_searchBar.setObjectName("fld_searchBar")
        self.horizontalLayout_5.addWidget(self.fld_searchBar)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.divider = QFrame(self.centralwidget)
        self.divider.setObjectName(u"divider")
        self.divider.setFrameShape(QFrame.HLine)
        self.divider.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_2.addWidget(self.divider)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(20, -1, 50, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbl_hdr_idnum = QtWidgets.QLabel(self.centralwidget)
        self.lbl_hdr_idnum.setObjectName("lbl_hdr_idnum")
        self.horizontalLayout_2.addWidget(self.lbl_hdr_idnum)
        self.lbl_hdr_name = QtWidgets.QLabel(self.centralwidget)
        self.lbl_hdr_name.setObjectName("lbl_hdr_name")
        self.horizontalLayout_2.addWidget(self.lbl_hdr_name)
        self.lbl_hhr_course = QtWidgets.QLabel(self.centralwidget)
        self.lbl_hhr_course.setObjectName("lbl_hhr_course")
        self.horizontalLayout_2.addWidget(self.lbl_hhr_course)
        self.lbl_hdr_yrlvl = QtWidgets.QLabel(self.centralwidget)
        self.lbl_hdr_yrlvl.setObjectName("lbl_hdr_yrlvl")
        self.horizontalLayout_2.addWidget(self.lbl_hdr_yrlvl)
        self.lbl_hdr_gender = QtWidgets.QLabel(self.centralwidget)
        self.lbl_hdr_gender.setObjectName("lbl_hdr_gender")
        self.horizontalLayout_2.addWidget(self.lbl_hdr_gender)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(1, 5)
        self.horizontalLayout_2.setStretch(2, 2)
        self.horizontalLayout_2.setStretch(3, 2)
        self.horizontalLayout_2.setStretch(4, 2)
        self.horizontalLayout_2.setStretch(5, 4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_7 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_7.setGeometry(QtCore.QRect(0, 0, 833, 322))
        self.scrollAreaWidgetContents_7.setObjectName("scrollAreaWidgetContents_7")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_7)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.btn_addStudent = QtWidgets.QPushButton(self.centralwidget)
        self.btn_addStudent.setObjectName("btn_addStudent")
        self.horizontalLayout_7.addWidget(self.btn_addStudent)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        # Add Styling
        self.loadStylesheet()
        
        # List Students
        self.scroll_contents_layout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_7)
        self.scroll_contents_layout.setAlignment(QtCore.Qt.AlignTop)
        
        
        for i in range(20):
            self.addStudent()
        
    
    def loadStylesheet(self):
        style_sheet_file = QFile("styles_main.qss")  # Path to your QSS file
        if style_sheet_file.open(QFile.ReadOnly | QFile.Text):
            text_stream = QTextStream(style_sheet_file)
            stylesheet = text_stream.readAll()
            QApplication.instance().setStyleSheet(stylesheet)
        else:
            print("Failed to load stylesheet.")
            
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_displayStudents.setText(_translate("MainWindow", "DISPLAY STUDENTS"))
        self.btn_displayCourses.setText(_translate("MainWindow", "DISPLAY COURSES"))
        self.label.setText(_translate("MainWindow", "Search: "))
        self.lbl_hdr_idnum.setText(_translate("MainWindow", "ID Number"))
        self.lbl_hdr_name.setText(_translate("MainWindow", "Full Name"))
        self.lbl_hhr_course.setText(_translate("MainWindow", "Course"))
        self.lbl_hdr_yrlvl.setText(_translate("MainWindow", "Year Level"))
        self.lbl_hdr_gender.setText(_translate("MainWindow", "Gender"))
        self.btn_addStudent.setText(_translate("MainWindow", "ADD NEW STUDENT"))
    
    def addStudent(self):
        # Create a new instance of the student item
        student_item = Ui_StudentItem()
        student_item_widget = QtWidgets.QWidget()
        student_item.setupUi(student_item_widget)

        # Add the student item widget to the existing layout
        self.scroll_contents_layout.addWidget(student_item_widget)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
