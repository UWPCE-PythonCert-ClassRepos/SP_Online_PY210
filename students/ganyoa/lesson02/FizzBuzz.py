'''
Fizz Buzz Exercise
-Write a program that prints the numbers from 1 to 100 inclusive.
-But for multiples of three print “Fizz” instead of the number.
-For the multiples of five print “Buzz” instead of the number.
-For numbers which are multiples of both three and five print “FizzBuzz” instead.
'''
for i in range(1, 101):
	a = i
	if i % 3 == 0:
		a = 'Fizz'
	if i % 5 == 0:
		a = 'Buzz'
	if i % 3 == 0 and i % 5 == 0:
		a = 'FizzBuzz'
	print(a)