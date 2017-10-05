#! /usr/bin/env python
# coding:utf-8
# Author qingniao
from __future__ import print_function

try:
    from pdb import set_trace
    from lib.base import Base
    from lib.data import Xssdata
    from logging  import getLogger
except ImportError as e:
    errmsg = e.message.split('named')[0]
    print(errmsg)
    exit()


class Action(Xssdata, Base):
    __author__ = 'qingniao'
    __doc__ = 'read file'
    __version__ = '1.0'

    def __init__(self, path, sep='\n'):
        self._debug = False
        try:
            with open(path) as f:
                if sep == '\n':
                    self._data = f.readlines()
                else:
                    self._data = f.read().split(sep)
        except IOError:
            self._data = None
            getLogger().error('{name}文件打开失败'.format(name=path))

    def get(self):
        if self._debug:
            set_trace()
        for char in self._data:
            yield char

    def debug(self, level):
        if self._debug:
            self._debug = False
            return False
        self._debug = True
        return True

