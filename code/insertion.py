#! /usr/bin/env python3

def insertion_sort(l):
    """ documentaion goes here"""
    for i in range(1, len(l)):
        for j in range (i, 0, -1):
            if l[j] < l[j-1]:
                l[j], l[j-1] = l[j-1], l[j]
            else:
                break

from random import randint

for n in 10, 100, 1000, 10000:
    a = [randint(0,100) for w in range (100)]
    print('n =', n)
    insertion_sort(a)
    print("done")    
print(a)

