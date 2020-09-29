# ---------------------------------------------------------------------------- #
# Title: slicing
# Description: Five functions to modify sequence data
#   #1 exchange_first_last - will exchange the first and last values
#   #2 every_other - will remove every other value in the sequence
#   #3 first4_last4_removed - will remove the first 4 and the last 4 values,
#   then it will only keep every other value in the remaining sequence
#   #4 reversed_order - used slicing to reverse sequence order
#   #5 reorder - take a sequence and reorder the last third, first third,
#                then the middle third
#
# ---------------------------------------------------------------------------- #

def exchange_first_last(seq):
    """
    Exchanges the first and last values
    :param seq: User inputs value they want to exchange first and last (seq)
    :return: Swaps the first and last values
    """
    first = seq[0]
    # The "first" variable gets the "0" position or first value
    last = seq[-1]
    # The "first" variable gets the "0" position or first value
    remain = seq[1:-1]
    # The "remain" variable includes every value minus the first and last value
    return last + remain + first
    # The return swaps the order of the first and last value

def every_other(seq):
    '''
    Removes every other value in the list
    :param seq: User inputs sequence value to display every other (seq)
    :return: every other value starting with the "0" position
    '''
    # The two (::) indicate the full list of values
    # The (2) indicates it will return every other value
    return seq[::2]

def first4_last4_removed(seq):
    '''
    will remove the first 4 and the last 4 values, then it will only keep every other value
    in the remaining sequence
    :param seq: User inputs sequence value (seq)
    :return: the sequence minus the first and last 4 values, then every other value in the
    remaining sequence
    '''
    # The first position (4) removes the first 4 character values
    # The (:) separates the next command
    # The (-4) is a negative and removes the 4 values from the end
    # The (2) indicates it will return every other value
    return seq[4:-4:2]

def reversed_order(seq):
    '''
    Used slicing to reverse sequence order
    :param seq: User inputs sequence value (seq)
    :return: Reversed order of sequence
    '''
    # The two (::) indicate the full list of values in the sequence
    # The (-1) is a negative and reverses order of all values
    return seq[::-1]

def reorder(seq):
    '''
    Take a sequence and reorder the last third, first third, then the middle third
    :param seq: User inputs sequence value (seq)
    :return: a new sequence order of last third, first third, then the middle third
    '''
    # first 1/3
    length = len(seq)
    # get the length of the sequence and divide it by 3
    first = length//3
    first_third = seq[:first]

    # remaining half
    length = len(seq)
    # get the remaining 2/3rds sequence
    remaining = length//3
    remaining_half = seq[remaining:]

    # middle 1/3
    length = len(remaining_half)
    # divide the remaining 2/3rds sequence in half
    middle = length//2
    # get left half
    middle_third = remaining_half[:middle]

    # last 1/3
    # get right half
    last_third = remaining_half[middle:]
    return last_third + first_third + middle_third

# run some tests

print(exchange_first_last("1this is a list of strings to test2"))
print(every_other("this is a list of strings to test"))
print(first4_last4_removed("this is a list of strings to test"))
print(reversed_order("this is a list of strings to test"))
print(reorder("FirstxSecondThirdx"))
print()

seq1 = "1this is a list of strings to test2"
seq2 = "this is a list of strings to test"
seq3 = "FirstxSecondThirdx"
assert exchange_first_last(seq1) == "2this is a list of strings to test1"
assert every_other(seq2) == "ti sals fsrnst et"
assert first4_last4_removed(seq2) == " sals fsrnst "
assert reversed_order(seq2) == "tset ot sgnirts fo tsil a si siht"
assert reorder(seq3) == "ThirdxFirstxSecond"

print("All tests passed!!")