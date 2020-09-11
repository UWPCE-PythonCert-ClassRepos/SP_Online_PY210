## Lesson 2, Exercise 2.4 Fibonnaci Series
## By: B. Matthews
## 9/11/2020

def fibonnaci(n):
#"""Generates a Fibonnaci series with length n"""

    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return fibonnaci(n-1) + fibonnaci(n-2)

def lucas(n):
#"""Generates a Lucas series with length n"""
    if (n == 0):
        return 2
    elif (n == 1):
        return 1
    else:
        return lucas(n-1) + lucas(n-2)

##Test the function
n = int(input("Enter a number >> "))

for i in range (n+1):
    print (lucas(i))

print ("Fibonnaci:", n,"th value is: ", fibonnaci(n))

print ("Lucas series: ", lucas(n))


