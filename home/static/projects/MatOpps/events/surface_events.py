import numpy as np

class SurfaceEvents:

    def plotSphere(self):
        x_0,y_0,z_0=self.UI.sCenterXCord.value(),self.UI.sCenterYCord.value(),self.UI.sCenterZCord.value()
        r=self.UI.sRadius.value()

        u = np.linspace(0, 2 * np.pi, 20)
        v = np.linspace(0, np.pi, 20)
        x = r * np.outer(np.cos(u), np.sin(v))
        y = r * np.outer(np.sin(u), np.sin(v))
        z = r * np.outer(np.ones(np.size(u)), np.cos(v))

        c=next(self.cycol)

        self.UI.graphWidget.canvas.axes.plot_wireframe(x, y, z, color=c)
        self.UI.graphWidget.canvas.draw()
    
    def plotPlane(self):

        nX,nY,nZ=self.UI.nVxCord.value(),self.UI.nVyCord.value(),self.UI.nVzCord.value()
        pX,pY,pZ=self.UI.ppXCord.value(),self.UI.ppYCord.value(),self.UI.ppXCord.value()
        x = np.linspace(-10,10,10)
        y = np.linspace(-10,10,10)

        X,Y = np.meshgrid(x,y)
        Z=(nX*X + nY*Y + (nX*pX+nY*pY+nZ*pZ))/nZ
        c=next(self.cycol)

        self.UI.graphWidget.canvas.axes.plot_wireframe(X, Y,Z, color=c)
        self.UI.graphWidget.canvas.axes.quiver(0,0,0, nX,nY,nZ, color=c)
        self.UI.graphWidget.canvas.draw()

