# slicing_lab.py
# Lisa Ferrier, Python 210: Lesson 03 Exercise

def exchange_first_last(seq):
    '''This function exchanges the first and last items in a sequence '''
    seq2 = seq[-1:]+seq[1:-1]+seq[:1]
    return seq2

def remove_every_other(seq):
    '''This function removes every other item in a sequence. '''
    seq2 = seq[::2]
    return seq2

def remove_first_last_4_every_other(seq):
    '''This function removes the first and last 4 items in a sequence, then every other item removed.'''
    seq2 = seq[4:-4:2]
    return seq2

def reverse_elements(seq):
    '''This functions reverses the order of items in a sequence'''
    seq2 = seq[(len(seq))::-1]
    return seq2


def thirds_rearrange(seq):
    '''
    This function evaluates a sequence, splits it into three pieces (first, mid, last) and rearranges the items in a new order. Finally, the three pieces are reassembled in the following order:
    last + first + mid
    '''
    seq_len= (len(seq))
    thirds = int(seq_len/3)
    first = seq[0:thirds]
    mid = seq[thirds:thirds*2]
    last = seq[seq_len-thirds-1:]
    return(last+first+mid)


exchange_first_last('hotdog')

remove_every_other('winter_is_coming.')

remove_first_last_4_every_other('this_is_a_longer_string.')

reverse_elements('racecar backwards is racecar')

thirds_rearrange('split me into thirds and rearrange')

if __name__ == "__main__":
    a_string = 'snowpocalypse'
    a_tupel = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)

    assert exchange_first_last(a_string) == 'enowpocalypss'
    assert exchange_first_last(a_tupel) == (15,1,2,3,4,5,6,7,8,9,10,11,12,13,14,0)
    assert remove_every_other(a_string) == 'sopclpe'
    assert remove_every_other(a_tupel) == (0,2,4,6,8,10,12,14)
    assert remove_first_last_4_every_other(a_string) == 'pcl'
    assert remove_first_last_4_every_other(a_tupel) == (4,6,8,10)
    assert reverse_elements(a_string) == 'espylacopwons'
    assert reverse_elements(a_tupel) == (15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0)
    assert thirds_rearrange(a_string) == ('lypsesnowpoca')
    assert thirds_rearrange(a_tupel) == (10,11,12,13,14,15,0,1,2,3,4,5,6,7,8,9)
    print("tests passed.")
