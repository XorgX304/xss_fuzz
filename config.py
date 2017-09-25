#! /usr/bin/env python
# coding:utf-8
# Author qingniao
from waf import url, num
from payload import tag


class Config(dict):
    """config class
    >>> foo = Config()
    >>> foo.bar = 1
    >>> foo.bar
        1
    """

    def __init__(self):
        super(dict, Config).__init__(self)
        self.update(self.conf)

    def __getattr__(self, item):
        try:
            return self.__getitem__(item)
        except KeyError:
            raise AttributeError("unable to access item '%s'" % item)

    def __setattr__(self, key, value):
        return self.__setitem__(key, value)

    conf = {'Program_name': 'xssfuzz',

            'version': '1.0',

            'mode_list': {
                'Filter': url,
                'Intercept': num,
            },

            'payloads': {
                'tag': tag,
            },

            # url = 'www.test.com'

            # CRITICAL = 50 ERROR = 40 WARNING = 30
            # INFO = 20 DEBUG = 10 NOTSET = 0
            # look logging._levelNames
            'log_level': None,

            # Warning, please know what you are doing before changing here
            # If it is a string, Convert to file object
            'log_output': None,
            # log file  max size
            'log_maxsize': None,

            # Shutdown will not be output at the console
            'log_debug': True,

            'proxy': {
                # "http": "http://user:pass@10.10.1.10:3128/",
                # "https": "http://10.10.1.10:1080",
                # "http": "http://127.0.0.1:8118", # TOR
            },

            # thread num
            'threads_count': 16,
            }

conf = Config()
