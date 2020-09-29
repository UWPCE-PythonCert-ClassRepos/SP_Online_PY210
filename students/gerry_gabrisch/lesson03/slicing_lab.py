
def exchange_first_last(seq): 
    '''Takes a sequence as input and places the last item first
       the first item last, and leave all other remaining items 
       in their original indexes.'''
    return seq[-1:]+seq[1:-1]+seq[0:1]
    
def remove_every_other_item(seq):
    '''Removes every odd numbered item in a squence
       and returns a new sequence.'''
    seq = seq[::2]
    return seq

def remove_first_and_last_4(seq):
    '''Removes the first four elements and the last four elements
    of a list. Only odd positioned (every other) element will be returned.
    This function will a text message if the sequence is too small for this function.'''
    #check sequence length...
    if len(seq) <=9:
        return "Sequence to small for this function."
    else:
        return seq[4:-4][::2]

def reverse_seq(seq):
    '''reverses a sequence by slicing'''
    #Get the length of the squence...
    return seq[::-1]
        
    
def mix_thirds(seq):
    '''For any sequence return a new sequence
    with the last third, then first third, 
    then the middle third in the new order.'''
    #Get the length of the squence...
    seqlength = len(seq)
    if seqlength < 3:
        return "Sequence to small for this function."
    else:
        #divide the sequence length by 3 using integer division to handle sequence lengths 
        #with an odd number of elements or those seqlengths not multiples of 3.
        firstpart = seqlength//3
        lastpart = seqlength - seqlength//3
        return seq[lastpart:] + seq[:-lastpart] +seq[firstpart+1:lastpart] 
        
if __name__ == "__main__":
    # run some tests
    
    seq ="123456789abcd"
    seqtup =(1,2,3,4,5,6,7,8,9,'a', 'b', 'c', 'd')
    seqlist = [1,2,3,4,5,6,7,8,9,'a', 'b', 'c', 'd']
    seqsmall ="12"
    seqtupsmall =(1,2)
    seqlistsmall = [1,2]    
    
    
    assert exchange_first_last(seq) == 'd23456789abc1'
    assert exchange_first_last(seqtup) == ('d',2,3,4,5,6,7,8,9,'a', 'b', 'c', 1)
    assert exchange_first_last(seqlist) == ['d',2,3,4,5,6,7,8,9,'a', 'b', 'c', 1]
    print('exchange_first_last() passed')
    
    assert remove_every_other_item(seq) == "13579bd"
    assert remove_every_other_item(seqtup) == (1,3,5,7,9,'b','d')
    assert remove_every_other_item(seqlist) == [1,3,5,7,9,'b','d']
    print('remove_every_other_item() passed')
    
    assert remove_first_and_last_4(seq) == "579"
    assert remove_first_and_last_4(seqtup) == (5,7,9)
    assert remove_first_and_last_4(seqlist) == [5,7,9]
    assert remove_first_and_last_4(seqsmall) ==  "Sequence to small for this function."
    assert remove_first_and_last_4(seqtupsmall) ==  "Sequence to small for this function."
    assert remove_first_and_last_4(seqlistsmall) ==  "Sequence to small for this function." 
    print('remove_first_and_last_4() passed')
    
    assert reverse_seq(seq) == "dcba987654321"
    assert reverse_seq(seqtup) == ('d', 'c', 'b', 'a', 9, 8, 7, 6, 5, 4, 3, 2, 1)
    assert reverse_seq(seqlist) == ['d', 'c', 'b', 'a', 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print('reverse_seq() passed')
    
    assert mix_thirds(seq) == 'abcd12346789'
    assert mix_thirds(seqlist) == ['a', 'b', 'c', 'd', 1, 2, 3, 4, 6, 7, 8, 9]
    assert mix_thirds(seqtup) == ('a', 'b', 'c', 'd', 1, 2, 3, 4, 6, 7, 8, 9)
    assert mix_thirds(seqsmall) ==  "Sequence to small for this function."
    assert mix_thirds(seqtupsmall) ==  "Sequence to small for this function."
    assert mix_thirds(seqlistsmall) ==  "Sequence to small for this function."     
    print  ('mix_thirds() passed')