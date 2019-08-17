# define exchange_first_last
def exchange_first_last(seq):
    """Exchange the first and last items of a sequence."""
    return seq[-1:] + seq[1:-1] + seq[:1]

# define remove_every_other
def remove_every_other(seq):
    """Remove every other item in a sequence."""
    return seq[::2]

# test all functions
if __name__ == "__main__":
    
    # exchange_first_last
    a_string = "Monty Python"
    a_list = ["M", "o", "n", "t", "y"]
    
    assert exchange_first_last(a_string) == "nonty PythoM"
    assert exchange_first_last(a_list) == ["y", "o", "n", "t", "M"]
    print('exchange_first_last: Success!')

    # remove_every_other
    assert remove_every_other(a_string) == "MnyPto"
    assert remove_every_other(a_list) == ["M", "n", "y"]
    print('remove_every_other: Success!')