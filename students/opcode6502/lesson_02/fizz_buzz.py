# fizz_buzz.py
# opcode6502: SP_Online_PY210

def fizz_buzz():
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print ("i: " + str(i) + " FizzBuzz")
        elif i % 3 == 0:
            print ("i: " + str(i) + " Fizz")
        elif i % 5 == 0:
            print ("i: " + str(i) + " Buzz")
        else:
            print ("i: " + str(i))

fizz_buzz()
