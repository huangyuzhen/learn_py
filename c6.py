#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import re
import zipfile
import os

filename = "channel.zip"

if os.path.isfile(filename):
    pass
else:
    url = 'http://www.pythonchallenge.com/pc/def/channel.zip'
    res = requests.get(url)
    print(res.url)
    with open("channel.zip", "wb") as f:
        f.write(res.content)

if os.path.isfile(filename):
    pass
else:
    exit

z = zipfile.ZipFile("channel.zip")
# print(z.namelist())

with z.open("readme.txt", "r") as f:
    content = f.read()
    print(content.decode())

pattern = re.compile(r'Next nothing is (\d+)')

name = 90052
comments = ''

while name:
    filename = "{}.txt".format(name)
    name = ''
    content = ''
    with z.open(filename) as f:
        content = f.read().decode()
        # print(filename, content)
        result = pattern.findall(content)
        if result:
            name = result[0]
        else:
            print("I am the end.")

        info = z.getinfo(filename)
        comments += info.comment.decode()

print(comments)
