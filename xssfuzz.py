#! /usr/bin/env python
# coding:utf-8
# Author qingniao

from optparse import OptionParser
from lib.log import Log, log_out

try:
    from config import Config as conf
    from lib.version import banner
except ImportError as e:
    errmsg = e.message.split('named')[1]
    Log.error('{error}'.format(error=errmsg))
    exit()


def help():
    """args process

    :return:arg: optionparser object
    :return:args: args
    """
    args = OptionParser(version=1.0)
    args.add_option('-m', '--mode', action='mode', help='xss fuzz test modu')
    args.add_option('-t', '--thread', action='thread', help='thread num')
    args.add_option('-u', '--url', action='url', help='fuzz test url')
    args.add_option('-d', '--data', action='data', help='post data')
    args.add_option('-c', '--config', action='config', help='config file')
    (arg, _) = args.parse_args()
    return arg, args


def main():
    log_out(conf, log)
    print(banner(conf.Program_name))
    arg, args = help()
    if not arg.url:
        args.print_help()
    if not arg.mode:
        arg.mode == 'Filter'

    try:
        if not conf.modelist[arg.mode] is None:
            attack = conf.modelist[arg.mode]
    except KeyError:
        Log.error('mode {name} is not exist'.format(name=arg.mode))
    Log.info('attack mode {name}'.format(name=arg.mode))
    fuzz = attack.get_waf(conf)


if __name__ == '__main__':
    main()
