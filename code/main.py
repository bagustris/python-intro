from random import randint
from sorting import insertion_sort, quick_sort
from performance import time_this

for n in 10, 100, 1000, 10000:
    a = [randint(0, 100) for w in range(n) ]
    print('quick_sort, n =', n)
    quick_sort(a.copy())
    t = time_this(quick_sort, a.copy())
    print('done, exec time=', t)
    print('insertion_sort, n =', n)
    insertion_sort(a.copy())
    t = time_this(insertion_sort, a.copy())
    print('done, exec_timei=', t)

print('all done :\)')
