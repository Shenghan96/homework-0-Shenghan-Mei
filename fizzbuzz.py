"""
fizzbuzz

Write a python script which prints the numbers from 1 to 100,
but for multiples of 3 print "fizz" instead of the number,
for multiples of 5 print "buzz" instead of the number,
and for multiples of both 3 and 5 print "fizzbuzz" instead of the number.
"""
for i in range(1, 101):
  print('fizz'[i%3*len('fizz')::] + 'buzz'[i%5*len('buzz')::] or i)
