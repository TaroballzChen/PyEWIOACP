from PyQt5.QtGui import QPixmap,QImage
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QFileDialog
from functools import partial

from CameraModule.BaslerCamLive import BaslerLive
from CameraModule.WebCamLive import WebcamLive
from CameraModule.IPCamLive import IPcamLive
from CameraModule.LoadVideo import VideoLive
from CameraModule.ImageTools import SnapShot,ImageCrop,VideoSpliter,PixelCoordinate,GrayLevel
from CameraModule.Detection import EdgeDetection,FrameGrayValueSumDetection

import numpy as np

class CameraUiOperation(BaslerLive,WebcamLive,IPcamLive,VideoLive,SnapShot,ImageCrop,VideoSpliter,PixelCoordinate,GrayLevel,EdgeDetection,FrameGrayValueSumDetection):
    def __init__(self):
        super(CameraUiOperation,self).__init__()
        self.CameraLiveButtonEnabledFlag = False
        self.image = None
        self.Imagecopytodisplay = None
    
    def CameraUiActionInitialize(self):
        self.CameraLiveButton.clicked.connect(self.StartCamera)
        self.CameraSnapshotButton.clicked.connect(self.snapshot)
        self.ShowMaskButton.clicked.connect(self.UIshowMask)
        self.ShowHSVButton.clicked.connect(self.UIshowHSV)
        self.VideoSourceFileDialog.clicked.connect(self.LoadVideoFileName)
        self.SplitFrameSaveFileDialog.clicked.connect(self.SplitToFrameSaveDir)
        self.StartSplitButton.clicked.connect(self.SplitFrameAction)
        self.ShowFindCoordinateTargetImagebtn.clicked.connect(self.ShowTargetImage)

    def StartCamera(self):
        self.preStartCameraAction()
        self.SwitchWebcamStatus(self.CameraLiveButtonEnabledFlag)
        if self.ChooseBaslercamSource.isChecked():
            BaslerLive.StartCamera(self)
        elif self.ChoseWebcamSource.isChecked():
            WebcamLive.StartCamera(self)
        elif self.ChooseFileSource.isChecked():
            VideoLive.StartCamera(self)
        elif self.ChooseIPcamSource.isChecked():
            IPcamLive.StartCamera(self)
        
        # plotGraph
        self.IntegrationPlot()

    def preStartCameraAction(self):
        if self.CameraLiveButtonEnabledFlag == False:
            self.DetectArea = np.ndarray([])

    def SwitchWebcamStatus(self,status):
        if not status:
            self.CameraLiveButtonEnabledFlag = True
            self.CameraLiveButton.setText("Stop")
        else:
            self.CameraLiveButtonEnabledFlag = False
            self.CameraLiveButton.setText("Live")

    def displayImage(self,img,window=1):
        self.ImagePreOperate(img)
        outImage = self.imgtoQImage(self.Imagecopytodisplay)
        if window ==1:
            self.LiveFrameShowLabel.setPixmap(QPixmap.fromImage(outImage))
            if self.DisplayAutoScaledCheckBox.isChecked():
                self.LiveFrameShowLabel.setScaledContents(True)   #是否自適應QLabel的大小
            else:
                self.LiveFrameShowLabel.setScaledContents(False)
        # if window ==2:
        #     self.SLabel.setPixmap(QPixmap.fromImage(outImage))
        #     self.snapLabel.setScaledContents(True)

    def ImagePreOperate(self,img):
        if self.SetImageSizeCheckBox.isChecked():
            img = self.CropImageAction(img)
        
        if self.GrayLevelTransformCheckBox.isChecked():
            img = self.GrayLevelTransform(img)

        if self.FrameGrayValueSumDataPlotCheckBox.isChecked():
            self.getFrameGrayValueProcess(img)
        
        self.image = img
        self.Imagecopytodisplay = self.image.copy()

        if self.EdgeDetectCheckBox.isChecked():
            self.EdgeDetectProcess(self.Imagecopytodisplay)
        
    def LoadVideoFileName(self):
        fileName_choose, _ , = QFileDialog.getOpenFileName(self,"Select Video File",".","Video File(*.mp4 *.mov *.avi *.flv *.wmv)")
        if fileName_choose =="":
            return
        self.SourceFilePath.setText(fileName_choose)

    def SplitToFrameSaveDir(self):
        SavePath = QFileDialog.getExistingDirectory(self,"Selct Split Frame Save Directory",".",)
        if SavePath == "":
            return
        self.SplitFrameSaveDir.setText(SavePath+"/")

    def UIshowMask(self):
        self.MaskTimer =QTimer(self)
        self.MaskTimer.timeout.connect(self.showMask)
        self.MaskTimer.start(5)
    
    def UIshowHSV(self):
        self.HSVTimer = QTimer(self)
        self.HSVTimer.timeout.connect(self.showHSV)
        self.HSVTimer.start(5)


    def imgtoQImage(self,img):
        qformat = QImage.Format_Indexed8
        try:
            if len(img.shape) ==3:     # shape 第0項為長 第1項為寬  第三項為channel RGB為3 灰階為1 RGBA含有透明度為4
                if img.shape[2] == 4:
                    qformat = QImage.Format_RGBA8888
                else:
                    qformat=QImage.Format_RGB888

            outImage = QImage(img,img.shape[1],img.shape[0],img.strides[0],qformat)
            outImage = outImage.rgbSwapped()

        except Exception:
            outImage = QImage(600,800,QImage.Format_RGB888)

        return outImage