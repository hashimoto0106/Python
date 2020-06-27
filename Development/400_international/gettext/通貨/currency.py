# -*- coding: utf-8 -*-
"""
Created on Sat May 23 22:02:34 2020

@author: PC
"""

import locale


locale.setlocale(locale.LC_ALL, '')                 # 全ロケール情報をユーザー環境のデフォルトに設定する場合
locale.setlocale(locale.LC_ALL, 'ja_JP.UTF-8')      # 任意のロケール情報に設定する場合1
locale.setlocale(locale.LC_ALL, ('ja_JP', 'UTF-8')) # 任意のロケール情報に設定する場合2

print(locale.currency(12345))
print(locale.currency(12345, symbol=False))
print(locale.currency(12345, grouping=True))
print(locale.currency(12345, grouping=True, international=True))
