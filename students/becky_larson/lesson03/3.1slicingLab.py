#!/usr/bin/env python """
"""Exchange first and last values in the list and return"""
"""I learned that using the = sign, they refer to the same object, so I used copy.  Could also use list command"""

"""tuple assert failing:  RETURNING:  (32, (54, 13, 12, 5, 32), 2). How to remove the parans"""
"""Is there a way to use same code for both string and tuple?"""
def exchange_first_last(seq):
  if(type(seq)) == str:
    a_new_sequence = seq[len(seq)-1] + seq[1:(len(a_string)-1)] + seq[0]
  else:
    a_new_sequence = seq[len(seq)-1] ,seq[1:(len(a_string)-1)] , seq[0]
  print("RETURNING: ", a_new_sequence)
  return a_new_sequence

def remove_everyother(seq):
  a_new_sequence = seq[::2]
  print("RETURNING: ", a_new_sequence)
  return a_new_sequence

def remove_1stLast4_everyother(seq):
  a_new_sequence = seq[4:-4:2]
  print("RETURNING: ", a_new_sequence)
  return a_new_sequence

def elements_reversed(seq):
  a_new_sequence = seq[::-1]
  print("RETURNING: ", a_new_sequence)
  return a_new_sequence

def each_third(seq):
  thirds=len(seq)/3
  firstThird = ("0:" + thirds)
  print(firstThird) 
  print(thirds) 
  return
  a_new_sequence = seq[::-1]
  print("RETURNING: ", a_new_sequence)
  return a_new_sequence
  
def run_assert():
  print("run_assert")
#  assert exchange_first_last(a_string) == "ghis is a strint"
#  print("string passed")
#  assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
#  print("tuple passed")
#  assert remove_everyother(a_string) == "ti sasrn"
#  print("string passed")
#  assert remove_everyother(a_tuple) == (2, 13, 5)
#  print("tuple passed")
#  assert remove_1stLast4_everyother(a_string) == " sas"
#  print("string passed")
#  assert remove_1stLast4_everyother(a_tuple) == ()
#  print("tuple passed")
#  assert elements_reversed(a_string) == "gnirts a si siht"
#  print("string passed")
#  assert elements_reversed(a_tuple) == (32, 5, 12,13,54, 2)
#  print("tuple passed")
  assert each_third(a_string) == "gnirts a si siht"
  print("string passed")
  assert each_third(a_tuple) == (5,32,2,54,13,12)
  print("tuple passed")

  
a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)

#number_list = list(range(1, 25))

if __name__ == "__main__":
#  run_assert()
  each_third(a_tuple)
  
#with the first and last items exchanged.
#with every other item removed.
#with the first 4 and the last 4 items removed, and then every other item in the remaining sequence.
#with the elements reversed (just with slicing).
#with the last third, then first third, then the middle third in the new order.