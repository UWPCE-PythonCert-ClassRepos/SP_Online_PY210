#!/usr/bin/env python3

'''

'''

# Task One

input_tuple = ( 2, 123.4567, 10000, 12345.67)
formatted_string = "file_{:0>3} :   {:5.2f}, {:3.2e}, {:3.2e}".format(*input_tuple)
print(formatted_string)

# Task Two

alt_formatted_string = f"""file_{input_tuple[0]:0>3} :   {input_tuple[1]:5.2f}, 
{input_tuple[2]:3.2e}, {input_tuple[3]:3.2e}""".replace('\n', '')
print(alt_formatted_string)

# Task Three

def formatter(input_tuple):
    formatter_string = f"the {len(input_tuple)} numbers are: "
    for tup in input_tuple:
        formatter_string += f"{tup}, "
    formatter_string = formatter_string[:-2]
    return formatter_string
print(formatter((2,3,5,7,9)))

# Task Four

five_tuple = (4, 30, 2017, 2, 27)
formatted_five_tuple = f"{five_tuple[3]:0>2} {five_tuple[4]} {five_tuple[2]} {five_tuple[0]:0>2} {five_tuple[1]}"
print(formatted_five_tuple)

# Task Five

fruits = ['oranges', 1.3, 'lemons', 1.1]
fruits_string = f"the weight of an {fruits[0][:-1]} is {fruits[1]} and the weight of a {fruits[2][:-1]} is {fruits[3]}"
mod_fruits_string = f"the weight of an {fruits[0][:-1].upper()} is {fruits[1] * 1.20} and the weight of a {fruits[2][:-1].upper()} is {fruits[3] * 1.20}"
print(fruits_string)
print(mod_fruits_string)
