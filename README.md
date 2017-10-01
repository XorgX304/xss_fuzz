
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
#This will use default WAF set
~~~

config
-
see `config.py`
default  mode config 
```
 # while url num
 'white_num': [200],
 # black url num, while_num priority
 'black_num': [504, 405, 403],
 # waf features, waf return string
 'waf_str': [],
```

see `payload/tag.py` 
changes it will changes default payload 
~~~
 self.exploit = '\'"><{tag}></{tagend}>'
~~~



Development
-
see `lib/data.py` and `lib/payload.py` and `lib/waf.py`

create python file ,create you class.
achieve `@abstractmethod` down function ,Then import add `config.py`
