#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# butter/fly
# http://www.pythonchallenge.com/pc/hex/idiout2.html
# http://www.pythonchallenge.com/pc/hex/unreal.jpg


import re
import requests
from requests.auth import HTTPBasicAuth


def getUrlByRange(range_start = 0):
    content_range = ''
    auth=HTTPBasicAuth('butter', 'fly')
    url = 'http://www.pythonchallenge.com/pc/hex/unreal.jpg'
    try:
        # bytes=0-
        byte_range = 'bytes={:d}-'.format(range_start)
        headers = {'Range': byte_range}
        r = requests.get(url, auth = auth, headers=headers)
        r.raise_for_status()
        content_range = r.headers.get('Content-Range')
        # print(content_range)
        r.encoding = r.apparent_encoding
        print(r.text)
    except Exception as e:
        print(e)

    return content_range
    
def main():
    pattern = re.compile(r"bytes (\d+)-(\d+)/(\d+)")
    range_start = 30203

    while True:
        content_range = getUrlByRange(range_start)
        m = pattern.search(content_range)
        if m:
            (_, end, length) = list(map(int, m.groups()))
            print(end, length)
            if end + 1 < length:
                range_start = end + 1
                continue
        break


if __name__ == "__main__":
    main()