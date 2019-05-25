#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from urllib.parse import unquote_to_bytes
import re, bz2


def getNothing(s):
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
    params = {'busynothing':s}

    content = ''
    info = None
    try:
        res = requests.get(url, params)
        res.raise_for_status()
        print(res.url)
        info = res.cookies.get('info')
        content = res.text
    except Exception as e:
        print(url, e)
    return content, info


nothing = 12345

words = ''
while nothing:
    content, ck = getNothing(nothing)
    if ck:
        print(ck)
        words += ck
    find = re.findall(r'the next busynothing is (\d+)', content)
    if find:
        nothing = find[0]
    else:
        nothing = ''

print("last is", content)
# print('result:', words)

bWords = unquote_to_bytes(words.replace('+', ' '))
result = bz2.decompress(bWords).decode()

print(result)

# answer: is it the 26th already? call his father and inform him that "the flowers are on their way". he'll understand.

# 27 is mozart's birthday, his father is Leopold
# use 13.py make a call, get
# 555-VIOLIN
