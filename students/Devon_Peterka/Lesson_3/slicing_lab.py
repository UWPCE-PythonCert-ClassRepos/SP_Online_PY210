#!/usr/bin/env python3

'''
Create functions to take a sequence and create a copy except:
1) with the first and last items exchanged
2) with every other term removed
3) with the first and last (4) terms removed
4) with reversed elements
5) with last 1/3, then first 1/3, then middle 1/3 in the new order
'''

# first and last terms swapped.
def first_last(seq):
    return seq[-1:] + seq[1:-1] + seq[:1]

# with every other term removed.
def every_other(seq):
    return seq[::2]

# with first and last (4) removed.
def no_firstlast_four(seq):
    return seq[4:-4]

# with elements reversed.
def reverse_it_all(seq):
    return seq[::-1]

# with last 1/3, first 1/3, then middle
# last, then first, then middle == last 1/3 first, then the remainder in original order
def swap_thirds(seq):   #seq is odd length, bias to the last 1/3 sequence
    return seq[-len(seq)//3:] + seq[:-len(seq)//3]

#Test out the functions
if __name__ == '__main__':
    #Test Them Out:
    seq = "this is a string"
    assert first_last(seq) == 'ghis is a strint'
    assert every_other(seq) == 'ti sasrn'
    assert no_firstlast_four(seq) == ' is a st'
    assert reverse_it_all(seq) == 'gnirts a si siht'
    assert swap_thirds(seq) == 'stringthis is a '
    print('Tested Sequence =', seq)

    #and test again with a tuple
    seq = (2, 54, 13, 12, 5, 32)
    assert first_last(seq) == (32, 54, 13, 12, 5, 2)
    assert every_other(seq) == (2, 13, 5)
    assert no_firstlast_four(seq) == ()
    assert reverse_it_all(seq) == (32, 5, 12, 13, 54, 2)
    assert swap_thirds(seq) == (5, 32, 2, 54, 13, 12)
    print('Tested Sequence =', seq)

    #and test one final time with a longer list
    seq = [1, 4, 'a', 'bob', 32, 'yahoo', 12.3, 1, 2, 3, 4]
    assert first_last(seq) == [4, 4, 'a', 'bob', 32, 'yahoo', 12.3, 1, 2, 3, 1]
    assert every_other(seq) == [1, 'a', 32, 12.3, 2, 4]
    assert no_firstlast_four(seq) == [32, 'yahoo', 12.3]
    assert reverse_it_all(seq) == [4, 3, 2, 1, 12.3, 'yahoo', 32, 'bob', 'a', 4, 1]
    assert swap_thirds(seq) == [1, 2, 3, 4, 1, 4, 'a', 'bob', 32, 'yahoo', 12.3]
    print('Tested Sequence =', seq)

    print('\nAll Tests Passed\n')

