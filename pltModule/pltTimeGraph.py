class pltContoursVsTime:
    def plotgraph(self,timer):
        if self.ContoursAreaDataPlotCheckBox.isChecked() == True:
            ax = self.prepltAction()
            ax.plot(self.DetectArea,color="k")
            self.canvas.draw()
            if self.CameraLiveButtonEnabledFlag == False or self.ContoursAreaDataPlotCheckBox.isChecked() == False:
                timer.stop()
    
    