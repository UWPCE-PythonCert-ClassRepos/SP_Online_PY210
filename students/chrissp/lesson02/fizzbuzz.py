def fizz_buzz():

    for i in range(1, 101):
        result = ""
        if i % 3 == 0:
            result = result + "Fizz"
        if i % 5 == 0:
            result = result + "Buzz"
        if result == "":
            result = str(i)
        print(result)

fizz_buzz()
