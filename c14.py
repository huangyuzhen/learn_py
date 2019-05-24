#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# <html>
# <head>
#   <title>walk around</title>
#   <link rel="stylesheet" type="text/css" href="../style.css">
# </head>
# <body>
# <center>
# <img src="italy.jpg"><br>
# <br>

# <!-- remember: 100*100 = (100+99+99+98) + (...  -->

# <img src="wire.png" width="100" height="100">

# </body>
# </html>

# http://www.pythonchallenge.com/pc/return/italy.html
# result: cat

from PIL import Image, ImageDraw

# image size 100x100
width = 100
x, y = (-1, 0)

points = []
for n in range(width, 0, -2):
    # one = (n, n-1, n-1, n-2)
    for _ in range(n):
        x += 1
        points.append((x, y))
    for _ in range(n-1):
        y += 1
        points.append((x, y))
    for _ in range(n-1):
        x -= 1
        points.append((x, y))
    for _ in range(n-2):
        y -= 1
        points.append((x, y))

print(len(set(points)))

source = Image.open("wire.png")
target = Image.new(source.mode, (width, width))

for i in range(width * width):
    pixel = source.getpixel((i,0))
    target.putpixel(points[i], pixel)

target.show()
