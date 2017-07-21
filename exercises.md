# Exercise 1

How to swap two numbers?

	a,b = b,a

# Exercise 2

- Write a "vocabulary" (3 words) from English to another language.
- Construct a dictionary from the language you have chosen to English **without rewriting everything**

```
e2i = {"book":"libro",
       "pen":"penna",
       "bottle":"bottiglia"}

for pair in e2i.items():
    print(pair[0], " --->", pair[1])

for key in e2i.keys():
    print(key)

i2e = {}

for key in e2i.keys():
    i2e[e2i[key]] = key

for pair in i2e.items():
    print(pair[0], " --->", pair[1])
```

# Exercise 3

- Implement the `insertion sort` algorithm in a function named `insertion_sort` which takes a list `l` as argument and sorts it `in place`.

```
for i = 1 --> length(l)
	j = i
	while j > 0 and l[j] < l[j-1] 
		swap l[j] and l[j-1]
		j = j - 1
```

Read list from file


In order to test it, generate a list of 10 **random integer numbers** and then call your function

```
from random import randint

randint(0,100)
```

what is the `Pythonic` way to construct such a list?

```
l = [randint(0,100) for k in range(10)]
```

- test if your algorithm works for `len(l)=10,100,1000,10000,100000`. What do you experience?

# Exercise 4

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

```
__all__ = ["insertion_sort", "quick_sort"]
```

# Exercise 5

- Write a module named `performance` where you have to implement a `time_this` function which takes a function as argument

- **Optional** produce nice plots with `matplotlib`

# Exercise 6

- Organize the modules `sorting` and `performance` in a package named `mysorting`

- How do you access your functions now?


# Exercise 7

- play with `matplotlib`
- have fun with Project Euler https://projecteuler.net/problems
  - 1, 2, 3, 14, 17 (dict), 57, 79, 102
