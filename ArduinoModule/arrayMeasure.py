from functools import partial
import queue

class ControlArrayMeasure:
    def __init__(self):
        self.ThreadJobComplete = queue.Queue(1)
        self.ArrayComplete = queue.Queue(1)
        self.procedureMeasureComplete = queue.Queue(1)

    def CreateControlArray(self,procedure,electrode_num):
        whole_array_text = ""
        for i,step in enumerate(procedure):
            self.BasicArray = [0 for _ in range(electrode_num)]
            self.ModfiyArrayOne(step)
            self.ModfiyArrayGnd(procedure,i)
            whole_array_text = self.ArrayWithFormat(whole_array_text,self.BasicArray)
        else:
            self.ArrayComplete.put(whole_array_text)
            self.ThreadJobComplete.put(True)

    def ArrayWithFormat(self,whole_array_text,linearray):
        line_array_text = ""
        for i,e in enumerate(linearray,start=1):
            line_array_text = "".join([line_array_text,"%d,"%e])
            if i%8 ==0:
                line_array_text += "\t"
        else:
            line_array_text +="\n"
            return whole_array_text + line_array_text


    def ProcedureTextToArray(self):
        StepProcedureText = self.ControlArrayProcedure.toPlainText().split('\n')
        RealProcedure = []
        for line in StepProcedureText:
            NumText = line.split(",")
            RealOneStepProcedure = [int(Unit) for Unit in NumText]
            RealProcedure.append(RealOneStepProcedure)
        else:
            self.procedureMeasureComplete.put(RealProcedure)


    def ModfiyArrayOne(self,Controlist):
        for num in Controlist:
            self.BasicArray[num-1] = 1

    def ModfiyArrayGnd(self,procedure,index):
        GND_list = [-1,1,2]
        if len(procedure) -1 == index:
            GND_list.append(-2)
        for GND in GND_list:
            new_index = index + GND
            if new_index<0 or new_index > len(procedure)-1:
                continue
            for e in procedure[new_index]:
                self.BasicArray[e-1] = -1
