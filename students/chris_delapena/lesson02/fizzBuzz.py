#Write program that prints 1 to 100
#for multiples of three print fizz
#for multiples of 5 print buzz
#for multiples of 3 and 5 write fizzbuzz

def fizzBuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
