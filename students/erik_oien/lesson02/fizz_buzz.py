def fizz_buzz():
    for i in range(1, 101):
        div3 = i % 3 == 0
        div5 = i % 5 == 0
        if div3 and div5:
            print("FizzBuzz")
        if div3:
            print("Fizz")
        if div5:
            print("Buzz")
        else:
            print(i)

fizz_buzz()