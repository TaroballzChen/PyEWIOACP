class pltContoursVsTime:
    def plotgraph(self,timer):
        ax = self.prepltAction()
        ax.plot(self.DetectArea,color="k")
        self.canvas.draw()
        if self.CameraLiveButtonEnabledFlag == False or self.ContoursAreaDataPlotCheckBox.isChecked() == False:
            timer.stop()
    

class pltFrameGrayValueSumVsTime:
    def plotgraph(self,timer):
        ax = self.prepltAction()
        ax.plot(self.DetectArea,color="k")
        self.canvas.draw()
        if self.CameraLiveButtonEnabledFlag == False or self.FrameGrayValueSumDataPlotCheckBox.isChecked() == False:
            timer.stop()