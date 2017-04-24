from PyQt4 import uic, QtCore
from PyQt4.QtGui import QMainWindow, QApplication
import sys

class MainWindowView(QMainWindow):

    def __init__(self):
        super(MainWindowView,self).__init__()
        uic.loadUi('./IndirectQuickRun.ui', self)
        self.setWindowTitle("Indirect QuickRun")
        
qApp = QApplication(sys.argv)
aw = MainWindowView()
aw.show()
qApp.exec_()
