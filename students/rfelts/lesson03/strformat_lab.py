# Russell Felts
# Assignment 3 - String Formatting Exercise


# Step 1 & 2
# Use string formatting to convert the tuple data to: 'file_002, 123.46, 1.00e+04, 1.23e+04'
# The first element is used to generate a filename. Pad the numbers with zeros to get the right sort order.
# The second element is a float displayed with 2 decimal places.
# The third value is an integer displayed with in scientific notation, with 2 decimal places shown.
# The fourth value is a float displayed in scientific notation with 3 significant figures.

tuple_1 = (2, 123.4567, 10000, 12345.67)

formated_tuple = 'file_{:0>3d}, {:.2f}, {:.2e}, {:.2e}'.format(*tuple_1)
print('Step 1:\nFormatting the tuple:', tuple_1, "\nUsing the format method.", formated_tuple, "\n")

fstring_tuple = f"file_{tuple_1[0]:03d}, {tuple_1[1]:.2f}, {tuple_1[2]:.2e}, {tuple_1[3]:.2e}"
print('Step 2:\nFormatting the tuple:', tuple_1, "\nUsing f-String.", fstring_tuple, "\n")


# Step 3
def format_tuple(numbers_tuple):
    """
    Dynamically build up the format string to accommodate formatting any tuple length.
    :param numbers_tuple - The tuple to format
    :return string - A dynamically formatted string
    """

    tuple_length = len(numbers_tuple)

    # Need to use [] or the join will add the , to the {} like {,}
    format_string = ("The {:d} numbers are: " + ", ".join(["{:d}"] * tuple_length))

    print("Step 3:\n" + format_string.format(tuple_length, *numbers_tuple) + "\n")

    return format_string.format(tuple_length, *numbers_tuple)


# Step 3 function tests.
test_tuple1 = (2, 4, 5, 6)
test_tuple2 = (10, 3, 29, 5, 11, 42)
assert format_tuple(test_tuple1) == "The 4 numbers are: 2, 4, 5, 6"
assert format_tuple(test_tuple2) == "The 6 numbers are: 10, 3, 29, 5, 11, 42"


# Step 4
# Given a 5 element tuple: ( 4, 30, 2017, 2, 27) use string formatting to print: '02 27 2017 04 30'

tuple_4 = (4, 30, 2017, 2, 27)
print(("Step 4: " + f"\'{tuple_4[3]:02d} {tuple_4[4]:d} {tuple_4[2]:d} {tuple_4[0]:02d} {tuple_4[1]:d}\'\n"))


# Step 5
# Given the following four element list: ['oranges', 1.3, 'lemons', 1.1] write an f-string that will display:
# "The weight of an orange is 1.3 and the weight of a lemon is 1.1."

list_5 = ['oranges', 1.3, 'lemons', 1.1]
print(("Step 5:\n" + f"The weight of an {list_5[0][:-1]} is {list_5[1]} " +
       f"and the weight of a {list_5[2][:-1]} is {list_5[3]}.\n"))

# Then change the f-string so that it displays the names of the fruit in upper case, and the weight 20% higher (that
# is 1.2 times higher).

print((f"The weight of an {list_5[0][:-1].upper()} is {list_5[1]*1.2} " +
       f"and the weight of a {list_5[2][:-1].upper()} is {list_5[3]*1.2}.\n"))


# Step 6
# Print a table of several rows, each with a name, an age and a cost. Make sure some of the costs are in the hundreds
# and thousands to test your alignment specifiers.

table = [['David', 48, 199.978], ['Jennie', 45, 2234.5], ['Peyton', 7, 10900.9999], ['Indy', 117, 200300400500.600]]

# Create dynamic padding for the name and cost columns
name_list = [item[0] for item in table]
name_padding = len(max(name_list)) + 4
cost_list = [item[2] for item in table]
cost_padding = len(str(max(cost_list)))
cost_padding += int((cost_padding / 3) + 4)

print("Step 6:\n" + f"{'NAME':<{name_padding}} AGE {'COST':>{cost_padding}}")

for row in table:
    print(f"{row[0]:<{name_padding}} {row[1]:>03d} {row[2]:>{cost_padding},.2f}")
