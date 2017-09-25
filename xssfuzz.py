#! /usr/bin/env python
# coding:utf-8
# Author qingniao

from optparse import OptionParser
from lib.log import log_out, Log
import warnings

warnings.filterwarnings(action="ignore", message=".*was already imported", category=UserWarning)
warnings.filterwarnings(action="ignore", category=DeprecationWarning)

try:

    from config import conf as conf
    from lib.version import banner
    from lib.error import ArgERROR
except ImportError as e:
    errmsg = e.message.split('named')[1]
    Log.error('{error}'.format(error=errmsg))
    exit()


def help():
    """args process

    :return:arg: args
    :return:args:optionparser object
    """
    args = OptionParser(version=conf.version)
    args.add_option('-m', '--mode', dest='mode', default='Filter', help='xss fuzz test mode')
    args.add_option('-t', '--thread', dest='thread', help='thread num')
    args.add_option('-u', '--url', dest='url', help='fuzz test url')
    args.add_option('-d', '--data', dest='data', help='post data')
    args.add_option('-p', '--payload', dest='payload', default='tag', help='default \'"<tag>')
    args.add_option('-l', '--list', dest='list', help='list all payload')
    (arg, _) = args.parse_args()
    return arg, args


def main():
    log_out(conf, Log)
    print(banner(conf.Program_name))
    arg, args = help()

    if arg.list:
        for _ in conf.payloads.keys():
            print(_)

    if not arg.url:
        args.print_help()

    conf.update(arg.__dict__)

    try:
        attack = conf.mode_list[conf.mode]
    except KeyError:
        errmsg = 'mode {name} is not exist'.format(name=conf)
        raise ArgERROR(errmsg)

    Log.info('attack mode {name}'.format(name=arg.mode))

    try:
        data = conf.payloads[conf.payload]
    except KeyError as e:
        errmsg = 'payload {name} is not exist'.format(name=e)
        raise ArgERROR(message=errmsg)
    payload = data.get_payload(conf)
    fuzz = attack.get_waf(conf, payload)
    fuzz.check(conf.url)


if __name__ == '__main__':
    try:
        main()
    except ArgERROR as e:
        Log.error(ArgERROR.errmsg)
    except KeyboardInterrupt:
        Log.error('user exit')
