for i in range(100):
    x = i + 1
    fizz_buzz = '' 
    if x % 3 == 0:
        fizz_buzz = "Fizz"
    if x % 5 == 0:
        fizz_buzz += "Buzz"
    if len(fizz_buzz):
        print(fizz_buzz)
    else:
        print(x)
