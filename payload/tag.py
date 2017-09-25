#! /usr/bin/env python
# coding:utf-8
# Author qingniao
from lib.payload import Payload
from data.tag import Tag


class NullTag(Payload):
    __doc__ = 'make tag'

    def __init__(self):
        super(Payload, self).__init__()
        self.name = 'tag'
        self.version = '1.0'
        self.exploit = '<{tag}></{tagend}>'
        self.data = {'tag': Tag(),
                     'tagend': Tag()
                     }

    def make_exploit(self):
        return self.exploit.format(tag=self.data['tag'], tagend=self.data['tagend'])


