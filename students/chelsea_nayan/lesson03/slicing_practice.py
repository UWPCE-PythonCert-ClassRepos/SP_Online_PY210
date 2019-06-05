# chelsea_nayan, UWPCE, Python 210
# Lesson 03: Slicing Lab Exercise

# -------- MY TEST CASES -----------------
seq_string1 = "This is a super cool string"
seq_string2 = "s"
seq_string3 = "0123456789-abcdefghijklmnopqrstuvwxyz"

seq_tuple1 = (0, 1, "love", ["hi", "this", "me"], 2, "hey")
seq_tuple2 = ("4",)
seq_tuple3 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17)

seq_list1 = ["This", "is", "a", "list", "of", "strings", 1, 2, 3, 4, 5, 6, 7, 8]
seq_list2 = [1]
seq_list3 = ["Number", "time", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "end"]

# ---------- THE FUNCTIONS ------------------

# This function takes a sequence and returns a copy of that sequence with the first and last items exchanged
def exchange_first_last(seq): # Corrected to remove type checking and indexing
    if len(seq) < 2: # This deals with sequences that have the length of 1. Returns the one item.
        return seq
    new_seq = seq[-1:] + seq[1:-1] + seq[0:1]
    return new_seq


# This function takes a sequence and returns a copy of that sequence with every other item removed
def rm_every_other(seq): # Corrected to remove type checking
    new_seq = seq[::2]
    return new_seq


# This function takes a sequence and returns a copy of that sequence with the first 4 and the last 4 items removed, and then every other item inbetween starting from seq[4]
def rm_ends_and_every_other(seq): # Corrected to remove type checking
    new_seq = seq[4:-4:2]
    return new_seq

# This function takes a sequence and returns a copy of that sequence with the elements reversed (just with slicing)
def reverse(seq): # Corrected to remove type checking
    new_seq = seq[::-1]
    return new_seq


# This function takes a sequence and returns a copy of that sequence with the middle third, then last third, then the first third in the new order. If sequence is not divisble by 3, it should round down to the nearest integer.
def thirds(seq): # Corrected to remove type checking
    third_len = int(len(seq)/3)
    new_seq = seq[third_len:] + seq[:third_len]
    return new_seq # Returns the new sequence and its correct type


# ----------- PRINTS OUT MY TEST CASES ------------------

# print(exchange_first_last(seq_string1))
# print(exchange_first_last(seq_string2))
# print(exchange_first_last(seq_string3))
# print(exchange_first_last(seq_tuple1))
# print(exchange_first_last(seq_tuple2))
# print(exchange_first_last(seq_tuple3))
# print(exchange_first_last(seq_list1))
# print(exchange_first_last(seq_list2))
# print(exchange_first_last(seq_list3))

# print(rm_every_other(seq_string1))
# print(rm_every_other(seq_string2))
# print(rm_every_other(seq_string3))
# print(rm_every_other(seq_tuple1))
# print(rm_every_other(seq_tuple2))
# print(rm_every_other(seq_tuple3))
# print(rm_every_other(seq_list1))
# print(rm_every_other(seq_list2))
# print(rm_every_other(seq_list3))

# print(rm_ends_and_every_other(seq_string1))
# print(rm_ends_and_every_other(seq_string2))
# print(rm_ends_and_every_other(seq_string3))
# print(rm_ends_and_every_other(seq_tuple1))
# print(rm_ends_and_every_other(seq_tuple2))
# print(rm_ends_and_every_other(seq_tuple3))
# print(rm_ends_and_every_other(seq_list1))
# print(rm_ends_and_every_other(seq_list2))
# print(rm_ends_and_every_other(seq_list3))

# print(reverse(seq_string1))
# print(reverse(seq_string2))
# print(reverse(seq_string3))
# print(reverse(seq_tuple1))
# print(reverse(seq_tuple2))
# print(reverse(seq_tuple3))
# print(reverse(seq_list1))
# print(reverse(seq_list2))
# print(reverse(seq_list3))

# print(thirds(seq_string1))
# print(thirds(seq_string2))
# print(thirds(seq_string3))
# print(thirds(seq_tuple1))
# print(thirds(seq_tuple2))
# print(thirds(seq_tuple3))
# print(thirds(seq_list1))
# print(thirds(seq_list2))
# print(thirds(seq_list3))
