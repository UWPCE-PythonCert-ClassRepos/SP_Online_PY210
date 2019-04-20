def exchange_first_last(seq):
    return seq[-1:] + seq[1:-1] + seq[:1]

def every_other(seq):
    return seq[::2]

def elements_reversed(seq):
    return seq[::-1]

def first4_last4_every_other(seq):
    return seq[4:-4:2]

def mid_last_first(seq):
    x = len(seq) // 3
    return seq[x:] + seq[:x]

if __name__ == '__main__':

    a_string = "we would like to test a long string here for the thorough test cases"
    a_tuple = (2, 54, 13, 12, 5, 32, 34, 8, 92, 16, 23, 75)

    assert exchange_first_last(a_string) == "se would like to test a long string here for the thorough test casew"
    assert exchange_first_last(a_tuple) == (75, 54, 13, 12, 5, 32, 34, 8, 92, 16, 23, 2)
    assert every_other(a_string) == "w ol iet etaln tighr o h hruhts ae"
    assert every_other(a_tuple) == (2, 13, 5, 34, 92, 23)
    assert first4_last4_every_other(a_string) == "ol iet etaln tighr o h hruhts "
    assert first4_last4_every_other(a_tuple) == (5, 34)

    assert elements_reversed(a_string) == "sesac tset hguoroht eht rof ereh gnirts gnol a tset ot ekil dluow ew"
    assert elements_reversed(a_tuple) == (75, 23, 16, 92, 8, 34, 32, 5, 12, 13, 54, 2)

    assert mid_last_first(a_string) == "a long string here for the thorough test caseswe would like to test "
    assert mid_last_first(a_tuple) == (5, 32, 34, 8, 92, 16, 23, 75, 2, 54, 13, 12)
    print("All tests passed!")
