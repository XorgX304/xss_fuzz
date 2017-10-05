#! /usr/bin/env python
# coding:utf-8
# Author qingniao


from logging import getLogger
import warnings

warnings.filterwarnings(action="ignore", message=".*was already imported", category=UserWarning)
warnings.filterwarnings(action="ignore", category=DeprecationWarning)

try:
    from config import conf as conf
    from lib.version import banner
    from lib.error import ArgERROR
    from lib.log import log_out
    from lib.cmdline import cmdLineParser
    import config
except ImportError as e:
    errmsg = e.message.split('named')[0]
    print errmsg
    exit()


def main():
    log_out(conf)
    print(banner(conf.Program_name))
    args = cmdLineParser()
    conf.update(cmdLineParser().parse_args()[0].__dict__)
    if conf.version:
        print conf.version
        exit()
    if conf.url is None:
        args.print_help()
        exit()

    try:
        attack = conf.mode_list[conf.mode]
    except KeyError:
        errmsg = 'mode {name} is not exist'.format(name=conf)
        raise ArgERROR(errmsg)

    Log.info('attack mode {name}'.format(name=conf.mode))

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
    try:
        Log = getLogger()
        main()
    except KeyboardInterrupt:
        Log.info('user exit')
