#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re


def stringCount(aString):
    result = ''

    lastChar = ''
    lastCount = 0
    for s in aString:
        if s == lastChar:
            lastCount += 1
        if s != lastChar:
            if lastChar != '':
                result += '{:d}{:s}'.format(lastCount, lastChar)

            lastCount = 1
            lastChar = s

    if lastChar != '':
        result += '{:d}{}'.format(lastCount, lastChar)

    return result


def stringCount2(aString):
    result = ''
    match = re.finditer(r'(\d)\1*', aString)
    for m in match:
        s = m.group()
        result += '{:d}{}'.format(len(s), s[0])
    return result


def stringCount3(aString):
    def repl(m):
        s = m.group()
        return '{:d}{}'.format(len(s), s[0])

    return re.sub(r'(\d)\1*', repl, aString)

def stringCount4(aString):
    lists = [str(len(m.group(0))) + m.group(1) for m in re.finditer(r"(\d)\1*", aString)]
    return "".join(lists)


s = '1'
for i in range(30):
    s = stringCount4(s)
    # print(s)

print(len(s))
