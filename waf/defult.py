#! /usr/bin/env python
# coding:utf-8
# Author qingniao
from lib.waf import Waf, check_exp
from threading import Thread
from json import dumps


class Defult(Waf):
    __author__ = 'qingniao'
    __doc__ = 'defult waf'

    def __init__(self, conf, payload):
        super(Defult, self).__init__()
        if conf.proxy:
            if isinstance(conf.proxy, dict):
                self.set_proxy(conf.proxy)
        self._name = 'url jump waf'
        self.payload = payload.make_exploit()
        self.thread_num = conf.thread_num
        self.cookies = conf.cookie
        self.white_num = conf.white_num
        self.black_num = conf.black_num
        self.waf_str = conf.waf_str
        self.output_file = conf.output_file


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
            tmp = self.ret.get()
            for _ in tmp:
                if _['response'].status_code in self.white_num:
                    self.exp.append(_)
                    continue
                if not _['response'].status_code in self.black_num:
                    self.exp.append(_)
                    continue
                if self.waf_str:
                    if self.waf_str in _['response'].content:
                        continue
                    self.exp.append(_)
        for _ in len(self.exp):
            with open(self.output_file) as f:
                f.write(dumps(self.exp[_]))


def get_waf(conf, payload):
    return Defult(conf, payload)


