#! python

#----------------------------------------------
# Lesson 3 - Exercise 3.1: Slicing Lab
#----------------------------------------------

def exchange_first_last(seq):
    """ This function takes a sequence and returns a sequence with the first
        an last item exchanged.
    """
    if len(seq) < 2:
        return seq
    return seq[-1:]+seq[1:-1]+seq[0:1]

def remove_every_other(seq):
    """ This function takes a sequence and returns a sequence with every
        other item removed.
    """
    return seq[::2]

def remove_first4_last4__keep_every_other(seq):
    """ This function takes a sequence and returns a sequence with the first 4
        and the last 4 items removed, and then every other item in the remaining
        sequence.
    """
    return seq[4:-4][1::2]

def reverse(seq):
    """ This function takes a sequence and returns a sequence with the
        elements reversed.
    """
    return seq[::-1]

def last_first_middle_third(seq):
    """ This function takes a sequence and returns a sequence with the last
        third, then first third, then the middle third.
    """
    #Basically, just move the last third to the front.
    # The addition is to divide the interval more evenly.
    interval = len(seq) // 3 + (len(seq) % 3) // 2
    return seq[-interval:]+seq[:len(seq)-interval]



if __name__ == "__main__":
    #run some tests
    a_string = "what are you doing?"
    assert exchange_first_last(a_string) == "?hat are you doingw"
    assert remove_first4_last4__keep_every_other(a_string) == "aeyud"
    assert last_first_middle_third(a_string) == "doing?what are you "
    a_string = "A"
    assert exchange_first_last(a_string) == "A"
    assert remove_every_other(a_string) == "A"
    assert remove_first4_last4__keep_every_other(a_string) == ""
    a_string = "1 2 3 4 5 6 7 8 9"
    assert remove_every_other(a_string) == "123456789"
    assert remove_first4_last4__keep_every_other(a_string) == "    "
    assert last_first_middle_third(a_string) == " 7 8 91 2 3 4 5 6"
    a_string = "hello there"
    assert remove_every_other(a_string) == "hlotee"
    a_tuple = (12, 13, 14, 15, 28, 29)
    assert exchange_first_last(a_tuple) == (29, 13, 14, 15, 28, 12)
    assert remove_every_other(a_tuple) == (12, 14, 28)
    assert remove_first4_last4__keep_every_other(a_tuple) == ()
    a_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22)
    assert remove_first4_last4__keep_every_other(a_tuple) == (6, 8, 10, 12, 14, 16, 18)
    assert last_first_middle_third(a_tuple) == (16, 17, 18, 19, 20, 21, 22, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
    a_tuple = ('ab', 'cd')
    assert exchange_first_last(a_tuple) == ('cd', 'ab')
    assert last_first_middle_third(a_tuple) == ('cd', 'ab')
    assert remove_every_other(a_tuple) == ('ab',)
    a_tuple = ()
    assert exchange_first_last(a_tuple) == ()
    assert remove_every_other(a_tuple) == ()
    a_list = ['hello']
    assert exchange_first_last(a_list) == ['hello']
    a_list = ['hello', 'there']
    assert remove_every_other(a_list) == ['hello']
    a_list = ['apple', 'banana', 'pineapple', 'peach', 'orange']
    assert exchange_first_last(a_list) == ['orange', 'banana', 'pineapple', 'peach', 'apple']
    assert remove_every_other(a_list) == ['apple', 'pineapple', 'orange']
    a_list = ['orange', 'grapes', 'apple', 'banana', 'watermelon', 'lemon', 'lime', 'pineapple', 'peach']
    assert remove_first4_last4__keep_every_other (a_list) == []
    assert last_first_middle_third(a_list) == ['lime', 'pineapple', 'peach', 'orange', 'grapes', 'apple', 'banana', 'watermelon', 'lemon']
    a_list = ['AB', 'CD', 'EF', 'GH', 'IJ', 'KL', 'MN', 'OP', 'QR', 'ST', 'UV', 'WX', 'YZ']
    assert remove_first4_last4__keep_every_other (a_list) == ['KL', 'OP']
    assert last_first_middle_third(a_list) == ['ST', 'UV', 'WX', 'YZ', 'AB', 'CD', 'EF', 'GH', 'IJ', 'KL', 'MN', 'OP', 'QR']

    print("test passed")
