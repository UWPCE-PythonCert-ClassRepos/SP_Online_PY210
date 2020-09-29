#Slicing Lab: Exercise 3.1

a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)

print('Function 1: exchange_first_last(seq)')
print('Function 2: every_other_removed(seq')
print('Function 3: trim_four(seq)')
print('Function 4: reverse(seq)')
print('Function 5: third_shuffle(seq)')


def exchange_first_last(seq):
    if len(seq) == 1:
        return seq
    else:
        return seq[-1:] + seq[1:len(seq)-1] + seq[:1]

def every_other_removed(seq):
    return seq[::2]

def trim_four(seq):
    return seq[4:len(seq)-4]

def reverse(seq):
    return seq[::-1]

def third_shuffle(seq):
    length = len(seq)
    first_th = round(length/3)
    last_th = round(2*length/3)
    return seq[last_th:] + seq[:first_th] + seq[first_th:last_th]


'''
Assertion tests for both:
   Strings and Tuples

'''
assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

assert every_other_removed(a_string) == 'ti sasrn'
assert every_other_removed(a_tuple) == (2,13,5)

assert trim_four(a_string) == ' is a st'
assert trim_four(a_tuple) == ()

assert reverse(a_string) == 'gnirts a si siht'
assert reverse(a_tuple) == (32,5,12,13,54,2)

assert third_shuffle(a_string) == 'tringthis is a s'
assert third_shuffle(a_tuple) == (5,32,2,54,13,12)

