from  PyQt5.QtWidgets  import *
class MatEvents:
    
    def changeResDims(self, r, c):
        self.UI.MatRes.setRowCount(r)
        self.UI.MatRes.setColumnCount(c)

    def changeADims(self):
        r, c=self.UI.nrA.value(), self.UI.ncA.value()
        self.UI.matA.setRowCount(r)
        self.UI.matA.setColumnCount(c)

    def changeBDims(self):
        r, c=self.UI.nrB.value(), self.UI.ncB.value()
        self.UI.matB.setRowCount(r)
        self.UI.matB.setColumnCount(c)

    def popMatrices(self, dim, mat):
        newM=self.matOps.popMatrix(dim)
        for i in range(0, int(dim[0])):
            for j in range(0, int(dim[1])):
                newM[i][j]=float(mat.item(i,j).text())

        return newM

    def ExtractData(self):
        
        dimA, dimB=[self.UI.matA.rowCount(), self.UI.matA.columnCount()],[self.UI.matB.rowCount(),self.UI.matB.columnCount()]
        tA= self.popMatrices(dimA, self.UI.matA)
        tB= self.popMatrices(dimB, self.UI.matB)

        tA.append(dimA)
        tB.append(dimB)
      
        return [tA, tB]
        
    def popResMat(self, mat, dim):
        self.changeResDims(dim[0], dim[1])
        for i in range(0, int(dim[0])):
            for j in range(0, int(dim[1])):
                self.UI.MatRes.setItem(i, j, QTableWidgetItem(str(mat[i][j])))

    def addMats(self, operand):
        data=self.ExtractData()

        if data!="Error":
            tA,tB=data[0],data[1]

            resM=self.matOps.matAddSub(operand, tA, tB)
            self.popResMat(resM, [len(resM), len(resM[0])])
        else:
            print("Error")

    def matProd(self):
        data=self.ExtractData()
        tA, tB=data[0],data[1]
        resM=self.matOps.matProd(tA, tB)
        self.popResMat(resM, [len(resM), len(resM[0])])

    def transM(self):
        data=self.ExtractData()
        A,B=data[0][:-1],data[1][:-1]
        resM=self.matOps.transpose(A)
        self.popResMat(resM, [len(resM), len(resM[0])])