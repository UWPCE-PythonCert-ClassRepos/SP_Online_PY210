def fibonacci(n):
    fib = [0, 1]

    for i in range(2,n):
        new_num = fib[i-2] + fib[i-1]
        fib.append(new_num)

    return fib

print(fibonacci(10))



