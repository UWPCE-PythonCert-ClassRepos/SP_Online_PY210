#--------------------------------------------------------------#
# Title: Lesson 3,
# Description: Fun slicing sequences
# ChangeLog (Who,When,What):
# JEmbury, 9/19/2020, created new script
#--------------------------------------------------------------#

def exchange_first_last(seq):
    new_seq = seq[1:-1]
    newer_seq = seq[-1:] + new_seq + seq[:1]
    return newer_seq

def every_other_remove(seq):
    return seq[0::2]

def remove4(seq):
    if len(seq)>8:
        return seq[4:-4:2]
    else:
        return seq[:0]

def reverse_seq(seq):
    return seq[::-1]

def rotate_thirds(seq):
    cut = len(seq)//3
    return seq[2*cut:] + seq[:cut] + seq[cut:2*cut]


#--------------------------------------------------------------#
if __name__ == '__main__':
    print('....\nActivating test sequence\n....\n')
    assert(exchange_first_last('hello there')) == 'eello therh'
    assert(exchange_first_last((2,54,13,12,5,32))) == (32,54,13,12,5,2)
    assert(every_other_remove((2,54,13,12,5,32))) == (2,13,5)
    assert(every_other_remove('hello there')) == 'hlotee'
    assert(remove4((2,54,13,12,5,32))) == ()
    assert(remove4((2,54,13,12,5,6,32,2,4,5,6))) == (5,32)
    assert(remove4('hello there')) == 'ot'
    assert(reverse_seq('hello there')) == 'ereht olleh'
    assert(reverse_seq((2,54,13,12,5,32))) == (32,5,12,13,54,2)
    assert(rotate_thirds((3,4,5))) == (5,3,4)
    assert(rotate_thirds('yellow')) == 'owyell'

    print("All tests have passed! Horray!")