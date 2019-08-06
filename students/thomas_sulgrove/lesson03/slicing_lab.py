#!/usr/bin/env python3
##SP_Online_PY210 lesson03 Slicing lab https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/slicing.html

##with the first and last items exchanged
def exchange_first_last(seq):
    a_new_sequece = list(seq) #whatever it is, gunna make it a list
    a_new_sequece[0], a_new_sequece[-1] = a_new_sequece[-1], a_new_sequece[0] #exhange the first and last thing
    
    #return it as the same format as was given
    if isinstance(seq, tuple):
        return tuple(a_new_sequece)
    if isinstance(seq, str):
        return str(''.join(a_new_sequece))
    
    
#with every other item removed
def remove_other(seq):
    a_new_sequece = list(seq) #whatever it is, gunna make it a list
    a_new_sequece = a_new_sequece[::2] #take every other index
    
    #return it as the same format as was given
    if isinstance(seq, tuple):
        return tuple(a_new_sequece)
    if isinstance(seq, str):
        return str(''.join(a_new_sequece))
    
    
#with the first 4 and the last 4 items removed, and then every other item in the remaining sequence.  
def remove_four_and_other(seq):
    a_new_sequece = list(seq) #whatever it is, gunna make it a list
    a_new_sequece = a_new_sequece[4:-4:2] #'4:-4' start at 4th and end 4 from end, :2 take every other thing.
    
    #return it as the same format as was given
    if isinstance(seq, tuple):
        return tuple(a_new_sequece)
    if isinstance(seq, str):
        return str(''.join(a_new_sequece))


#with the elements reversed (just with slicing).
def reverse(seq):
    a_new_sequece = list(seq) #whatever it is, gunna make it a list
    a_new_sequece = a_new_sequece[::-1] #':-1' reverse it
    
    #return it as the same format as was given
    if isinstance(seq, tuple):
        return tuple(a_new_sequece)
    if isinstance(seq, str):
        return str(''.join(a_new_sequece))


#with the last third, then first third, then the middle third in the new order
def thirds(seq):
    a_new_sequece = list(seq)
    n = len(a_new_sequece) / 3
    first_third = a_new_sequece[0:int(round(n))]
    middle_third = a_new_sequece[int(round(n)):int(round(n*2))]
    last_third = a_new_sequece[int(round(n*2)):]
    a_new_sequece = last_third + first_third + middle_third
    
    #return it as the same format as was given
    if isinstance(seq, tuple):
        return tuple(a_new_sequece)
    if isinstance(seq, str):
        return str(''.join(a_new_sequece))
   
    
#test variables  
a_string = "mayo and bologna sammich"
a_tuple = (1, 2, 3, 5, 8, 13, 21, 34, 55, 89)

##exchange_first_last tests    
assert exchange_first_last(a_string) == "hayo and bologna sammicm"
assert exchange_first_last(a_tuple) == (89, 2, 3, 5, 8, 13, 21, 34, 55, 1)

##remove_other tests
assert remove_other(a_string) == "my n oon amc"
assert remove_other(a_tuple) == (1, 3, 8, 21, 55) 

#remove_four_and_other tests
assert remove_four_and_other(a_string) == " n oon a"
assert remove_four_and_other(a_tuple) == (8,) 
 
##reverse tests
assert reverse(a_string) == "hcimmas angolob dna oyam"
assert reverse(a_tuple) == (89, 55, 34, 21, 13, 8, 5, 3, 2, 1) 

##thirds tests
assert thirds(a_string) == " bologna sammichmayo and"
assert thirds(a_tuple) == (34, 55, 89, 1, 2, 3, 5, 8, 13, 21)







