from time import sleep

class SendCommand:
    def __init__(self):
        pass

    def SerialWrite(self,command):
        self.Serial.write(command.encode("utf-8"))
        rv = self.Serial.readline()
        self.Serial.flushInput()
    

    def SeriesLight(self):
        command = "b"
        self.SerialWrite(command)

    def DFPMix(self):
        command = "n"
        self.SerialWrite(command)
    
    def QFPMix(self):
        command = "m"
        self.SerialWrite(command)
    
    def QFPXMix(self):
        command = "x"
        self.SerialWrite(command)

    # Magnetic bead with NAEB Experiment
    
    def MagbeadsSampleGo(self):
        command = "g"
        self.SerialWrite(command)

    def XMix(self):
        command = "h"
        self.SerialWrite(command)

    def WasteClean(self):
        command = "i"
        self.SerialWrite(command)

    def WasteClean2(self):
        command = "j"
        self.SerialWrite(command)
        
    def NAEBGo(self):
        command = "k"
        self.SerialWrite(command)

    def NAEBGo2(self):
        command = "l"
        self.SerialWrite(command)
        
