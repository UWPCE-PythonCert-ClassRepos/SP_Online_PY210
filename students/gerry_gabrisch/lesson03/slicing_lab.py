def exchange_first_last(seq): 
    '''Takes a sequence as input and places the last item first
       the first item last, and leave all other remaining items 
       in their original indexes.'''
    #Get the last item in the sequence...
    end = seq[-1]
    #Get the first item in the sequence...
    start = seq[0]
    #Get everything in the sequence between the first and last elements...
    seq = seq[1:-1]
    #Lists have different ways of maninulating elements.  Check if it'
    # a list and rebuild it.
    if type(seq).__name__ == 'list':
        seq.insert(0,end)
        seq.append(start)
        return seq 
    #If the input was a string, identify it and add it together.
    if type(seq).__name__ == 'str':
        seq = end + seq + start
        return seq 
    #and because tuples are immutable concert it to a list, do the exchange, then cast
    #the list back to a tuple...
    if type(seq).__name__ == 'tuple':
        seq = list(seq)
        seq.insert(0,end)
        seq.append(start)
        return tuple(seq)         

def remove_every_other_item(seq):
    '''Removes every odd numbered item in a squence
       and returns a new sequence.'''
    seq = seq[::2]
    return seq

def remove_first_and_last_4(seq):
    '''removes the first four elements and the last four elements
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
    positions = len(seq)-1
    #For lists...
    if type(seq).__name__ == 'list':
        #make an empty list to hold the reversal...
        reversed = []
        #go through the list backwards and append the elements to the list...
        while positions >=0:
            reversed.append(seq[positions])
            positions -= 1
        return reversed
    #for strings...
    if type(seq).__name__ == 'str':
        #make empty string to hold the reversal...
        reversed = ''
        #go through backwards and concantonate the elements in reverse...
        while positions >=0:
            reversed = reversed + seq[positions]
            positions -= 1
        return reversed
    #For tuples just create a list from the tuple, dot the same as a list,
    #then convert the list back to a tuple...
    if type(seq).__name__ == 'tuple':
        seq = list(seq)
        reversed = []
        while positions >=0:
            reversed.append(seq[positions])
            positions -= 1
        return tuple(reversed)
    
def mix_thirds(seq):
    '''for any sequence return an new sequence
    with the last third, then first third, 
    then the middle third in the new order.'''
    #Get the length of the squence...
    seqlength = len(seq)
    if seqlength < 3:
        return "Sequence to small for this function."
    else:
        #divide the sequence lenght by 3 using integer division to handle sequence lenghts 
        #with an odd number of elements or those seqlengths not multiples of 3.
        firstpart = seqlength//3
        lastpart = seqlength - seqlength//3
        #For lists...
        if type(seq).__name__ == 'list':
            return seq[lastpart:] + seq[:-lastpart] +seq[firstpart+1:lastpart] 
        #for strings...
        if type(seq).__name__ == 'str':
            #return the mix.
            return seq[lastpart:] + seq[:-lastpart] +seq[firstpart+1:lastpart]
        #For tuples just create a list from the tuple, dot the same as a list,
        #then convert the list back to a tuple...
        if type(seq).__name__ == 'tuple':
            seq = list(seq)
            mixedlist = [] + seq[lastpart:] + seq[:-lastpart] +seq[firstpart+1:lastpart] 
            return tuple(mixedlist)    



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