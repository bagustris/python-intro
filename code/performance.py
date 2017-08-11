#! /usr/bin/env python3
from time import time

def simple_time_this(f,n):
    t0 = time()
    f(n)
    t = time()
    execution_time = t - t0
    return execution_time

def time_this(f, v, n=10, dt=60):
    t0 = time()
    for k in range(1, n+1):
        f(v.copy())
        t = time()
        if (t-t0) > dt:
            break
    t = time()
    return (t-t0)/k
