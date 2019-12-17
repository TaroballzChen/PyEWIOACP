import cv2
from functools import partial
from PyQt5.QtCore import QTimer

class IPcamLive:
    def __init__(self):
        pass

    def StartCamera(self):
        if self.CameraLiveButtonEnabledFlag == True:
            self.videocap = cv2.VideoCapture(self.IPCameraURL.text())
            self.IPCamTimer = QTimer(self)
            self.IPCamTimer.timeout.connect(partial(IPcamLive.UpdateFrame,self))
            self.IPCamTimer.start(35)
        else:
            IPcamLive.StopCamera(self)
        
    def StopCamera(self):
        self.videocap.release()
        self.IPCamTimer.stop()

    def UpdateFrame(self):
        ret , image = self.videocap.read()
        if ret ==False:
            IPcamLive.StopCamera(self)
            self.SwitchWebcamStatus(self.CameraLiveButtonEnabledFlag)
            return
        if type(image) != None:
            self.displayImage(image,1)
