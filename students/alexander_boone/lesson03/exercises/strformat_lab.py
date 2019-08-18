#!/usr/bin/env python3

# --------------------------------------------------- TASK 1 -----------------------------------------------------
print("------------------ TASK 1 ------------------")
t = (2, 123.4567, 10000, 12345.67)

s = f"file_{t[0]:03} :   {t[1]:.2f}, {t[2]:.2E}, {t[3]:.2E}"
print(s)

# --------------------------------------------------- TASK 2 -----------------------------------------------------
print("------------------ TASK 2 ------------------")
t = (2, 123.4567, 10000, 12345.67)

s2 = "file_{:03d} :   {:.2f}, {:.2E}, {:.2E}".format(t[0], t[1], t[2], t[3])
print(s2)

# --------------------------------------------------- TASK 3 -----------------------------------------------------
print("------------------ TASK 3 ------------------")
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
print("------------------ TASK 4 ------------------")
t_4 = (4, 30, 2017, 2, 27)

print(f"{t_4[3]:02d} {t_4[4]:02d} {t_4[2]:d} {t_4[0]:02d} {t_4[1]:02d}")

# --------------------------------------------------- TASK 5 -----------------------------------------------------
print("------------------ TASK 5 ------------------")
l_5 = ['oranges', 1.3, 'lemons', 1.1]

print(f"The weight of an {l_5[0][:-1]} is {l_5[1]} and the weight of a {l_5[2][:-1]} is {l_5[3]}")
 # prints string in uppercase with a weight that is 20% greater
print(f"The weight of an {l_5[0][:-1].upper()} is {l_5[1] * 1.2} and the weight of a {l_5[2][:-1].upper()} is {l_5[3] * 1.2}")

# --------------------------------------------------- TASK 6 -----------------------------------------------------
print("------------------ TASK 6 ------------------")

l6 = list()
l6.append('{:<6}{:<15}{:<11}{:<10}{:<6}{:>10}'.format('Name:', 'iPhone', 'Age (yrs):', 2, 'Cost:', '$1,049.99'))
l6.append('{:<6}{:<15}{:<11}{:<10}{:<6}{:>10}'.format('Name:', 'Keyboard', 'Age (yrs):', 0, 'Cost:', '$45.99'))
l6.append('{:<6}{:<15}{:<11}{:<10}{:<6}{:>10}'.format('Name:', 'French Press', 'Age (yrs):', 1, 'Cost:', '$24.99'))

for table_item in l6:
    print(table_item)

# extra task
print("\nExtra Task")
t6 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
l6_2 = ' '.join(list(['{:^5d}'] * 10))
print(l6_2.format(*t6))