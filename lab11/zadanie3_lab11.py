import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure()
ax = fig.add_subplot(321, projection='3d')

X = np.arange(-5,5,0.25)
Y = np.arange(-5,5,0.25)
X,Y = np.meshgrid(X,Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R) 

surf = ax.plot_surface(X, Y, Z, cmap=cm.Blues, linewidth = 0, antialiased = False)
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter( '%.02f' ))

ax2 = fig.add_subplot(322, projection = '3d' )
surf = ax2.plot_surface(X, Y, Z, cmap =cm.RdPu,
linewidth = 0 , antialiased = False )

ax2 = fig.add_subplot(323, projection = '3d' )
surf = ax2.plot_surface(X, Y, Z, cmap =cm.Purples,
linewidth = 0 , antialiased = False )

ax3 = fig.add_subplot(324, projection = '3d' )
surf = ax3.plot_surface(X, Y, Z, cmap =cm.GnBu,
linewidth = 0 , antialiased = False )

ax5 = fig.add_subplot(325, projection = '3d' )
surf = ax5.plot_surface(X, Y, Z, cmap =cm.Greens,
linewidth = 0 , antialiased = False )





plt.show()