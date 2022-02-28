import os,pickle
from PySide2.QtCore import Slot
from PySide2.QtWidgets import QMainWindow, QWidget, QMessageBox, QDialog, QTableWidgetItem
from PySide2.QtCore import *
from PySide2.QtWidgets import QWidget
from main_view import Ui_AgendaWindow
class AgendaWindow(QWidget,Ui_AgendaWindow):
    def __init__(self):
        super().__init__()

        self.contactos = list()
        if os.path.exists('contactos.pickle'):
            archivo = open('contactos.pickle', 'rb')
            while True:
                try:
                    contacto = pickle.load(archivo)
                    self.contactos.append(contacto)
                except:
                    break
            archivo.close()

        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        #Hacer el resto de la ventana Transparente
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.print_table()

        self.agregar_pushButton.clicked.connect(self.agregar)
        self.eliminarAgenda_pushButton.clicked.connect(self.eliminar)
    
    @Slot()
    def agregar(self):
        contacto = list()
        #Estructura de cada contacto: Nombre(0), apellido(1), codigo(2), correo(3)
        contacto.append(self.nombre_lineEdit.text())
        contacto.append(self.apellido_lineEdit.text())
        contacto.append(self.codigo_lineEdit.text())
        contacto.append(self.correo_lineEdit.text())
        archivo = open ('contactos.pickle', 'ab')
        pickle.dump(contacto,archivo)
        archivo.close()
        self.contactos.append(contacto)
        self.print_table()
    
    @Slot()
    def eliminar(self):
        self.contactos.clear()
        if os.path.exists('contactos.pickle'):
            os.remove('contactos.pickle')
        print(len(self.contactos))
        self.print_table()

    def print_table(self):
        self.contactos_tableWidget.setColumnCount(4)
        self.contactos_tableWidget.setRowCount(len(self.contactos))
        self.contactos_tableWidget.setHorizontalHeaderLabels(['Nombre','Apellido','codigo','correo'])
        for row in range (len(self.contactos)):
            for column in range (0,4):
                self.contactos_tableWidget.setItem(
                    row,
                    column,
                    QTableWidgetItem(str(self.contactos[row][column]))
                )