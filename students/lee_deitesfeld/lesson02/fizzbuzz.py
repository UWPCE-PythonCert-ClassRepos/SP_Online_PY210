#--------------------------
#Title: FizzBuzz 1-100
#Description: Prints 1-100, where multiples of 3 print 'fizz', multiples of 5
    #print 'buzz' and multiples of both print 'FizzBuzz'

#Original Dev: Lee Deitesfeld
#Change Log:
#20190331LAD Created script
#--------------------------

#iterates numbers 1 to 100
for i in range(1,101):
    #if number divisible by 3 and 5, print "FizzBuzz"
    if (i % 3 == 0 and i % 5 == 0):
        print("FizzBuzz")
    #if number divisible by 5, print "Buzz"
    elif i % 5 == 0:
        print("Buzz")
    #if number divisible by 3, print "Fizz"
    elif i % 3 == 0:
        print("Fizz")
    #if number not divisible by 3 or 5, print number
    else: print(i)
