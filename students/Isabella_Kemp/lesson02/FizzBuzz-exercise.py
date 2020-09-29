#Isabella Kemp
#12/23/2019
#Fizz Buzz

for x in range (1,101):
    if x % 3 == 0 and x % 5 == 0:
        print ("Fizz Buzz")
    elif x % 3 == 0:
        print ("Fizz")
    elif x % 5 == 0:
        print ("Buzz")
    else:
        print (x)


