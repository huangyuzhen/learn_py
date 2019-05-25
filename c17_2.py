##!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from requests.cookies import RequestsCookieJar

url = 'http://www.pythonchallenge.com/pc/stuff/violin.php'
msg = 'the flowers are on their way'

cookie_jar = RequestsCookieJar()
cookie_jar.set('info', msg, domain = "www.pythonchallenge.com", path = "/")

res = requests.get(url, cookies = cookie_jar)
print(res.text)

# oh well, don't you dare to forget the balloons.</font>
