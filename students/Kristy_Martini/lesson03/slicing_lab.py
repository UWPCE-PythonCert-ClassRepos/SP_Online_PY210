import math

def exchange_first_last(seq):
    if (type(seq) is int or type(seq) is str):
        was_int = False
        if (type(seq) is int):
            seq = str(seq)
            was_int = True
        new_seq = seq[len(seq)-1] + seq[1:len(seq)-1] + seq[0]
        if was_int:
            new_seq = int(new_seq)
    else: 
        was_tuple = False
        if(type(seq) is tuple):
            seq = list(seq)
            was_tuple = True
        first_element = seq[0]
        last_element = seq[len(seq)-1]
        seq[0] = last_element
        seq[len(seq)- 1] = first_element
        if was_tuple:
            new_seq = tuple(seq)
    print(new_seq)
    return new_seq

def remove_every_other(seq):
    i = 0
    if(type(seq) is int or type(seq) is str):
        was_int = False
        if (type(seq) is int):
            seq = str(seq)
            was_int = True
        new_seq = ''
        while i < len(seq):
            new_seq += seq[i]
            i += 2
        if was_int:
            new_seq = int(new_seq)
    else: 
        was_tuple = False
        if(type(seq) is tuple):
            seq = list(seq)
            was_tuple = True
        new_seq = list()
        while i < len(seq):
            new_seq.append(seq[i])
            i += 2
        if was_tuple:
            new_seq = tuple(new_seq)
    print(new_seq)
    return new_seq

def remove_keep_middle(seq):
    if (type(seq) is int):
        seq = str(seq)
    if (type(seq) is tuple):
        seq = list(seq)
    new_seq = seq[4:len(seq)-4]
    new_seq = remove_every_other(new_seq)
    return new_seq

def reverse(seq):
    if(type(seq) is int or type(seq) is str):
        was_int = False
        if (type(seq) is int):
            seq = str(seq)
            was_int = True
        i = len(seq)-1
        new_seq = ''
        while i >= 0:
            new_seq += seq[i]
            i-= 1
        if was_int:
            new_seq = int(new_seq)
    else: 
        i = len(seq)-1
        was_tuple = False
        if(type(seq) is tuple):
            seq = list(seq)
            was_tuple = True
        new_seq = list()
        while i >= 0:
            new_seq.append(seq[i])
            i -=1
        if was_tuple:
            new_seq = tuple(new_seq)
    print(new_seq)
    return new_seq        

def rearrange_thirds(seq):
    was_int = False
    was_tuple = False
    if (type(seq) is int):
        seq = str(seq)
        was_int = True
    if(type(seq) is tuple):
        seq = list(seq)
        was_tuple = True
    third = math.floor(len(seq)/3)
    last_third = seq[2*third:len(seq)]
    middle_third = seq[third:2*third]
    first_third = seq[0:third]
    new_seq = last_third + first_third + middle_third
    if was_int:
        new_seq = int(new_seq)
    if was_tuple:
        new_seq = tuple(new_seq)
    print(new_seq)
    return new_seq

if __name__ == "__main__":
    full_name = "Kristine Marie Martini"
    number = 26284604
    test_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

    assert exchange_first_last(full_name) == "iristine Marie MartinK"
    assert exchange_first_last(number) == 46284602
    assert exchange_first_last(test_tuple) == (10, 2, 3, 4, 5, 6, 7, 8, 9, 1)

    assert remove_every_other(full_name) == "Kitn ai atn"
    assert remove_every_other(number) == 2240
    assert remove_every_other(test_tuple) == (1, 3, 5, 7, 9)

    assert remove_keep_middle(full_name) == "tn ai a"
    assert remove_keep_middle(number) == ''
    assert remove_keep_middle(test_tuple) == [5]

    assert reverse(full_name) == "initraM eiraM enitsirK"
    assert reverse(number) == 40648262
    assert reverse(test_tuple) == (10, 9, 8, 7, 6, 5, 4, 3, 2, 1)

    assert rearrange_thirds(full_name) == " MartiniKristine Marie"
    assert rearrange_thirds(number) == 46042628
    assert rearrange_thirds(test_tuple) == (7, 8, 9, 10, 1, 2, 3, 4, 5, 6)