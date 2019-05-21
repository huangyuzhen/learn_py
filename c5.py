#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import pickle


url = 'http://www.pythonchallenge.com/pc/def/banner.p'
res = requests.get(url)
print(res.url)

data = pickle.loads(res.content)

for line in data:
    s = ''
    for one in line:
        s += one[0] * one[1]
    print(s)

