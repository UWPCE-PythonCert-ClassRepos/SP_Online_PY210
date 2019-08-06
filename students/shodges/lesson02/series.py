#!/usr/bin/env python3

def fibonacci(n):
    """Returns the nth element of the fibonacci sequence.  Note that n is 0-based."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fi2 = 0 # fibonacci(i-2)
        fi1 = 1 # fibonacci(i-1)
        for i in range(2,n+1):
            fi = fi2 + fi1
            fi2 = fi1
            fi1 = fi
        return fi
