#Function switches first and last items
def exchange_first_last(seq):
    return seq[-1:] + seq[1:-1] + seq[0:1]

#Function removes every other item
def remove_every_other(seq):
    return seq[::2]

#Function removes first and last 4 items, then every other remaining item
def remove_first_four_and_last_four_ever_other_remaining(seq):
    return seq[4:-4:2]

#Function reverses items
def reveresed_sequence(seq):
    return seq[::-1]

#Function reorders sequence to middle, last, first
def last_third_first_third_middle_third(seq):
    third = int(len(seq)/3)
    return seq[2*third:] + seq[:third] + seq[third:2*third]

#Test functions
if __name__ == "__main__":
    s = 'this is my test string'
    l = [1,2,3,4,5,6,7,8,9,10,11,12]
    t = (20,21,22,23,24,25,26,27,28,29,30,31,32)

    #Test function that switches first and last items
    assert exchange_first_last(s) == 'ghis is my test strint'
    assert exchange_first_last(l) == [12, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 1]
    assert exchange_first_last(t) == (32, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 20)

    #Test function that removes every other item
    assert remove_every_other(s) == 'ti sm etsrn'
    assert remove_every_other(l) == [1, 3, 5, 7, 9, 11]
    assert remove_every_other(t) == (20, 22, 24, 26, 28, 30, 32)

    #Test function that removes first and last 4 items, then every other remaining item
    assert remove_first_four_and_last_four_ever_other_remaining(s) == ' sm ets'
    assert remove_first_four_and_last_four_ever_other_remaining(l) == [5, 7]
    assert remove_first_four_and_last_four_ever_other_remaining(t) == (24, 26, 28)

    #Test function that reverses items
    assert reveresed_sequence(s) == 'gnirts tset ym si siht'
    assert reveresed_sequence(l) == [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert reveresed_sequence(t) ==(32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20)

    #Test function that reorders items in middle, last, first
    assert last_third_first_third_middle_third(s) == 't stringthis is my tes'
    assert last_third_first_third_middle_third(l) == [9, 10, 11, 12, 1, 2, 3, 4, 5, 6, 7, 8]
    assert last_third_first_third_middle_third(t) == (28, 29, 30, 31, 32, 20, 21, 22, 23, 24, 25, 26, 27)

    print('test passed')

