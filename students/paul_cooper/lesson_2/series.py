n = 8
# this returns the nth nuber in the fibonacci series
def fibonacci(n):
	if n <=0:
		print('incorrect number')
	elif n == 1:
		return 0
	elif n == 2:
		return 1
	else:
		return fibonacci(n-1)+fibonacci(n-2)
			

print(fibonacci(n))

# this returns the nth number in the Lucas series
def lucas(n):
	if n <=0:
		print('incorrect number')
	elif n == 1:
		return 2
	elif n == 2:
		return 1
	else:
		return lucas(n-1)+lucas(n-2)

print(lucas(n))
