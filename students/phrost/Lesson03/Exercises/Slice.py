### Lesson_3 - Slice Lab

def vice_versa(seq):
    """ Return the sequence with the first and last items swapped """
    return seq[-1::] + seq[1:-1] + seq[:1]

def every_other(seq):
    """ Returns sequence with every other item deleted """
    return seq[::2]

def four(seq):
    """ Returns sequence with the first and last four elements removed, and ever
        other of the remaining items."""
    return seq[4:-4][::2]

def inverse(seq):
    """ Returns sequence reversed """
    return seq[::-1]

def three(seq):
    """ Divides sequence by three then moves the last third to the begining,
        the first third to the middle and fiannly the middle third to the end. """
    thirds = len(seq) // 3
    return seq[(thirds * 2)::] + seq[:thirds:] + seq[thirds:(thirds *2):]

###TESTS###
a_string = "this is a string"
a_tuple = (1,4,9,16,25,36,49,64,81,100,111,124)

###seq 1 test###
assert vice_versa(a_string) == "ghis is a strint"
assert vice_versa(a_tuple) == (124,4,9,16,25,36,49,64,81,100,111,1)

###seq 2 test###
assert every_other(a_string) == "ti sasrn"
assert every_other(a_tuple) == (1,9,25,49,81,111)

###seq 3 test###
assert four(a_string) == " sas"
assert four(a_tuple) == (25,49)

###seq 4 test###
assert inverse(a_string) == "gnirts a si siht"
assert inverse(a_tuple) == (124,111,100,81,64,49,36,25,16,9,4,1)

###seq 5 test###
a_string = "stringthis is a "
a_tuple = (25,36,49,64,1,4,9,16,25,81,100,111,124)

print("All assertions passed!")
