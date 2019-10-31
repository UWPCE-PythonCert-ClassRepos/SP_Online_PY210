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
   
seq1='abcdefghijklmnop'
seq2=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p')
seq3=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']

print(exchange_first_last(seq2))
print(remove_every_other(seq1))
print(first_last_four_removed(seq1))

print(seq_reverse(seq1))
print(seq_third(seq1))

if __name__ == "__main__":
    # run some tests
    assert exchange_first_last(seq1) == 'pbcdefghijklmnoa'
    assert exchange_first_last(seq2) == ('p','b','c','d','e','f','g','h','i','j','k','l','m','n','o','a')
    assert exchange_first_last(seq3) == ['p','b','c','d','e','f','g','h','i','j','k','l','m','n','o','a']




    print("tests passed")