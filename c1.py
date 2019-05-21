#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import string

def convert(s):
    result = ''
    for one in s:
        if one >= 'a' and one <= 'x':
            result += chr(ord(one)+2)
        elif one in ('yz'):
            result += chr(ord(one)-24)
        else:
            result += one
    return result



s1 = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
s2 = convert(s1)

print(s2)

x = string.ascii_lowercase
y = x[2:] + x[:2] 
print(x,y)

trans = str.maketrans(x,y)
s3 = s1.translate(trans)
print(s3)

url = 'map'
print(url.translate(trans))
