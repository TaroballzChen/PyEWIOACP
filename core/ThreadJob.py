import threading
from PyQt5.QtCore import QThread, pyqtSignal

def DoThreadJob(target_func):
    THREAD = threading.Thread(target = target_func)
    THREAD.start()



class DoQThreadJob(QThread):

        def __init__(self,func):
                QThread.__init__(self)
                self.func = func
                
        def __del__(self):
                self.wait()

        def run(self):
               self.func()
