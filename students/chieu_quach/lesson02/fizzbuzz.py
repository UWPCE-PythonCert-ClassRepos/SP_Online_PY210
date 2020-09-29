# Write a program that prints the numbers from 1 to 100 inclusive
# But for multiples of thre print "Fizz" instead of the number
# For the multiples of five print "Buzz" instead of the number
# For numbers which are multiples of both three and five print "FizzBuzz" instead.

num = 0
while num < 101:
    s = ""
    num = num + 1
    if num % 3 == 0:
        s = "Fizz"
    if num % 5 == 0:
        s = "Buzz"
    if ((num % 3 == 0) and (num % 5 == 0)):
        s = "FizzBuzz"
    if s == "":
        s = num
    
    print (s)
