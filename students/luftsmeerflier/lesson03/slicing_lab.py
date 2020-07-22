#/usr/bin/env python3

# with the first and last items exchanged

def exchange_first_last(seq):	
	return seq[-1:] + seq[1:-1] + seq[:1]

def every_other_removed(seq):
    return seq[::2]

# with the first 4 and the last 4 items removed, and the nevery other item in the remaning sequence
def first_and_last_four_removed(seq):
	return seq[4:-4:2]

#with the elements reversed (just with slicing)
def elements_reversed(input):
	return input[::-1]

# Pass
assert exchange_first_last("hello") == "oellh"
assert exchange_first_last((1,2,3)) == (3,2,1)

# Pass
assert every_other_removed("hello") == "hlo"
assert every_other_removed((1,2,3,4,5)) == (1,3,5)

# Pass 
assert first_and_last_four_removed("helloworld") == "o"
assert first_and_last_four_removed((1,2,3,4,5,6,7,4,3,2,1)) == (5,7) 

# Pass
assert elements_reversed("hello") == "olleh"
assert elements_reversed((1,2,3)) == (3,2,1)


print("All tests pass")

