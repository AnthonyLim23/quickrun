from PyQt4 import uic, QtCore
from PyQt4.QtGui import QMainWindow, QApplication, QWidget
import sys


class ScanTab(QWidget):
    def __init__(self):
        super(ScanTab, self).__init__()
        self.energytab = uic.loadUi('./EnergyWindowScan.ui', self)
        self.sqwtab = uic.loadUi('./SQWMomentScan.ui', self)

class MainWindowView(QMainWindow):
    def __init__(self):
        super(MainWindowView, self).__init__()
        self.ui = uic.loadUi('./IndirectQuickRun.ui', self)
        self.setWindowTitle("Indirect QuickRun")
        self.tabs = ScanTab()
        self.ui.tb_quickrun.addTab(self.tabs.energytab, "Energy Window Scan")
        self.ui.tb_quickrun.addTab(self.tabs.sqwtab, "SQW Moments Scan")


qApp = QApplication(sys.argv)
aw = MainWindowView()
aw.show()
qApp.exec_()
