#! /usr/bin/env python
# coding:utf-8
# Author qingniao
import sys
from optparse import OptionParser, OptionGroup, OptionError


def cmdLineParser(argv=None):
    """
    This function parses the command line parameters and arguments
    """

    if not argv:
        argv = sys.argv
    parser = OptionParser()

    try:

        parser.add_option("--version", dest="showVersion",
                          action="store_true",
                          help="Show program's version number and exit")

        target = OptionGroup(parser, "Target", "At least one of these "
                                               "options has to be provided to define the target(s)")
        target.add_option("-u", "--url", dest="url", help="Target URL (e.g. \"http://www.site.com/vuln.php?id=1\")")
        target.add_option("-c", dest="configFile",
                          help="Load options from a configuration INI file")

        request = OptionGroup(parser, "Request", "These options can be used "
                                                 "to specify how to connect to the target URL")
        request.add_option("--data", dest="data",
                           help="Data string to be sent through POST")

        request.add_option("--cookie", dest="cookie",
                           help="HTTP Cookie header value")

        request.add_option("--user-agent", dest="agent",
                           help="HTTP User-Agent header value")

        request.add_option("--random-agent", dest="randomAgent",
                           action="store_true",
                           help="Use randomly selected HTTP User-Agent header value")
        request.add_option("--host", dest="host",
                           help="HTTP Host header value")

        request.add_option("--referer", dest="referer",
                           help="HTTP Referer header value")

        request.add_option("-H", "--header", dest="header",
                           help="Extra header (e.g. \"X-Forwarded-For: 127.0.0.1\")")

        request.add_option("--headers", dest="headers",
                           help="Extra headers (e.g. \"Accept-Language: fr\\nETag: 123\")")

        attack = OptionGroup(parser, "attack", "attack mode")
        attack.add_option('-m', '--mode', dest='mode', default='defult', help='xss fuzz test mode')
        attack.add_option('-p', '--payload', dest='payload', default='tag', help='default \'"<tag>')

        parser.add_option_group(target)
        parser.add_option_group(request)
        parser.add_option_group(attack)
        return parser

    except (OptionError, TypeError), e:
        parser.error(e)


if __name__ == '__main__':
    cmdLineParser()