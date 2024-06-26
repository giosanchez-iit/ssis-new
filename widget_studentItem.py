from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StudentItem(object):
    def setupUi(self, Form, id_num="", full_name="", course="", year="", gender="", status=""):
        Form.setObjectName("Form")
        Form.resize(708, 72)
        Form.setStyleSheet('''
            QWidget#Form:hover {
                background-color: #dddddd;
            }
        ''')
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_idNum = QtWidgets.QLabel(Form)
        self.lbl_idNum.setObjectName("lbl_idNum")
        self.horizontalLayout.addWidget(self.lbl_idNum)
        self.lbl_fullName = QtWidgets.QLabel(Form)
        self.lbl_fullName.setObjectName("lbl_fullName")
        self.horizontalLayout.addWidget(self.lbl_fullName)
        self.lbl_course = QtWidgets.QLabel(Form)
        self.lbl_course.setObjectName("lbl_course")
        self.horizontalLayout.addWidget(self.lbl_course)
        self.lbl_year = QtWidgets.QLabel(Form)
        self.lbl_year.setObjectName("lbl_year")
        self.horizontalLayout.addWidget(self.lbl_year)
        self.lbl_gender = QtWidgets.QLabel(Form)
        self.lbl_gender.setObjectName("lbl_gender")
        self.horizontalLayout.addWidget(self.lbl_gender)
        self.btn_edit = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_edit.sizePolicy().hasHeightForWidth())
        self.lbl_status = QtWidgets.QLabel(Form)
        self.lbl_status.setObjectName(u"lbl_status")
        self.lbl_status.setAlignment(QtCore.Qt.AlignCenter)  
        self.horizontalLayout.addWidget(self.lbl_status)
        self.btn_edit.setSizePolicy(sizePolicy)
        self.btn_edit.setObjectName("btn_edit")
        self.horizontalLayout.addWidget(self.btn_edit)
        self.btn_delete = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_delete.sizePolicy().hasHeightForWidth())
        self.btn_delete.setSizePolicy(sizePolicy)
        self.btn_delete.setObjectName("btn_delete")
        self.horizontalLayout.addWidget(self.btn_delete)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 5)
        self.horizontalLayout.setStretch(2, 2)
        self.horizontalLayout.setStretch(3, 2)
        self.horizontalLayout.setStretch(4, 2)
        self.horizontalLayout.setStretch(5, 2)
        self.horizontalLayout.setStretch(6, 2)
        self.horizontalLayout.setStretch(7, 2)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # Set the initial values of labels
        self.lbl_idNum.setText(id_num)
        self.lbl_fullName.setText(full_name)
        self.lbl_course.setText(course)
        self.lbl_year.setText(year)
        self.lbl_gender.setText(gender)
        self.lbl_status.setText(status)
        
        # text is gray if NONE
        if course == "NONE":
            self.lbl_course.setStyleSheet("color: rgb(150,150,150);")
        
        # set border color depending on status
        border_color = "rgb(200, 81, 62)"  # default to red
        if status == "Enrolled":
            border_color = "rgb(100, 200, 150)"  # green if enrolled

        # set border style
        self.lbl_status.setStyleSheet("color: black; border: 2px solid {}; border-radius: 10px; margin: 15px; text-align: center;".format(border_color))
        
        # Center the status label in its cell
        self.gridLayout.setAlignment(QtCore.Qt.AlignCenter)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_edit.setText(_translate("Form", "Edit"))
        self.btn_delete.setText(_translate("Form", "Delete"))