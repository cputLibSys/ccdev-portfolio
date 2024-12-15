from  PyQt5.QtWidgets  import *

from PyQt5 import QtCore, QtWidgets
from  matplotlib.backends.backend_qt5agg  import  FigureCanvas
from mpl_toolkits.mplot3d import Axes3D

from  matplotlib.figure  import  Figure
import matplotlib.pyplot as plt
 
import numpy as np

class  graphWidget(QWidget):
    
    def  __init__ (self ,  parent  =  None ):

        QWidget.__init__( self ,  parent )

        fig=plt.figure()
        self.canvas  =  FigureCanvas( fig, )
        self.canvas.setMaximumSize(700,700)
        self.canvas.setFixedSize( 700,700)

        self.canvas.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        #self.canvas.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.canvas.setFocus()
        self.canvas.updateGeometry()

        self.canvas.axes  =  self.canvas.figure.add_subplot( 111, projection='3d')

        self.canvas.axes.set_xlim(-20, 20)
        self.canvas.axes.set_ylim(-20, 20)
        self.canvas.axes.set_zlim(-20, 20)

        self.canvas.axes.set_xlabel("X")
        self.canvas.axes.set_ylabel("Y")
        self.canvas.axes.set_zlabel("Z")
       
        vertical_layout  =  QVBoxLayout() 
        vertical_layout.addWidget (self.canvas)
        self.setLayout( vertical_layout )
        
        #x,y,z=r*np.cos([i for i in range(1, 15)])*np.sin([i for i in range(1, 15)]),r*np.sin([i for i in range(1, 15)])*np.sin([i for i in range(1, 15)]),r*np.cos([i for i in range(1, 15)])

        

        