#!usr/bin/env/python3
seq = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
seq2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
seq3 = 'The quick brown fox jumps over the lazy dog'


def exchange_first_last(seq):
    if type(seq) == str:
        first = seq[0]
        last = seq[-1]
        mid = seq[1:-1]
        newstr= last + mid + first
        return(newstr)
    else:
        seq[0],seq[-1] = seq[-1],seq[0]
        return(seq)

print('list')
print(exchange_first_last(seq2))
print ('string')
print(exchange_first_last(seq3))