#! /usr/bin/env python
# coding:utf-8
# Author qingniao
import base64
from HTMLParser import HTMLParser
from abc import ABCMeta, abstractmethod
from urllib import unquote, quote


class Payload:
    __metaclass__ = ABCMeta
    __author__ = 'qingniao'
    __doc__ = 'payload base class'

    def __init__(self):
        self.name = 'payload'
        self.version = '1.0'
        self.exploit = '{}'
        self.data = {}

    def get_exploit(self):
        return self.exploit

    def get_data(self):
        return self.data

    @abstractmethod
    def make_exploit(self):
        """Make exploit data

        :return:
        """
        pass

    @staticmethod
    def base64_decode(data):
        """Base64 decode
        >>>print base64_encode('eHNZ')
            'xss'
        :param data: base64 data
        :return: data
        :rtype: str
        """
        return base64.b64decode(data)

    @staticmethod
    def base64_encode(data):
        """ Base64 encode
        >>>print base64_encode('xss')
            'eHNZ'

        :rtype: str
        :param data: str data
        :return: base64 data
        """
        return base64.b64encode(data)

    @staticmethod
    def url_encode(data):
        """Url encode
        >>>print url_encode('1 2&')
            '1%202%26'

        :rtype str
        :param data:
        :return:url encode data
        """
        return quote(data)

    @staticmethod
    def url_decode(data):
        """Url encode
        >>>print url_decode('1%202%26')
            '1 2&'
        :rtype str
        :param data:
        :return:url decode str
        """
        return unquote(data)

    @staticmethod
    def html_decode(data):
        """Url encode
        >>>print html_decode('&lt')
            '<'
        :rtype str
        :param data:html encode data
        :return:url decode str
        """
        _ = HTMLParser()
        return _.unescape(data)




