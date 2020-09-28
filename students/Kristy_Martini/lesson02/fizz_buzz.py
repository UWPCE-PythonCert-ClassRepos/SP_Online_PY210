def fizz_buzz():
    """
    Function that prints numbers from 1-100 (inclusive) and will replace the number
    with "Fizz" if it is a multiple of 3, "Buzz" if it is a multiple of 5, or 
    "FizzBuzz" if it is a multiple of both 3 and 5.
    """
    for i in range(1,101):
        if not (i % 5) and not (i % 3):
            print("FizzBuzz")
        elif not (i % 3):
            print("Fizz")
        elif not (i % 5):
            print("Buzz")
        else:
            print(i)        

if __name__ == "__main__":
    fizz_buzz()