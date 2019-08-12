###############################
# Fizz Buzz
# 06/24/2019 Jinee Han
# Python Programming Lesson 2
#####################################

for i in range(101):
    if i == 0:
        pass
    elif (i%3) == 0 and (i%15) != 0:
        print ("Fizz")
    elif (i%5) == 0 and (i%15) != 0:
        print ("Buzz")
    elif (i%15) == 0:
        print ("FizzBuzz")
    else: print (i)





























