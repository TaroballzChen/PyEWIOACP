import cv2
from functools import partial
from PyQt5.QtCore import QTimer

class WebcamLive:
    def __init__(self):
        pass

    def StartCamera(self):
        if self.CameraLiveButtonEnabledFlag == True:
            self.videocap = cv2.VideoCapture(self.WebCamDeviceID.value())
            self.WebCamTimer = QTimer(self)
            self.WebCamTimer.timeout.connect(partial(WebcamLive.UpdateFrame,self))
            self.WebCamTimer.start(35)
        else:
            WebcamLive.StopCamera(self)
        
    def StopCamera(self):
        self.videocap.release()
        self.WebCamTimer.stop()

    def UpdateFrame(self):
        ret , image = self.videocap.read()
        if ret ==False:
            WebcamLive.StopCamera(self)
            self.SwitchWebcamStatus(self.CameraLiveButtonEnabledFlag)
            return
        if type(image) != None:
            self.displayImage(image,1)
