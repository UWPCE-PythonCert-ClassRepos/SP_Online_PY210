#!/usr/bin/env python3


"""

fibonacci module

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

def Sum_Series(n, arg1=0, arg2=1):
    seriesAry = []
    for i in range(n+1):
        if i == 0:
            seriesAry.append(arg1)
        elif i == 1:
            seriesAry.append(arg2)
        else:
            seriesAry.append(seriesAry[i-1]+seriesAry[i-2])
            
    return seriesAry[n]



####################################

# main, test funcs

if __name__ == "__main__":

    # run some tests

    testVal = 7
    expectedRsltFib = 13
    expectedRsltLuc = 29

    print ("")
    
    rslt = Fibonacci(testVal)
    print ("Series Fibonacci of " + str(testVal) + " == " + str(rslt))
    assert rslt == expectedRsltFib

    rslt = Lucas(testVal)
    print ("Series Lucas of " + str(testVal) + " == " + str(rslt))
    assert rslt == expectedRsltLuc 

    rslt = Sum_Series(testVal, 0, 1)
    print ("Sum_Series with args Fibonacci of " + str(testVal) + " == " + str(rslt))
    assert rslt == expectedRsltFib
    rslt = Sum_Series(testVal)
    print ("Sum_Series with args Fibonacci of " + str(testVal) + " == " + str(rslt))
    assert rslt == expectedRsltFib
    rslt = Sum_Series(testVal, 2, 1)
    print ("Sum_Series with args Fibonacci of " + str(testVal) + " == " + str(rslt))
    assert rslt == expectedRsltLuc

    print ("All Tests Passed")

