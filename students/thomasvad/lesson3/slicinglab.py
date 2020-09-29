
def seq1(seq):
    '''swaps th first and last items of a sequence'''
    newseq = seq[-1:] + seq[1:-1] + seq[:1]
    return newseq


def seq2(seq):
    '''returns every other item removed'''
    newseq = seq[::2]
    return newseq


def seq3(seq):
    '''removes the first 4, last 4 and every other item'''
    newseq = seq[4:-4:2]
    return newseq


def seq4(seq):
    '''returns elements reversed'''
    newseq = seq[::-1]
    return newseq

def seq5(seq):
    """returns the last third, then first third, then the middle third of a sequence"""
    apart = int(len(seq)/3)
    newseq = seq[-apart:] + seq[:apart] + seq[apart:-apart]
    return newseq

if __name__ == "__main__":
#test
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)

    assert seq1(a_string) == "ghis is a strint"
    assert seq1(a_tuple) == (32, 54, 13, 12, 5, 2)

    assert seq2(a_string) == "ti sasrn"
    assert seq2(a_tuple) == (2, 13, 5)

    assert seq3(a_string) == " sas"
    assert seq3(a_tuple) == ()

    assert seq4(a_string) == "gnirts a si siht"
    assert seq4(a_tuple) == (32, 5, 12, 13, 54, 2)

    assert seq5(a_string) == "tringthis is a s"
    assert seq5(a_tuple) == (5, 32, 2, 54, 13, 12)

    print('passed test')
