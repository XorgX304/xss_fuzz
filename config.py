#! /usr/bin/env python
# coding:utf-8
# Author qingniao
from waf import url, num


class Config:
    def __init__(self):
        pass

    Program_name = 'xssfuzz'

    mode_list = {
        'Filter': url,
        'Intercept': num,
    }

    # CRITICAL = 50 ERROR = 40 WARNING = 30
    # INFO = 20 DEBUG = 10 NOTSET = 0
    # look logging._levelNames
    log_level = None

    # Warning, please know what you are doing before changing here
    # If it is a string, Convert to file object
    log_output = None
    # log file  max size
    log_maxsize = None

    # Shutdown will not be output at the console
    log_debug = True

    proxy = None


