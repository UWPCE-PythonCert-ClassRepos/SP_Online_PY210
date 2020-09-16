def exchange_first_last(seq):
    new_line = seq[-1:] + seq[1:-1] + seq[:1]
    return new_line


def every_other_letter_removed(seq):
    new_line = seq[0:-1:2]
    return new_line


def first_4_last_4_gone_every_others_remain(seq):
    new_line = seq[4:-4:2]
    return new_line


def element_reversed(seq):
    new_line = seq[::-1]
    return new_line


def every_third_new_orders(seq):
    devider = len(seq)//3
    new_line = seq[-int(devider):] + seq[:int(devider)] + \
        seq[int(devider):-int(devider)]
    return new_line

# Test


a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)

print(exchange_first_last(a_string))
print(every_other_letter_removed(a_string))
print(first_4_last_4_gone_every_others_remain(a_string))
print(element_reversed(a_string))
print(every_third_new_orders(a_string))

assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
assert every_other_letter_removed(a_string) == "ti sasrn"
assert first_4_last_4_gone_every_others_remain(a_string) == " sas"
assert element_reversed(a_string) == "gnirts a si siht"
assert every_third_new_orders(a_string) == "tringthis is a s"
print('\n')
print("Test completed")
