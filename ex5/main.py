#!/usr/bin/env python3

from mysorting.sorting import *
from random import randint
import mysorting.performance

a=[randint(0,100) for k in range(20)]
print("insertion_sort")
print(mysorting.performance.time_this(insertion_sort,a.copy()))
print("quick_sort")
print(mysorting.performance.time_this(quick_sort,a.copy()))

print("done")

