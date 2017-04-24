from view import MainWindow
from model import MultiplyModel, ResetModel
from presenter import Presenter
import unittest

class PresenterTest(unittest.TestCase):

    def setUp(self):
        self.view=MainWindow()
        self.pres = Presenter(self.view,MultiplyModel,ResetModel)

    def test_mul(self):
        self.pres.onInputChanged()

    def test_reset(self):
        self.pres.resetToZero()

if __name__ == "__main__":
    unittest.main()
