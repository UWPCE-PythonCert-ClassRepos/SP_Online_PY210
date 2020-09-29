def fibonacci(n):
    i = 0
    while i <= 10:
        print(n)
        n += n
        print(n)
        i += 1


# Works
# fibonacci(10)


def lucas_numbers(n):
    i = 0
    while i <= 10:
        print(n)
        nn = n - 1
        print(nn)
        print(n + nn)
        i += 1


# Works
# lucasNumbers(10)

def sum_series(n, *x):
    option = input(
        "Please insert number 1 for fibanocci series; or 0 for lucas numbers series.")
    if option == '' or option == 1:
        fibonacci(n)
    else:
        lucas_numbers(n)


sum_series(10)
