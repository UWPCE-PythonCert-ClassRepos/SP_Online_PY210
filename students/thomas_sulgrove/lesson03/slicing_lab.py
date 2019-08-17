#!/usr/bin/env python3
##SP_Online_PY210 lesson03 Slicing lab https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/slicing.html

def exchange_first_last(seq):
    #seq[-1:] last item
    #seq[1:-1] middle items
    #seq[:1] first item
    #exchagne the first and last items.
    return seq[-1:] + seq[1:-1] + seq[:1]

def remove_other(seq):
    #return every other item
    return seq[::2] 
    
    
def remove_four_and_other(seq):
    #remove the first and last 4 items, then return everything else
    return seq[4:-4:2]
    
def reverse(seq):
    #reverse the order of the items
    return seq[::-1]

def thirds(seq):
    #find the # of indexes to split into thirds
    n = len(seq) / 3
    #return last third, then the first third, then the middle third.
    #return seq[n*2:] + seq[0:n] + seq[n:n*2]
    return seq[int(round(n*2)):] + seq[0:int(round(n))] + seq[int(round(n)):int(round(n*2))]
    
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
assert thirds(a_string) == " sammichmayo and bologna"
assert thirds(a_tuple) == (34, 55, 89, 1, 2, 3, 5, 8, 13, 21)

