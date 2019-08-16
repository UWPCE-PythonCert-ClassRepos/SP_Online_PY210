# Fizz Buzz Program
for i in range(100):
    fizz = (i+1) % 3
    buzz = (i+1) % 5

    if fizz == 0 and buzz == 0:
        print("FizzBuzz")
    elif fizz == 0:
        print("Fizz")
    elif buzz == 0:
        print("Buzz")
    else:
        print(i+1)
