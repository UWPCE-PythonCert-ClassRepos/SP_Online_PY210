# Task One
print("Task One")
tuple_one = (2, 123.4567, 10000, 12345.67)
str_file_one = "file_{:03d}: {:.2f}, {:.2e}, {:.3g}".format(tuple_one[0], tuple_one[1], tuple_one[2], tuple_one[3])
print(str_file_one)


# Task Two

print("\nTask Two")
str_file_two = f'file_{tuple_one[0]:03d}: {tuple_one[1]:.2f}, {tuple_one[2]:.2e}, {tuple_one[3]:.3g}'
print(str_file_two)


# Task Three

print("\nTask Three")
def formatter(in_tuple):
    """Returns a formatted string based on the tuple input."""
    form_string_list = []
    for item in in_tuple:
        form_string_list.append("{:d}")
    form_string = ", ".join(form_string_list)
    print("the {} numbers are: {}".format(len(in_tuple), form_string.format(*in_tuple)))
task_three_test_1 = (2,3,5)
task_three_test_2 = (2,3,5,7,9)
formatter(task_three_test_1)
formatter(task_three_test_2)


# Task Four

print("\nTask Four")
tuple_four = (4, 30, 2017, 2, 27)
print("{3:02d} {4:02d} {2:02d} {0:02d} {1:02d}".format(tuple_four[0], tuple_four[1], tuple_four[2], tuple_four[3], tuple_four[4]))


# Task Five

print("\nTask Five")
list_five = ['oranges', 1.3, 'lemons', 1.1]
print(f"The weight of an {list_five[0][:-1]} is {list_five[1]} and the weight of a {list_five[2][:-1]} is {list_five[3]}.")
print(f"The weight of an {list_five[0][:-1].upper()} is {list_five[1]*1.2} and the weight of a {list_five[2][:-1].upper()} is {list_five[3]*1.2}.")


# Task Six
print("\nTask Six")
rows = (
    ("Bob", 350, "$24.15"),
    ("A_bunch_of_random_names_strung_together_into_one_really_long_name", 9, "$10000.00"),
    ("Jimmy Johns", 555555555555555555555555555555555555555, "$100000000000000.00"),
    ("Sally", 85, "$0.45"),
    ("Mr. Rogers", 105, "$999999999999999999999999.99"))
max_len_str = [0]*len(rows) # List providing the lengths of the longest items in each column
for row in rows:
    for item in range(len(row)):
        if(len(str(row[item]))) > max_len_str[item]:
            max_len_str[item] = len(str(row[item]))

format_string_six = f'{{:<{max_len_str[0]+5}}}{{:<{max_len_str[1]+5}}}{{:<{max_len_str[2]+5}}}' # Format string taking into account the longest item in each column.

for row in rows:
    print(format_string_six.format(*row))
    
print("\nTask Six Bonus")
tuple_six = (1,2,3,4,5,6,7,8,9,10)
print(("{:<5}"*len(tuple_six)).format(*tuple_six))