#!usr/bin/env/python3
seq = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
seq2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
seq3 = 'The quick brown fox jumps over the lazy dog'

def exchange_first_last(seq):
    seq[0],seq[-1] = seq[-1],seq[0]
    return(seq)

def exchange_first_last_str(seq):
    alt_seq = seq
    first = seq[0]
    last = seq[-1]

    mutable_str[0],mutable_str[-1] = mutable_str[-1],mutable_str[0]
    return(seq)
str = input("Enter a string : ")
new_str = str[-1:] + str[1:-1] + str[:1]
print(new_str)

print(exchange_first_last(seq2))
print(exchange_first_last_str(seq3))