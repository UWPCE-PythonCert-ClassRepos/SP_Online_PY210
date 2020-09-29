# Print numbers 1 to 100,
# replacing multiples of 3 with "Fizz"
# and multiples of 5 with "Buzz"
# and multiples of both with "FizzBuzz"
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(str(i))