import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
fig = plt.figure()
fig = plt.figure()

ax = fig.add_subplot(121, projection = '3d' )

t = np.arange(5)
z = t
x = np.sin(t)*np.cos(t)
y = np.tan(t)
ax.plot(x, y, z, label = 'wykres liniowy' )


ax1=fig.add_subplot(122, projection='3d')
z1=np.arange(20)
y1=np.cos(z1)
x1=np.cos(np.pi*z1)
ax1.scatter(x1, y1, z1, label="wykres punktowy")
plt.show()

