# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 18:05:19 2019

@author: PC
"""

import Vektor
import numpy as np
import matplotlib.pyplot as plt


def vector3D():
    e1 = np.array([1, 0, 0])
    e2 = np.array([0, 5, 0])

    # 外積
    cross1 = np.cross(e1, e2)
    print(cross1)
    cross2 = np.cross(e2, e1)
    print(cross2)

    # 3Dベクトル可視化
    loc = [0, 0, 0]  # 始点を設定
    fig = plt.figure(figsize = (6, 6))  # FigureとAxes
    ax = fig.add_subplot(111, projection='3d')
    Vektor.coordinate_3d(ax, '3D Vector Graph', [-5, 5], [-5, 5], [-5, 5], grid = True)  # 座標設定
    Vektor.plot_3D(ax, "vector1", loc, e1, "red")
    Vektor.plot_3D(ax, "vector1", loc, e2, "blue")
    Vektor.plot_3D(ax, "vector1", loc, cross1, "black")
    Vektor.plot_3D(ax, "vector1", loc, cross2, "yellow")


def vector2D():
    v = np.array([2, 1])
    w = np.array([-1, 1])

    # 外積
    cross1 = np.cross(e1, e2)
    print(cross1)
    cross2 = np.cross(e2, e1)
    print(cross2)

    # 2Dベクトル可視化
    loc = [0, 0]  # 始点を設定
    fig = plt.figure(figsize = (6, 6))  # FigureとAxes
    ax = fig.add_subplot(111)
    Vektor.coordinate_2d(ax, '2D Vector Graph', [-5, 5], [-5, 5])  # 座標設定
    Vektor.plot_2D(ax, "vector1", loc, v, "red")  # [0,0]を始点にv1を描画
    Vektor.plot_2D(ax, "vector2", v, w, "blue")  # v1の終点を始点にｖ2を描画
    Vektor.plot_2D(ax, "vector3", [0, 0], v + w, "green")  # [0,0]を始点にv+wを描画


def main():
    vector3D()
    vector2D()


if __name__ == '__main__':
    main()
