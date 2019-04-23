
def multiples_of_num(num1,num2):
    if num1%num2 ==0:
        return True
    else:
        return False

def fizz_buzz():
    for num in range(1,101):
        if multiples_of_num(num,3) and multiples_of_num(num,5):
            print('FizzBuzz')
        elif multiples_of_num(num,3):
            print('Fizz')
        elif multiples_of_num(num,5):
            print('Buzz')
        else:
            print(num)


fizz_buzz()
