## Functions that take a sequence as an argument, and return a copy of that sequence ##

# Take seq as an argument and return a copy of seq with the first and last items exchanged
def exchange_first_last(seq):
    first_item = seq[:1]
    last_item = seq[-1:]
   
    a_new_sequence = last_item + seq[1:-1] + first_item
    #print("First and Last items exchanged", a_new_sequence)
    
    return a_new_sequence



# Take seq as an argument and return a copy of every other item removed
def every_other_item(seq):

   # print("Every other item removed", seq[::2])

    return seq[::2]


# Take seq as an argument with the first 4 and the last 4 items removed, and then every other item in the remaining sequence.
def first_last_fouritems_removed(seq):
   
   fitstlast4_removed = seq[4:-4:]

   next_everyother_item = fitstlast4_removed[::2]

   #print("First 4 and last 4 items removed", fitstlast4_removed)
   #print("Next print every other item", next_everyother_item) 
   #print(next_everyother_item) 

   return next_everyother_item


# Take seq as an argument with the elements reversed (just with slicing)
def elements_reversed(seq):

   # print("Elements reversed", seq[::-1])

    return seq[::-1]


# Take seq as an argument with the last third, then first third, then the middle third in the new order.
def last_first_middle3rd(seq):
     first_third = seq[:3]
     last_third = seq[-3:]
     newseq = seq[3:-3:]
 
     l = int(len(newseq)/2)
     
     middle_third = newseq[l-1: l+2]
 
     #print(last_third + first_third + middle_third)

     return (last_third + first_third + middle_third)



if __name__ == '__main__':

    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32, 25, 27, 44, 55, 66, 11, 15, 20)

    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple) == (20, 54, 13, 12, 5, 32, 25, 27, 44, 55, 66, 11, 15, 2)
    
    # Every other item removed
    assert every_other_item(a_string) == "ti sasrn"
    assert every_other_item(a_tuple) == (2, 13, 5, 25, 44, 66, 15)

    assert first_last_fouritems_removed(a_tuple) ==(5, 25, 44)
    assert first_last_fouritems_removed(a_string) == " sas"

    assert elements_reversed(a_tuple) == (20, 15, 11, 66, 55, 44, 27, 25, 32, 5, 12, 13, 54, 2)
    assert elements_reversed(a_string) == "gnirts a si siht"

    assert last_first_middle3rd(a_tuple) == (11, 15, 20, 2, 54, 13, 25, 27, 44)
   # assert last_first_middle3rd(a_string)


    print("All Tests Pass...")

""" 
def middle(s):
    if len(s) == 0:
        return ""
    elif len(s) % 2 != 0:
        print(s[len(s)//2])
        return s[len(s)//2]
    elif len(s) % 2 == 0:
        print(s[len(s)//2 - 1] + s[len(s)//2])
        return s[len(s)//2 - 1] + s[len(s)//2]

print(middle("this is a test")) """
