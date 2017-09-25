
xssfuzz
====  
~~~
                   ____             
   _  ____________/ __/_  __________
  | |/_/ ___/ ___/ /_/ / / /_  /_  /
 _>  <(__  |__  ) __/ /_/ / / /_/ /_
/_/|_/____/____/_/  \__,_/ /___/___/
                                    
~~~
xssfuzz is a xss fuzz test tool.Provides good customization

setup
-

~~~
#python2.x
git clone https://github.com/blue-bird1/xss_fuzz
pip -r  requirements.txt
./xssfuzz.py -h
Usage: xssfuzz.py [options]

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -m MODE, --mode=MODE  xss fuzz test mode
  -t THREAD, --thread=THREAD
                        thread num
  -u URL, --url=URL     fuzz test url
  -d DATA, --data=DATA  post data
  -p PAYLOAD, --payload=PAYLOAD
                        default '"<tag>
  -l LIST, --list=LIST  list all payload

~~~

Example
-
~~~
./xssfuzz.py -u 'www.baidu.com?id=1'
#This is the WAF detector for the jump domain name 
~~~

config
-
see `config.py`
What's important is the two? `mode_list` and `payloads`

see `payload/tag.py` 
changes it will changes default payload 
~~~
 self.exploit = '\'"><{tag}></{tagend}>'
~~~

see `waf/Url.py`
~~~
 for _ in tmp:
        if not urlparse(_['response'].url).netloc == url:
                    self.exp.append(_)
~~~
it is detector method

Development
-
see `lib/data.py` and `lib/payload.py` and `lib/waf.py`

create python file ,create you class.
achieve `@abstractmethod` down function ,Then import add `config.py`
