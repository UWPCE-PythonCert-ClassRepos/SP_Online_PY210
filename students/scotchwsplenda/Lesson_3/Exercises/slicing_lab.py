a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)


def first_last(x):
    '''with the first and last items exchanged.'''
    return x[-1:]+x[1:-1]+x[:1]


assert first_last(a_string) == "ghis is a strint"
assert first_last(a_tuple) == (32, 54, 13, 12, 5, 2)


def ery_oth(x):
    '''with every other item removed.'''
    return x[::2]


assert ery_oth(a_string) == "ti sasrn"
assert ery_oth(a_tuple) == (2, 13, 5)


def four_x_four(x):
    '''with the first 4 and the last 4 items removed, and then every other item
    in the remaining sequence.'''
    return x[4:-4:2]


assert four_x_four(a_string) == " sas"
assert four_x_four(a_tuple) == ()


def put_ur_tingdown(x):
    '''with the elements reversed (just with slicing).'''
    return x[::-1]


assert put_ur_tingdown(a_string) == "gnirts a si siht"
assert put_ur_tingdown(a_tuple) == (32, 5, 12, 13, 54, 2)


trd_string = "123456789"
trd_tuple = (2, 54, 13, 12, 5, 32)


def thirds(x):
    '''with the last third, then first third, then the middle third in the new
    order.'''
    lgt = len(x)
    if lgt % 3 != 0:
        raise Exception("Give me something divisible by 3")
    trd = int(lgt/3)
    return x[-trd:]+x[:trd]+x[trd:-trd]


assert thirds(trd_string) == "789123456"
assert thirds(trd_tuple) == (5, 32, 2, 54, 13, 12)
