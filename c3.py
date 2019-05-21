#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import re


res = requests.get('http://www.pythonchallenge.com/pc/def/equality.html')
html = res.text

find = re.findall(r'<!--(.*)-->', html, re.S)
text = find[0]

find2 = re.findall(r'[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]', text)
letter = ''.join(find2)

print(letter)


# linkedlist
