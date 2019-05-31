#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import bz2, zlib

with open("21/package.pack", 'rb') as f:
    data = f.read()

    s = ''
    while True:
        if data[:2] == b'x\x9c':
            data = zlib.decompress(data)
            s += ' '
        elif data[:3] == b'BZh':
            data = bz2.decompress(data)
            s += '#'
        elif data[-2:] == b'\x9cx':
            data = data[::-1]
            s += '\n'
        else:
            break
    print(data)
    print(data[::-1])
    print(s)