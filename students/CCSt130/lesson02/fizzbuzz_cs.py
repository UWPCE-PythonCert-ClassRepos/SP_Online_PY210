# -*- coding: utf-8 -*-
"""
This code determines whether a number 1 to 100 is divisible by x or y and if 
it is divisible by both. It will print 1 of 2 strings if TRUE and a third string
if n is divisible by both x and y.
"""

"""
Lesson02 :: FizzBuzz Exercise
@author: Chuck Stevens :: CCSt130
Created on Wed May 22 15:55:35 2019
"""

def fizzbuzz(numero, div1, div2): 
    """ Evaluates a range and determines if n is divisible by x and or y. """

    # assign to a list for loop
    divisors = [div1, div2]

    i = 0 # while loop counter
    
    while(i <= 1):

        #rem1 = (numero % div1)
        rem1 = (numero % divisors[0])
        
        #rem2 = (numero % div2)
        rem2 = (numero % divisors[1])
        
        # put in a list
        remainders = [rem1, rem2]        
        
        value = (numero - 1) # offset index for screen output
        
        print("Value assigned to myArray[%d] is: %d. " % ((value), numero))

        # Check first divisor
        if(numero >= divisors[i]):
            print("When %d is divided by ** %d,** its Remainder is: %d." % (numero, divisors[i], remainders[i]))
            # Is it Divisible?
            if(remainders[i] == 0):
                print("Therefore, %d is divisible by %d." % (numero, divisors[i]))
                # print correct word depending upon divisor
                if(divisors[i] == divisors[0]):                
                    print("%d: FIZZ! \n" % numero)
                else:
                    print("%d: BUZZ! \n" % numero)
            else: # Not divisible by divisor
                    print("Therefore, %d is not divisible by %d." % (numero, divisors[i]))
                    print("%d: Nuts! \n" % (numero))
        else: # Values below divisor
            print("A Value of '%d' is less than '%d', therefore, %d is not divisible by %d." % (numero, divisors[i], numero, divisors[i]))
            print("%d: Fiddlesticks! \n" % (numero))
        # using counter so that fizzbuzz statement prints 1x
        # admittedly a bit inelegant            
        if(remainders[0] == 0 and remainders[1] == 0 and i == 1): 
            print("Wow! %d is divisible by %d and %d!" % (numero, divisors[0], divisors[1]))
            print("%d: FIZZ!BUZZ! \n" % (numero))

        i += 1 # increment while loop
                
if __name__ == "__main__":

    def main():

        # range to be evaluated
        my_list = range(1,101)
    
        print()
        print("Evaluating :: ", end = "")
        print(my_list)
        print()

        # divisors    
        div1 = 3;
        div2 = 5;
        
        for num in my_list:

            fizzbuzz(num, div1, div2)

main()


# submitted by Chuck S!
