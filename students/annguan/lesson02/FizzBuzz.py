#Lesson 2 Fizz Buzz Exercise
#Run program "FizzBuzz()"

def FizzBuzz():
    """FizzBuzz prints the numbers from 1 to 100 inclusive:
    for multiples of three print Fizz;
    for multiples of five print Buzz
    for numbers which are multiples of both three and Five, print FizzBuzz
    """
    for i in range (1,101):
        if i % 3 == 0 and i % 5 ==0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)