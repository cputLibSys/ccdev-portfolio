import sys
sys.path.append(r"~/Documents/MatOps/Wrappers/ComplexMath")
#from complexops import ComplexOpsWrapper


from  PyQt5.QtWidgets  import *
class ComplexEvents():
    def addComplexNum(self):
        real_part=self.UI.cnRe.value()
        imag_part=self.UI.cnIm.value()

        i=self.setComplexN([real_part, imag_part])-1
        self.UI.cNtbl.setItem(i,0, QTableWidgetItem(str(real_part)))
        self.UI.cNtbl.setItem(i,1, QTableWidgetItem(str(imag_part)))
        self.UI.cNtbl.setRowCount(self.UI.cNtbl.rowCount()+1)


    def ComplexSum(self):
        rows = sorted(set(int(index.row()) for index in self.UI.cNtbl.selectedIndexes()))
        if len(rows)==2:
            print(self.SUM([rows[0], rows[1]],0))
        elif len(rows)>2:
            print(self.SUM(rows,1))

    def ComplexProd(self):
        rows = sorted(set(int(index.row()) for index in self.UI.cNtbl.selectedIndexes()))
        if len(rows)==2:
            print(self.PRODUCT(rows[0], rows[1]))
        elif len(rows)>2 or len(rows)>2: 
            print(self.RecursiveProd(rows))

    def ComplexDIV(self):
        rows = sorted(set(int(index.row()) for index in self.UI.cNtbl.selectedIndexes()))
        print(self.DIV(rows[0], rows[1]))
    #def RecursiveComplexProd(self):
