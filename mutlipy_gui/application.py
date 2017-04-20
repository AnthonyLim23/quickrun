from PyQt4 import QtGui
from view import MainWindow
from model import MultiplyModel, ResetModel
from presenter import Presenter
import sys


class Multiply(QtGui.QMainWindow):

    def __init__(self):
        super(Multiply, self).__init__()
        self.resize(400,300)

        self.view = MainWindow(self)
        self.presenter = Presenter(self.view, MultiplyModel, ResetModel)
        self.view.inputChanged.connect(self.presenter.onInputChanged)
        self.view.resetClicked.connect(self.presenter.resetToZero)


def main():
    app = QtGui.QApplication(sys.argv)
    myapp = Multiply()
    myapp.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
