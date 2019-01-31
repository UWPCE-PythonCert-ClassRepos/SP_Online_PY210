def fibonnaci(n):
    """Runs recursive function to define the fibonnaci sequence: fibonnaci(n) = fibonnaci(n-2) + fibonnaci(n-1).
       
    fibonnaci(0) = 0, index zero of the fibonacci sequence.
    fibonnaci(1) = 1, index one of the fibonnaci sequence.
    Input n will return the value of index n of the fibonnaci sequence.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonnaci(n - 2) + fibonnaci(n - 1)
    
    
def lucas(n):
    """Runs recursive function to define the lucas sequence: lucas(n) = lucas(n-2) + lucas(n-1).
       
    lucas(0) = 2, index zero of the lucas sequence.
    lucas(1) = 1, index one of the lucas sequence.
    Input n will return the value of index n of the lucas sequence.
    """
    if n == 0:
        return 2
    elif n == 1:
        return 1
    return lucas(n - 2) + lucas(n - 1)
    
    
def sum_series(n, index_0_value = 0, index_1_value = 1):
    """Runs recursive function to define a sequence given values for the first two indices: num_series(n) = num_series(n-2) + num_series(n-1).
       
    num_series(0) = index_0_value, index zero of the sequence. The default value for this is 0, but can be replaced by another input.
    num_series(1) = index_1_value, index one of the sequence. The default value for this is 1, but can be replaced by another input.
    Input n will return the value of index n of the sequence.
    """
    if n == 0:
        return index_0_value
    elif n == 1:
        return index_1_value
    return sum_series(n - 2, index_0_value, index_1_value) + sum_series(n - 1, index_0_value, index_1_value)


# This block of code is used to test the fibonnaci(n) function.
assert fibonnaci(0) == 0, "The value of the 0th index in the fibonnaci sequence is incorrect."
assert fibonnaci(1) == 1, "The value of the 1st index in the fibonnaci sequence is incorrect."
assert fibonnaci(2) == 1, "The value of the 2nd index in the fibonnaci sequence is incorrect."
assert fibonnaci(5) == 5, "The value of the 5th index in the fibonnaci sequence is incorrect."
assert fibonnaci(10) == 55, "The value of the 10th index in the fibonnaci sequence is incorrect."

# This block of code is used to test the lucas(n) function.
assert lucas(0) == 2, "The value of the 0th index in the lucas sequence is incorrect."
assert lucas(1) == 1, "The value of the 1st index in the lucas sequence is incorrect."
assert lucas(2) == 3, "The value of the 2nd index in the lucas sequence is incorrect."
assert lucas(5) == 11, "The value of the 5th index in the lucas sequence is incorrect."
assert lucas(10) == 123, "The value of the 10th index in the lucas sequence is incorrect."

# This block of code is used to test the sum_series(n) function in the default state.
assert sum_series(0) == 0, "The value of the 0th index in the sum_series default sequence is incorrect."
assert sum_series(1) == 1, "The value of the 1st index in the sum_series default sequence is incorrect."
assert sum_series(2) == 1, "The value of the 2nd index in the sum_series default sequence is incorrect."
assert sum_series(5) == 5, "The value of the 5th index in the sum_series default sequence is incorrect."
assert sum_series(10) == 55, "The value of the 10th index in the sum_series default sequence is incorrect."

# This block of code is used to test the sum_series(n) function as a lucas sequence.
assert sum_series(0,2,1) == 2, "The value of the 0th index in the sum_series lucas sequence is incorrect."
assert sum_series(1,2,1) == 1, "The value of the 1st index in the sum_series lucas sequence is incorrect."
assert sum_series(2,2,1) == 3, "The value of the 2nd index in the sum_series lucas sequence is incorrect."
assert sum_series(5,2,1) == 11, "The value of the 5th index in the sum_series lucas sequence is incorrect."
assert sum_series(10,2,1) == 123, "The value of the 10th index in the sum_series lucas sequence is incorrect."

# This block of code is used to test the sum_series(n) function with a 0th index of 5 and 1st index of 3.
assert sum_series(0,5,3) == 5, "The value of the 0th index in the sum_series general sequence is incorrect."
assert sum_series(1,5,3) == 3, "The value of the 1st index in the sum_series general sequence is incorrect."
assert sum_series(2,5,3) == 8, "The value of the 2nd index in the sum_series general sequence is incorrect."
assert sum_series(5,5,3) == 30, "The value of the 5th index in the sum_series general sequence is incorrect."
assert sum_series(10,5,3) == 335, "The value of the 10th index in the sum_series general sequence is incorrect."