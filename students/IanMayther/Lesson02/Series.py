#Exercise2.4.py

def fibonacci(n):
    if n == 0:
        return print("0")
    elif n == 1:
        return print("1")
    elif n > 1:
        fib = [0, 1]
        for x in range(2, n+1):
            x = fib[x-1] + fib[x-2]
            fib.append(x)
        return print(fib[n])

fibonacci(7)
