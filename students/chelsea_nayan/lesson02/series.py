# chelsea_nayan, UWPCE PYTHON 210, Lesson02: Fibonacci Series Exercise

# This function takes in n and returns the nth value in the fibonacci series starting with 0 index
def fibonacci(n):
    array = [0]*n # Created an array with size n (8 would create an array of length 8 filled with the value 0)
    array[0], array[1] = 0, 1 # Set up the first two numbers of the fibonacci series
    for item in range(len(array)): # This loop populates the rest of the array with the next numbers in fibonacci series
        if item >= 2:
            array[item] = array[item - 2] + array[item - 1]
    return(array[n - 1]) # Returns the nth value of the fibonacci series

# This function takes in n and returns the nth value in the lucas series. It is the same structure as the fibonacci function, but just changed the first index of the array to 2
def lucas(n):
    array = [0]*n # Created an array with size n (8 would create an array of length 8 filled with the value 0)
    array[0], array[1] = 2, 1 # Set up the first two numbers of the lucas series
    for item in range(len(array)): # This loop populates the rest of the lucas series numbers in the array
        if item >= 2:
            array[item] = array[item - 2] + array[item - 1]
    return(array[n - 1]) # Returns the nth value of the lucas series

# A generalized fibonacci function that takes in one parameter that determines which element in the series to print. The two optional parameters will have default values of 0 and 1 and determines the first two values for the series to be produced
def sum_series(n, num1 = 0, num2 = 1): # Set the default first two numbers in the series to the fibonacci ones
    array = [0]*n # Created an array with size n (8 would create an array of length 8 filled with the value 0)
    array[0], array[1] = num1, num2 # Set up the first two numbers of the generalized series, default is fibonacci
    for item in range(len(array)): # This loop populates the rest of the generalized series numbers in the array
        if item >= 2:
            array[item] = array[item - 2] + array[item - 1]
    return(array[n - 1]) # Returns the nth value of the generalized series

print('TESTS') # This block of code demonastrates that my three functions work properly
print('The 14th number in the fibonacci series is:', fibonacci(14))
print('The 10th number in the fibonacci series is:', fibonacci(10))
print()
print('The 8th number in the lucas series is:', lucas(8))
print('The 37th number in the lucas series is:', lucas(37))
print()
print('Using the default starting numbers, the 10th number of the generalized series is:', sum_series(10))
print('Using the lucas series starting numbers, the 37th number of the generalized series is:', sum_series(37, 2, 1))
print('Using 3 and 4 as the first two numbers in the series, the 6th number of the generalized series is:', sum_series(6, 3, 4))
