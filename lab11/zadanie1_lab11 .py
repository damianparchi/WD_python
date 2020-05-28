import numpy as np 
import matplotlib.pyplot as plt  

fig = plt.figure()
ax = fig.gca(projection='3d')

t = np.linspace(0, 2 * np.pi, 100)
z = t 
x = np.sin(t)
y = 2*np.cos(t) 
ax.plot(x,y,z,label='zadanie 1')

ax.set_xlabel('X label')
ax.set_ylabel('Y label')
ax.set_zlabel('Z label')


ax.legend()
plt.show()