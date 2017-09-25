#! /usr/bin/env python
# coding:utf-8
# Author qingniao
from __future__ import print_function

import pdb
from abc import ABCMeta, abstractmethod
from requests.api import get, post
from requests.exceptions import HTTPError, ConnectionError, RequestException, ConnectTimeout
from log import Log
from threading import Lock
from Queue import Queue


class Waf:
    __metaclass__ = ABCMeta
    __author__ = 'qingniao'
    __doc__ = 'check waf base class'

    def __init__(self):
        self._name = 'waf'
        self._version = '1.0'
        self.payload = []
        self._headers = {
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0'
        }
        self.exp = []
        self._proxies = {}
        self.lock = Lock()
        self.quest = Queue()
        self.ret = Queue()
        self.cookies = None

    @abstractmethod
    def check(self, url, **kwargs):
        pass

    def get_name(self):
        return self._name

    def get_payload(self):
        return self.payload

    def add_header(self, key, value):
        self._headers[key] = value

    def delete_header(self, key):
        self._headers.pop(key)

    def url_get(self, url, **kwargs):
        """url get method

        :rtype: object:requests.Response
        """
        try:
            Log.info('get url {url}'.format(url=url))
            return get(url=url,proxies=self._proxies, cookies=self.cookies, **kwargs)
        except HTTPError:
            Log.error('{url} http error'.format(url=url))
        except ConnectTimeout:
            Log.error('{url} connect timeout'.format(url=url))
        except ConnectionError:
            Log.error('{url} connect fail'.format(url=url))
        except RequestException:
            Log.error('{url} request error'.format(url=url))

    def url_post(self, url, data=None, json=None, **kwargs):
        """url post method

        :param kwargs:
        :rtype: object:requests.Response
        """
        try:
            Log.info(
                'post url {url} data {data} '.format(url=url, data=data, cookies=self.cookies, proxies=self._proxies))
            return post(url=url, data=data, json=json, **kwargs)
        except HTTPError:
            Log.error('{url} http error'.format(url=url))
        except ConnectTimeout:
            Log.error('{url} connect timeout'.format(url=url))
        except ConnectionError:
            Log.error('{url} connect fail'.format(url=url))
        except RequestException:
            Log.error('{url} request error'.format(url=url))

    def set_payload(self, payload):
        self.payload = payload
        Log.info('set payload success')

    def set_proxy(self, proxy):
        self._proxies.update(proxy)
        Log.info('set proxy success')

    def post_attack(self, url, data, **kwargs):
        """post attack api
        Lock is already in use
        :param url: attack url
        :param data: post data
        """

        ret = []
        args = data.split('&')
        for payload in self.payload:
            for x in range(len(args)):
                _ = args[:]
                _[x] = _[x] + payload
                req_data = '&'.join(_)
                response = self.url_post(url=url, data=req_data, headers=self._headers,**kwargs
                                         )
                try:
                    if self.lock.acquire():
                        ret.append({'payload': payload,
                                    'arg': args[x],
                                    'response': response})
                        self.ret.put(ret)
                finally:
                    self.lock.release()

    def get_attack(self, url, **kwargs):
        """get attack api
        Lock is already in use
        :param url: attack url
        """
        ret = []
        if len(url.split('?')) == 1:
            print('url not attack args. e.g.http://test.com?id=1')
            return
        path = url.split('?')[0]
        args = url.split('?')[1].split('&')

        for payload in self.payload:

            for _ in range(len(args)):
                __ = args[:]
                __[_] = __[_] + payload
                get_url = path + '?' + '&'.join(__)
                response = self.url_get(get_url, headers=self._headers, **kwargs)

                try:
                    self.lock.acquire()
                    ret.append({'payload': payload, 'arg': args[_],
                                'response': response})
                    self.ret.put(ret)
                finally:
                    self.lock.release()

    def lock(self, func, *args, **kwargs):
        try:
            if self.lock.acquire():
                func(*args, **kwargs)
        finally:
            self.lock.release()


def check_exp(func):
    def _func(*args, **kwargs):
        if not args[0].payload:
            print('not, it\'s payload is None.'
                  'Please make sure you\'re not wrong.')
            return None
        else:
            return func(*args, **kwargs)

    return _func
