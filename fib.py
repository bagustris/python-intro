def fib(n):
    """ Print fib up to n"""
    a, b = 0,1
    while a<n:
        def summ(a,b):
            a,b = b,a+b
            return a,b
        print(a, end=' ')
        a,b = summ(a,b)
    print()

fib(10)
help(fib)




