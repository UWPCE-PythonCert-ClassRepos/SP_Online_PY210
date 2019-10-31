#Fizz Buzz exercise, created by Niels Skvarch
#updated to include stop+step for inclusion of "100"
#is it better practise to just step the stop step up by one or to include the 3 variables and pass them to range?

for i in range(101):
    if i % 3 == 0 and i % 5 == 0:
        print("fizz buzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)
		

		