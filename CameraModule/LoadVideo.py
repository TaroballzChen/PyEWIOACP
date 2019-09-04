import cv2
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
        self.videocap.release()

    def UpdateFrame(self):
        ret , image = self.videocap.read()
        if ret == False:
            VideoLive.StopCamera(self)
            self.SwitchWebcamStatus(self.CameraLiveButtonEnabledFlag)
            return
        if type(image) != None:
            self.displayImage(image,1)

