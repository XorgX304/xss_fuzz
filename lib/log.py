#! /usr/bin/env python
# coding:utf-8
# Author qingniao
from logging.handlers import RotatingFileHandler
from sys import stderr
from logging import getLogger, ERROR, StreamHandler

Log = getLogger()
Log.setLevel(ERROR)
error = StreamHandler(stderr)
Log.addHandler(error)


def log_out(conf, log):
    """set log output
    set log file and level
    :return: None
    """
    try:
        if conf.log_level:
            log.setLevel(conf.log_level)
    except Exception as e:
        log.error(e)
        log.error('level keep is error')
    try:
        if conf.log_output:
            out = conf.log_output
            if isinstance(conf.log_output, str):
                out = RotatingFileHandler(conf.log_output, conf.log_maxsize)
            # Make sure you enter an Output object,I can't make sure this object is correct.
            # Modify here, I believe you are capable
            log.addHandler(out)
        if not conf.log_debug:
            log.removeHandler(stderr)
    except Exception as e:

        log.error(e)
        log.error('log out keep is stderr')
