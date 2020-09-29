# Title: Slicing Lab
# Dev: Roslyn Melookaran
# Date: 9/9/20
# Change Log: (Who, When, What)
# R. Melookaran, 9/9/20, created script)
# --------------------------------------------------------------


def first_last_exchange(seq):
    """ Compute new sequence with the first and last items exchanged.
            :param: seq(string or touple or list)
            :return: new_seq(string or touple or list)
            """
    new_seq = seq[-1:] + seq[1:-1] + seq[0:1]
    return new_seq


def remove_every_other(seq):
    """ Compute new sequence with every other item removed.
                :param: seq(string or touple or list)
                :return: new_seq(string or touple or list)
                """
    new_seq = seq[0:-1:2]
    return new_seq


def first_last_remove_every_other(seq):
    """ Compute new sequence with the first 4 and the last 4 items removed, and then every other item in the remaining sequence.
                :param: seq(string or touple or list)
                :return: new_seq(string or touple or list)
                """
    new_seq = seq[4:]
    new_seq = new_seq[:-4]
    new_seq = new_seq[0:-1:2]
    return new_seq


def reverse(seq):
    """ Compute new sequence with the elements reversed (just with slicing).
               :param: seq(string or touple or list)
               :return: new_seq(string or touple or list)
               """
    new_seq = seq[::-1]
    return new_seq


def reorder_thirds(seq):
    """ Compute new sequence with the last third, then first third, then the middle third in the new order.
                :param: seq(string or touple or list)
                :return: new_seq(string or touple or list)
                """
    n = int(len(seq) / 3)
    new_seq = seq[-n:] + seq[:n] + seq[n:-n]
    return new_seq


# --------------MAIN---------------------

a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)
b_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)

if __name__ == "__main__":
    # run some tests
    # Checking the first_last_exchange() function
    assert first_last_exchange(a_string) == "ghis is a strint"
    assert first_last_exchange(a_tuple) == (32, 54, 13, 12, 5, 2)
    # Checking the remove_every_other() function
    assert remove_every_other(a_string) == "ti sasrn"
    assert remove_every_other(a_tuple) == (2, 13, 5)
    # Checking the first_last_remove_every_other() function
    assert first_last_remove_every_other(b_tuple) == (5, 7)
    assert first_last_remove_every_other(a_tuple) == ()
    assert first_last_remove_every_other(a_string) == " sas"
    # Checking the reverse() function
    assert reverse(a_tuple) == (32, 5, 12, 13, 54, 2)
    assert reverse(a_string) == "gnirts a si siht"
    # Checking the reorder_thirds() function
    assert reorder_thirds(a_tuple) == (5, 32, 2, 54, 13, 12)
    assert reorder_thirds(a_string) == "tringthis is a s"
    print("Success")
