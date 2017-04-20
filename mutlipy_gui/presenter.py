class Presenter(object):
    def __init__(self, view, MultiplyModel, ResetModel):
        self.view = view
        self.mul_model = MultiplyModel
        self.res_model = ResetModel

    def onInputChanged(self):
        inOne = self.view.input_one.value()
        inTwo = self.view.input_two.value()
        result = self.mul_model(inOne, inTwo).mul()
        self.view.setResult(result)


    def resetToZero(self):
        inOne = self.view.input_one
        inTwo = self.view.input_two
        result_lcd = self.view.result_lcd
        self.res_model(inOne).setToZero()
        self.res_model(inTwo).setToZero()
        self.res_model(result_lcd).setToZero()
