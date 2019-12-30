def exchange_first_last(seq):
    '''Returns a copy of a sequence with the first and last items
    exchanged.'''
    a_new_sequence = seq[-1:] + seq[1:-1] + seq[:1]
    return a_new_sequence

def remove_every_other(seq):
    '''Returns a copy of a sequence withevery other item removed.'''
    a_new_sequence = seq[::2]
    return a_new_sequence
   
def first_last_four_removed(seq):
    '''Returns a copy of a sequence with the first 4 and the last
    4 items removed, and then every other item in the remaining
    sequence.'''
    a_new_sequence = seq[4:-4:2]
    return a_new_sequence

def seq_reverse(seq):
    '''Returns a copy of a sequence with the elements reversed. '''
    a_new_sequence = seq[::-1]
    return a_new_sequence

def seq_third(seq):
    '''Returns a copy of a sequence with the last third, then
    first third, then the middle third in the new order.'''
    a = len(seq)//3
    a_new_sequence =seq[2*a:] +seq[:2*a]
    return a_new_sequence
   
string1='aAbBcCdDeEfFgGhH'
tuple1=(1,2,3,4,5,6,7,8,9,10,11,12)
list1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o']

if __name__ == "__main__":
    # run some tests
    assert exchange_first_last(string1) == 'HAbBcCdDeEfFgGha'
    assert exchange_first_last(tuple1) == (12,2,3,4,5,6,7,8,9,10,11,1)
    assert exchange_first_last(list1) == ['o','b','c','d','e','f','g','h','i','j','k','l','m','n','a']
   
    assert remove_every_other(string1) == 'abcdefgh'
   
    assert first_last_four_removed(tuple1) == (5,7)

    assert seq_reverse(list1) == ['o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
   
    assert seq_third(tuple1) == (9, 10, 11, 12, 1, 2, 3, 4, 5, 6, 7, 8)

    print("tests passed")