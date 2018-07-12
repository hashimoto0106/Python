import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['lines.linewidth'] = 10    #線幅10points
mpl.rcParams['lines.linestyle'] = '--'  #線種 破線
mpl.rc('lines', linewidth=10, linestyle='--')

t = np.arange(0, 2*np.pi, 0.1)
plt.figure(1)
plt.plot(t, np.sin(t))
plt.show()

#Run Command設定
print('--------Run Command設定--------')
print(mpl.rcParams)

#設定ファイル(matplotlibrc)
print('--------設定ファイル(matplotlibrc)--------')
print(mpl.get_configdir())
print(mpl.matplotlib_fname())

#スタイルシート
print('--------Style Seet--------')
print(plt.style.available)
