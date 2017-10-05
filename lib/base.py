#! /usr/bin/env python
# coding:utf-8
# Author qingniao


class Base:
    __author__ = 'qingniao'
    __doc__ = 'base class'

    def __init__(self, name, version):
        self._name = name
        self.version = version

    def getname(self):
        return self.name

    def getversion(self):
        return self.version or 1.0
