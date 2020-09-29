#Fizz Buzz Exercise
#By Reem Alqaysi
#program that prints the numbers from 1 to 100 inclusive.

def fizzbuzz():
    for number in range(1,101):
#For numbers which are multiples of both three and five print “FizzBuzz” instead
        if((number%3==0) and (number%5==0)):
            print('FizzBuzz')
#For the multiples of five print “Buzz” instead of the number.
        elif(number%5==0):
            print('Buzz')
#for multiples of three print “Fizz” instead of the number.
        elif(number%3==0):
            print('Fizz')
        else:
            print (number)



fizzbuzz()
