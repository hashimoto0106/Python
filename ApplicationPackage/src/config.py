# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 15:53:21 2020

@author: sample
"""

import configparser


INI_FILE = '../parameter/config.ini'

inifile = configparser.ConfigParser()
inifile.read(INI_FILE, 'UTF-8')

# パラメータ取得
config_log = inifile.get('config', 'log')
syslog_facility = inifile.get('syslog', 'facility')
syslog_option = inifile.get('syslog', 'option')
database = inifile.get('database', 'database')
line_notify_api = inifile.get('line', 'notify_api')
line_notify_token = inifile.get('line', 'notify_token')
translation_language = inifile.get('translation', 'language')
translation_dictionary_dir = inifile.get('translation', 'dictionary_dir')
translation_dictionary_file = inifile.get('translation', 'dictionary_file')


def init():
    print()


def logging_paramter():
    import logger
    logger.app_logger.debug("config_log:%s", config_log)
    logger.app_logger.debug("syslog_facility:%s", syslog_facility)
    logger.app_logger.debug("syslog_option:%s", syslog_option)
    logger.app_logger.debug("database:%s", database)
    logger.app_logger.debug("line_notify_api:%s", line_notify_api)
    logger.app_logger.debug("line_notify_token:%s", line_notify_token)
    logger.app_logger.debug("translation_language:%s", translation_language)
    logger.app_logger.debug("translation_dictionary_dir:%s", translation_dictionary_dir)
    logger.app_logger.debug("translation_dictionary_file:%s", translation_dictionary_file)
