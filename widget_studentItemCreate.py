import csv
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StudentCreate(object):
    def setupUi(self, Form):
        
        Form.setObjectName("Form")
        Form.resize(727, 46)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fld_idNum = QtWidgets.QLineEdit(Form)
        self.fld_idNum.setObjectName("fld_idNum")
        self.horizontalLayout.addWidget(self.fld_idNum)
        self.fld_fullName = QtWidgets.QLineEdit(Form)
        self.fld_fullName.setObjectName("fld_fullName")
        self.horizontalLayout.addWidget(self.fld_fullName)
        self.cbb_course = QtWidgets.QComboBox(Form)
        self.cbb_course.setObjectName("cbb_course")
        self.horizontalLayout.addWidget(self.cbb_course)
        self.cbb_yrLvl = QtWidgets.QComboBox(Form)
        self.cbb_yrLvl.setObjectName("cbb_yrLvl")
        self.horizontalLayout.addWidget(self.cbb_yrLvl)
        self.cbb_gender = QtWidgets.QComboBox(Form)
        self.cbb_gender.setObjectName("cbb_gender")
        self.horizontalLayout.addWidget(self.cbb_gender)
        self.lbl_status = QtWidgets.QLabel(Form)
        self.lbl_status.setText("")
        self.lbl_status.setObjectName("lbl_status")
        self.horizontalLayout.addWidget(self.lbl_status)
        self.btn_save = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy)
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout.addWidget(self.btn_save)
        self.btn_cancel = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cancel.sizePolicy().hasHeightForWidth())
        self.btn_cancel.setSizePolicy(sizePolicy)
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout.addWidget(self.btn_cancel)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 5)
        self.horizontalLayout.setStretch(2, 2)
        self.horizontalLayout.setStretch(3, 2)
        self.horizontalLayout.setStretch(4, 2)
        self.horizontalLayout.setStretch(5, 2)
        self.horizontalLayout.setStretch(6, 2)
        self.horizontalLayout.setStretch(7, 2)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        # Apply stylesheet
        style_sheet_file = QtCore.QFile("styles_main.qss")
        if style_sheet_file.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text):
            text_stream = QtCore.QTextStream(style_sheet_file)
            stylesheet = text_stream.readAll()
            style_sheet_file.close()

            # Apply stylesheet to the form
            Form.setStyleSheet(stylesheet)

            # Set font size and family for all labels, buttons, and text fields
            self.btn_save.setStyleSheet("font-size: 16px; font-family: \"Atkinson Hyperlegible Regular\";")
            self.btn_cancel.setStyleSheet("font-size: 16px; font-family: \"Atkinson Hyperlegible Regular\";")
            self.fld_idNum.setStyleSheet("font-size: 16px; font-family: \"Atkinson Hyperlegible Regular\";")
            self.fld_fullName.setStyleSheet("font-size: 16px; font-family: \"Atkinson Hyperlegible Regular\";")
            self.cbb_course.setStyleSheet("font-size: 16px; font-family: \"Atkinson Hyperlegible Regular\";")
            self.cbb_yrLvl.setStyleSheet("font-size: 16px; font-family: \"Atkinson Hyperlegible Regular\";")
            self.cbb_gender.setStyleSheet("font-size: 16px; font-family: \"Atkinson Hyperlegible Regular\";")

            # Add padding to buttons
            self.btn_save.setStyleSheet("padding: 10px;")
            self.btn_cancel.setStyleSheet("padding: 10px;")

            # Increase the height of the text fields
            self.fld_idNum.setStyleSheet("height: 40px;")
            self.fld_fullName.setStyleSheet("height: 40px;")
            self.cbb_course.setStyleSheet("height: 40px;")
            self.cbb_yrLvl.setStyleSheet("height: 40px;")
            self.cbb_gender.setStyleSheet("height: 40px;")
        else:
            print("Failed to load stylesheet.")


        self.retranslateUi(Form)
        
        # Populate combo boxes with predefined options
        self.populateComboBoxes()
        
        QtCore.QMetaObject.connectSlotsByName(Form)

    def populateComboBoxes(self):
        # Populate gender combo box
        self.cbb_gender.addItems(["Man", "Woman", "Non-Binary", "Other"])
        self.cbb_gender.setCurrentIndex(-1)

        # Populate year level combo box
        self.cbb_yrLvl.addItems(["1", "2", "3", "4", "5"])
        self.cbb_yrLvl.setCurrentIndex(-1)
        
        # Populate course combo box
        self.populateCourseComboBox()

    def applyStyleSheet(self, Form):
        # Load stylesheet from file
        style_sheet_file = QtCore.QFile("styles_main.qss")
        if style_sheet_file.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text):
            text_stream = QtCore.QTextStream(style_sheet_file)
            stylesheet = text_stream.readAll()
            style_sheet_file.close()

            # Apply stylesheet to the form
            Form.setStyleSheet(stylesheet)

            # Set font size and family for all labels, buttons, and text fields
            self.btn_save.setStyleSheet("font-size: 16px; font-family: \"Atkinson Hyperlegible Regular\";")
            self.btn_cancel.setStyleSheet("font-size: 16px; font-family: \"Atkinson Hyperlegible Regular\";")
            self.fld_idNum.setStyleSheet("font-size: 16px; font-family: \"Atkinson Hyperlegible Regular\";")
            self.fld_fullName.setStyleSheet("font-size: 16px; font-family: \"Atkinson Hyperlegible Regular\";")
            self.cbb_course.setStyleSheet("font-size: 16px; font-family: \"Atkinson Hyperlegible Regular\";")
            self.cbb_yrLvl.setStyleSheet("font-size: 16px; font-family: \"Atkinson Hyperlegible Regular\";")
            self.cbb_gender.setStyleSheet("font-size: 16px; font-family: \"Atkinson Hyperlegible Regular\";")

            # Add padding to buttons
            self.btn_save.setStyleSheet("padding: 10px;")
            self.btn_cancel.setStyleSheet("padding: 10px;")

            # Increase the height of the text fields
            self.fld_idNum.setStyleSheet("height: 40px;")
            self.fld_fullName.setStyleSheet("height: 40px;")
            self.cbb_course.setStyleSheet("height: 40px;")
            self.cbb_yrLvl.setStyleSheet("height: 40px;")
            self.cbb_gender.setStyleSheet("height: 40px;")
        else:
            print("Failed to load stylesheet.")
            
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
        
        self.cbb_course.setCurrentIndex(-1)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.fld_idNum.setText(_translate("Form", " "))
        self.fld_fullName.setText(_translate("Form", " "))
        self.btn_save.setText(_translate("Form", " "))
        self.btn_cancel.setText(_translate("Form", " "))