import cv2,datetime,numpy
from functools import partial
from PyQt5.QtCore import QTimer

class VideoLive:
    def __init__(self):
        pass

    def StartCamera(self):
        if self.CameraLiveButtonEnabledFlag == True:
            self.videocap = cv2.VideoCapture(self.SourceFilePath.text())
            self.VideoTimer = QTimer(self)
            self.VideoTimer.timeout.connect(partial(VideoLive.UpdateFrame,self))
            self.VideoTimer.start(20)
        else:
            VideoLive.StopCamera(self)
            
    def StopCamera(self):
        self.VideoTimer.stop()
        self.exportPltData()
        self.videocap.release()

    def UpdateFrame(self):
        ret , image = self.videocap.read()
        if ret == False:
            VideoLive.StopCamera(self)
            self.SwitchWebcamStatus(self.CameraLiveButtonEnabledFlag)
            return
        if type(image) != None:
            self.displayImage(image,1)
    
    def exportPltData(self):
        if self.ContoursAreaDataPlotCheckBox.isChecked() or self.FrameGrayValueSumDataPlotCheckBox.isChecked():
            timestr = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S.%f")
            numpy.savetxt("./output_plt_data/%s.csv"%timestr,self.DetectArea)