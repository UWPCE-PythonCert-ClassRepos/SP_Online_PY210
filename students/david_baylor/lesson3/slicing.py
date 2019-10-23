"""
slicing.py
By David Baylor on 10/10/19
uses python 3

Demonstrates basic slicing.
"""

def exchange_first_last(seq):
    """exchange the first last item of the sequence"""
    first = seq[:1]
    last = seq[-1:]
    seq[:1], seq[-1:] = last, first
    return seq

def remove_every_other(seq):
    """remove every other item in the sequence"""
    new_list = []
    for i in range(len(seq)):
        if not i % 2:
            new_list.append(seq[i])
    return new_list

def remove_first_last_4(seq):
    """remove the first and last 4 items in the lsit"""
    del seq[:4]
    del seq[-4:]
    return seq

def reverse_seq(seq):
    """reverse the sequence"""
    return seq[::-1]

def move_thirds(seq):
    """move the last third (rounded to the nerest integer) to the front"""
    third = int(round(len(seq)/3))
    last_third = seq[(-1*third):]
    del seq[(-1*third):]
    seq = last_third + seq
    return seq

print(exchange_first_last(["a","b","c","d",5,6,7,8,9,10]))
print(remove_every_other(["a","b","c","d",5,6,7,8,9,10]))
print(remove_first_last_4(["a","b","c","d",5,6,7,8,9,10]))
print(reverse_seq(["a","b","c","d",5,6,7,8,9,10]))
print(move_thirds(["a","b","c","d",5,6,7,8,9,10]))


