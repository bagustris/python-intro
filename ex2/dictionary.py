#! /usr/bin/env python3

e2i = {"book" : "libro",
       "water" : "acqua",
       "pen": "penna"}

for pair in e2i.items():
    print(pair[0], "--->", pair[1])

for key in e2i.keys():
    print(key, "--->", e2i[key])

i2e = {}

for key in e2i.keys():
    i2e[e2i[key]] = key

for pair in i2e.items():
    print(pair[0], "--->", pair[1])

