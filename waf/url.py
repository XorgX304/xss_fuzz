#! /usr/bin/env python
# coding:utf-8
# Author qingniao
from lib.waf import Waf, check_exp


class Url(Waf):
    __author__ = 'qingniao'
    __doc__ = 'check URL jump class waf'

    def __init__(self, conf):
        if isinstance(conf.proxy,dict):
            self.set_proxy(conf.proxy)
        self._name = 'url jump waf'

    @check_exp
    def check(self, url, data=None, **kwargs):
        payload = self.payload
        if data:
                    ret = self.post_attack(url, data=data, payload=payload)
        else:
                    ret = self.get_attack(url, payload=payload)
        for _ in ret:
            if not _['response'].url == url:
                self.exp.append(_)


def get_waf(conf):
    return Url(conf)
