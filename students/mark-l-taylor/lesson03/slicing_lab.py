''' Slicing Lab
Write some functions that take a sequence as an argument, and return a copy of that sequence:

- with the first and last items exchanged.
- with every other item removed.
- with the first 4 and the last 4 items removed, and then every other item in the remaining sequence.
- with the elements reversed (just with slicing).
- with the last third, then first third, then the middle third in the new order.
'''

def exchange_first_last(seq):
    '''Return sequence with the first and last items exchanged'''
    #Handle a single item sequence, cannot exchange so just return
    if len(seq) == 1:
        return seq
    else:        
        return seq[-1:] + seq[1:-1] + seq[0:1]
    
def remove_every_other_item(seq):
    '''Return sequence with every other item removed'''
    return seq[0::2]

def remove_first_last_4(seq):
    '''Return sequence with the first 4 and last 4 items removed'''
    return seq[4:-4]

def reverse(seq):
    '''Return sequence with the elements reversed'''
    return seq[::-1]
    
    
def reorder_thirds(seq):
    '''Return sequence with the last third, then first third, then the middle third in the new order.
       In the event of a remainder in the dividing of the sequence, the extra will be in end of the new sequence'''
    third = len(seq)//3
    return seq[-1 * third:] + seq[0:third] + seq[third:-1*third]
    
if __name__ == "__main__":
    a_string = "this is a string"
    a_short_string = 'a'
    a_tuple = (2, 54, 13, 12, 5, 32)
    a_empty_seq = ''
    

    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
    assert exchange_first_last(a_short_string) == 'a'
    assert exchange_first_last(a_empty_seq) == ''
  
    assert remove_every_other_item(a_string) == "ti sasrn"
    assert remove_every_other_item(a_tuple) == (2,13,5)
    assert remove_every_other_item(a_short_string) == 'a'
    assert remove_every_other_item(a_empty_seq) == ''

    
    assert remove_first_last_4(a_string) == ' is a st'
    assert remove_first_last_4(a_tuple) == ()
    assert remove_first_last_4(a_short_string) == ''
    assert remove_first_last_4(a_empty_seq) == ''

    assert reverse(a_string) == 'gnirts a si siht'
    assert reverse(a_tuple) == (32, 5, 12, 13, 54, 2)
    assert reverse(a_short_string) == 'a'
    assert reverse(a_empty_seq) == ''
    
    assert reorder_thirds(a_string) == 'tringthis is a s'
    assert reorder_thirds(a_tuple) == (5, 32, 2, 54, 13, 12)
    assert reorder_thirds(a_short_string) == 'a'
    assert reorder_thirds(a_empty_seq) == ''
    
    print('Passed all test.')