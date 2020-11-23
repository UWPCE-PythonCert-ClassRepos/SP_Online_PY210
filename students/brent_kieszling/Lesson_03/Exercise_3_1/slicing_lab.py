#-------------------------------------------#
#Tittle: slicing_lab, PYTHON210 - Exercise 3.1
#Desc: Functions For Differing Slices
#Change Log: (Who, When, What)
#Brent Kieszling, <2020-Nov-4>, created file
#-------------------------------------------#

#DATA---------------------------------------
a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)
a_long_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)


#PROCESS------------------------------------
def exchange_first_last(sequence):
    """Exchange the first and last item of the sequence
    
    Args:
        sequence (sequence): Initial sequence to be modified
        
    Returns:
        a_new_sequence (sequence): Modified sequence
    """
    length = len(sequence)
    first = sequence[0:1]
    last = sequence[length-1:length]
    middle = sequence[1:length-1]
    a_new_sequence = last + middle + first
    return a_new_sequence

def remove_every_other(sequence):
    """Remove every other item of the sequence
    
    Args:
        sequence (sequence): Initial sequence to be modified
        
    Returns:
        a_new_sequence (sequence): Modified sequence
    """
    a_new_sequence = sequence[::2]
    return a_new_sequence

def remove_ends_4(sequence):
    """Remove the first and last four items from the sequence
    
    Args:
        sequence (sequence): Initial sequence to be modified
        
    Returns:
        a_new_sequence (sequence): Modified sequence
    """
    a_new_sequence = sequence[4:len(sequence)-4]
    return a_new_sequence

def reverse(sequence):
    """Reverse the order of the sequence
    
    Args:
        sequence (sequence): Initial sequence to be modified
        
    Returns:
        a_new_sequence (sequence): Modified sequence
    """
    a_new_sequence = sequence[::-1]
    return a_new_sequence

def swap_thirds(sequence):
    """Split sequence into thirds and restructure as last, first, and middle.
    
    Args:
        sequence (sequence): Initial sequence to be modified
        
    Returns:
        a_new_sequence (sequence): Modified sequence
    """
    length = len(sequence)
    third = length//3
    first = sequence[:third]
    middle = sequence[third: length-third]
    last = sequence[length-third:]
    a_new_sequence = last + first + middle
    return a_new_sequence


#PRESENTATION INPUT/OUTPUT------------------





assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

assert remove_every_other(a_string) == "ti sasrn"
assert remove_every_other(a_tuple) == (2, 13, 5)

assert remove_ends_4(a_string) == " is a st"
assert remove_ends_4(a_tuple) == ()
assert remove_ends_4(a_long_tuple) == (5, 6, 7, 8)

assert reverse(a_string) == "gnirts a si siht"
assert reverse(a_tuple) == (32, 5, 12, 13, 54, 2)

assert swap_thirds(a_string) == "tringthis is a s"
assert swap_thirds(a_tuple) == (5, 32, 2, 54, 13, 12)

print("Tests passed.")







