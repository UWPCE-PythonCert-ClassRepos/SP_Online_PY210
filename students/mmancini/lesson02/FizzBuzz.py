def fizz_buzz(iBeg, iEnd):
    for i in range(iBeg, iEnd):
        if (i%3 == 0 and i%5 == 0):
            print (str(i) + " FizzBuzz")
        elif (i%3 == 0):
            print (str(i) + " Fizz")
        elif i%5 == 0:
            print (str(i) + " Buzz")

        else:
            print (str(i))

beg=1
end=100
fizz_buzz(beg, end)