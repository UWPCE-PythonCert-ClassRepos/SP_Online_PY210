NE = 101
NS = 1

for num in range(NS,NE): 
    if num % 3 != 0 and num % 5 != 0:
        print(num)
    if num % 3 == 0 and num % 5 == 0: 
        print("FizzBuzz") 
    if num % 3 == 0 and num % 5 != 0:
        print("Fizz")
    if num % 3 != 0 and num % 5 == 0:
        print("Buzz")
    else: 
        pass