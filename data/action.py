#! /usr/bin/env python
# coding:utf-8
# Author qingniao

from pdb import set_trace
from lib.base import Base
from lib.data import Xssdata


class Action(Xssdata, Base):
    __author__ = 'qingniao'
    __doc__ = 'return action attribute'
    __version__ = '1.0'

    def __init__(self):
        self._debug = False
        self._data = [
            'onafterprint',
            'onbeforeprint',
            'onbeforeunload',
            'onerror',
            'onhaschange',
            'onload',
            'onmessage',
            'onoffline',
            'ononline',
            'onpagehide',
            'onpageshow',
            'onpopstate',
            'onredo',
            'onresize',
            'onstorage',
            'onundo',
            'onunload',
            'onblur',
            'onchange',
            'oncontextmenu',
            'onfocus',
            'onformchange',
            'onforminput',
            'oninput',
            'oninvalid',
            'onreset',
            'onselect',
            'onsubmit',
            'onkeydown',
            'onkeypress',
            'onkeyup',
            'onclick',
            'ondblclick',
            'ondrag',
            'ondragend',
            'ondragenter',
            'ondragleave',
            'ondragover',
            'ondragstart',
            'ondrop',
            'onmousedown',
            'onmousemove',
            'onmouseout',
            'onmouseover',
            'onmouseup',
            'onmousewheel',
            'onscroll',
            'onabort',
            'oncanplay',
            'oncanplaythrough',
            'ondurationchange',
            'onemptied',
            'onended',
            'onerror',
            'onloadeddata',
            'onloadedmetadata',
            'onloadstart',
            'onpause',
            'onplay',
            'onplaying',
            'onprogress',
            'onratechange',
            'onreadystatechange',
            'onseeked',
            'onseeking',
            'onstalled',
            'onsuspend',
            'ontimeupdate',
            'onvolumechange',
            'onwaiting',
        ]

    def get(self):
        if self._debug:
            set_trace()
        for char in self._data:
            yield char

    def debug(self, level):
        if self._debug:
            self._debug = False
            return False
        self._debug = True
        return True


