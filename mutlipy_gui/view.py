from PyQt4.QtGui import QLabel, QLCDNumber, QFrame, QDoubleSpinBox, QPushButton, QVBoxLayout,QWidget
from PyQt4.QtCore import QRect, pyqtSignal


class MainWindow(QWidget):
    # set up signals
    resetClicked = pyqtSignal()
    inputChanged = pyqtSignal()
    input_one = None

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # --------------------------------------------------------

        # main window
        self.setObjectName("Multiply")
        self.resize(400, 300)

        # label
        self.label = QLabel(self)
        self.label.setGeometry(QRect(20, 10, 250, 50))
        self.label.setText("Multiply two numbers!")
        # self.label.show()

        # input frame
        self.input_frame = QFrame(self)
        self.input_frame.setGeometry(QRect(20, 60, 350, 130))
        self.input_frame.setFrameShape(QFrame.StyledPanel)
        self.input_frame.setFrameShadow(QFrame.Raised)

        # set the layout of the frame
        self.verticalLayout = QVBoxLayout(self.input_frame)
        self.verticalLayout.setObjectName("verticalLayout")

        # first input
        self.input_one = QDoubleSpinBox(self.input_frame)
        self.input_one.setObjectName("input_one")
        self.input_one.setDecimals(4)
        self.input_one.setSingleStep(0.01)

        self.verticalLayout.addWidget(self.input_one)

        # second input
        self.input_two = QDoubleSpinBox(self.input_frame)
        self.input_two.setObjectName("input_two")
        self.input_two.setDecimals(4)
        self.input_two.setSingleStep(0.01)

        self.verticalLayout.addWidget(self.input_two)

        # LCD result
        self.result_lcd = QLCDNumber(self)
        self.result_lcd.setObjectName("result_lcd")
        self.result_lcd.setGeometry(QRect(20, 200, 350, 80))
        self.result_lcd.setDigitCount(10)
        self.result_lcd.setSmallDecimalPoint(True)

        # Reset Button
        self.reset_button = QPushButton(self)
        self.reset_button.setGeometry(QRect(270, 10, 100, 30))
        self.reset_button.setObjectName("reset_button")
        self.reset_button.setText("Reset")

        # --------------------------------------------------------

        # connect slots

        self.reset_button.clicked.connect(self.onResetClick)
        self.input_one.valueChanged.connect(self.onInputChanged)
        self.input_two.valueChanged.connect(self.onInputChanged)

        # define slots

    def onResetClick(self):
        self.resetClicked.emit()

    def onInputChanged(self):
        self.inputChanged.emit()

    def setResult(self, value):
        self.result_lcd.display(value)
