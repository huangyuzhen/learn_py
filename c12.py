#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# <title>dealing evil</title>

# evil1.jpg
# evil2.jpg
# evil2.gfx
# evil3
# evil4

with open("evil2.gfx", 'rb') as f:
    content = f.read()

sep = 5
for i in range(sep):
    with open("{}.jpg".format(i), 'wb') as f:
        f.write(content[i::sep])


