def fizz_buzz(n):
    i = 0
    while i <= n:
        if i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        elif i % 3 == 0 and i % 5 == 0:
            print("fizzBuzz")
        else:
            print(i)
        i += 1


# fizzBuzz(2)

# fizzBuzz(15)

# fizzBuzz(74)

# fizzBuzz(100)
