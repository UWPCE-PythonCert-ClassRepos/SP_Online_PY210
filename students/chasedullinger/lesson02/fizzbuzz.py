# PY210 Lesson 02 FizzBuzz - Chase Dullinger

def FizzBuzz(upperBound=100,Fizz=3,Buzz=5):
    for i in range(upperBound+1):
        result = ""
        if i % Fizz == 0:
            result += "Fizz"
        if i % Buzz == 0:
            result += "Buzz"
        if not result:
            result = i
        print(result)


if __name__=="__main__":
    FizzBuzz()
