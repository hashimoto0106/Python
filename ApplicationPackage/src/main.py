# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 22:18:02 2020

@author:sample
"""

import os
import time
import config
import logger
import database
# import rsyslog
# import syslog
import help
import console
import line
import function
import parameter
import translation
from tqdm import tqdm
from datetime import datetime


def proc():
    print(parameter.PARAMETER1)
    print(parameter.PARAMETER2)
    function.get_fruit_price(1, 0)
    for i in tqdm(range(10)):
        time.sleep(0.02)


if __name__ == "__main__":

    logger.app_logger.info('Application Start')
    print(console.Fore.RED + "Red")
    print(console.Color.RED + "BLACK" + console.Color.END)
    # rsyslog.open()
    # rsyslog.logging(syslog.LOG_ALERT, 'Application started')
    now = datetime.now()
    start_time = time.time()
    
    os.system('cls')  # コンソールクリア
    # database.create_table()  # テーブル生成
    logger.logging_environment()  # 実行環境ログ
    config.logging_paramter()  # Parameter読み込み

    translation.init()
    print(_('*****************************This is sample message.'))
    print('This string isn\'t translated.')
    
    proc()

    # line.send_message("Application End")
    proc_time = (time.time()-start_time)
    database.insert(now, proc_time)  # データベース追加
    logger.app_logger.info('Application End(%.6lf[sec])', proc_time)
    # rsyslog.logging(syslog.LOG_ALERT, 'Application End')
    # rsyslog.close()
