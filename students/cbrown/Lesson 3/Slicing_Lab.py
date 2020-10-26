# Sequence Slicing Lesson 2
#First and Last Items Removed
def seq_slice(sequence):
    '''takes a sequence and returns a copy with first & last exchanged
    '''
    first_item = sequence[0:1]
    last_item = sequence[-1:]
    middle_copy = sequence[1:-1]

    new_seq = last_item + middle_copy + first_item

    return new_seq

assert seq_slice(['Carol','John','Bob']) == ['Bob','John','Carol']
assert seq_slice("Master Plan") == "naster PlaM"

#Every Other Item Removed
def every_other(sequence):
    seq_copy = sequence[0::2]
    return seq_copy

assert every_other(['Plan','Agree','First']) == ['Plan','First']

#First Four Last Four
def first_last(sequence):
    first_four = sequence[4:-4]
    other = first_four[::2]
    return other

assert first_last('When I Say This') == '  a '

#Elements Reversed
def reversed(sequence):
    reverse = sequence[::-1]
    return reverse

assert reversed('Ann Arbor, Michigan') == 'nagihciM ,robrA nnA'

#Last Third. First Third. Middle Third.
def thirds(sequence):
    num = int(len(sequence)/3)
    first = sequence[:num]
    second = sequence[num:(num + num)]
    third = sequence[(num + num):]

    switched_seq = third + first + second

    return switched_seq

assert thirds('California') == 'rniaCalifo'
