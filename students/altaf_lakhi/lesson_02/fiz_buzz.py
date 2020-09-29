def fizzbuzz():
    for n in range(0,101):
        if n % 3 == 0 and n % 5 == 0:
            print('fizzbuzz')
            n = 1  
        elif n % 3 == 0:
            print('fizz')
        elif n % 5 == 0:
            print('buzz')
        else:
            print(n)
    
    
fizzbuzz()