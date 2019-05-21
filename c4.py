#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import re

def getNothing(s):
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
    params = {'nothing':s}
    
    content = ''
    try:
        res = requests.get(url, params)
        print(res.url)
        res.raise_for_status()
        content = res.text
    except Exception as e:
        print(url, e)
    return content


# nothing = 12345
nothing = 8022
nothing = 74258

while nothing:
    content = getNothing(nothing)
    print(content)
    find = re.findall(r'the next nothing is (\d+)', content)
    if find:
        nothing = find[0]
    else:
        nothing = ''

print(content)