# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 21:07:59 2018

@author: hashimoto
"""

import plot as plt
import numpy as np

x = np.arange(-10.0, 10.0, 0.1)
y = np.arange(-10.0, 10.0, 0.1)

#plt.show_2D_grahp("test", x, y, "xlabel", "ylabel", -9, 8, -7, 6, "r")

# 平均 50, 標準偏差 10 の正規乱数を1,000件生成
z = np.random.normal(50, 10, 1000)
# ヒストグラムを出力
#plt.show_histgram("Histgram Test", z, 10)


# 矢印（ベクトル）の始点
X = 0,1
Y = 0,1
# 矢印（ベクトル）の成分
U = 2,0.25
V = 1,0.5
plt.show_2D_vector("Vector", X, Y, U, V, "xlabel", "ylabel", -1, 3, -1, 3)
