#! /usr/bin/env python
# coding:utf-8
# Author qingniao
from __future__ import print_function

try:
    from lib.payload import Payload
except ImportError as e:
    errmsg = e.message.split('named')[0]
    print(errmsg)
    exit()


class Mark(Payload):
    __doc__ = 'make tag'

    def __init__(self, conf=None, data=None):
        super(Mark, self).__init__()
        self.name = 'mark'
        self.version = '1.0'
        self.mark = conf.mark
        self.exploit = self.mark*6+"{exp}"+self.mark*6
        self.data = {
            'exp':data
        }
        self.re = "{head}[^{mark}]*{end}".format(head=self.mark*6,mark=self.mark,end=self.mark*6)

    def make_exploit(self):
        for _ in self.data['exp'].get():
            yield self.exploit.format(exp=_)


def get_payload(conf=None, data=None):
    return Mark(conf, data)