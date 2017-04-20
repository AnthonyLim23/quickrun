from PyQt4 import QtGui


class MultiplyModel(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mul(self):
        return self.x * self.y


class ResetModel(object):
    def __init__(self, widget):

        self.widget = widget

    def setToZero(self):

        if type(self.widget) == QtGui.QLCDNumber:
            self.widget.display(0)
        if type(self.widget) == QtGui.QDoubleSpinBox:
            self.widget.setValue(0.0)
