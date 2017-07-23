#!/usr/bin/env python3

from sorting import *
from random import randint
import performance

for n in 2,10,100,1000:#,10000:
    a=[randint(0,9999999) for k in range(n)]
    print("--------------------------------------")
    print("sorting for len(a) =",n)
    print("insertion_sort")
    print(performance.time_this(insertion_sort,a.copy()))
    print("quick_sort")
    print(performance.time_this(quick_sort,a.copy()))

print("done")


import matplotlib.pyplot as plt

fig1 = plt.figure()

insertion = []
quick = []
a = 2

samples = [k for k in range(2,1000,100)]
for n in samples:
    a=[randint(0,9999999) for k in range(n)]
    insertion.append(performance.time_this(insertion_sort,a.copy()))
    quick.append(performance.time_this(quick_sort,a.copy()))

plt.plot(samples,insertion, label='insertion')
plt.plot(samples,quick, label='quick')
plt.legend()
plt.show()

