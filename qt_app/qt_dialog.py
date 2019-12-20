import sys
from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication, QWidget, QPushButton, QLineEdit, QMenuBar, QStatusBar
import PyQt5.QtCore as QtCore

class Ui_Dialog(object):

    def save_data(self):
        d= self.lineEdit.text()
        print(d)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(397, 219)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(110, 100, 112, 34))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(110, 60, 113, 27))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        #Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        Dialog.setWindowTitle('child window')
        #self.pushButton.setText(_translate("Dialog", "B2", None))
        self.pushButton.setText('Done')
        self.pushButton.clicked.connect(self.save_data)

class Ui_MainWindow(object):

    def connect(self):
        self.updateWindow=QDialog()
        self.ui_update=Ui_Dialog()
        self.ui_update.setupUi(self.updateWindow)
        self.updateWindow.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(391, 248)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 60, 113, 27))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 100, 112, 34))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 391, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle('main window')
        self.pushButton.setText('push me')
        self.pushButton.clicked.connect(self.connect)

class Dialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.close)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.onClicked)

    def onClicked(self):
        updateDialog = Dialog()
        updateDialog.exec_()
        self.lineEdit.setText(updateDialog.lineEdit.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
