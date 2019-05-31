#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# butter/fly
# http://www.pythonchallenge.com/pc/hex/bin.html

import requests
from requests.auth import HTTPBasicAuth
import re
import mailparser
import base64


auth=HTTPBasicAuth('butter', 'fly')

url = 'http://www.pythonchallenge.com/pc/hex/bin.html'
r = requests.get(url, auth = auth)
r.encoding = r.apparent_encoding
html = r.text

email = ''
m = re.search(r'<!--\n(.*)\n-->', html, re.S)
if m:
    email = m.group(1)

mail = mailparser.parse_from_string(email)
print(mail.subject)

for att in mail.attachments:
    filename = att['filename']
    if not filename:
        continue
    data = att['payload']
    if att['content_transfer_encoding'] == 'base64':
        data = base64.b64decode(data)

    mode = "w"
    if att['binary']:
        mode = "wb"
    with open(filename, mode) as f:
        print("attachment save to:", filename)
        f.write(data)

