#sequence to test
a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)

#function: first and last items exchanged
def exchange_first_last(seq):
    return seq[-1:] + seq[1:-1] + seq[:1]

#function: every other item removed removed
def alternate_removed(seq):
    return seq[::2]

#function: first 4 and last 4 items removed
def dislike_4s(seq):
    return seq[4:-4]

#function: elements reversed
def reversed(seq):
    return seq[::-1]

#function: last third, then first, then the middle third in the new order (??????)
def thirds_remix(seq):
    new_s = seq[3:-3]
    return seq[-3:-2] + seq[2:3] + new_s[2:3]

if __name__ == "__main__":
    # test exchange function
    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

    #test alternate removal function
    assert alternate_removed(a_string) == "ti sasrn"
    assert alternate_removed(a_tuple) == (2, 13, 5)

    #test dislike_4s
    assert dislike_4s(a_string) == " is a st"
    assert dislike_4s(a_tuple) == ()

    #test reversal function
    assert reversed(a_string) == "gnirts a si siht"
    assert reversed(a_tuple) == (32, 5, 12, 13, 54, 2)

    #test thirds remix function
    assert thirds_remix(a_string) == "iii"
    assert thirds_remix(a_tuple) == (12, 13)

    print("tests passed")