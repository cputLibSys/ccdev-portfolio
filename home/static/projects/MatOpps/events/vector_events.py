from operator import add

class VectorEvents:

    vList={}

    def getVector(self):
        
        return [self.UI.xVcord.value(), self.UI.yVcord.value(), self.UI.zVcord.value()]

    def plotVector(self, orig, vect):

        origin=orig
        vector=vect
        #x,y,z=[vector]
        x_lims,y_lims,z_lims=eval(self.UI.Vx_lims.text()),eval(self.UI.Vy_lims.text()),eval(self.UI.Vz_lims.text())
        c=next(self.cycol)

        self.UI.graphWidget.canvas.axes.scatter(origin[0],origin[1], origin[2], color=c)
        self.UI.graphWidget.canvas.axes.quiver(origin[0], origin[1], origin[2], vector[0], vector[1], vector[2],color=c, arrow_length_ratio=0.1)
        
        self.UI.graphWidget.canvas.axes.set_xlim(int(x_lims[0]), int(x_lims[1]))
        self.UI.graphWidget.canvas.axes.set_ylim(int(y_lims[0]), int(y_lims[1]))
        self.UI.graphWidget.canvas.axes.set_zlim(int(z_lims[0]), int(z_lims[1]))

        self.UI.graphWidget.canvas.draw()
        self.UI.vNameList.addItem(self.UI.Vname.text())
        self.vList[self.UI.Vname.text()]=vector

    def addToVList(self):
        currVector=self.UI.vNameList.currentText()
        self.UI.aVnameList.addItem(currVector)

    def addVectors(self):
        vectors=[self.UI.aVnameList.itemText(i) for i in range(self.UI.aVnameList.count())]
        superposition=[0,0,0]
        for vector in vectors:
            superposition[0]+=self.vList[vector][0]
            superposition[1]+=self.vList[vector][1]
            superposition[2]+=self.vList[vector][2]

        #self.plotVector(superposition)
        print(superposition)
