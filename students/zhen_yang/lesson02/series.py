# define function fibonacci()
def fibonacci(num):
    if num == 0 :
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)

# define function lucas()
def lucas(num):
    if num == 0 :
        return 2 
    elif num == 1:
        return 1 
    else:
        return lucas(num-1) + lucas(num-2)


# define the sum_series()
def sum_series(num,*argv):
    if argv: # using optional parameters 
        if num == 0 :
           return argv[0] 
        elif num == 1:
           return argv[1] 
        else:
           return sum_series(num-1,argv[0],argv[1]) + sum_series(num-2,argv[0],argv[1])
    else:# no optional paramter then producing fibonnaci number
        if num == 0 :
            return 0
        elif num == 1:
            return 1
        else:
            return sum_series(num-1,0,1) + sum_series(num-2,0,1)

# run some tests
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

assert lucas(4) == 7

# test that sum_series matches fibonacci
assert sum_series(5) == fibonacci(5)
assert sum_series(7, 0, 1) == fibonacci(7)

# test if sum_series matched lucas
assert sum_series(5, 2, 1) == lucas(5)

# test if sum_series works for arbitrary initial values
assert sum_series(0, 3, 2) == 3
assert sum_series(1, 3, 2) == 2
assert sum_series(2, 3, 2) == 5
assert sum_series(3, 3, 2) == 7
assert sum_series(4, 3, 2) == 12
assert sum_series(5, 3, 2) == 19

print("tests passed")
