# this prints Fizz if the number is divisible by 3
# this prints Buzz if the number is divisible by 5
# this prints FizzBuzz if the number is divisible by 3 and 5

for i in range(1,101):

	if i%3 == 0 and i%5 == 0:
		print('FizzBuzz')
	elif i%5 == 0:
		print('Buzz')
	elif i%3 == 0:
		print('Fizz')
	else:
		print(i)

	