import mock

import sys
import unittest
from PyQt4.QtTest import QTest
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import Qt
import application

app = QApplication(sys.argv)

class Test(unittest.TestCase):


    def setUp(self):
        self.form = application.Multiply()
        self.ui = self.form.view

    def test_zero(self):

        self.assertEqual(self.ui.input_one.value(),0.0)
        self.assertEqual(self.ui.input_two.value(),0.0)
        self.assertEqual(self.ui.result_lcd.value(),0.0)

    def test_multiply(self):

        self.ui.input_one.setValue(2.0)
        self.ui.input_two.setValue(3.5)
        self.assertEqual(self.ui.result_lcd.value(),7.0)

    def test_reset(self):

        self.test_multiply()
        self.assertEqual(self.ui.result_lcd.value(),7.0)
        print(self.ui.result_lcd.value())
        QTest.mouseClick(self.ui.reset_button,Qt.LeftButton)
        print(self.ui.result_lcd.value())
        self.test_zero()

    def test_pres(self):
        self.pres = self.form.presenter
        self.pres.onInputChanged()
        self.pres.resetToZero()

if __name__ == "__main__":
    unittest.main()
