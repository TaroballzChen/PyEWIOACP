class StatusBarDisplay:
    def __init__(self):
        pass
    
    def StatusBarDisplayInitialize(self):
        self.StatusBar.showMessage("Arduino Disconnected")

    def ArduinoConnectSucced(self):
        self.StatusBar.showMessage("Arduino Connect")