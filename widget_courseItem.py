from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CourseItem(object):
    def setupUi(self, Form, course_code="", course_description=""):
        Form.setObjectName("Form")
        Form.resize(710, 72)
        Form.setStyleSheet('''
            QWidget#Form:hover {
                background-color: #dddddd;
            }
        ''')
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.lbl_courseCode = QtWidgets.QLabel(Form)  # Changed label name to lbl_courseCode
        self.lbl_courseCode.setObjectName("lbl_courseCode")  # Changed object name
        self.horizontalLayout.addWidget(self.lbl_courseCode)
        
        self.lbl_courseDescription = QtWidgets.QLabel(Form)  # Changed label name to lbl_courseDescription
        self.lbl_courseDescription.setObjectName("lbl_courseDescription")  # Changed object name
        self.horizontalLayout.addWidget(self.lbl_courseDescription)
        
        self.btn_edit = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_edit.sizePolicy().hasHeightForWidth())
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
        self.horizontalLayout.setStretch(1, 13)
        self.horizontalLayout.setStretch(2, 2)
        self.horizontalLayout.setStretch(3, 2)
        
        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # Set the initial values of labels
        self.lbl_courseCode.setText(course_code)
        self.lbl_courseDescription.setText(course_description)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_edit.setText(_translate("Form", "Edit"))
        self.btn_delete.setText(_translate("Form", "Delete"))
