# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 17:27:11 2019

@author: PC
"""

import numpy as np
import matplotlib.pyplot as plt
import Matrix


def test_3d():
    a = np.array((1,1,0))  # 元の行列
    
    # 回転行列生成
    R = Matrix.rotate_x_deg( 45.0 )  # X軸
    R = Matrix.rotate_y_deg( 45.0 )  # Y軸
    R = Matrix.rotate_z_deg( 45.0 )  # Z軸
    
    # 並進行列生成
#    R = Matrix.L( 5.0 )  # X軸
    
    b = np.dot(R,a)  # 回転後のベクトルを計算
    b = np.array(b,dtype=np.uint8)  # 整数型に変換
    print("a=" + str(a))
    print("R=" + str(R))
    print("b=" + str(b[0]))

    # 3Dベクトル可視化
    loc = [0, 0, 0]  # 始点を設定
    fig = plt.figure(figsize = (6, 6))  # FigureとAxes
    ax = fig.add_subplot(111, projection='3d')
    Matrix.coordinate_3d(ax, [-2, 2], [-2, 2], [-2, 2], grid = True)  # 3D座標を設定
    Matrix.visual_vector_3d(ax, loc, a, "red")
    Matrix.visual_vector_3d(ax, loc, b[0], "blue")


def test_2d():
    v = np.array([2, 1])
    w = np.array([-1, 1])

    # 可視化
    loc = [0, 0]  # 始点を設定
    fig = plt.figure(figsize = (6, 6))  # FigureとAxes
    ax = fig.add_subplot(111)
    Matrix.init(ax, '2D Matric', 10, 10)  # 座標設定

    Matrix.plot_point(ax, 0, 0, '.', "black")
    Matrix.plot_point(ax, v[0], w[0], '.', "red")
    Matrix.plot_point(ax, 6, 5, '.', "blue")
    Matrix.plot_point(ax, 8, -2, '.', "green")


def main():
    test_3d()
    test_2d()


if __name__ == '__main__':
    main()

