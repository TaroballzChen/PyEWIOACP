from time import sleep
import serial
import glob
import sys

class ArduinoConnect:
    def __init__(self):
        self.Portlist = []
        self.Serial = None

    def DetectOS(self):
        if sys.platform.startswith('win'):
            return ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            # this excludes your current terminal "/dev/tty"
            return glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            return glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')


    def GetPort(self):
        ports = self.DetectOS()
        self.Portlist.clear()
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                self.Portlist.append(port)
            except (OSError, serial.SerialException):
                pass
    

    def ConnectAction(self,serial_port):
        self.Serial = serial.Serial(serial_port,9600,timeout=2)
        for _ in range(1,10):
            rv = self.Serial.readline()
            self.Serial.flushInput()
            sleep(0.1)
            STR = rv.decode("utf-8")
            if STR[0:5] == "Ready":
                return True
        else:
            return False