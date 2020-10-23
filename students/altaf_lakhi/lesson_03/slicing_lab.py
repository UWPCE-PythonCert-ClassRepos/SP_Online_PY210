
def exchange_first_last(seq):
    for i in seq:
        seq1 = seq[-1:] + seq[1:-1] + seq[:1]
        return seq1


def other_item_removed(seq):
    for i in seq:
        seq2 = seq[0::2]
        return seq2


def four_removed(seq):
    for i in seq:
        seq3 = seq[4:-4:2]
        return seq3


def elements_reversed(seq):
    for i in seq:
        seq4 = seq[::-1]
        return seq4


def thirds(seq):
    length = len(seq)
    for i in seq:
        first = (length//3)
        seq5 = seq[first*2:]+seq[0:first]+seq[first:first*2]
        return seq5

#Test

a_string ="this is a string"
a_tuple = (2, 54, 13, 12, 5, 32, 10, 54, 78, 83, 24, 61)

assert exchange_first_last(a_string) == "ghis is a strint"
assert other_item_removed(a_string) == "ti sasrn"
assert four_removed(a_string) == " sas"
assert elements_reversed(a_string) == "gnirts a si siht"
assert thirds(a_string) == "stringthis is a "
assert exchange_first_last(a_tuple) == (61, 54, 13, 12, 5, 32, 10, 54, 78, 83, 24, 2)
assert other_item_removed(a_tuple) == (2, 13, 5, 10, 78, 24)
assert four_removed(a_tuple) == (5, 10)
assert elements_reversed(a_tuple) == (61, 24, 83, 78, 54, 10, 32, 5, 12, 13, 54, 2)
assert thirds(a_tuple) == (78, 83, 24, 61, 2, 54, 13, 12, 5, 32, 10, 54)
print("test passed")


