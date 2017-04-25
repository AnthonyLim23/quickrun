from PyQt4 import uic, QtCore
from PyQt4.QtGui import QMainWindow, QApplication, QWidget
import sys


class ScanTab(QWidget):
    def __init__(self):
        super(ScanTab, self).__init__()
        self.energytab = uic.loadUi('./EnergyWindowScan.ui')
        self.sqwtab = uic.loadUi('./SQWMomentScan.ui')
        self.diffractiontab = uic.loadUi('./DiffractionScan.ui')


class MainWindowView(QMainWindow):
    def __init__(self):
        super(MainWindowView, self).__init__()
        self.ui = uic.loadUi('./IndirectQuickRun.ui', self)
        self.setWindowTitle("Indirect QuickRun")
        self.tabs = ScanTab()
        self.ui.tb_quickrun.insertTab(0,self.tabs.energytab, "Energy Window Scan")
        self.ui.tb_quickrun.insertTab(1,self.tabs.sqwtab, "SQW Moments Scan")
        self.ui.tb_quickrun.insertTab(2,self.tabs.diffractiontab, "Diffraction Scan")

qApp = QApplication(sys.argv)
aw = MainWindowView()
aw.show()
qApp.exec_()
