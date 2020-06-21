def fibonacci(n):
    fib = [0, 1]
    for i in range(n):
        fib.append(fib[len(fib)-1] + fib[len(fib)-2])
    print(fib[n-1])

fibonacci(7)

def lucas(n):
    luc = [2, 1]
    for i in range(n):
        luc.append(luc[len(luc)-1] + luc[len(luc)-2])
    print(luc[n-1])

lucas(7)

def sum_series(n, num = [0, 1]):
    for i in range(n):
        num.append(num[len(num)-1] + num[len(num)-2])
    print(num[n-1])

sum_series(7)
sum_series(7, num = [2, 1])
