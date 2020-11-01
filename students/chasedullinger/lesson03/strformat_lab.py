#!/usr/bin/env python3
# PY210 Lesson 03 Slicing Lab Exercise - Chase Dullinger

# Task 1
working_tuple = (2, 123.4567, 10000, 12345.67)

output_string = "file_{:03d} :   {:.2f}, {:.2e}, {:.2e}".format(*working_tuple)


print(output_string)
# Test against string from assignment
assert output_string == "file_002 :   123.46, 1.00e+04, 1.23e+04"

# Task 2 Alternate formatting method
alternate_format_string = f"file_{working_tuple[0]:03d} : \
  {working_tuple[1]:.2f}, {working_tuple[2]:.2e}, {working_tuple[3]:.2e}"

print(alternate_format_string)

assert alternate_format_string == "file_002 :   123.46, 1.00e+04, 1.23e+04"


def formatter(in_tuple):
    form_string = "the {} numbers are:{}{}".format(len(in_tuple), " {:d},"*(
                                                len(in_tuple) - 1), " {:d}")
    return form_string.format(*in_tuple)


print(formatter((2, 3, 5)))

print(formatter((2, 3, 5, 7, 9)))

assert formatter((2, 3, 5)) == 'the 3 numbers are: 2, 3, 5'
assert formatter((2, 3, 5, 7, 9)) == 'the 5 numbers are: 2, 3, 5, 7, 9'


five_elements = (4, 30, 2017, 2, 27)

five_element_string = "{:02d} {:02d} {:04d} {:02d} {:02d}".format(
    five_elements[3], five_elements[4], five_elements[2],
    five_elements[0], five_elements[1])

print(five_element_string)

assert five_element_string == '02 27 2017 04 30'

# Task 5
four_element_list = ['oranges', 1.3, 'lemons', 1.1]

four_element_string = f"The weight of an {four_element_list[0][:-1]}\
 is {four_element_list[1]} and the weight of a {four_element_list[2][:-1]}\
 is {four_element_list[3]}"

print(four_element_string)
assert four_element_string == "The weight of an orange is 1.3 and the weight \
of a lemon is 1.1"

four_element_modified_string = f"The weight of an \
{four_element_list[0][:-1].upper()}\
 is {four_element_list[1] * 1.2} \
 and the weight of a {four_element_list[2][:-1].upper()}\
  is {four_element_list[3] * 1.2}"

print(four_element_modified_string)

# Task 6
name_list = ["Bob", "Sue", "Joe", "John", "Jane"]
age_list = [34, 23, 35, 12, 54]
cost_list = [10, 10000, 34, 245, 898]

longest_name = len(max(name_list, key=len))
longest_age = len(str(max(age_list)))
longest_cost = len(str(max(cost_list)))

print(longest_name)
print(longest_age)
print(longest_cost)

print("{0:<{1}} {2:>{3}}{4:>{5}}".format("name", longest_name,
                                         "age",
                                         longest_age,
                                         "cost",
                                         longest_cost))
for i, name in enumerate(name_list):
    string_to_print = "{0:<{1}} {2:>{3}} {4:>{5}}".format(name, longest_name,
                                                          age_list[i],
                                                          longest_age,
                                                          cost_list[i],
                                                          longest_cost)
    print(string_to_print)

consecutive_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print("".join("{:<5}"*len(consecutive_tuple)).format(*consecutive_tuple))
