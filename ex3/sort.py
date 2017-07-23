#!/usr/bin/env python3

def insertion_sort(l):
    for i in range(1,len(l)):
        for j in range(i,0,-1):
            if l[j] < l[j-1]:
                l[j], l[j-1] = l[j-1], l[j]
            else:
                break

a = []
with open('sort_this.txt', 'r') as f:
    for line in f:
        a.append(int(line))

print(a)

insertion_sort(a)

print("after insertion_sort")
print(a)


from random import randint

for n in 10,100,1000,10000:
    a=[randint(0,9999999) for k in range(n)]
    print("sorting for len(a) =",n)
    insertion_sort(a)
