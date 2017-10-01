#! /usr/bin/env python
# coding:utf-8
# Author qingniao
from json import dumps

from testtools import TestCase
from data import tag
from collections import Iterable
from lib.log import log_out
from config import conf
from logging import  getLogger
from sys import stdout
from waf.defult import Defult
from payload.tag import NullTag


class TestData(TestCase):
    def setUp(self):
        super(TestData, self).setUp()
        self.data = tag.Tag()

    def test_data(self):
        self.assertEqual(self.data.debug(None), True, message='data debug mode test error')
        self.assertEqual(self.data.debug(None), False, message='data debug mode test error')
        self.assertIsNotNone(self.data.get(), message='data class test error')
        self.assertIsInstance(self.data.get(), Iterable, msg='data class get data error .it not is a generator')


class TestLog(TestCase):
    def setUp(self):
        super(TestLog,self).setUp()

    def test_log(self):
        log_out(conf)
        log = getLogger()
        if not conf.log:
            self.assertIsNone(log.handlers, message='unexpected log output')
        elif conf.log_debug:
            self.assertIn(stdout, log.handlers, message='log console output error')


class TestWaf(TestCase):
    def setUp(self):
        super(TestWaf,self).setUp()
        Log = getLogger()
        Log.setLevel(50)

    def test_waf(self):
        waf = Defult(conf, NullTag())
        waf.check('http://www.baidu.com/?id=1')
        self.assertIsNotNone(waf.exp, message='error, This is an impossible goal. but it have a result.')
        print dumps(waf.exp[0])



