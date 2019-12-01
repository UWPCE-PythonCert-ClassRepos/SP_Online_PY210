def fizz_buzz(): 
    for num in range(1, 16): 
        if (num % 3 == 0) and (num % 5 == 0):
            print("FizzBuzz") 
        elif num % 3 == 0: 
            print("Fizz")
        elif num % 5 == 0: 
            print("Buzz")
        else:
            print(num)

if __name__ == '__main__': 
    fizz_buzz()