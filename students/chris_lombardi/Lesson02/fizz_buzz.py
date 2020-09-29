#UWPCE PY210
#Lesson02, Fizz Buzz

def eval_fizzbuzz(num):
    """Evaluate whether a number is divisble by 3 and/or 5"""
    if num % 3 == 0 and num % 5 ==0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num

def main():
    for i in range(1,101):
        print(eval_fizzbuzz(i))

main()