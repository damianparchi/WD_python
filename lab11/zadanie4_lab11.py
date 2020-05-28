import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
fig = plt.figure(figsize=(8,3))

ax1 = fig.add_subplot(231, projection = '3d')
ax2 = fig.add_subplot(232, projection = '3d')
ax3 = fig.add_subplot(233, projection = '3d')
ax4 = fig.add_subplot(234, projection = '3d')
ax5 = fig.add_subplot(235, projection = '3d')

_x = np.arange(4)
_y = np.arange(5)
__xx, __yy = np.meshgrid(_x, _y)
x, y = __xx.ravel(),__yy.ravel()
top = x+y 
bottom = np.zeros_like(top)
width = depth = 1
ax1.bar3d(x,y,bottom,width,depth,top,shade=True, color = 'Blue')
ax1.set_title('Wykres zacieniony')
ax2.bar3d(x,y,bottom,width,depth,top,shade=False, color = 'red')
ax2.set_title('wykres niezacieniony')
ax3.bar3d(x,y,bottom,width,depth,top,shade=True,color = 'Green')
ax3.set_title('wykres trzeci')
ax4.bar3d(x,y,bottom,width,depth,top,shade=True,color = 'Black')
ax4.set_title('wykres czwarty')
ax5.bar3d(x, y, bottom, width, depth, top, shade = True , color='White')
ax5.set_title('Wykres piaty')


plt.show()