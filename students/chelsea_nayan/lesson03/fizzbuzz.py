# chelsea_nayan, UWPCE PYTHON210, Lesson02:Fizz Buzz Exercise


# This function prints the numbers from low to high inclusive. For multiples of three, "Fizz" is printed instead of the numer and for multiples of five, "Buzz" is printed. If the number both divisble by three and five, it prints out "FizzBuzz"
def fizzbuzz(low, high):
    i = low
    while i <= high:
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0 and i % 5 != 0:
            print("Fizz")
        elif i % 5 == 0 and i % 3 != 0:
            print("Buzz")
        else:
            print(i)
        i += 1

#The example given in the lesson page
fizzbuzz(1,100)
