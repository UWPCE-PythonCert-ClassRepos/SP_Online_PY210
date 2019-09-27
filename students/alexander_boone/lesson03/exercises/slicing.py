# define exchange_first_last
def exchange_first_last(seq):
    """Exchange the first and last items of a sequence."""
    return seq[-1:] + seq[1:-1] + seq[:1]

# define remove_every_other
def remove_every_other(seq):
    """Remove every other item in a sequence."""
    return seq[::2]

# define remove_end_fours
def remove_end_fours(seq):
    """Remove the first and last four items of the sequence and return every other item of remaining sequence"""
    return seq[4:-4:2]

# define reverse_seq
def reverse_seq(seq):
    """Reverse the elements in a sequence."""
    return seq[::-1]

# define reorder_seq_thirds
def reorder_seq_thirds(seq):
    """Reorder a sequence into last third, first third, then middle third."""
    l = len(seq)
    # check seq length
    if l % 3 != 0:
        raise Exception('The input sequence length should be divisible by 3. The input length was: {}'.format(l))
    third = int(l/3)
    return seq[-third:] + seq[:third] + seq[third:-third]


# test all functions
if __name__ == "__main__":
    
    # test variables
    a_string = "Monty Python"
    a_list = ["M", "o", "n", "t", "y"]
    a_long_string = "One more step closer to writing LeetCode"
    a_long_list = ["all", "i", "do", "is", "code", "code", "code", "no", "matter", "what", "got", "coding", "on", "my", "mind", "I", "can", "never", "get", "enough"]
    num_string = "123456789"
    num_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)

    # exchange_first_last
    assert exchange_first_last(a_string) == "nonty PythoM"
    assert exchange_first_last(a_list) == ["y", "o", "n", "t", "M"]
    print('exchange_first_last: Success!')

    # remove_every_other
    assert remove_every_other(a_string) == "MnyPto"
    assert remove_every_other(a_list) == ["M", "n", "y"]
    print('remove_every_other: Success!')

    # remove_end_fours
    assert remove_end_fours(a_long_string) == "mr tpcoe owiigLe"
    assert remove_end_fours(a_long_list) == ["code",  "code", "matter", "got", "on", "mind"]
    print('remove_end_fours: Success!')

    # reverse_seq
    assert reverse_seq(a_string) == "nohtyP ytnoM"
    assert reverse_seq(a_list) == ["y", "t", "n", "o", "M"]
    print('reverse_seq: Success!')

    # reorder_seq_thirds
    assert reorder_seq_thirds(num_string) == "789123456"
    assert reorder_seq_thirds(num_tuple) == (7, 8, 9, 1, 2, 3, 4, 5, 6)
    print('reorder_seq_thirds: Success!')
    

