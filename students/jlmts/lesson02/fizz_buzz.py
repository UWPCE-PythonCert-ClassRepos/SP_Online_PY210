# lesson 2.3: fizz buzz exercise, J. Umetsu

# program to print numbers from 1 to 100
    # print "fizz" for multiples of three
    # print "buzz" for multiples of five
    # print "fizzbuzz" for multiples of both three and five 
def fizz_buzz(n):
    if n>100:
        return 0
    elif (n%3 and n%5) > 0:
        print(n)
        return fizz_buzz(n+1)
    elif n%3==0 and n%5== 0:
        print('FizzBuzz')
        return fizz_buzz(n+1)
    elif n%3==0:
        print('Fizz')
        return fizz_buzz(n+1)
    elif n%5==0:
        print('Buzz')
        return fizz_buzz(n+1)
        
fizz_buzz(1)
        