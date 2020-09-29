# Homework 0 - Basics

In this homework, you'll practice some basic tools you'll use throughout the course.

Please put any written answers in [`answers.md`](answers.md)

You may need to use conda to install `tqdm` to run the starter code for problem 4.

## Survey

Write a script in `survey.py` which outputs answers to the following questions.

1. Your name
2. Your program / year
3. What are your academic interests? (research/coursework)
4. What programming languages do you have experience with?
5. What is your experience with Python?  (is is ok to have no experience)
6. What time zone are you in? (Chicago is UTC -5)
7. What is something you would like to learn in this course?
8. Do you have any questions or concerns you would like to share?


Feel free to make this a reverse [code golf](https://en.wikipedia.org/wiki/Code_golf), e.g. make functions/variables to help you print your answers in an unnecessarily complicated way.  There are no rules, and no points will be awarded.  However, your output should look like the following when run from a terminal
```
$ python survey.py
1. <answer to question 1>
2. <answer to question 2>
...
```


## Problem 0
Implement the following [Fizzbuzz](https://imranontech.com/2007/01/24/using-fizzbuzz-to-find-developers-who-grok-coding/) program:

Write a python script [`fizzbuzz.py`](fizzbuzz.py) which prints the numbers from 1 to 100, but for multiples of 3 print "fizz" instead of the number, for multiples of 5 print "buzz" instead of the number, and for multiples of both 3 and 5 print "fizzbuzz" instead of the number.

## Problem 1

The [Egyptian multiplication algorithm](https://en.wikipedia.org/wiki/Ancient_Egyptian_multiplication) (or Russian peasant algorithm) computes the product `a * n` using repeated additions. The algorithm uses the basic rule `a * n = (a + a) * (n // 2)` if `n` is even, and `a * n = (a + a) * (n // 2) + a` if `n` is odd.  Recall `//` is integer (floor) division.

You can view [`egyptian.py`](egyptian.py) for a basic Python implementation.

How many additions are done in the Egyptian multiplication algorithm?  Your answer should be in terms of `log2(n)` and the number of non-zero bits of `n` (when `n` is represented as a binary integer), denoted `#(n)`.  Hint: how many additions are done at each level of recursion, and how many levels of recursion are there?

Write a function called `power(a, n)` to compute `a**n` via repeated multiplications by adapting the Egyptian multiplication algorithm.  Implement this function in the file `egyptian.py`.  Have the script print a few interesting powers, including `3**3`, `4**4` and `5**3`.

In general, you can use the Egyptian multiplication algorithm on any associative operation (meaning `a` can be an element of any semi-group) c.f. Stepanov and Rose, "From Mathematics to Generic Programming."

## Problem 2 - Fibonacci Numbers

The [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_number) is defined as a linear recursion

`F_0 = 0, F_1 = 1, F_n = F_{n-1} + F_{n-2}`

The first few numbers in the sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21, ...

One method to compute the Fibonacci number `F_n` is to compute each number recursively. In pseudocode:
```
fibonacci(n)
	return fibonacci(n-1) + fibonacci(n-2)
```

Write a recursive function in Python to compute `fibonacci(n)` - name this function `fibonacci_recursive`.  Put in the appropriate checks for if `n=0` or `n=1`.

Another way to compute `fibonacci(n)` is through a simple iteration.  In pseudocode:
```
fibonacci(n):
	a = 0
	b = 1
	for n-1 iterations:
		a, b = b, a+b
	return b
```
Write a Python function named `fibonacci_iter` to implement this algorithm.


Print the first 30 Fibonacci numbers using both these functions.

Which of these algorithms do you expect to be asymptotically faster?  Why?

## Problem 3 - Numpy Basics

We can re-write the Fibonacci recurrence using a matrix-vector product:
```
[F_n    ] = [1, 1] * [F_{n-1}]
[F_{n-1}]   [1, 0]   [F_{n-2}]
```
Let `x_n = [F_n, F_{n-1}]^T` above, and let `A` denote the matrix `[[1,1],[1,0]]` above.  Then we can write `x_n = A^n x_1`, where `x_1 = [1,0]`.

Write a Python function `fibonacci_power` that computes `F_n` using the above relation, using numpy for vectors and matrices.  Use your adaptation of the Egyptian algorithm in part 1 to compute the power `A^n`.

Print the first 30 Fibonacci numbers using this function.  Compare to your answer from problem 3.

What is the asymptotic number of additions done in this algorithm?  How does this compare to the algorithms in problem 2?

## Problem 4 - PyPlot Basics

Use PyPlot to create a plot of the run times of your three functions to compute Fibonacci numbers.  

* Use a log-log scale for your plot.
* There should be three lines.
* Your plot should have a legend.
* Your plot should have labels for its x and y axes.
* Your plot should have a title
* save your plot as `fibonacci_runtime.png`

embed the image in `answers.md` and give a short interpretation of what you see.

## Feedback

If you'd like share how long it took you to complete this assignment, it will help adjust the difficulty for future assignments.  You're welcome to share additional feedback as well.
