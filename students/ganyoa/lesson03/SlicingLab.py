def exchange_first_last(seq):
    # exchange the item in the first position with the last
    if len(seq) >= 2:
        seq = seq[-1:] + seq[1:-1] + seq[:1]
    return seq

def remove_every_other(seq):
    #remove every other item
    return seq[::2]

def first_last_four(seq):
    #remove the first four and last four, then remove every other item
    return seq[4:-4:2]

def reverse(seq):
    #reverse the sequence
    return seq[::-1]

def thirds(seq):
    #rearrange to show last third, first third, then middle third
    t = int(len(seq) / 3)
    return seq[-t:] + seq[:t] + seq[t:(t*2)]