# Python introduction
### Alberto Sartori, Bagus Tris Atmaja

## Exercise 1

How to swap two numbers?
## Solution 1
`>>> c, d = d, c`

## Exercise 2

- Write a "vocabulary" (3 words) from English to another language.
- Construct a dictionary from the language you have chosen to English **without rewriting everything**

## Solution 2
```
  dictionary = {'book' : 'buku',
      'table' :'meja',
      'chair' : 'kursi' }
   
  for k in dictionary.keys():
      print(k, "-->", dictionary[k])
```

## Exercise 3

- Implement the `insertion sort` algorithm in a function named `insertion_sort` which takes a list `l` as argument and sorts it `in place`.

```
for i = 1 --> length(l)
	j = i
	while j > 0 and l[j] < l[j-1] 
		swap l[j] and l[j-1]
		j = j - 1
```

Test it sorting the `sort_this.txt` file.

- How can we generate a new list with **random integer numbers** 

```
from random import randint

randint(0,100)
```

what is the `Pythonic` way to construct such a list?


- Test if your algorithm works for `len(l)=10,100,1000,10000`. What do you experience? Can you sort a list of `100k` elements?

## Exercise 4

- Write a module named `sorting` where you put the `insertion_sort` and a `quick_sort`

```
def quick_sort(array):
    begin = 0
    end = len(array) -1
    def _quick_sort(array, begin, end):
        if begin >= end:
            return
        pivot = partition(array, begin, end)
        _quick_sort(array, begin, pivot-1)
        _quick_sort(array, pivot+1, end)
    return _quick_sort(array, begin, end)


def partition(array, begin, end):
    pivot = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot
```

- Test the performance of the `quick_sort` 

- How can I hide the `partition` function to the user?

- Write a module named `performance` where you have to implement a `time_this` function which takes a function as argument

```
from time import time
t0 = time()
f()
t = time()
execution_time = t - t0 
```

- **Optional** produce nice plots with `matplotlib`

## Exercise 5

- Organize the modules `sorting` and `performance` in a package named `mysorting`

- How do you access your functions now?

## Exercise 6

- play with `matplotlib`
- have fun with Project Euler https://projecteuler.net/problems
  - 1, 2, 3, 14, 17 (dict), 57, 79, 102
