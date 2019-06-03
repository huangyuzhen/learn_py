#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw

img = Image.open("22/white.gif")
new = Image.new("RGB", (500, 200))
draw = ImageDraw.Draw(new)
x, y = 0, 100
line = []
for frame in range(img.n_frames):
    img.seek(frame)
    left, upper, right, lower = img.getbbox()

    # print(left, upper)
    # print(left, upper, right - left, lower-upper )
    # get the direction; like a joystick,

    # end of a move(letter), shift to the right
    if left == upper == 100:
        # new char
        x += 50
        y = 100
        draw.line(line)
        line = []

    x += left - 100
    y += upper - 100

    line.append(x)
    line.append(y)

if len(line):
    draw.line (line)

new.show()