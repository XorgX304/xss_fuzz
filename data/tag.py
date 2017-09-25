#! /usr/bin/env python
# coding:utf-8
# Author qingniao
from pdb import set_trace

from lib.base import Base
from lib.data import Xssdata


class Tag(Xssdata, Base):
    __author__ = 'qingniao'
    __doc__ = 'return tag name url:http://www.w3school.com.cn/tags/index.asp'
    __version__ = '1.0'

    def __init__(self):
        self._debug = False
        self._tag_list = [
            'a',
            'script'
            'img',
            'body',
            'meta',
            'h1',
            'ul',
            'abbr',
            'b',
            'applet',
            'address',
            'area',
            'acronym',
            'article',
            'aside',
            'audio',
            'base',
            'basefont',
            'bdi',
            'bdo',
            'big',
            'blockquote',
            'br',
            'button',
            'canvas',
            'caption',
            'center',
            'cite',
            'cite',
            'code',
            'col',
            'colgroup',
            'command',
            'datalist',
            'dd',
            'del',
            'details',
            'dir',
            'div',
            'dfn',
            'dialog',
            'dl',
            'dt',
            'em',
            'embed',
            'fieldset',
            'figcaption',
            'figure',
            'font',
            'footer',
            'form',
            'frame',
            'frameset',
            'head',
            'header',
            'hr',
            'html',
            'i',
            'iframe',
            'input',
            'ins',
            'isindex',
            'kbd',
            'keygen',
            'label',
            'legend',
            'li',
            'link',
            'map',
            'mark',
            'menu',
            'mentitem',
            'meter',
            'nav',
            'noframes',
            'noscript',
            'object',
            'ol',
            'optgroup',
            'option',
            'output',
            'p',
            'param',
            'pre',
            'progress',
            'q',
            'rp',
            'rt',
            'ruby',
            's',
            'samp',
            'section',
            'select',
            'smali',
            'source',
            'span',
            'strike',
            'strong',
            'style',
            'sub',
            'summary',
            'sup',
            'table',
            'tbody',
            'td',
            'textarea',
            'tfoot',
            'th',
            'thead',
            'time',
            'title',
            'tr',
            'track',
            'tt',
            'u',
            'ul',
            'var',
            'video',
            'wbr',
            'xmp'
        ]

    def debug(self, level):
        self._debug = True

    def get(self):
        if self._debug:
            set_trace()
        for tag in self._tag_list:
            yield tag

    def __str__(self):
        return self._tag_list.pop()





