# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI Templates/widget_studentItemEdit.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_zz(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(729, 86)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_idNum = QtWidgets.QLabel(Form)
        self.lbl_idNum.setObjectName("lbl_idNum")
        self.horizontalLayout.addWidget(self.lbl_idNum)
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
        self.horizontalLayout.setStretch(0, 2)
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

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lbl_idNum.setText(_translate("Form", "2022-0025"))
        self.fld_fullName.setText(_translate("Form", "Gio Kiefer A. Sanchez"))
        self.lbl_status.setText(_translate("Form", "Enrolled"))
        self.btn_save.setText(_translate("Form", "Save"))
        self.btn_cancel.setText(_translate("Form", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
