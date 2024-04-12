# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI Templates/widget_studentItemEdit.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import csv
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StudentEdit(object):
    def setupUi(self, Form, id_number, full_name, course, year_level, gender, status):
        Form.setObjectName("Form")
        Form.resize(729, 86)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        # QLabel for ID Number
        self.lbl_idNum = QtWidgets.QLabel(Form)
        self.lbl_idNum.setObjectName("lbl_idNum")
        self.lbl_idNum.setText(id_number)  # Set ID number
        self.horizontalLayout.addWidget(self.lbl_idNum)
        
        # QLineEdit for Full Name
        self.fld_fullName = QtWidgets.QLineEdit(Form)
        self.fld_fullName.setObjectName("fld_fullName")
        self.fld_fullName.setText(full_name)  # Set full name
        self.horizontalLayout.addWidget(self.fld_fullName)
        
        # QComboBox for Course
        self.cbb_course = QtWidgets.QComboBox(Form)
        self.cbb_course.setObjectName("cbb_course")
        self.horizontalLayout.addWidget(self.cbb_course)
        
        # QComboBox for Year Level
        self.cbb_yrLvl = QtWidgets.QComboBox(Form)
        self.cbb_yrLvl.setObjectName("cbb_yrLvl")
        self.horizontalLayout.addWidget(self.cbb_yrLvl)
        
        # QComboBox for Gender
        self.cbb_gender = QtWidgets.QComboBox(Form)
        self.cbb_gender.setObjectName("cbb_gender")
        self.horizontalLayout.addWidget(self.cbb_gender)
        
        # QLabel for Status
        self.lbl_status = QtWidgets.QLabel(Form)
        self.lbl_status.setObjectName("lbl_status")
        self.lbl_status.setText(status)  # Set status
        self.horizontalLayout.addWidget(self.lbl_status)
        
        # QPushButton for Save
        self.btn_save = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy)
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout.addWidget(self.btn_save)
        
        # QPushButton for Cancel
        self.btn_cancel = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cancel.sizePolicy().hasHeightForWidth())
        self.btn_cancel.setSizePolicy(sizePolicy)
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout.addWidget(self.btn_cancel)
        
        # Set stretch for widgets
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 5)
        self.horizontalLayout.setStretch(2, 2)
        self.horizontalLayout.setStretch(3, 2)
        self.horizontalLayout.setStretch(4, 2)
        self.horizontalLayout.setStretch(5, 2)
        self.horizontalLayout.setStretch(6, 2)
        self.horizontalLayout.setStretch(7, 2)
        
        # Add horizontal layout to grid layout
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        # Populate combo boxes with predefined options
        self.populateComboBoxes()
        
        # Set values for course, year level, and gender
        self.cbb_course.setCurrentText(course)
        self.cbb_yrLvl.setCurrentText(year_level)
        self.cbb_gender.setCurrentText(gender)
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def populateComboBoxes(self):
        # Populate gender combo box
        self.cbb_gender.addItems(["Man", "Woman", "Non-Binary", "Other"])

        # Populate year level combo box
        self.cbb_yrLvl.addItems(["1", "2", "3", "4", "5"])
        
        # Populate course combo box
        self.populateCourseComboBox()

    def populateCourseComboBox(self):
        # Clear existing items in the combo box
        self.cbb_course.clear()

        # Read the Courses.csv file and populate the combo box
        self.cbb_course.addItem("NONE")
        with open("Courses.csv", 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                course_code = row['course_code']
                # Add the course in the format "Course Code - Course Description"
                self.cbb_course.addItem(f"{course_code}")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_save.setText(_translate("Form", "Save"))
        self.btn_cancel.setText(_translate("Form", "Cancel"))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_save.setText(_translate("Form", "Save"))
        self.btn_cancel.setText(_translate("Form", "Cancel"))