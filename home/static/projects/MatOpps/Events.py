from Wrappers.linear_algebra.mat_maths import *
from itertools import cycle
import matplotlib
from  PyQt5.QtWidgets  import *
from events.mat_events import *
from events.vector_events import *
from events.scatter_events import *
from events.surface_events import *
from events.complex_events import *

class Events(ScatterEvents, SurfaceEvents, VectorEvents, MatEvents, ComplexEvents):
    def changeContext(self):
        i = int(self.UI.currentContext.currentIndex())
        if i==1:
            self.UI.graphWidget.canvas.axes.cla()
            self.UI.graphWidget.canvas.axes  =  self.UI.graphWidget.canvas.figure.add_subplot( 111)
        else:
            self.UI.graphWidget.canvas.axes.cla()
            self.UI.graphWidget.canvas.axes  =  self.UI.graphWidget.canvas.figure.add_subplot( 111, projection='3d')

        self.UI.graphWidget.canvas.draw()

    def __init__(self, ui):

        self.UI=ui
        self.matOps=BasicOps()

        self.cycol = cycle('bgrcmk')

        self.UI.currentContext.currentIndexChanged.connect(self.changeContext)

        self.UI.matAddBtn.clicked.connect(lambda:self.addMats('+'))
        self.UI.matSubBtn.clicked.connect(lambda:self.addMats('-'))
        self.UI.matProdBtn.clicked.connect(lambda: self.matProd())
        self.UI.matTransBtn.clicked.connect(lambda: self.transM())
        self.UI.nrA.valueChanged.connect(lambda:self.changeADims())
        self.UI.ncA.valueChanged.connect(lambda:self.changeADims())
        self.UI.nrB.valueChanged.connect(lambda:self.changeBDims())
        self.UI.ncB.valueChanged.connect(lambda:self.changeBDims())

        self.UI.addSphereBtn.clicked.connect(lambda:self.plotSphere())

        self.UI.scatterBtn.clicked.connect(self.Scatter)
        self.UI.addScatRowBtn.clicked.connect(lambda:self.addScatRow('+'))
        self.UI.removeScatRowBtn.clicked.connect(lambda:self.addScatRow('-'))

       

        self.UI.addVectorBtn.clicked.connect(lambda:self.plotVector([self.UI.xOrigCord.value(), self.UI.yOrigCord.value(), self.UI.zOrigCord.value()],self.getVector()))
        self.UI.addToVListBtn.clicked.connect(self.addToVList)
        self.UI.vectorAdditionBtn.clicked.connect(self.addVectors)
        
        self.UI.addPlaneBtn.clicked.connect(self.plotPlane)

        self.UI.addCMN.clicked.connect(self.addComplexNum)
        self.UI.cnSumBtn.clicked.connect(self.ComplexSum)
        self.UI.cnProdBtn.clicked.connect(self.ComplexProd)
        self.UI.cnDivBtn.clicked.connect(self.ComplexDIV)