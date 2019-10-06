"""
series.py
by David Baylor
uses python 3

Determins the nth number in the Fibonacci of Lucas counting system.
"""
def fib(n):
    """determin a number in the Fibonacci counting system"""
    if n==1:
        return 0
    elif n==2: 
        return 1
    else: 
       return fib(n-2) + fib(n-1)

def lucas(n):
    """determin a number in the Lucas counting system"""
    if n==1:
        return 2
    elif n==2: 
        return 1
    else: 
       return lucas(n-2) + lucas(n-1)

print("Fibonacci")
for i in range(1,21):
    print(fib(i))

print("Lucas")
for i in range(1,21):
    print(lucas(i))
