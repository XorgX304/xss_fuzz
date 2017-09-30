#! /usr/bin/env python
# coding:utf-8
# Author qingniao
from logging.handlers import RotatingFileHandler
from sys import stderr
from logging import getLogger, ERROR, StreamHandler
from os.path import join, isdir

from os import mkdir


def log_out(conf):
    """set log output
    set log file and level
    :return: None
    """
    try:
        if not conf.log:
            return False
        Log = getLogger()
        if isinstance(conf.log_file, str):
            if not isdir(conf.log_path):
                mkdir(conf.log_path)
            path = join(conf.log_path, conf.file)
            f = RotatingFileHandler(path, mode='a+', maxBytes=conf.log_maxsize)
            Log.addHandler(f)
        else:
            Log.addHandler(conf.log_output)

        if conf.log_level:
            Log.setLevel(conf.log_level)
        else:
            Log.setLevel(ERROR)
    except IOError as e:
        Log.error('Log file error, No such file or directory')
