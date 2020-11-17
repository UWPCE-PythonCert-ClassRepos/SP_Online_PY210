a_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
b_list = ['dog','cat','monkey','bird', 'fox']
a_string = 'It was a dark and stormy night'
b_string = 'Gaius'
c_string =  'Julius'
d_string = 'Ceasar'

seq = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
seq2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
#seq = ['dog','cat','monkey','bird', 'fox']
def exchange_first_last(seq):
    seq[0], seq[-1] = seq[-1], seq[0]
    print(seq)


def remove_every_other(seq):
    del seq[1::2]
    print(seq)

def remove_four_begin_end(seq):
    middle = seq[4:-4:2]
    print(middle)
    
def reverse(seq):
    print(seq[::-1])

def thirds(seq):
    third = len(seq)/3
    front = seq[:int(third)]
    middle = seq[int(third):(int(third)*2)]
    end = seq[(int(third)*2):]
    print(front)
    print(middle)
    print(end)
    print(end + front + middle)