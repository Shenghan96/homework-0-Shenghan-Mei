"""
fibonacci

functions to compute fibonacci numbers

Complete problems 2 and 3 in this file.
"""

import time # to compute runtimes
from tqdm import tqdm # progress bar

# Question 2
def fiboncci_recursive(n):
    if n <= 1:
        return n
    else:
        return(fiboncci_recursive(n-1) + fiboncci_recursive(n-2))

for i in range(30):
    print(fiboncci_recursive(i))

    pass


# Question 2
def fibonacci_iter(n):
    a=0;
    b=1;
    i=1;
    yield a
    while i<=n:
        yield b
        a,b=b,a+b;
        i=i+1;
    

for x in fibonacci_iter(29):
    print(x)

    pass


# Question 3
def fibonacci_power(n):
    pass


if __name__ == '__main__':
    """
    this section of the code only executes when
    this file is run as a script.
    """
    def get_runtimes(ns, f):
        """
        get runtimes for fibonacci(n)

        e.g.
        trecursive = get_runtimes(range(30), fibonacci_recusive)
        will get the time to compute each fibonacci number up to 29
        using fibonacci_recursive
        """
        ts = []
        for n in tqdm(ns):
            t0 = time.time()
            fn = f(n)
            t1 = time.time()
            ts.append(t1 - t0)

        return ts


    nrecursive = range(35)
    trecursive = get_runtimes(nrecursive, fibonacci_recursive)

    niter = range(10000)
    titer = get_runtimes(niter, fibonacci_iter)

    npower = range(10000)
    tpower = get_runtimes(npower, fibonacci_power)

    ## write your code for problem 4 below...
