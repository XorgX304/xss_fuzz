#! /usr/bin/env python
# coding:utf-8
# Author qingniao
from threading import Thread

from lib.waf import Waf
from re import compile, search
from difflib import Differ


class Filter(Waf):
    def __init__(self, conf, payload):
        super(Filter, self).__init__()
        self.payload = payload.make_exploit()
        self.thread_num = conf.thread_num
        self.cookies = conf.cookie
        self.data = conf.data

    def check(self, url,data=None, **kwargs):
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
        re = compile(self.payload.re)
        diff = Differ()
        while not self.ret.empty():
            tmp = self.ret.get()
            for _ in tmp:
                match = re.match(_['response'].content)
                if match:
                    self.exp.append(''.join('\n', diff.compare(match.group().splitlines(), _['payload'])))



