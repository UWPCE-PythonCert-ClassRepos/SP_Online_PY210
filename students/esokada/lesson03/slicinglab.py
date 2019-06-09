def exchange_first_last(seq):
    '''Return a sequence with the first and last elements switched.'''
    return seq[-1:] + seq[1:-1] + seq[:1]

def every_other_removed(seq):
    '''Return a sequence with every other element removed.'''
    return seq[::2]

def first_four(seq):
    '''Return a sequence with the first and last four elements removed, and every other skipped.'''
    return seq[4:-4:2]

def reverse(seq):
    '''Return a sequence with the elements in reverse order.'''
    return seq[::-1]

def last_third(seq):
    '''Return a sequence in the order of: last third, first third, middle third.'''
    #Splitting exactly in thirds for sequences with a length divisible by 3:
    if len(seq) % 3 == 0:
        size = len(seq)//3
    #Adding padding for sequences with a length not divisible by 3:
    else:
        size = len(seq)//3 + 1
    return seq[size*2:] + seq[:size] + seq[size:size*2]


#tests

a_string = "abcde"
a_list = [1, 2, 3, 4, 5, 6]

assert exchange_first_last(a_string) == "ebcda"
assert exchange_first_last(a_list) == [6, 2, 3, 4, 5, 1]

assert every_other_removed(a_string) == "ace"
assert every_other_removed(a_list) == [1, 3, 5]

firstfourtest = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

assert first_four(firstfourtest) == [5, 7]

assert reverse(a_string) == "edcba"
assert reverse(a_list) == [6, 5, 4, 3, 2, 1]

assert last_third(a_string) == "eabcd"
assert last_third(a_list) == [5, 6, 1, 2, 3, 4]

print("tests passed")