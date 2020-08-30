#!/usr/bin/env python3

'''
lab is intended to be a practice with formmating strings in Python
(both with the traditional ".format()" method, as well as using the
newer "fstring" method.)  The exercises are broken up into 6 tasks.
'''

# Task One

print("Task One")
input_tuple = (2, 123.4567, 10000, 12345.67)
formatted_string = (
    "file_{:0>3} :   {:5.2f}, {:3.2e}, {:3.2e}"
    ).format(*input_tuple)
print(formatted_string)
print()

# Task Two

print("Task Two")
alt_formatted_string = f"""file_{input_tuple[0]:0>3} :   {input_tuple[1]:5.2f},
{input_tuple[2]:3.2e}, {input_tuple[3]:3.2e}""".replace('\n', '')
print(alt_formatted_string)
print()

# Task Three

print("Task Three")


def formatter(input_tuple):
    formatter_string = f"the {len(input_tuple)} numbers are: "
    for tup in input_tuple:
        formatter_string += f"{tup}, "
    formatter_string = formatter_string[:-2]
    return formatter_string


print(formatter((2, 3, 5, 7, 9)))
print()

# Task Four

print("Task Four")
five_tuple = (4, 30, 2017, 2, 27)
formatted_five_tuple = f"{five_tuple[3]:0>2} {five_tuple[4]} {five_tuple[2]} "
f"{five_tuple[0]:0>2} {five_tuple[1]}"
print(formatted_five_tuple)
print()

# Task Five

print("Task Five")
fruits = ['oranges', 1.3, 'lemons', 1.1]
fruits_string = f"the weight of an {fruits[0][:-1]} is {fruits[1]} and the "
f"weight of a {fruits[2][:-1]} is {fruits[3]}"
mod_fruits_string = f"the weight of an {fruits[0][:-1].upper()} is "
f"{fruits[1] * 1.20} and the weight of a {fruits[2][:-1].upper()} "
f"is {fruits[3] * 1.20}"
print(fruits_string)
print(mod_fruits_string)
print()

# Task Six

print("Task Six")
name_age_cost_list = ([["name1", 1, 12.50], ["name2", 2, 500.00],
                      ["name3", 50, 100000.00]])
header_list = ["Name", "Age", "Cost"]
print(f"|{header_list[0]:^10}|{header_list[1]:^5}|{header_list[2]:^16}|")
for item in name_age_cost_list:
    print(f"|{item[0]:10}|{item[1]:5}| ${item[2]:14,.2f}|")
print()
ten_int_tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(("{:5}\n"*len(ten_int_tup)).format(*ten_int_tup))
