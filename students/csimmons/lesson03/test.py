#!usr/bin/env/python3
seq = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
seq2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
seq3 = 'The quick brown fox jumps over the lazy dog'


def thirds(seq):
    thirds = len(seq)/3
    print(int(thirds))
    front = seq[:int(thirds)]
    middle = seq[int(thirds):(int(thirds)*2)]
    end = seq[(int(thirds)*2):]
    print(front)
    print(middle)
    print(end)
  

thirds(seq3)
