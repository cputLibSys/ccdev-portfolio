class ScatterEvents():
    
    def Scatter(self):
        X,Y=[],[]
        for i in range(0,int(self.UI.RegresData.rowCount())):
            x=int(self.UI.RegresData.item(i, 0).text())
            y=int(self.UI.RegresData.item(i, 1).text())
            X.append(x)
            Y.append(y)
        
        self.UI.graphWidget.canvas.axes.scatter(X,Y)
        self.UI.graphWidget.canvas.draw()
    
    def addScatRow(self, operand):
        n=self.UI.nScatRows.value()
        if operand=='+':
            self.UI.RegresData.setRowCount(self.UI.RegresData.rowCount()+n)
        elif operand=='-':
            self.UI.RegresData.setRowCount(self.UI.RegresData.rowCount()-n)
