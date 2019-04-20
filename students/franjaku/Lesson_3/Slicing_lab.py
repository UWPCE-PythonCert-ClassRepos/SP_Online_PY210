#!/Lesson 3 Slicing Lab

def exchange_first_last(seq_in):

    seq1 = seq_in[0:1]
    seq2 = seq_in[1:len(seq_in)-1]
    seq3 = seq_in[len(seq_in)-1:len(seq_in)]

    return seq3+seq2+seq1

def remove_every_other(seq_in):

    seq_out=seq_in[0::2]

    return seq_out

def remove_first_last_4_every_other(seq_in):

    seq_out = seq_in[4:len(seq_in)-4:2]

    return seq_out

def reverse_reverse(seq_in):

    seq_out = seq_in[len(seq_in)-1::-1]

    return seq_out

def thirds_swap(seq_in):

    seq12 = seq_in[:len(seq_in)//3*2]
    seq3 = seq_in[len(seq_in)//3*2:len(seq_in)]

    seq_out = seq3+seq12

    return seq_out

if (__name__ == '__main__'):
    a_list = list(range(12))
    a_str = "abcdefghijkl"
    a_tuple = tuple(range(12))

    print('Test')

    print('exchange first and last items')
    assert exchange_first_last(a_list) == [11,1,2,3,4,5,6,7,8,9,10,0]
    assert exchange_first_last(a_str) == "lbcdefghijka"
    assert exchange_first_last(a_tuple) == (11,1,2,3,4,5,6,7,8,9,10,0)
    print('passed exchange tests')

    print('remove every other')
    assert remove_every_other(a_list) == [0,2,4,6,8,10]
    assert remove_every_other(a_str) == "acegik"
    assert remove_every_other(a_tuple) == (0,2,4,6,8,10)
    print('passed remove test')

    print('remove first 4, last 4 and every other remaining')
    assert remove_first_last_4_every_other(a_list) == [4,6]
    assert remove_first_last_4_every_other(a_str) == "eg"
    assert remove_first_last_4_every_other(a_tuple) == (4,6)
    print('passed remove first/last 4 and every other test')

    print('reverse list by slicing')
    assert reverse_reverse(a_list) == [11,10,9,8,7,6,5,4,3,2,1,0]
    assert reverse_reverse(a_str) == "lkjihgfedcba"
    assert reverse_reverse(a_tuple) == (11,10,9,8,7,6,5,4,3,2,1,0)
    print('passed reverse by slicing test')

    print('thirds swaping')
    assert thirds_swap(a_list) == [8,9,10,11,0,1,2,3,4,5,6,7]
    assert thirds_swap(a_str) == "ijklabcdefgh"
    assert thirds_swap(a_tuple) == (8,9,10,11,0,1,2,3,4,5,6,7)
    print('passed thirds swaping')

    print('Passed all tests')