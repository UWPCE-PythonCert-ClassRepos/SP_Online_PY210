# Write some functions that take a sequence as an argument, and return a copy of that sequence:
# The first and last items exchanged for a string
a_string = "this is a string"
def exchange_first_last_string(a_string):
    first = (a_string[0])
    middle = (a_string[1:-1])
    last = (a_string[-1])
    a_new_sequence = last + middle + first
    #print(type(a_new_sequence))
    return print(a_new_sequence)
# Function called here
exchange_first_last_string(a_string)

#assert exchange_first_last_string(a_string) == 'ghis is a strint'
print()

#  The first and last items exchanged for a tuple
a_tuple = (2, 54, 13, 12, 5, 32)

def exchange_first_last_tuple(a_tuple): # use tuple assignment
    (s1, s2, s3, s4, s5, s6) = a_tuple # unpack the tuple and assign
    a_new_sequence = ((s6, s2, s3, s4, s5, s1)) # pack and assign to the order needed
    return print(a_new_sequence) # how can I return my variable without a print statement?

exchange_first_last_tuple(a_tuple)
#assert exchange_first_last_tuple(a_tuple) == (32, 54, 13, 12, 5, 2)
