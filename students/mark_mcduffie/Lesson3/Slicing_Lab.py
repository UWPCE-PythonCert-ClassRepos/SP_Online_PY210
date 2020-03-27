#Mark McDuffie
#Slicing Lab

#These are functions that take a sequence as an argument,
#and return a manipulated copy

#returns a sequence with the first and last element changed
def first_last(seq):
    first = seq[0]
    last = seq[-1]
    new = last + seq[1:-1] + first
    return new

#returns a sequence with every other element removed
def every_other(seq):
    x = len(seq)
    new = ''
    for i in range(x):
        if(i % 2 == 0):
            new += seq[i]
    return new

#returns a sequence with every other element removed
#as well as the first 4 and last 4 elements
def first_last_4(seq):
    removed = seq[4:-4]
    x = len(removed)
    new = ''
    for i in range(x):
        if(i % 2 == 0):
            new += removed[i]
    return new

#returns a given sequence in reverse order
def reverse(seq):
    new = seq[::-1]
    return new

#returns a sequence split up into 3 thirds, (first, middle, last)
#with the thirds reordered into last middle first
def thirds(seq):
    x = len(seq)
    first = ''
    second = ''
    third = ''
    for i in range(x):
        if(i < x/3):
            first += seq[i]
        elif(i >= x/3 and i < 2 * x /3):
            second += seq[i]
        else:
            third += seq[i]
    return third + first + second

#Tests to see if the functions return the expected result
seq = "this is a string"
assert first_last(seq) == "ghis is a strint"
assert every_other(seq) == "ti sasrn"
assert first_last_4(seq) == " sas"
assert reverse(seq) == "gnirts a si siht"
assert thirds(seq) == "tringthis is a s"
print("Tests Passed")