#! /usr/bin/env python3

dictionary = {'book' : 'buku',
    'table' :'meja',
    'chair' : 'kursi' }

inv_dictionary = {v: k for k, v in dictionary.items()}

for k in inv_dictionary.keys():
     print(k, "-->", inv_dictionary[k])

