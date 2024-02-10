# Информация о проекте
# Необходимо написать проект, содержащий функционал работы с заметками.
# Программа должна уметь создавать заметку, сохранять её, читать список заметок,
# редактировать заметку, удалять заметку.

from PyQt5.QtWidgets import QApplication, QMainWIndow, QMassageBox
from PyQt5.QtCore import Qt, QTimer
import sys
import datetime
def aplic():
    app = QApplication(sys.argv)
    okno = Window()
    okno.show()
    sys.exit(app.exec_())

if _name_ == '_main_':
    aplic()

class Window(QMainWIndow):
    def _init_(self):
        super(Window, self)._init_()

        self.setWindowTitle("programs")
        self.setGeometry(400,400,600,300)