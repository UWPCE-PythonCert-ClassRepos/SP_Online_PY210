'''
Jack Anderson - SP_Online_PY210


Write some functions that take a sequence as an argument, and return a copy of that sequence:
1. with the first and last items exchanged.
2. with every other item removed.
3. with the first 4 and the last 4 items removed, and then every other item in the remaining sequence.
4. with the elements reversed (just with slicing).
5. with the last third, then first third, then the middle third in the new order.
'''

def exchange_fist_last(seq):
    """
    Action to check if a string, list, or tuple is provided and then returns a copy of the provided sequence
    with the first and last items exchanged
    :param seq: The sequence to be copied and and changed
    :return: Copy of sequence with first and last item exchanged
    """
    first = seq[0]
    last = seq[-1]
    copy = seq[1:-1]
    check = type(seq)

    if check == str:
        a_new_sequence = "{}{}{}".format(last,copy,first)
        return(a_new_sequence)

    else:
        list = []
        list.append(last)
        for i in copy:
            list.append(i)
        list.append(first)
        a_new_sequence = list

        if check == tuple:
            return tuple(a_new_sequence)
        else:
            return(a_new_sequence)



def remove_every_other_item(seq):
    """
    Action to return a copy of the provided sequence with every other item in the provided sequence removed
    :param seq: The sequence to be copied and and changed
    :return: Copy of sequence with every other item removed
    """
    every_other = seq[::2]
    return every_other


def first_last_4_removed(seq):
    """
    Action to remove the first 4 and last 4 items in the provided sequence and then return a copy of
    evey other remaining item
    :param seq: The sequence to be copied and and changed
    :return: Copy of every other item in sequence after first and last 4 items are removed
    """
    remaining_items = seq[4:-4:2]
    return(remaining_items)


def reverse_elements(seq):
    reverse_order = seq[::-1]
    return reverse_order


def order_by_thirds(seq):
    #with the last third, then first third, then the middle third in the new order.
    total = len(seq)
    x = int(total / 3)
    first = seq[0:x]
    middle = seq[x:x+x]
    last = seq[x+x:total]
    a_new_sequence = last + first + middle
    return(a_new_sequence)



###############################################################################################################
#   TESTING
##############################################################################################################

a_test_string2 = "abcdefghikjlmnop"

a_test_tuple2 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, \
                 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34)

a_test_string = "this is a string"

a_test_tuple = (2, 54, 13, 12, 5, 32, 47)

a_test_list = ['jack', 1, exchange_fist_last(a_test_string), 14, 32, 'joe', "2231", 7, 1977]


if __name__ == "__main__":
    # run some tests against exchange_fist_last()
    assert exchange_fist_last(a_test_string) == "ghis is a strint"
    assert exchange_fist_last(a_test_string2) == "pbcdefghikjlmnoa"
    assert exchange_fist_last(a_test_tuple) == (47, 54, 13, 12, 5, 32, 2)
    assert exchange_fist_last(a_test_list) == [1977, 1, "ghis is a strint", 14, 32, 'joe', "2231", 7, 'jack']

    # run some tests against remove_every_other_item()
    assert remove_every_other_item(a_test_string) == "ti sasrn"
    assert remove_every_other_item(a_test_string2) == "acegijmo"
    assert remove_every_other_item(a_test_tuple) == (2, 13, 5, 47)
    assert remove_every_other_item(a_test_list) == ['jack', 'ghis is a strint', 32, '2231', 1977]

    # run some tests against first_last_4_removed()
    assert first_last_4_removed(a_test_string) == " sas"
    assert first_last_4_removed(a_test_string2) == "egij"
    assert first_last_4_removed(a_test_tuple2) == (5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29)
    assert first_last_4_removed(a_test_list) == [32]

    # run some tests against reverse_elements()
    assert reverse_elements(a_test_string) == "gnirts a si siht"
    assert reverse_elements(a_test_string2) == "ponmljkihgfedcba"
    assert reverse_elements(a_test_tuple) == (47, 32, 5, 12, 13, 54, 2)
    assert reverse_elements(a_test_list) == [1977, 7, '2231', 'joe', 32, 14, 'ghis is a strint', 1, 'jack']

    # run some tests against order_by_thirds()
    assert order_by_thirds(a_test_string) == "stringthis is a "
    assert order_by_thirds(a_test_string2) == "jlmnopabcdefghik"
    assert order_by_thirds(a_test_tuple2) == (23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 1, 2, 3, 4, 5, 6, 7, 8, \
                                              9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22)
    assert order_by_thirds(a_test_list) == ['2231', 7, 1977, 'jack', 1, 'ghis is a strint', 14, 32, 'joe']


    print("All tests passed")
