#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import wave

w = wave.open('indian.wav', 'rb')
params = w.getparams()
nframes = w.getnframes()


w2 = wave.open('indian2.wav', 'wb')
w2.setparams(params)

for i in range(nframes):
    d = w.readframes(1)
    w2.writeframes(d[::-1])

w.close()
w2.close()
