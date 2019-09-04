class pltContoursVsTime:
    def plotgraph(self,timer):
        ax = self.prepltAction()
        ax.plot(self.DetectArea,color="k")
        self.canvas.draw()
        if self.CameraLiveButtonEnabledFlag == False:
            timer.stop()
    
    