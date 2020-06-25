# -*- coding: utf-8 -*-
"""
Created on Sat May 23 22:07:38 2020

@author: PC
"""

#from fabric.colors import green
from colorama import Fore, Back, Style

class Color:
    BLACK     = '\033[30m'
    RED       = '\033[31m'
    GREEN     = '\033[32m'
    YELLOW    = '\033[33m'
    BLUE      = '\033[34m'
    PURPLE    = '\033[35m'
    CYAN      = '\033[36m'
    WHITE     = '\033[37m'
    END       = '\033[0m'
    BOLD      = '\038[1m'
    UNDERLINE = '\033[4m'
    ACCENT = '\033[01m'  # 強調
    FLASH = '\033[05m'  # 点滅
    INVISIBLE = '\033[08m'
    REVERCE   = '\033[07m'  # 反転
    RED_FLASH = '\033[05;41m' #赤背景+点滅
