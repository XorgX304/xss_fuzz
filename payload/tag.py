#! /usr/bin/env python
# coding:utf-8
# Author qingniao
from lib.payload import Payload
from data.tag import Tag


class NullTag(Payload):
    __doc__ = 'make tag'

    def __init__(self, conf=None):
        super(NullTag, self).__init__()
        self.name = 'tag'
        self.version = '1.0'
        self.exploit = '\'"><{tag}></{tagend}>'
        self.data = {'tag': Tag().get(),

                     }

    def make_exploit(self):
        for _ in self.data['tag']:
                yield self.exploit.format(tag=_, tagend=_)


def get_payload(conf=None):
    return NullTag(conf)




