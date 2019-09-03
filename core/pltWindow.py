import matplotlib
matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

class PlotWindowUiOperation():
    def __init__(self):
        super(PlotWindowUiOperation,self).__init__()

    def PlotWindowInitialize(self):
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas,self)
        self.PlotWindow.addWidget(self.toolbar)
        self.PlotWindow.addWidget(self.canvas)

    def PlotWindowUiActionInitialize(self):
        self.PlotWindowInitialize()

    def plotAction(self):
        pass
    