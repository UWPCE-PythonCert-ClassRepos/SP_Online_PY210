x = range(1, 101)
for i in x:    
    if i % 3 == 0 and i % 5 ==0:
        print ("FizzBuzz")
    elif i % 3 == 0:
        print ("Fizz")
    elif i % 5 == 0:
        print ("Buzz")
    else:
        print (i)