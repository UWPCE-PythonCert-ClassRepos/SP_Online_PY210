def exchange_first_last(seq):
    if len(seq) >= 2:
        seq = seq[-1:]+seq[1:-1]+seq[:1]
    return seq