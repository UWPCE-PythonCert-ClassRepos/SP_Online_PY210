#!/usr/bin/env python3

#slicing Lab: Exercise 1 
#all the functions had been tested in if __name__=="__main__" block of the code
print('First Task:exachange_first_last(seq)')
print('Second Task:remove_other_item(seq)')
print('Third Task:remove_first_last_four(seq)')
print('Fourth Task:reverse_elements(seq)')
print('Fifth Task:first_last_middle(seq)')

def exchange_first_last(seq):
    """
    with the first and last items exchanged from sequence seq
    """
    return (seq if len(seq)==1 else seq[-1:]+seq[1:len(seq)-1]+seq[:1])

def remove_other_item(seq):
    """
    this function will return the sequence seq with
    every other item removed
    """
    return (seq[0:len(seq):2])

def remove_first_last_four(seq):
    """
    this function will return the value of sequence seq
    with first and last 4 items removed
    and rest sequence with every other item removed
    """
    return (seq[4:-4:2])
    
def reverse_elements(seq):
    """
    this function will return
    reverse of the sequence seq
    """
    return (seq[len(seq)-1::-1])
def first_last_middle(seq):
    """
    it will return new sequence of seq - last third then
    first third and then middle third
    """
    return (seq[len(seq)-3:]+seq[:3]+seq[(len(seq)//2)-1:(len(seq)//2)+2])
            
if __name__=="__main__":
    a_string = "this is a string"
    assert exchange_first_last(a_string) == "ghis is a strint"
    a_tuple = (2, 54, 13, 12, 5, 32)
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
    assert remove_other_item(a_string)== "ti sasrn"
    seq=[0,1,2,3,4,5,6,7,8,9,10]
    assert remove_first_last_four(seq) == [4,6]
    assert remove_first_last_four(a_string) == ' sas'
    assert reverse_elements(seq)==[10,9,8,7,6,5,4,3,2,1,0]
    seq=list(range(0,25))
    assert first_last_middle(seq) == [22, 23, 24, 0, 1, 2, 11, 12, 13]
