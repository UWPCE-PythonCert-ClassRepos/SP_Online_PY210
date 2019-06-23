def first_last(seq):
    return (seq[-1:]+seq[1:-1]+seq[:1])

def every_other(seq):
    return (seq[0::2])

def remove_high_low(seq):
    return (seq[4:-4])
def reverse(seq):
    return (seq[-1::-1])
def change_order(seq):
    split = int(len(seq)/3)
    return (seq[2*split:]+seq[:split]+seq[split:2*split])

a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32,2,6,1,0,'my',6)

assert first_last(a_string) == "ghis is a strint"
assert first_last(a_tuple) == (6, 54, 13, 12, 5, 32,2,6,1,0,'my',2)
assert every_other(a_string) == "ti sasrn"
assert every_other(a_tuple) == (2, 13, 5, 2,1,'my')
assert remove_high_low(a_string) == " is a st"
assert remove_high_low(a_tuple) ==  (5, 32,2,6)
assert reverse(a_string) == 'gnirts a si siht'
assert change_order(a_tuple) == (1, 0, 'my', 6, 2, 54, 13, 12, 5, 32, 2, 6)
assert change_order(a_string) == 'stringthis is a '





