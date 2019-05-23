#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# <title>odd even</title>

from PIL import Image, ImageDraw


image = Image.open("cave.jpg")
width,height = image.size
print(image.size)

halfSize = (width//2, height//2)
newImage = Image.new(image.mode, halfSize)

for x in range(0, width, 2):
    for y in range(0, height, 2):
        pixel = image.getpixel((x, y))
        newImage.putpixel((x//2, y//2), pixel)

newImage.show()
