#! /usr/bin/env python3

dictionary = {'book' : 'buku',
    'table' :'meja',
    'chair' : 'kursi' }

for k in dictionary.keys():
    print(k, "-->", dictionary[k])

for i in dictionary.items():
    
    print(i)
    print(i[0])
    print(i[1])
