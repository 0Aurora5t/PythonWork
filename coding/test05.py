import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig=plt.figure()
ax=fig.gca(projection='3d')
#测试数据
theta=np.linspace(-4*np.pi,4*np.pi,100)
z=np.linspace(-4,4,100)*0.3
r=z**4+1
x=r*np.sin(theta)
y=r*np.cos(theta)
ax.plot(x,y,z,'b^-',label='3D Picture Test')
mpl.rcParams['legend.fontsize']=10
ax.legend()
plt.show()
