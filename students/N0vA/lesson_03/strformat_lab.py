#!/usr/bin/env python3
### String Formatting Lab ###

tup_1 = (2, 123.4567, 10000, 12345.67)

# Task 1
print('Formatting for Task 1...')
print('file_{:03} :  {:.2f}, {:.2E}, {:.3}'.format(tup_1[0], round(tup_1[1],2), tup_1[2], tup_1[3]))

# Task 2
print('Formatting for Task 2...')
p_2 = f"file_{tup_1[0]:03} :  {tup_1[1]:.2f}, {tup_1[2]:.2E}, {tup_1[3]:.2E}"
print(p_2)

# Task 3
def tup_format(tup):
    # Find length of tuple
    l = len(tup)

    # Create new tuple
    temp = tuple(['{:d}'] * l)
    temp_2 = ', '.join(temp)
    new_tup = temp_2.format(*tup)
    final = f'The {l} numbers are: {new_tup}'
    return final

print('Test function: tup_format')
test_1 = (1, 2, 3, 4, 5)
print(test_1)
tup_format(test_1)

# Task 4
tup_4 = (4, 30, 2017, 2, 27)

print('Formatting for Task 4...')
print(f"{tup_4[3]:02d} {tup_4[4]} {tup_4[2]} {tup_4[0]:02d} {tup_4[1]}")

# Task 5
list_5 = ['oranges', 1.3, 'lemons', 1.1]
print('Formatting for Task 5...')
print(f'The weight of an {list_5[0][:-1]} is {list_5[1]} and the weight of a {list_5[2][:-1]} is {list_5[3]}')

# Print with weight 20% higher
print('Printing with weight 20 percent higher')
print(f'The weight of an {list_5[0][:-1].upper()} is {list_5[1] * 1.2} and the weight of a {list_5[2][:-1].upper()} is {list_5[3] * 1.2}')

# Task 6: Create a table with name, age, and cost

def my_table():
    my_list = ['Nike Free Run 2.0', 8, 44.99], ['Pixel XL', 4, 350.00], ['Jeep Liberty', 12, 10000]
    format_strings = '{:25} {:} {:8.2f}'
    for item in my_list:
        print(format_strings.format(*item))

# Print tuple with 10 numbers in 2 rows of 5 characters
print('Bonus')
tup_6 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(('{:5}' * len(tup_6)).format(*tup_6))