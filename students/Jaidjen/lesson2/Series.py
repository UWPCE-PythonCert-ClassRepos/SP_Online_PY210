
#this function is to do the fibonacci series
def fibonacci(n):
    if n<=1:
        return n
    else:
        return(fibonacci(n-1)+fibonacci(n-2))

nterms =10
print("Fibonacci sequence:")
for i in range(nterms):
    print(fibonacci(i))


def lucas(n):
    if n == 0:
        return 2;
    if n == 1:
        return 1;

    return(lucas(n-2)+lucas(n-1))

nterms=10

print("Lucas sequence:")
for i in range(nterms):
    print(lucas(i))


def sum_series(n):
    n = 0
    n = 2
    if n == 0:
        print(fibonacci)
    else:
        print(lucas)