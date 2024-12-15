from cmath import cos
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math as m
pts=[[], [], []]

#X, Y, Z, U, V, W = zip(*soa)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def Sphere(r):

    x0, y0, z0=[0, 0, 0]
    
    for i in range(0, 360, 10):
        for j in range(0, 180, 10):
            x=x0+r*m.cos(m.radians(i))*m.sin(m.radians(j))
            y=y0+r*m.sin(m.radians(i))*m.sin(m.radians(j))
            z=z0+r*m.cos(m.radians(j))
            pts[0].append(x)
            pts[1].append(y)
            pts[2].append(z)

    ax.quiver(x0, y0, z0, pts[0][0], pts[1][0], pts[2][0])

    ax.quiver(x0, y0, z0, pts[0][0], 0, 0, color='red') #proj of r onto x-axis
    ax.quiver(x0, y0, z0, 0, pts[1][0], 0, color='green') #proj of r onto y-axis
    ax.quiver(x0, y0, z0, 0, 0, pts[2][0], color='orange') #proj of r onto z-axis
    ax.scatter(pts[0][0], pts[1][0], pts[2][0], color="orange")


x0, y0, z0=[0, 0, 0]
x=x0+4*m.cos(m.radians(30))*m.sin(m.radians(45))
y=y0+4*m.sin(m.radians(30))*m.sin(m.radians(45))
z=z0+4*m.cos(m.radians(45))



Sphere(10)
ax.scatter(pts[0], pts[1], pts[2], alpha=0.1)

ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_zlim([-10, 10])
plt.show()