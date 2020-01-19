def swap_fir_la(seq):
    """Swaps the first and last elements of a finite sequence"""
    fir=seq[0:1]
    la=seq[len(seq):len(seq)-2:-1]
    mid=seq[1:len(seq)-1]
    return la+mid+fir

def remove_mod2(seq):
    """removes every other item"""
    return seq[::2]

def fourfour_mod2(seq):
    """removes first and last 4 elements and then every other"""
    return seq[4:-4:2]

def uno_reverse(seq):
    """reverses the sequence"""
    return seq[::-1]

def third(seq):
    f=seq[0:len(seq)//3]
    m=seq[len(seq)//3:2*len(seq)//3]
    l=seq[2*len(seq)//3:len(seq)]
    return l+f+m