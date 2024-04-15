from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CourseCreate(object):
    def setupUi(self, Form, course_code="", course_description=""):
        Form.setObjectName("Form")
        Form.resize(710, 72)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.line_courseCode = QtWidgets.QLineEdit(Form)  # Changed label to line edit
        self.line_courseCode.setObjectName("line_courseCode")  # Changed object name
        self.horizontalLayout.addWidget(self.line_courseCode)
        
        self.line_courseDescription = QtWidgets.QLineEdit(Form)  # Changed label to line edit
        self.line_courseDescription.setObjectName("line_courseDescription")  # Changed object name
        self.horizontalLayout.addWidget(self.line_courseDescription)
        
        self.btn_save = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(2)
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
        self.horizontalLayout.setStretch(1, 13)
        self.horizontalLayout.setStretch(2, 2)
        self.horizontalLayout.setStretch(3, 2)
        
        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # Set the initial values of line edits
        self.line_courseCode.setText(course_code)
        self.line_courseDescription.setText(course_description)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_save.setText(_translate("Form", "Save"))
        self.btn_cancel.setText(_translate("Form", "Cancel"))
