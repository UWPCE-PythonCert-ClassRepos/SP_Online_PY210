#### Slicing Lab Exercises ####

# Sequences to test with functions
long_string = "This is a long string to test the functions"
nums = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
a_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g','h']


# Write a function that exchanges the first and last items
def first_last(seq):
    """This is a function that exchanges the first and last items
of a sequence.  This should work for any sequence."""
    return seq[-1:] + seq[1:-1] + seq[:1]

def every_other(seq):
    """Write a function that takes a sequence and removes
    every other item and returns the new sequence"""
    return seq[::2]

def missing_mid(seq):
    """Write a function that removes the first 4 and last
    4 items and then every other item in the remaining 
    middle sequence."""
    return seq[4:-4:2]

def backwards(seq):
    """Return a sequence in reverse order using only
    slicing."""
    return seq[::-1]

def by_thirds(seq):
    """Write a function that returns the last third,
    then first third, then middle third of a sequence
    in that order."""
    l = len(seq)
    # Function breaks if not an integer
    if l % 3 != 0:
        print('Rounding to nearest integer...')
    x = int(l/3)
    return seq[-x:] + seq[:x] + seq[x:-x]


# test the functions
if __name__ == "__main__":

    # tests for first_last
    assert first_last(long_string) == "shis is a long string to test the functionT"
    assert first_last(nums) == (15, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 1)
    assert first_last(a_list) == ['h', 'b', 'c', 'd', 'e', 'f', 'g','a']
    print('Tests for first_last: Passed')

    # tests for every_other
    assert every_other(long_string) == "Ti saln tigt ettefntos"
    assert every_other(nums) == (1, 3, 5, 7, 9, 11, 13, 15)
    assert every_other(a_list) == ['a', 'c', 'e', 'g']
    print('Tests for every_other: Passed')

    # tests for missing_mid
    assert missing_mid(long_string) == " saln tigt ettefnt"
    assert missing_mid(nums) == (5, 7, 9, 11)
    assert missing_mid(a_list) == []
    print('Tests for missing_mid: Passed')

    # tests for backwards
    assert backwards(long_string) == "snoitcnuf eht tset ot gnirts gnol a si sihT"
    assert backwards(nums) == (15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
    assert backwards(a_list) == ['h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
    print('Tests for backwards: Passed')

    # tests for by_thirds
    assert by_thirds(long_string) == " the functionsThis is a long string to test"
    assert by_thirds(nums) == (11, 12, 13, 14, 15, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    assert by_thirds(a_list) == ['g', 'h', 'a', 'b', 'c', 'd', 'e', 'f']
    print('Tests for by_thirds: Passed')


