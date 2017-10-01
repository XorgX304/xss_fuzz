#! /usr/bin/env python
# coding:utf-8
# Author qingniao
from abc import ABCMeta, abstractmethod


class Xssdata:
    __metaclass__ = ABCMeta
    __author__ = 'qingniao'
    __doc__ = 'data base class'

    def __init__(self):
        self._name = 'data'
        self.version = '1.0'

    @abstractmethod
    def debug(self, level):
        pass

    @abstractmethod
    def get(self):
        """return data generator

        :return:generator
        """
        pass




