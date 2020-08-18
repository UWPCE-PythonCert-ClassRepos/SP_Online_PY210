#!/usr/bin/env python
#ClassNote:  I pass parameters for the numbers 1 thru 100.  I hope that is ok.
def print_numbers(x,y):

  i = x
  while i < y+1:
#    print("i=",i)
    if(i % (3*5)  == 0):
      print("FizzBuzz")
    elif(i % 3  == 0):
      print("Fizz")
    elif(i % 5  == 0):
      print("Buzz")
    else:
      print(i)
    i +=1 

print_numbers(1,100)
