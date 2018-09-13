# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 22:25:05 2018

@author: hashimoto
"""

import numpy as np
import pandas as pd


def main():
    # CSVファイル読み込み
    capdata = pd.read_csv(filepath_or_buffer="wireshark_capture_log.csv", encoding="ms932", sep=",")

    # データ抽出
    time_delta = []
    for no in capdata["frame.number"]:
        if capdata.iat[no-1, 5] == 305:
#            print(capdata.iat[no-1, 1])
            time_delta.append(capdata.iat[no-1, 1])

    # 合計
    sum = np.sum(time_delta)
    print(u"合計"+str(sum))

    # 平均
    mean = np.mean(time_delta)
    print(u"平均"+str(mean))

    # 中央
    median = np.median(time_delta)
    print(u"中央"+str(median))

    # 最頻
#    mode = np.mode(capdata["frame.time_delta"])
#    print(u"最頻値"+str(mode))

    # 最小
    min = np.min(time_delta)
    print(u"最小"+str(min))

    # 最大
    max = np.max(time_delta)
    print(u"最大"+str(max))

    # 標準偏差
    std = np.std(time_delta)
    print(u"標準偏差："+str(std))

    # 分散
    var = np.var(time_delta)
    print(u"分散："+str(var))


if __name__ == '__main__':
    main()
