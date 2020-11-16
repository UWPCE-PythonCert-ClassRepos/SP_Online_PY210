#!usr/bin/env/python3
seq2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
seq3 = 'The quick brown fox jumps over the lazy dog'


def thirds(seq):
    thirds = len(seq)/3
    print(int(thirds))
    front = seq[:thirds]
    print(front)
    middle = seq[:thirds]
    end = seq[:thirds]
    print(middle)
    print(end)
  

thirds(seq2)