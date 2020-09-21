#--------------------------------------------------------------#
# Title: Lesson 2, FizzBuzz
# Description: Print the words "Fizz" and "Buzz"
# ChangeLog (Who,When,What):
# JEmbury, 9/18/2020, created new script
#--------------------------------------------------------------#
for i in range (0,101):
    if i%3==0 and i%5==0: # check if divisible by 3 and 5
        print("FizzBuzz")
    elif i%3==0: # check if divisible by 3
        print("Fizz")
    elif i%5==0: # check if divisible by 5
        print("Buzz")
    else:
        print(str(i)) # else print current number