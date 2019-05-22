#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image
import re


url = 'http://www.pythonchallenge.com/pc/def/oxygen.html'
# download http://www.pythonchallenge.com/pc/def/oxygen.png

image = Image.open('oxygen.png').convert('RGBA')
width, height = image.size
source = image.load()

# for y in range(height):
#     d = source[0, y]
#     if d[0] == d[1] and d[0] == d[2]:
#         print(y, d)

y = 43
s = 'Answer:'
for x in range(width):
    d = source[x, y]
    if d[0] == d[1] and d[0] == d[2]:
        c = chr(d[0])
        if c != s[-1]:
            print(d)
            s += c

print(s)
# print(s)
# smart guy, you made it. the next level is [105, 10, 16, 101, 103, 14, 105, 16, 121]

number = re.findall(r'(\d+)', s)
l= list(map(chr, [105, 110, 116, 101, 103, 114, 105, 116, 121]))
print("".join(l))
