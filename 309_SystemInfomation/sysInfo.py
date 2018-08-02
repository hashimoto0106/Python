# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 01:47:43 2018

@author: hashimoto
"""

import platform

# インタープリタ
print('Version      :' + platform.python_version())
print('Version tuple:' + str(platform.python_version_tuple()))
print('Compiler     :' + platform.python_compiler())
print('Build        :' + str(platform.python_build()))

# プラットフォーム
print('Normal       :' + platform.platform())
print('Aliased      :' + platform.platform(aliased=True))
print('Terse        :' + platform.platform(terse=True))

# オペレーティングシステムとハードウェアの情報
print('uname        :' + str(platform.uname()))
print('system       :' + platform.system())
print('node         :' + platform.node())
print('release      :' + platform.release())
print('version      :' + platform.version())
print('machine      :' + platform.machine())

# 実行可能なアーキテクチャ
print('interpreter:' + str(platform.architecture()))
print('/bin/ls    :' + str(platform.architecture('/bin/ls')))
