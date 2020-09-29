def fbzz(x):
    for i in range(x+1):
#this line has to be here, or will have wrong answer at 3 or 5
        if i%3==0 & i%5==0:
            print('FizzBuzz')
        elif i%3 == 0:
            print('Fizz')
        elif i%5 == 0:
            print('Buzz')
        else:
            print(i)
print(fbzz(100))