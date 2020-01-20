from PyQt5.QtWidgets import QTableWidgetItem,QMessageBox,QFileDialog,QSpinBox
from PyQt5.QtCore import QTimer
from core.ThreadJob import DoThreadJob
import numpy,time

class ControlProcedure:
    def __init__(self):
        pass

    def AddNewRow(self):
        row = self.ControlProcedureList.rowCount()
        self.ControlProcedureList.insertRow(row)
        

    def RemoveSelectedRow(self):
        row = self.ControlProcedureList.currentRow()
        self.ControlProcedureList.removeRow(row)

    # Logic
    def StartProcess(self):
        self.ProcedureReload()
        self.ControlProcedureList.selectRow(0)
        self.ControlProcedureTimer = QTimer(self)
        self.ControlProcedureTimer.timeout.connect(self.ExcuteProcess)
        self.ControlProcedureTimer.start()
        
    def ExcuteProcess(self):
        totalRow = self.ControlProcedureList.rowCount()
        currentRow = self.ControlProcedureList.currentRow()
        Action = self.ControlProcedureList.item(currentRow,0).text()
        isFinish = self.ControlProcedureList.item(currentRow,2).text()
        SpendTime = int(self.ControlProcedureList.item(currentRow,1).text())
        

        if isFinish == "" and self.IsActionExists(Action):
            f = getattr(self,Action)    
            DoThreadJob(f)   # Do something 
            self.ControlProcedureList.setItem(currentRow,2,QTableWidgetItem("V"))
            if self.isProcessEnd(currentRow,totalRow):
                self.ControlProcedureTimer.stop()
                return

        elif self.IsActionExists(Action) == False:
            self.ControlProcedureTimer.stop()
            QMessageBox.information(self,"Action is NOT exists","%s action isn't exists, Please confirm."%Action,QMessageBox.Ok)
            return

        self.ControlProcedureList.selectRow(currentRow+1)
        self.ControlProcedureTimer.setInterval(SpendTime)
        return
        
    def isProcessEnd(self,currentRow,totalRow):
        if totalRow == (currentRow+1):
            return True
        else:
            return False


    def IsActionExists(self,Action):
        if hasattr(self,Action):
            return True
        else:
            return False

    def ProcedureReload(self):
        totalRow = self.ControlProcedureList.rowCount()
        for row in range(totalRow):
            self.ControlProcedureList.setItem(row,2,QTableWidgetItem(""))

    def StopProcess(self):
        self.ControlProcedureTimer.stop()

    def GetProcedureFileName(self):
        fileName, _ = QFileDialog.getSaveFileName(self,"Contorl Process File Choose","./ProcessFile", "Text Files(*.pcs)")
        if fileName == "":
            return
        self.ProcessSourceFilePath.setText(fileName)
    
    def ReadProcedureFile(self):
        FileName = self.ProcessSourceFilePath.text()
        with open(FileName,"r") as file:
            all = file.readlines()
            return [p.strip() for p in all]
    
    def LoadProcedure(self):
        timelist = numpy.ndarray([])
        try:
            ProcedureList = self.ReadProcedureFile()
            self.ControlProcedureList.setRowCount(0)
            for i in range(len(ProcedureList)):
                self.AddNewRow()
                rowItem = ProcedureList[i].split("\t")
                self.ControlProcedureList.setItem(i,0,QTableWidgetItem(rowItem[0]))
                self.ControlProcedureList.setItem(i,1,QTableWidgetItem(rowItem[1]))
                timelist = numpy.append(timelist,int(rowItem[1]))
            else:
                sec = timelist.sum() / 1000
                convertTime = time.strftime("%H:%M:%S",time.gmtime(sec))
                self.ProcedureEstimatedTime.setText(convertTime)

        except FileNotFoundError:
            QMessageBox.information(self,"File Not Found!!!","File Not Found! plese confirm",QMessageBox.Ok)
    
    def GetControlProcedureListItem(self):
        totalRow = self.ControlProcedureList.rowCount()
        l = []
        for row in range(totalRow):
            actionText = self.ControlProcedureList.item(row,0).text()
            spendTimeText = self.ControlProcedureList.item(row,1).text()
            l.append(actionText+"\t"+spendTimeText)
        else:
            return [p+"\n" for p in l]
    
    def SaveProcedure(self):
        ProcedureList = self.GetControlProcedureListItem()
        FileName = self.ProcessSourceFilePath.text()
        if FileName == "":
            return
        with open(FileName,'w') as file:
            file.writelines(ProcedureList)
        QMessageBox.information(self,"Save Success","Save Sucessful.",QMessageBox.Ok)
        

    