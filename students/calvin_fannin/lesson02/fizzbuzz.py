

for num in range(1,101):
    result =''
    #if divisable by 3 add fizz to string
    if (num % 3 == 0):
            result = 'Fizz'
    #if divisable by 5 add buzz to the string
    if (num % 5 == 0):
            result = result + 'Buzz'
    if (result == ''):
        #if it string has nothing in it then print the number
        print (num)
        #print the string if it has a value
    else:
        print(result)

