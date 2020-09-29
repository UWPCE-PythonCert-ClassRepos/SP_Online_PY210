def exchange_first_last(seq):
    seq1=list(seq)
    temp = seq1[0]
    seq1[0] =seq1[-1]
    seq1[1] = temp
    seq2=' '.join(seq1)
    print(seq2)
