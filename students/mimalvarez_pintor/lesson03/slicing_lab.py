# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 22:22:44 2020

@author: miriam
"""

#Slicing Lab
def exchange_first_last(seq):
    return(seq[-1:]+seq[1:-1]+seq[:1])
#print(exchange_first_last(a_string))
#print(exchange_first_last(a_tuple))

def every_other_rmv(seq):
    return(seq[0::2])
#print(every_other_rmv(a_string))
#print(every_other_rmv(a_tuple))

def FirstLastFourRmv_EveryOther(seq):
    return(seq[4:-4:2])
#print(FirstLastFourRmv_EveryOther(a_string))
#print(FirstLastFourRmv_EveryOther(a_tuple))
    
def reverse(seq):    
    return (seq[-1::-1])
#print(reverse(a_string))
#print(reverse(a_tuple))

def change_order(seq):
    third = int(len(seq)/3)
    return (seq[2*third:]+seq[:third]+seq[third:2*third])
#print(change_order(a_string))
#print(change_order(a_tuple))

#TEST
a_string = "this is a very interesting string that will be used for testing"
a_tuple = (2, 54, 13, 12, 5, 32, 30, 31, 32, 33, 34, 35, 26)

assert exchange_first_last(a_string) == "ghis is a very interesting string that will be used for testint"
assert exchange_first_last(a_tuple) == (26, 54, 13, 12, 5, 32, 30, 31, 32, 33, 34, 35, 2)
assert every_other_rmv(a_string) == "ti savr neetn tigta ilb sdfrtsig"
assert every_other_rmv(a_tuple) == (2, 13, 5, 30, 32, 34, 26)
assert FirstLastFourRmv_EveryOther(a_string) == " savr neetn tigta ilb sdfrts"
assert FirstLastFourRmv_EveryOther(a_tuple) ==  (5, 30, 32)
assert reverse(a_string) == 'gnitset rof desu eb lliw taht gnirts gnitseretni yrev a si siht'
assert reverse(a_tuple) ==(26, 35, 34, 33, 32, 31, 30, 32, 5, 12, 13, 54, 2)
assert change_order(a_string) == 'l be used for testingthis is a very interesting string that wil'
assert change_order(a_tuple) == (32, 33, 34, 35, 26, 2, 54, 13, 12, 5, 32, 30, 31)