#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image

source = Image.open("mozart.gif").convert('RGB')
print(source.mode, source.size)
width, height = source.size

target = Image.new(source.mode, (1250, 500))

flag = False
x_new, y_new = (0,0)

for y in range(height):
    for x in range(width):
        pixel = source.getpixel((x,y))
        point = (x_new, y_new)
        target.putpixel(point, pixel)
        x_new += 1

        if pixel == (255,0,255):
            if not flag:
                x_new, y_new = 0, y_new+1
            flag = True
        else:
            flag = False

target.show()

# the answer is romance
