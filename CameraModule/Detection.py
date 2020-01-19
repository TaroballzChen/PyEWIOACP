import cv2
import numpy as np
from core.ThreadJob import DoThreadJob
from functools import partial

class EdgeDetection:
    def __init__(self):
        pass

    def BlurredFrame(self,img):
        frame = cv2.GaussianBlur(img,(7,7),0)
        return frame

    def ConvertHSV(self,img):
        frame = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        return frame

    def CreateMask(self,hsvimg,lower,upper):
        mask = cv2.inRange(hsvimg,lower,upper)
        return mask

    def ObjectContours(self,mask):
        try:
            _,contours,_ =  cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
        except ValueError:
            contours, _ =  cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
            return contours
        return contours

    def ImageDrawContours(self,img,contours):
        for contour in contours:
            area = cv2.contourArea(contour)

            if area > 1:
                cv2.drawContours(img,contour,-1,(0,255,0),1)        
    
    
    def getContoursArea(self,contours):
        if not contours:
            self.DetectArea = np.append(self.DetectArea,0)
            return
        for contour in contours:
            area = cv2.contourArea(contour)
            self.DetectArea = np.append(self.DetectArea,area)
        
    def showMask(self):
        blurred_frame = self.BlurredFrame(self.image.copy())
        hsvimg = self.ConvertHSV(blurred_frame)
        lower = np.array([self.EdgeDetectLowerB.value(),self.EdgeDetectLowerG.value(),self.EdgeDetectLowerR.value()])
        upper = np.array([self.EdgeDetectUpperB.value(),self.EdgeDetectUpperG.value(),self.EdgeDetectUpperR.value()])
        mask = self.CreateMask(hsvimg,lower,upper)
        cv2.imshow("Mask",mask)
        cv2.waitKey(1)
        if cv2.getWindowProperty("Mask",cv2.WND_PROP_VISIBLE) <1:
            cv2.destroyWindow("Mask")
            self.MaskTimer.stop()
            return


    def showHSV(self):
        blurred_frame = self.BlurredFrame(self.image.copy())
        hsvimg = self.ConvertHSV(blurred_frame)
        cv2.imshow("HSV",hsvimg)
        cv2.waitKey(1)
        if cv2.getWindowProperty("HSV",cv2.WND_PROP_VISIBLE) <1:
            cv2.destroyWindow("HSV")
            self.HSVTimer.stop()
            return

    def EdgeDetectProcess(self,img):
        blurred_frame = self.BlurredFrame(img)
        hsvimg = self.ConvertHSV(blurred_frame)
        lower = np.array([self.EdgeDetectLowerB.value(),self.EdgeDetectLowerG.value(),self.EdgeDetectLowerR.value()])
        upper = np.array([self.EdgeDetectUpperB.value(),self.EdgeDetectUpperG.value(),self.EdgeDetectUpperR.value()])
        mask = self.CreateMask(hsvimg,lower,upper)
        contours = self.ObjectContours(mask)
        DoThreadJob(partial(self.ImageDrawContours,img,contours))
        DoThreadJob(partial(self.getContoursArea,contours))

class FrameGrayValueSumDetection:

    def __init__(self):
        pass
    
    def RecordFrameGrayVal(self,img):
        self.DetectArea = np.append(self.DetectArea,img.sum())

    def getFrameGrayValueProcess(self,img):
        DoThreadJob(partial(self.RecordFrameGrayVal,img))
        