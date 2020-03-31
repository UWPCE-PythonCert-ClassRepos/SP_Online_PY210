#########################
# Slicing Lab Exercises #
#########################

# Test examples
a_string = "This is a test string"
a_list = list(range(11)) # generate list[0,1,2,3,4,5,6,7,8,9,10]
a_tuple = tuple(range(0, 21, 2)) # generate tuple(0,2,4,6,8,10,12,14,16,18,20)

########################################
# 1. define exchange_first_last(my_seq)#
# Take a sequence as an argument and return a copy of the sequence with
# the first and the lasts items exchanged.
########################################
def exchange_first_last(my_seq):
    tmp_seq = my_seq[-1:] + my_seq[1:len(my_seq) - 1] + my_seq[0:1]
    #print(f"1. The returned seq:{tmp_seq}, type:{type(tmp_seq)}")
    return tmp_seq

assert exchange_first_last(a_string) == "ghis is a test strinT"
assert exchange_first_last(a_list) == [10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
assert exchange_first_last(a_tuple) == (20, 2, 4, 6, 8, 10, 12, 14, 16, 18, 0)

########################################
# 2. define every_other_removed(my_seq)#
# Take a sequence as an argument and return a copy of the sequence with
# the every other item removed.
########################################
def every_other_removed(my_seq):
    tmp_seq = my_seq[::2]
    #print(f"2. The returned seq:{tmp_seq}")
    return tmp_seq

assert every_other_removed(a_string) == "Ti sats tig"
assert every_other_removed(a_list) == [0, 2, 4, 6, 8, 10]
assert every_other_removed(a_tuple) == (0, 4, 8, 12, 16, 20)

########################################
# 3. define first4_last4_removed(my_seq)#
# Take a sequence as an argument and return a copy of the sequence with
# the first 4 and last 4 items removed and every other item in the
# remaining sequence.
########################################
def first4_last4_removed(my_seq):
    tmp_seq = my_seq[4:-4:2]
    #print(f"3. The returned seq:{tmp_seq}")
    return tmp_seq

# Test
assert first4_last4_removed(a_string) == " sats t"
assert first4_last4_removed(a_list) == [4, 6]
assert first4_last4_removed(a_tuple) == (8, 12)

#############################
# 4. define reverse(my_seq) #
# Take a sequence as an argument and return a copy of the sequence with
# the elements reversed.
#############################
def reverse(my_seq):
    tmp_seq = my_seq[::-1]
    #print(f"4. The returned seq:{tmp_seq}")
    return tmp_seq

# Test
assert reverse(a_string) == "gnirts tset a si sihT"
assert reverse(a_list) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
assert reverse(a_tuple) == (20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 0)


######################################
# 5. define last_first_third(my_seq) #
# Take a sequence as an argument and return a copy of the sequence with
# the last third, then first third, then the middle third in the new order
######################################
def last_first_third(my_seq):
    first_seq = my_seq[:3]
    last_seq = my_seq[-3:]
    middle_len = int(len(my_seq[3:-3]) / 2)
    tmp_seq = my_seq[3:-3]
    middle_seq = tmp_seq[middle_len - 1:middle_len + 2]
    tmp_seq = last_seq + first_seq + middle_seq
    #print(f"5. The returned seq:{tmp_seq}")
    return tmp_seq

# Test
assert last_first_third(a_string) == "ingThi te"
assert last_first_third(a_list) == [8, 9, 10, 0, 1, 2, 4, 5, 6]
assert last_first_third(a_tuple) == (16, 18, 20, 0, 2, 4, 8, 10, 12)

print("All Tests Pass...")
