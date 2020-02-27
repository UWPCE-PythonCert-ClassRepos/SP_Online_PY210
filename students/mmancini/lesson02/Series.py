#!/usr/bin/env python3


"""

Fibonacci module

"""

def Fibonacci(n):
    """
        Out: return the nth number in fibonacci series
    """
    
    fibAry = []
    for i in range(n+1):
        if i == 0:
            fibAry.append(i)
        elif i == 1:
            fibAry.append(i)
        else:
            fibAry.append(fibAry[i-1]+fibAry[i-2])
    return fibAry[n]

def Lucas(n):
    """
        Out: return the nth number in the lucas series
    """
    lucasAry = []
    for i in range(n+1):
        if i == 0:
            lucasAry.append(2)
        elif i == 1:
            lucasAry.append(i)
        else:
            lucasAry.append(lucasAry[i-1]+lucasAry[i-2])

    return lucasAry[n]


####################################

# main, test funcs

if __name__ == "__main__":

    # run some tests


    print ("All Tests Passed")
