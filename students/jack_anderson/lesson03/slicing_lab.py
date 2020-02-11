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

    # if check == str:
    #     last = 1
    #     middle =
    #     first =
    #     a_new_sequence = "{}{}{}".format(last,copy,first)
    #
    #
    # return sequence


a_test_string2 = "abcdefghikjlmnop"
a_test_tuple2 = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33)
a_test_string = "this is a string"
a_test_tuple = (2, 54, 13, 12, 5, 32, 47)
a_test_list = ['jack', 1, exchange_fist_last(a_test_string), 14, 32, 'joe', "2231", 7, 1977]

def print_results(x):
    print(exchange_fist_last(x))

print_results(a_test_tuple2)