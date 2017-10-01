#! /usr/bin/env python
# coding:utf-8
# Author qingniao

from pdb import set_trace

from lib.base import Base
from lib.data import Xssdata


class Attribute(Xssdata, Base):
    __author__ = 'qingniao'
    __doc__ = 'return global attribute'
    __version__ = '1.0'

    def __init__(self):
        self._debug = False
        self._data = [
            'accesskey',
            'class',
            'contenteditable',
            'contextmenu',
            'data-*',
            'dir',
            'draggable',
            'dropzone',
            'hidden',
            'id',
            'lang',
            'spellcheck',
            'style',
            'tabindex',
            'title',
            'translate',
        ]

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


