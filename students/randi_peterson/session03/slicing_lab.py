def exchange_firstandlast(seq):
#Return sequence with first and last elements exchanged
    seq_first = seq[0:1]
    seq_last = seq[-1:]
    seq_middle = seq[1:-1]
    new_seq = seq_last + seq_middle + seq_first
    return new_seq

def remove_everyother(seq):
    #Return sequence with every other item removed
    new_seq = seq[0:len(seq):2]
    return new_seq

def fourandfour(seq):
    #Return sequence with first four and last four items and every other of the remaining items removed
    new_seq = seq[4:-4:2]
    return new_seq

def reverse_elements(seq):
    #Return elements reversed
    new_seq = seq[::-1]
    return new_seq

def reorder_thirds(seq):
    #Return sequence in the new order: last third, first third, middle third
    if (len(seq)%3) != 0:
        print('Warning: input sequence length was not a multiple of 3. Results may not be what you want due to rounding.')
    third = int(len(seq)/3)
    first_third = seq[0:third]
    second_third = seq[third:-third]
    third_third = seq[-third:]
    new_seq = third_third + first_third + second_third
    return new_seq


#Run test cases
strtest = 'hello there how are you?'
tuptest = (1,2,3,4,5,6,7,8,9,10,11,12)
lsttest = [13,14,15,16,17,18,19,20,21,22,23,24]

if __name__ == "__main__":
    #Test first and last flip
    assert exchange_firstandlast(strtest) == '?ello there how are youh'
    assert exchange_firstandlast(tuptest) == (12, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 1)
    assert exchange_firstandlast(lsttest) == [24, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 13]

    #Test remove every other
    assert remove_everyother(strtest) == 'hloteehwaeyu'
    assert remove_everyother(tuptest) == (1,3,5,7,9,11)
    assert remove_everyother(lsttest) == [13,15,17,19,21,23]

    #Test remove first and last four and every other remaining
    assert fourandfour(strtest) == 'oteehwae'
    assert fourandfour(tuptest) == (5, 7)
    assert fourandfour(lsttest) == [17, 19]

    #Test reverse elements
    assert reverse_elements(strtest) == '?uoy era woh ereht olleh'
    assert reverse_elements(tuptest) == (12,11,10,9,8,7,6,5,4,3,2,1)
    assert reverse_elements(lsttest) == [24,23,22,21,20,19,18,17,16,15,14,13]


    #Test reorder thirds
    assert reorder_thirds(strtest) == 'are you?hello there how '
    assert reorder_thirds(tuptest) == (9,10,11,12,1,2,3,4,5,6,7,8)
    assert reorder_thirds(lsttest) == [21,22,23,24,13,14,15,16,17,18,19,20]

    print("tests passed")

