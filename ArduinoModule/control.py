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
