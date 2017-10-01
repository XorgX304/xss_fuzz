#! /usr/bin/env python
# coding:utf-8
# Author qingniao
from pdb import set_trace

from lib.base import Base
from lib.data import Xssdata


class Char(Xssdata, Base):
    __author__ = 'qingniao'
    __doc__ = 'return Special char'
    __version__ = '1.0'

    def __init__(self):
        self._debug = False
        self._char = [chr(_) for _ in range(1, 48) + range(59, 65) + range(91, 97) + range(123, 127)]

    def get(self):
        if self._debug:
            set_trace()
        for char in self._char:
            yield char

    def debug(self, level):
        if self._debug:
            self._debug = False
            return False
        self._debug = True
        return True


