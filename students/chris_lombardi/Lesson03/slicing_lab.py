#UWPCE, PY210
#Lesson03, Slicing Lab

def first_last(seq):
    """Swaps the first and last values in a sequence"""
    #Test for a sequence of multiple values
    if len(seq) <= 1:
        return seq

    first = seq[:1]
    last = seq[-1:]
    return last + seq[1:-1] + first

def rem_every_other(seq):
    """Removes every other value in a sequence"""
    return seq[::2]

def rem_first_last_four(seq,num=4):
    """
    Removes the first and last x elements in a sequence and then
    every other value remaining.

    param seq: The sequence to be evaluated.
    param num=4: number of elements to remove from the front and end
    """

    if len(seq) <= 1:
        return seq
    if len(seq) < num * 2:
        x = int(len(seq) / 2)
        if len(seq) % 2 == 0:
            x = x - 1
        alt_seq=seq[x:x*-1]
        return rem_every_other(alt_seq)
    else:
        alt_seq = seq[num:num*-1]
        return rem_every_other(alt_seq)

def reverse_seq(seq):
    return seq[::-1]

def last_first_mid_third(seq):
    x = int(len(seq)/3)
    return seq[x*-1:] + seq[0:x] + seq[x:-x]

if __name__ == '__main__':
    str_test = 'hello my name is'
    l = [0,1,2,3,4,5,6,7,8,10,12,14]
    t = (2,4,6,8,10,12,14,16,18)
    l1 = [1]

    #Test first_last()
    print('Testing first_last()...')
    assert first_last(str_test) == 'sello my name ih' #Test string sequence
    assert first_last(l) == [14,1,2,3,4,5,6,7,8,10,12,0] #Test list sequence
    assert first_last(t) == (18,4,6,8,10,12,14,16,2) #Test tuple sequence
    assert first_last(l1) == [1] #Test for sequence of size 1

    #Test remove_every_other()
    print('Testing remove_every_other()...')
    assert rem_every_other(str_test) == 'hlom aei'
    assert rem_every_other(l) == [0,2,4,6,8,12]
    assert rem_every_other(t) == (2,6,10,14,18)
    assert rem_every_other(l1) == [1]

    #Test rem_first_last_four
    print('Testing rem_first_last_four()...')
    assert rem_first_last_four(str_test) == 'om a'
    assert rem_first_last_four(l) == [4,6]
    assert rem_first_last_four(t) == (10,)
    assert rem_first_last_four(l1) == [1]

    print('Testing reverse_seq()...')
    assert reverse_seq(str_test) == 'si eman ym olleh'
    assert reverse_seq(l) == [14,12,10,8,7,6,5,4,3,2,1,0]
    assert reverse_seq(t) == (18,16,14,12,10,8,6,4,2)
    assert reverse_seq(l1) == [1]

    print('Testing last_first_mid_third()...')
    assert last_first_mid_third(str_test) == 'me ishello my na'
    assert last_first_mid_third(l) == [8,10,12,14,0,1,2,3,4,5,6,7]
    assert last_first_mid_third(t) == (14,16,18,2,4,6,8,10,12)
    assert last_first_mid_third(l1) == [1]

    print('All tests pass.')