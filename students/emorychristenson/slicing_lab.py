def exchange_first_last(seq):
    return seq[-1:] + seq[1:-1] + seq[0:1]

def every_other_item(seq):
    return seq[::2]
    
def first_last_four(seq):
    return seq[4:-4:2]

def reverse(seq):
    return seq[::-1]

def third_swap(seq):
    return seq[-(len(seq) // 3):] + seq[:(len(seq) // 3) * 2]


if __name__ == "__main__":
    #run some tests
    a_string = "strings are ok!"
    a_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8)

    # swap first and last items
    assert exchange_first_last(a_string) == "!trings are oks"
    assert exchange_first_last(a_tuple) == (8, 1, 2, 3, 4, 5, 6, 7, 0)

    # remove every other item
    assert every_other_item(a_string) == "srnsaeo!"
    assert every_other_item(a_tuple) == (0, 2, 4, 6, 8)
    
    # remove first 4, last 4, print every other in remaining sequence
    assert first_last_four(a_string) == ("nsae")
    assert first_last_four(a_tuple) == (4,)

    # reverse sequence
    assert reverse(a_string) == "!ko era sgnirts"
    assert reverse(a_tuple) == (8, 7, 6, 5, 4, 3, 2, 1, 0)

    # last third, first third, middle third
    assert third_swap(a_string) == "e ok!strings ar"
    assert third_swap(a_tuple) == (6, 7, 8, 0, 1, 2, 3, 4, 5)

    print("Tests passed.")