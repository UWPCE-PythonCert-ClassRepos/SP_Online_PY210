def exchange_first_last(seq):
    """Exchange the first and last items of a sequence."""
    return seq[-1:] + seq[1:-1] + seq[:1]

a_string = "Monty Python"
a_list = ["M", "o", "n", "t", "y"]


if __name__ == "__main__":
    assert exchange_first_last(a_string) == "nonty PythoM"
    assert exchange_first_last(a_list) == ["y", "o", "n", "t", "M"]
    
    print('No assertion failures. Success!')