# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'quick_api_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QuickApiDialogBase(object):
    def setupUi(self, QuickApiDialogBase):
        QuickApiDialogBase.setObjectName("QuickApiDialogBase")
        QuickApiDialogBase.resize(290, 132)
        self.gridLayout = QtWidgets.QGridLayout(QuickApiDialogBase)
        self.gridLayout.setObjectName("gridLayout")
        self.lineedit_xy = gui.QgsFilterLineEdit(QuickApiDialogBase)
        self.lineedit_xy.setProperty("qgisRelation", "")
        self.lineedit_xy.setObjectName("lineedit_xy")
        self.gridLayout.addWidget(self.lineedit_xy, 0, 0, 1, 1)
        self.map_button = QtWidgets.QToolButton(QuickApiDialogBase)
        self.map_button.setObjectName("map_button")
        self.gridLayout.addWidget(self.map_button, 0, 1, 1, 1)
        self.crs_input = gui.QgsProjectionSelectionWidget(QuickApiDialogBase)
        self.crs_input.setObjectName("crs_input")
        self.gridLayout.addWidget(self.crs_input, 1, 0, 1, 2)
        self.button_box = QtWidgets.QDialogButtonBox(QuickApiDialogBase)
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.gridLayout.addWidget(self.button_box, 2, 0, 1, 2)

        self.retranslateUi(QuickApiDialogBase)
        self.button_box.accepted.connect(QuickApiDialogBase.accept)
        self.button_box.rejected.connect(QuickApiDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(QuickApiDialogBase)

    def retranslateUi(self, QuickApiDialogBase):
        _translate = QtCore.QCoreApplication.translate
        QuickApiDialogBase.setWindowTitle(_translate("QuickApiDialogBase", "Quick API"))
        self.map_button.setText(_translate("QuickApiDialogBase", "..."))
from qgis import gui
