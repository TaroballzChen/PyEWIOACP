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

    def LeftIN(self):
        command = "c"
        self.SerialWrite(command)

    def RightIN(self):
        command = "d"
        self.SerialWrite(command)
    
    def ToLeftOut(self):
        command = "e"
        self.SerialWrite(command)

    def ToRightOut(self):
        command = "f"
        self.SerialWrite(command)

    def LeftRightIN(self):
        command = "g"
        self.SerialWrite(command)

    def Mix(self):
        command = "h"
        self.SerialWrite(command)

    def ToTopOut(self):
        command = "i"
        self.SerialWrite(command)

    def ToBottomOut(self):
        command = "j"
        self.SerialWrite(command)
        
    def TopIN(self):
        command = "k"
        self.SerialWrite(command)

    def BottomIN(self):
        command = "l"
        self.SerialWrite(command)
    
    def LRinAndMix(self):
        command = "a"
        self.SerialWrite(command)

    def ServoMag(self):
        command = "="
        self.SerialWrite(command)
    
    def Null(self):
        command = "Hello"
        print(command)