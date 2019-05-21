#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import re


res = requests.get('http://www.pythonchallenge.com/pc/def/ocr.html')
html = res.text

find = re.findall(r'(%%.*)-->', html, re.S)
text = find[0]

d = {}
for s in text:    
    d[s] = d.get(s, 0) +1
    if d[s] == 1:
        print(s)

L1 = []
for k,v in d.items():
    L1.append({'k':k, 'v':v})

L2 = sorted(L1, key = lambda x: x['v'])
print(L2)


# equality
