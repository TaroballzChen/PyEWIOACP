import matplotlib
matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

from PyQt5.QtCore import QTimer
from functools import partial

from pltModule.pltTimeGraph import pltContoursVsTime,pltFrameGrayValueSumVsTime
class PlotWindowUiOperation(pltContoursVsTime,pltFrameGrayValueSumVsTime):
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

    def IntegrationPlot(self):
        if self.ContoursAreaDataPlotCheckBox.isChecked() == True:
            self.Dopltgraph(pltContoursVsTime.plotgraph)
        elif self.FrameGrayValueSumDataPlotCheckBox.isChecked() == True:
            self.Dopltgraph(pltFrameGrayValueSumVsTime.plotgraph)
        else:
            pass

    def prepltAction(self):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.clear()
        return ax

    def Dopltgraph(self,pltfunc):
        pltTimer = QTimer(self)
        pltTimer.timeout.connect(partial(pltfunc,self,pltTimer))
        pltTimer.start(1000)
    