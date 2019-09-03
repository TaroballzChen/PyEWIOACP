import cv2
from pypylon import pylon
from functools import partial
from PyQt5.QtCore import QTimer

class BaslerLive:
    def __init__(self):
       self.camera = None

    @property
    def PylonImageToCVImage_perferences(self):
        """
        converting to opencv bgr format option
        """
        self.converter = pylon.ImageFormatConverter()
        self.converter.OutputPixelFormat = pylon.PixelType_BGR8packed
        self.converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned

    def StartCamera(self):
        if self.CameraLiveButtonEnabledFlag == True:
            self.GrabFrameContinusely()
            self.BaslerTimer = QTimer(self)
            self.BaslerTimer.timeout.connect(partial(BaslerLive.UpdateFrame,self))
            self.BaslerTimer.start(5)
        else:
            BaslerLive.StopCamera(self)

    def StopCamera(self):
        self.BaslerTimer.stop()
        self.camera.StopGrabbing()
    
    def CameraConnect(self):
        """
        conecting to the first available camera
        """
        camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
        return camera

    def GrabFrameContinusely(self):
        """
        Grabing Continusely (video) with minimal delay
        """
        self.camera = self.CameraConnect()
        self.camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)

    def UpdateFrame(self):
        if self.camera.IsGrabbing():
            grabResult = self.camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
            if grabResult.GrabSucceeded():
                image = self.converter.Convert(grabResult)
                image = image.GetArray()

                self.displayImage(image,1)
            
            grabResult.Release()