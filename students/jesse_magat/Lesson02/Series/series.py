def fibonacci(n):
    if n==0:
        return 0 # Catch if the value is 0. If this error handling is skipped then function will error since '0' is not defined
    if n==1:
        return 1 # same logic as value '0' error handling above
 
    val_one = 0
    val_two = 1
    for i in range(n-1): #keeps looping --> skipped the first iteration
            val_final = val_one + val_two
            val_one = val_two # change the value of the first value to the second value
            val_two = val_final #New val_two value as the final value --> then repeats until the loop is done
            #print(i)
    return (val_final)
    
#fibonacci(5)



def lucas(n):
    if n==0:
        return 2 # Catch if the value is 0. If this error handling is skipped then function will error since '0' is not defined
    if n==1:
        return 1 # same logic as value '0' error handling above
    val_one = 2
    val_two = 1
    for i in range(n-1): #keeps looping --> skipped the first iteration
            val_final = val_one + val_two
            val_one = val_two # change the value of the first value to the second value
            val_two = val_final #New val_two value as the final value --> then repeats until the loop is done
            #print(i)
    return (val_final)
    
#lucas(5)



def sum_series(n,val_one=0, val_two=1):
    if n ==0:
        val_final = val_two #error handling to give the value of 2nd value when n = 0 (since adding 1st and 2nd values)
    elif n==1:
        val_final = val_one #error handling to give value 1st value when n = 1 (since it is adding zero it will equal 1st value)
    else:
        for i in range(2,n+1): #range start at 2; added one to match sequence of the two functions - so test would not fail
            val = val_one + val_two
            val_one = val_two
            val_two = val 
            val_final = val
    return (val_final) 
    

#sum_series(6,2,1) 


if __name__ == "__main__":
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(2) == 3
    assert lucas(3) == 4
    assert lucas(4) == 7
    assert lucas(5) == 11
    assert lucas(6) == 18
    assert lucas(7) == 29

    assert sum_series(6) == fibonacci(6)

    # test if sum_series matched lucas
    assert sum_series(6, 2, 1) == lucas(6)

    print("tests passed")