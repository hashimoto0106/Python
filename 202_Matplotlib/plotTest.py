# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def main():
    # xの値を生成
    x = np.arange(-3.14, 3.14, 0.25)
    # 高さを計算
    sin = np.sin(x) # sin(x)の計算
    cos = np.cos(x) # cos(x)の計算
    tan = np.tan(x) # tan(x)の計算
    exp = np.exp(x) # 指数関数の計算
    log = np.log(x) # 対数関数の計算
    # グラフ表示
    plt.plot(x, sin,"-o",lw=2,alpha=0.7,label="sin(x)")
    plt.plot(x, cos,"-o",lw=2,alpha=0.7,label="cos(x)")
    plt.plot(x, tan,"-o",lw=2,alpha=0.7,label="tan(x)")
    plt.plot(x, exp,"-o",lw=2,alpha=0.7,label="exp(x)")
    plt.plot(x, log,"-o",lw=2,alpha=0.7,label="log(x)")
    fn = "Times New Roman"                      # フォント
    plt.tick_params(labelsize=15)               # 軸目盛のフォントサイズ
    plt.xlabel("$x$", fontsize=30, fontname=fn) # x軸のラベル
    plt.ylabel("$y$", fontsize=30, fontname=fn) # y軸のラベル
    plt.xlim([-4, 4])                           # x軸の範囲
    plt.ylim([-4, 4])                           # y軸の範囲
    plt.grid()                                  # グリッドの表示
    plt.legend(fontsize=13)                     # 凡例の表示
    plt.show()                                  # グラフの描画

if __name__ == '__main__':
    main()