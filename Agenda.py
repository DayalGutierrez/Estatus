from PySide2.QtWidgets import QMainWindow, QWidget, QMessageBox
from mainwindow import AgendaWindow
from PySide2.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication()
    window = AgendaWindow()
    window.show()
    app.exec_()
