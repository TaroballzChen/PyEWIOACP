from functools import partial
from PyQt5.QtCore import QTimer

from core.ThreadJob import DoThreadJob,DoQThreadJob
from ArduinoModule.connect import ArduinoConnect
from ArduinoModule.control import SendCommand
from ArduinoModule.arrayMeasure import ControlArrayMeasure

class ArduinoUiOperation(ArduinoConnect,SendCommand,ControlArrayMeasure):
    def __init__(self):
        super(ArduinoUiOperation,self).__init__()
        ControlArrayMeasure.__init__(self)
        self.ThreadTimer = QTimer(self)

    def ArduinoUiActionInitialize(self):
        self.RefreshPortsButton.clicked.connect(self.GetPort)
        self.ArduinoConnectButton.clicked.connect(partial(DoThreadJob,self.DoConnect))
        self.CreateArduinoControlArrayBtn.clicked.connect(self.CreateControlArray)

        # Path Control
        self.SixteenOfOne.clicked.connect(partial(DoThreadJob,self.SeriesLight))
        self.OneOfOne.clicked.connect(partial(DoThreadJob,self.DFPMix))
        self.OneOfThree.clicked.connect(partial(DoThreadJob,self.QFPMix))
        self.TwoOfOne.clicked.connect(partial(DoThreadJob,self.QFPXMix))
        
        # Magnetic beads with NAEB Experiment Path Control
        self.SixOfOne.clicked.connect(partial(DoThreadJob,self.MagbeadsSampleGo))
        self.SixOfTwo.clicked.connect(partial(DoThreadJob,self.XMix))
        self.SixOfThree.clicked.connect(partial(DoThreadJob,self.NAEBGo))
        self.SixOfFour.clicked.connect(partial(DoThreadJob,self.NAEBGo2))
        self.SevenOfOne.clicked.connect(partial(DoThreadJob,self.WasteClean))
        self.SevenOfTwo.clicked.connect(partial(DoThreadJob,self.WasteClean2))

    def GetPort(self):
        ArduinoConnect.GetPort(self)
        self.PortComboBox.clear()
        self.PortComboBox.addItems(self.Portlist)
    
    def DoConnect(self):
        self.ArduinoConnectButton.setEnabled(False)
        self.RefreshPortsButton.setEnabled(False)
        self.PortComboBox.setEnabled(False)
        try:
            succ = self.ConnectAction(self.PortComboBox.currentText())
            
            if not succ:
                raise TimeoutError("Arduino Connect Timeout")
    
            self.ArduinoConnectSucced() #show in status bar


        except Exception:
            self.ArduinoConnectButton.setEnabled(True)
            self.RefreshPortsButton.setEnabled(True)
            self.PortComboBox.setEnabled(True)
    
    def CreateControlArray(self):
        
        electrode_num = self.ArduinoElectrodeNumber.value()

        DoQThreadJob(self.ProcedureTextToArray).start()
        # procedure = self.ProcedureTextToArray()

        DoThreadJob(partial(ControlArrayMeasure.CreateControlArray,self,self.procedureMeasureComplete.get(),electrode_num))

        if self.ThreadJobComplete.get():
            self.ArrayPannelUpdate(self.ArrayComplete.get())
            self.ThreadTimer.singleShot(5,self.PopupArduinoControlArrayWindowUI.show)
        
    
    def ArrayPannelUpdate(self,string):
        self.PopupArduinoControlArrayWindowUI.ShoWArduinoControlArray.setText(string)
        self.PopupArduinoControlArrayWindowUI.ShoWArduinoControlArray.update()
    
        