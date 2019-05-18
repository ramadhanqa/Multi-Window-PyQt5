import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi

class MainPage(QDialog):
    def __init__(self):
        super(MainPage,self).__init__()
        loadUi('test.ui',self)
        self.pushButton.clicked.connect(self.move)


    def move(self):
        from OtherPage import SecondPage
        theclass = SecondPage()
        theclass.exec_()

app = QApplication(sys.argv)
widget = MainPage()
widget.show()
sys.exit(app.exec_())