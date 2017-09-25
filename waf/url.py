#! /usr/bin/env python
# coding:utf-8
# Author qingniao
from lib.waf import Waf, check_exp
from threading import Thread
from urlparse import urlparse

class Url(Waf):
    __author__ = 'qingniao'
    __doc__ = 'check URL jump class waf'

    def __init__(self, conf, payload):
        super(Url, self).__init__()
        if conf.proxy:
            if isinstance(conf.proxy, dict):
                self.set_proxy(conf.proxy)
        self._name = 'url jump waf'
        self.payload = payload.make_exploit()
        self.thread_num = conf.thread_num

    @check_exp
    def check(self, url, data=None, **kwargs):
        for _ in range(self.thread_num):
            if data:
                self.quest.put(
                 Thread(target=self.post_attack, args=(url), kwargs={'data': data,
                                                           }))
            else:
                self.quest.put(Thread(target=self.get_attack, kwargs={'url': url}))

        while not self.quest.empty():
            thread = self.quest.get()
            thread.start()
            thread.join()
        while not self.ret.empty():
            url = urlparse(url).netloc
            tmp = self.ret.get()
            for _ in tmp:
                if not urlparse(_['response'].url).netloc == url:
                    self.exp.append(_)

def get_waf(conf, payload):
    return Url(conf, payload)
