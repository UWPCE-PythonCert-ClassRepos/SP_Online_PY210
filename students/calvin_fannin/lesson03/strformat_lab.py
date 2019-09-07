a_tuple = (2, 123.4567, 10000,12345.67)


print('file_{:0>3}'.format(a_tuple[0]) + " :    " + '{:.2f}'.format(a_tuple[1])
      + ', {:.2e}'.format(a_tuple[2]) + ', {:.2e}'.format(a_tuple[3]))

print(f"file_{a_tuple[0]:0>3} :    {a_tuple[1]:.2f}, {a_tuple[2]:.2e}, {a_tuple[3]:.2e}")




def formatter(in_tuple):
    size = len(in_tuple)
    form_string = 'The {}'.format(size) + " numbers are: " + "{:d} " * size
    return form_string.format(*in_tuple)


print(formatter((2,3,5,56,7,8)))


tuple_five = (4, 30, 2017, 2, 27)
print('{:0>2} {:0>2} {:0>2} {:0>2} {:0>2}'.format(*tuple_five))

