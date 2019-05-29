#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# balloons -> bright -> brightness -> deltas.gz


import difflib

with open("deltas.txt", "r") as f:
    lines = f.readlines()

a = []
b = []
for line in lines:
    a.append(line[:53])
    b.append(line[56:-1])

differ = difflib.Differ()
diffs  = differ.compare(a, b)

L = [[],[],[]]
for d in diffs:
    line = d[2:]
    if d[0] == ' ':
        L[0].append(line)
    elif d[0] == '+':
        L[1].append(line)
    elif d[0] == '-':
        L[2].append(line)
    else:
        pass

print(len(L[0]), len(L[1]), len(L[2]))

def savePicture(filename, picData):
    data = b''
    for s in picData:
        data += bytes.fromhex(s)

    with open(filename, "wb") as f:
        f.write(data)

for i in range(3):
    filename = "c18_{}.png".format(i)
    savePicture(filename, L[i])
    

