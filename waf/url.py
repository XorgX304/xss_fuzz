#! /usr/bin/env python
# coding:utf-8
# Author qingniao
from lib.waf import Waf, check_exp


class Url(Waf):
    __author__ = 'qingniao'
    __doc__ = 'check URL jump class waf'

    def __init__(self, conf, payload):
        super(Waf, Url).__init__(self)
        if conf.proxy:
            if isinstance(conf.proxy,dict):
                self.set_proxy(conf.proxy)
        self._name = 'url jump waf'
        self.payload = payload

    @check_exp
    def check(self, url, data=None, **kwargs):
        exp = self.payload.make_exploit()
        for payload in exp:
            if data:
                    ret = self.post_attack(url, data=data, payload=payload)
            else:
                    ret = self.get_attack(url, payload=payload)
        for _ in ret:
            if not _['response'].url == url:
                self.exp.append(_)


def get_waf(conf):
    return Url(conf)
