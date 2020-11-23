a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)

def exchange_first_last(seq):
    return seq[-1:] + seq[1:-1] + seq[:1]
print(exchange_first_last(a_string))
def remove_every_other_item(seq):
    return seq[::2]
print(remove_every_other_item((a_tuple)))

def remove_first_last_four(seq):
    return seq[4:-4]
print(remove_first_last_four(a_string))

def elements_reversed(seq):
    return seq[::-1]
print(elements_reversed(a_string))

def new_order(seq):
    third=int(len(seq)//3)
    return seq[-third:] + seq[:third] +seq[third:-third]

print(new_order(a_tuple))