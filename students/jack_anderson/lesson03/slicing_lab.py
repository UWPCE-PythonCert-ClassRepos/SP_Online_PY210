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
    Action to return a copy of provided sequence with the first and last items exchanged
    :param seq: The sequence to be copied and and changed
    :return: Copy of sequence with first and last item exchanged
    """
    first = seq[0]
    last = seq[-1]
    copy = seq[1:-1]
    a_new_sequence = last + copy + first
    print(a_new_sequence)

    # else:
    #     list = []
    #     for i in seq:
    #         list.append(i)
    #         first = list[0]
    # last = list[-1]
    #
    # seq_copy = list[1:-1]
    # # seq_copy.append(last)
    # seq_copy.append(first)
    # print(last, seq_copy, first)

# def every_other_item_removed(seq):
#     return a_new_sequence
#
# def first_last_4_removed(seq):
#     return sequence
#
# def reverse_elements(seq):
#     return sequence
#
# def order_by_thirds(seq):
#     return sequence





def print_results(x):
    exchange_fist_last(x)




print_results("Jack is a cool dude yo!")