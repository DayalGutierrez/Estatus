# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_AgendaWindow(object):
    def setupUi(self, AgendaWindow):
        if not AgendaWindow.objectName():
            AgendaWindow.setObjectName(u"AgendaWindow")
        AgendaWindow.resize(630, 528)
        self.horizontalLayout = QHBoxLayout(AgendaWindow)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(AgendaWindow)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.528, y1:1, x2:0.536, y2:0, stop:0.382418 rgba(228, 59, 59, 255), stop:1 rgba(3, 23, 28, 255));\n"
"\n"
"border-radius:20px;\n"
"border:1px solid #000000;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.Titulo_label = QLabel(self.frame)
        self.Titulo_label.setObjectName(u"Titulo_label")
        self.Titulo_label.setGeometry(QRect(2, 12, 621, 61))
        font = QFont()
        font.setPointSize(26)
        self.Titulo_label.setFont(font)
        self.Titulo_label.setLayoutDirection(Qt.LeftToRight)
        self.Titulo_label.setStyleSheet(u"background-color: rgba(0, 0, 0, 0%);\n"
"border:none;\n"
"color: rgb(255, 255, 255);\n"
"")
        self.Titulo_label.setAlignment(Qt.AlignCenter)
        self.nombre_lineEdit = QLineEdit(self.frame)
        self.nombre_lineEdit.setObjectName(u"nombre_lineEdit")
        self.nombre_lineEdit.setGeometry(QRect(20, 160, 151, 31))
        self.nombre_lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.agregar_pushButton = QPushButton(self.frame)
        self.agregar_pushButton.setObjectName(u"agregar_pushButton")
        self.agregar_pushButton.setGeometry(QRect(10, 460, 91, 31))
        font1 = QFont()
        font1.setPointSize(10)
        self.agregar_pushButton.setFont(font1)
        self.agregar_pushButton.setStyleSheet(u"background-color: rgb(51, 159, 51);\n"
"")
        self.nombre_label = QLabel(self.frame)
        self.nombre_label.setObjectName(u"nombre_label")
        self.nombre_label.setGeometry(QRect(40, 120, 88, 30))
        font2 = QFont()
        font2.setPointSize(15)
        self.nombre_label.setFont(font2)
        self.nombre_label.setLayoutDirection(Qt.LeftToRight)
        self.nombre_label.setStyleSheet(u"background-color: rgba(0, 0, 0, 0%);\n"
"border:none;\n"
"color: rgb(255, 255, 255);\n"
"")
        self.nombre_label.setAlignment(Qt.AlignCenter)
        self.apellido_label = QLabel(self.frame)
        self.apellido_label.setObjectName(u"apellido_label")
        self.apellido_label.setGeometry(QRect(40, 200, 88, 30))
        self.apellido_label.setFont(font2)
        self.apellido_label.setLayoutDirection(Qt.LeftToRight)
        self.apellido_label.setStyleSheet(u"background-color: rgba(0, 0, 0, 0%);\n"
"border:none;\n"
"color: rgb(255, 255, 255);\n"
"")
        self.apellido_label.setAlignment(Qt.AlignCenter)
        self.codigo_label = QLabel(self.frame)
        self.codigo_label.setObjectName(u"codigo_label")
        self.codigo_label.setGeometry(QRect(40, 280, 77, 30))
        self.codigo_label.setFont(font2)
        self.codigo_label.setLayoutDirection(Qt.LeftToRight)
        self.codigo_label.setStyleSheet(u"background-color: rgba(0, 0, 0, 0%);\n"
"border:none;\n"
"color: rgb(255, 255, 255);\n"
"")
        self.codigo_label.setAlignment(Qt.AlignCenter)
        self.Correo_label = QLabel(self.frame)
        self.Correo_label.setObjectName(u"Correo_label")
        self.Correo_label.setGeometry(QRect(40, 360, 74, 30))
        self.Correo_label.setFont(font2)
        self.Correo_label.setLayoutDirection(Qt.LeftToRight)
        self.Correo_label.setStyleSheet(u"background-color: rgba(0, 0, 0, 0%);\n"
"border:none;\n"
"color: rgb(255, 255, 255);\n"
"")
        self.Correo_label.setAlignment(Qt.AlignCenter)
        self.contactos_tableWidget = QTableWidget(self.frame)
        self.contactos_tableWidget.setObjectName(u"contactos_tableWidget")
        self.contactos_tableWidget.setGeometry(QRect(210, 140, 401, 351))
        self.contactos_tableWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.subt_tabla__label = QLabel(self.frame)
        self.subt_tabla__label.setObjectName(u"subt_tabla__label")
        self.subt_tabla__label.setGeometry(QRect(214, 90, 391, 30))
        self.subt_tabla__label.setFont(font2)
        self.subt_tabla__label.setLayoutDirection(Qt.LeftToRight)
        self.subt_tabla__label.setStyleSheet(u"background-color: rgba(0, 0, 0, 0%);\n"
"border:none;\n"
"color: rgb(255, 255, 255);\n"
"")
        self.subt_tabla__label.setAlignment(Qt.AlignCenter)
        self.apellido_lineEdit = QLineEdit(self.frame)
        self.apellido_lineEdit.setObjectName(u"apellido_lineEdit")
        self.apellido_lineEdit.setGeometry(QRect(20, 240, 151, 31))
        self.apellido_lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.codigo_lineEdit = QLineEdit(self.frame)
        self.codigo_lineEdit.setObjectName(u"codigo_lineEdit")
        self.codigo_lineEdit.setGeometry(QRect(20, 320, 151, 31))
        self.codigo_lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.correo_lineEdit = QLineEdit(self.frame)
        self.correo_lineEdit.setObjectName(u"correo_lineEdit")
        self.correo_lineEdit.setGeometry(QRect(20, 400, 151, 31))
        self.correo_lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.eliminarAgenda_pushButton = QPushButton(self.frame)
        self.eliminarAgenda_pushButton.setObjectName(u"eliminarAgenda_pushButton")
        self.eliminarAgenda_pushButton.setGeometry(QRect(110, 460, 91, 31))
        font3 = QFont()
        font3.setPointSize(7)
        self.eliminarAgenda_pushButton.setFont(font3)
        self.eliminarAgenda_pushButton.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"")

        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(AgendaWindow)

        QMetaObject.connectSlotsByName(AgendaWindow)
    # setupUi

    def retranslateUi(self, AgendaWindow):
        AgendaWindow.setWindowTitle(QCoreApplication.translate("AgendaWindow", u"Form", None))
        self.Titulo_label.setText(QCoreApplication.translate("AgendaWindow", u"Agenda escolar", None))
        self.agregar_pushButton.setText(QCoreApplication.translate("AgendaWindow", u"Agregar", None))
        self.nombre_label.setText(QCoreApplication.translate("AgendaWindow", u"Nombre", None))
        self.apellido_label.setText(QCoreApplication.translate("AgendaWindow", u"Apellido", None))
        self.codigo_label.setText(QCoreApplication.translate("AgendaWindow", u"Codigo", None))
        self.Correo_label.setText(QCoreApplication.translate("AgendaWindow", u"Correo", None))
        self.subt_tabla__label.setText(QCoreApplication.translate("AgendaWindow", u"Contactos existentes", None))
        self.eliminarAgenda_pushButton.setText(QCoreApplication.translate("AgendaWindow", u"Eliminar agenda", None))
    # retranslateUi

