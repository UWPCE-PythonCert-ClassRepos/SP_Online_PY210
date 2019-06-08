def fibonacci(n):
	"function returns the nth number in the fibonacci series"
	fib = []
	for i in range(n+1):
		if i == 0:
			fib.append(i)
		elif i == 1:
			fib.append(i)
		else:
			fib.append(fib[i-1]+fib[i-2])
	return fib[n]

def lucas(n):
	"function returns the nth number in the lucas series"
	luc = []
	for i in range(n+1):
		if i == 0:
			luc.append(2)
		elif i == 1:
			luc.append(i)
		else:
			luc.append(luc[i-1]+luc[i-2])

	return luc[n]

def sum_series(n, a=0, b=1):
	free_series = []
	for i in range(n+1):
		if i == 0:
			free_series.append(a)
		elif i == 1:
			free_series.append(b)
		else:
			free_series.append(free_series[i-1]+free_series[i-2])
            
	return free_series[n]

