#! /usr/bin/env python
# coding:utf-8
# Author qingniao

from optparse import OptionParser
from lib.log import log_out
from logging import getLogger
import warnings

warnings.filterwarnings(action="ignore", message=".*was already imported", category=UserWarning)
warnings.filterwarnings(action="ignore", category=DeprecationWarning)

Log = getLogger()

try:
    from config import conf as conf
    from lib.version import banner
    from lib.error import ArgERROR
except ImportError as e:
    errmsg = e.message.split('named')[0]
    Log.error('{error}'.format(error=errmsg))
    exit()


def help():
    """args process

    :return:arg: args
    :return:args:optionparser object
    """
    args = OptionParser(version=conf.version)
    args.add_option('-m', '--mode', dest='mode', default='defult', help='xss fuzz test mode')
    args.add_option('-t', '--thread', dest='thread', help='thread num')
    args.add_option('-u', '--url', dest='url', help='fuzz test url')
    args.add_option('-d', '--data', dest='data', help='post data')
    args.add_option('-p', '--payload', dest='payload', default='tag', help='default \'"<tag>')
    args.add_option('-l', '--list', dest='list', help='list all payload')
    args.add_option('-c', '--cookies', dest='cookie', help='request cookie')
    (arg, _) = args.parse_args()
    return arg, args


def main():
    log_out(conf)
    print(banner(conf.Program_name))
    arg, args = help()

    if arg.list:
        for _ in conf.payloads.keys():
            print(_)
        exit()

    if not arg.url:
        args.print_help()
        exit()

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
    Log.info('test finish, result file {name}'.format(name=conf.output_file))


if __name__ == '__main__':
    #   try:
    Log = getLogger()
    main()
#    except ArgERROR as e:
#       Log.error(ArgERROR.errmsg)
#  except KeyboardInterrupt:
#     Log.error('user exit')
