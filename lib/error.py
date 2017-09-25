#! /usr/bin/env python
# coding:utf-8
# Author qingniao


class ArgERROR(Exception):
    def __init__(self, errmsg):
        self.errmsg = errmsg
