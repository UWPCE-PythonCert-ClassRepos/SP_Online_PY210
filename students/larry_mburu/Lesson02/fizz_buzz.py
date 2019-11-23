def fizz_buzz(): 
    for num in range(1, 16): 
        if (num % 3 == 0 ) and (num % 5 == 0):
            print(num)
            print("FizzBuzz") 
        if num % 3 == 0: 
            print(num)
            print("Fizz")
        if num % 5 == 0: 
            print(num)
            print("Buzz")

if __name__ == '__main__': 
    fizz_buzz()