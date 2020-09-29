# Fizz Buzz Exercise
for i in range(0,101):
    if (i%3==0 and i%5 ==0 ):
        print(f"FizzBuzz:{i} ",end = "")
        if i % 10 == 0 :
            print("\n")
    elif (i % 3 == 0 and i%5 !=0): 
        print(f"Fizz:{i} ",end = "")
        if i % 10 == 0 :
            print("\n")
    elif (i % 3 != 0 and i%5 ==0): 
        print(f"Buzz:{i} ",end = "")
        if i % 10 == 0 :
            print("\n")
    #else:
    #    pass

