#!/usr/bin/env python3


def main():
    # Test exchange_first_last function
    assert exchange_first_last("this is a string") == "ghis is a strint"
    assert exchange_first_last(
        (2, 54, 13, 12, 5, 32)) == (32, 54, 13, 12, 5, 2)

    # Test remove_every_other function
    assert remove_every_other("this is a string") == "ti sasrn"
    assert remove_every_other((2, 54, 13, 12, 5, 32)) == (2, 13, 5)

    # Test remove_four function
    assert remove_four("this is a string") == " sas"
    assert remove_four((2, 54, 13, 12, 5, 32)) == ()

    # Test seq_reverse function
    assert seq_reverse("this is a string") == "gnirts a si siht"
    assert seq_reverse((2, 54, 13, 12, 5, 32)) == (32, 5, 12, 13, 54, 2)

    # Test seq_thirds function
    seq_thirds("this is a string") == "stringthis is a"
    seq_thirds((2, 54, 13, 12, 5, 32)) == (5, 32, 2, 25, 13, 12)


def exchange_first_last(seq):
    """Swap the first and last values in the input."""
    return seq[-1:] + seq[1:-1] + seq[:1]


def remove_every_other(seq):
    """Remove every second value from the input."""
    return seq[::2]


def remove_four(seq):
    """
    Remove the first 4 and last 4 values from the input, then remove every
    second value from the remainder.
    """
    return seq[4:-4:2]


def seq_reverse(seq):
    """Reverse the order of the input."""
    return seq[::-1]


def seq_thirds(seq):
    """
    Reorder input to be the last third, then first third, then middle third.
    """
    # Use the length to find indices for the thirds
    first = len(seq) // 3
    second = first * 2
    return seq[second:] + seq[:first] + seq[first:second]


if __name__ == "__main__":
    main()
