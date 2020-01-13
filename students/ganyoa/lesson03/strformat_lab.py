
tups = (2, 123.4567, 10000, 12345.67)

print("--- Task01 ---")
print('file_{:03d} :    {:.2f}, {:.2e}, {:.2e}'.format(tups[0], tups[1], tups[2], tups[3]))

print("\n" + "--- Task02 ---")
print(f'file_{tups[0]:03d} :    {tups[1]:.2f}, {tups[2]:.2e}, {tups[3]:.2e}')

print("\n" + "--- Task03 ---")
print("enter numbers into function 'formatter()'")
def formatter(in_tuple):
    form_string = 'the ' + str(len(in_tuple)) + ' numbers are: {:d}'
    for t in range(len(in_tuple)-1):
        form_string += ', {:d}'
    return form_string.format(*in_tuple)

print("\n" + "--- Task04 ---")