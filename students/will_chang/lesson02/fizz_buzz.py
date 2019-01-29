def test_fizz_buzz():
    """Runs through list of 1-100 inclusive:
    
    If divisible by 15: Print 'FizzBuzz'
    If divisible by 3: Print 'Fizz'
    If divisible by 5: Print 'Buzz'
    """
    for i in range(1,101):
        if(i % 3 == 0 and i % 5 == 0):
            print('FizzBuzz')
        elif(i % 3 == 0):
            print('Fizz')
        elif(i % 5 == 0):
            print('Buzz')
        else:
            print(i)