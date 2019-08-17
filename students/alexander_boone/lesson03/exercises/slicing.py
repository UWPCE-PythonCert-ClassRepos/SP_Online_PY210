# define exchange_first_last
def exchange_first_last(seq):
    """Exchange the first and last items of a sequence."""
    return seq[-1:] + seq[1:-1] + seq[:1]

# define remove_every_other
def remove_every_other(seq):
    """Remove every other item in a sequence."""
    return seq[::2]

# 
def remove_end_fours(seq):
    """Remove the first and last four items of the sequence and return every other item of remaining sequence"""
    return seq[4:-4:2]

# test all functions
if __name__ == "__main__":
    
    # test variables
    a_string = "Monty Python"
    a_list = ["M", "o", "n", "t", "y"]
    a_long_string = "One more step closer to writing LeetCode"
    a_long_list = ["all", "i", "do", "is", "code", "code", "code", "no", "matter", "what", "got", "coding", "on", "my", "mind", "I", "can", "never", "get", "enough"]
    
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

    

