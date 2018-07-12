import  matplotlib.pyplot as plt
import  matplotlib.gridspec as gs
import numpy as np

G = gs.GridSpec(3, 3)

axes_1 = plt.subplot(G[0, :])
plt.xticks([]), plt.yticks([])
plt.text(0.5, 0.5, 'Figure1', ha='center', va='center', size=10)

axes_2 = plt.subplot(G[1, :-1])
x = np.arange(-np.pi, np.pi, 0.1)
y = np.sin(x)
plt.plot(x, y)
plt.text(0.5, 0.5, 'Figure2', ha='center', va='center', size=10)

axes_3 = plt.subplot(G[1:, -1])
plt.xticks([]), plt.yticks([])
plt.text(0.5, 0.5, 'Figure3', ha='center', va='center', size=10)

axes_4 = plt.subplot(G[-1, 0])
plt.xticks([]), plt.yticks([])
plt.text(0.5, 0.5, 'Figure4', ha='center', va='center', size=10)

axes_5 = plt.subplot(G[-1, -2])
plt.xticks([]), plt.yticks([])
plt.text(0.5, 0.5, 'Figure5', ha='center', va='center', size=10)

plt.show()