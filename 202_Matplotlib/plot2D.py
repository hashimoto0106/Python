import numpy as np
from numpy import sin, cos
import matplotlib.pyplot as plt

x = np.arange(-np.pi, np.pi, 0.1)
y1 = sin(x)
y2 = cos(x)

plt.figure(1)
plt.clf()

plt.plot(x, y1, label='sin')
plt.plot(x, y2, 'r*', markersize=10, label='cos')

plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.legend(loc='best')
plt.show()
