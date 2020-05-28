import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
fig = plt.figure()
ax = fig.add_subplot(121, projection = '3d' )
X = np.arange(- 5 , 5 , 0.25 )
Y = np.arange(- 5 , 5 , 0.25 )
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X** 2 + Y** 2 )
Z = np.sin(R)
surf = ax.plot_surface(X, Y, Z, cmap =cm.Greens,
linewidth = 0 , antialiased = False )
ax.set_zlim(- 1.01 , 1.01 )
ax.zaxis.set_major_locator(LinearLocator( 10 ))
ax.zaxis.set_major_formatter(FormatStrFormatter( '%.02f' ))

X1 = np.arange(- 5 , 5 , 0.1 )
Y1 = np.arange(- 5 , 5 , 0.1 )
XX1, YY1 = np.meshgrid(X1, Y1)
R = np.sqrt(XX1** 2 + YY1** 2 )
Z = np.sin(R)
ax2 = fig.add_subplot(122, projection = '3d' )
surf2 = ax2.plot_surface(XX1, YY1, Z, cmap =cm.Oranges,
linewidth = 0 , antialiased = True )
ax2.set_zlim(- 1.01 , 1.01 )
ax2.zaxis.set_major_locator(LinearLocator( 10 ))
ax2.zaxis.set_major_formatter(FormatStrFormatter( '%.02f' ))

plt.show()