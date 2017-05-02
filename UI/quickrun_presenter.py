
class QuickRunPresenter(object):

    def __init__(self, view):
        self._view = view

    def onPlotClicked(self):
        view = self._view

        plot_option = view.getPlotOption()
        print(plot_option)

        return None

