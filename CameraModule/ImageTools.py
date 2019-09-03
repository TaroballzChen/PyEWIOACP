import cv2
import time
from functools import partial
from PyQt5.QtCore import QTimer

ShotSavePath = "./snapshot_pic/"

class SnapShot:
    def __init__(self):
        pass
    
    def snapshot(self):
        try:
            cv2.imwrite(ShotSavePath+"%s.jpg"%time.time(),self.image.copy())
        except Exception:
            pass

class ImageCrop:
    def __init__(self):
        pass

    def CropImageAction(self,img):
        X = self.CropImgXcoordinate.value()
        Y = self.CropImgYcoordinate.value()
        w = self.CropImgWidth.value()
        h = self.CropImgHeight.value()

        return img[Y:Y + h, X:X + w]

class VideoSpliter:
    def __init__(self):
        pass

    def SpliterOptionsCorrect(self):
        if self.CameraLiveButtonEnabledFlag == False and self.ChooseFileSource.isChecked() == True:
            self.StartSplitButton.setEnabled(False)
            return True
        else:
            return False

    def SplitFrameAction(self):
        if self.SpliterOptionsCorrect():
            self.videocap = cv2.VideoCapture(self.SourceFilePath.text())
            self.splitsec = 0
            time_per_frame = self.TimePerFrame.value()
            self.splitcount = 0
            self.splitTimer = QTimer(self)
            self.splitTimer.timeout.connect(partial(self.splitframeaction,time_per_frame))
            self.splitTimer.start(100)
            
    def getframe_succ(self,sec):
        self.videocap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
        hasFrames,image = self.videocap.read()
        if hasFrames:
            self.displayImage(image,1)
            cv2.imwrite("%simage%d.jpg"%(self.SplitFrameSaveDir.text(),self.splitcount),self.image.copy())
        return hasFrames
        
    def splitframeaction(self,time_per_frame):
        if self.getframe_succ(self.splitsec):
            self.splitcount+=1
            self.splitsec = round(self.splitsec + time_per_frame,2)
        else:
            self.StopSplit()

    def StopSplit(self):
        self.StartSplitButton.setEnabled(True)
        self.splitTimer.stop()
        self.videocap.release()

class PixelCoordinate:
    def __init__(self):
        pass

    def LeftClickEvent(self,event,x,y,flags,param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.CoordinateDisplay.appendPlainText("( X: %d , Y: %d )"%(x,y))
            self.CoordinateDisplay.update()
            cv2.circle(self.FindCoordinateTarget,(x,y),5,(55,255,155,),2)
            cv2.imshow("Find Pixel Coordinate",self.FindCoordinateTarget)

    def ShowTargetImage(self):
        self.FindCoordinateTarget = self.image.copy()
        cv2.imshow("Find Pixel Coordinate",self.FindCoordinateTarget)
        cv2.setMouseCallback("Find Pixel Coordinate",self.LeftClickEvent)
        cv2.waitKey(0)
        if cv2.getWindowProperty("Find Pixel Coordinate",cv2.WND_PROP_VISIBLE) <1:
            cv2.destroyWindow("Find Pixel Coordinate")
            return