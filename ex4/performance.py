from time import time

def time_this(f,v, n=10, dt=60):
    t0 = time()
    for k in range(1,n+1):
        f(v.copy())
        t = time()
        if (t-t0) > dt:
            break
    t = time()
    return (t-t0)/k
