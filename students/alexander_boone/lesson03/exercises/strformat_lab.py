#!/usr/bin/env python3

# --------------------------------------------------- TASK 1 -----------------------------------------------------

t = (2, 123.4567, 10000, 12345.67)

s = f"file_{t[0]:03} :   {t[1]:.2f}, {t[2]:.2E}, {t[3]:.2E}"
print(s)

# --------------------------------------------------- TASK 2 -----------------------------------------------------

t = (2, 123.4567, 10000, 12345.67)

s2 = "file_{:03d} :   {:.2f}, {:.2E}, {:.2E}".format(t[0], t[1], t[2], t[3])
print(s2)

# --------------------------------------------------- TASK 3 -----------------------------------------------------

def formatter(tup):
    """Return string listing out comma-separated values contained within input tuple."""
    # get length of tuple
    l = len(tup)

    # create tuple of format specifiers and join into string
    f_tuple = tuple(['{:d}'] * l)
    f_string = ', '.join(f_tuple)

    # create formatted strings with correct values
    f_string2 = "The {:d} numbers are: ".format(l)
    f_string3 = f_string.format(*tup)
    

    # concatenate strings and return final string
    f_string_final = f_string2 + f_string3
    return f_string_final

# --------------------------------------------------- TASK 4 -----------------------------------------------------