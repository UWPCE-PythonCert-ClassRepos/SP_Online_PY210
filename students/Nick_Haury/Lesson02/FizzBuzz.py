'''
implementation of the well known "FizzBuzz" "puzzle" as follows:
print the numbers between 1 and 100 inclusive
*except*
for the numbers divisible by 3, instead print Fizz
for the numbers divisible by 5, instead print Buzz
for the numbers divisible by both, instead print FizzBuzz
'''

if __name__ == "__main__":
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print (i)