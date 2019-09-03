from PyQt5 import QtWidgets, uic

from core.statusbar import StatusBarDisplay
from core.Arduino import ArduinoUiOperation
from core.Camera import CameraUiOperation
from core.pltWindow import PlotWindowUiOperation

UI_Path = "./core/MainUI/PyEWIOACP.ui"

PopupArduinoArrayUI_Path = "./core/MainUI/ShowArduinoArray.ui"

class PopupArduinoArrayUI():
    def __init__(self):
        self.PopupArduinoControlArrayWindowUI = uic.loadUi(PopupArduinoArrayUI_Path)
        self.PopupArduinoControlArrayWindowUI.closeEvent = self.ControlArrayCloseEvent

    def ControlArrayCloseEvent(self,event):
        self.PopupArduinoControlArrayWindowUI.ShoWArduinoControlArray.clear()


class main_ui(QtWidgets.QMainWindow,StatusBarDisplay,ArduinoUiOperation,PopupArduinoArrayUI,CameraUiOperation,PlotWindowUiOperation):

    def __init__(self):
        super(main_ui,self).__init__()
        ArduinoUiOperation.__init__(self)
        PopupArduinoArrayUI.__init__(self)
        CameraUiOperation.__init__(self)
        PlotWindowUiOperation.__init__(self)
        uic.loadUi(UI_Path,self)
        self.InitializeUiAction()
    
    def InitializeUiAction(self):
        self.StatusBarDisplayInitialize()
        self.ArduinoUiActionInitialize()
        self.CameraUiActionInitialize()
        self.PlotWindowUiActionInitialize()


        

