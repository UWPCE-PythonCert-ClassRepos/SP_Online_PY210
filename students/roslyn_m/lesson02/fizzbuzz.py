# Title: Fizz Buzz
# Dev: Roslyn Melookaran
# Date: 9/2/20
# Change Log: (Who, When, What)
# R. Melookaran, 9/2/20, created script)
# --------------------------------------------------------------

for i in range(1,100):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%5==0:
        print("Buzz")
    elif i%3==0:
        print("Fizz")
    else:
        print(i)