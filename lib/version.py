#! /usr/bin/env python
# coding:utf-8
# Author qingniao
import pyfiglet as pyfiglet


def banner(char):
    """char draw

    :param char:
    :return:char draw
    """
    text = pyfiglet.Figlet(font='slant')
    return text.renderText(char)


