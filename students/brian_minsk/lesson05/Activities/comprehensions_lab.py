# Author: Brian Minsk

food_prefs = {"name": "Chris",
              "city": "Seattle",
              "cake": "chocolate",
              "fruit": "mango",
              "salad": "greek",
              "pasta": "lasagna"}

"""Print the dict by passing it to a string format method, so that you get
something like: 'Chris is from Seattle, and he likes chocolate cake, mango
fruit, greek salad, and lasagna pasta'
"""

print(f"{food_prefs['name']} is from {food_prefs['city']} and he likes \
{food_prefs['cake']} cake, {food_prefs['fruit']} fruit, {food_prefs['salad']} \
salad, and {food_prefs['pasta']} pasta.")

"""Using a list comprehension, build a dictionary of numbers from zero to
fifteen and the hexadecimal equivalent (string is fine). (the hex() function
gives you the hexidecimal representation of a number as a string)
"""

# first way
dec_list = [i for i in range(16)]
hex_list = [hex(i) for i in range(16)]
dex_hex_dict1 = dict(zip(dec_list, hex_list))

# second way
dec_hex_list = [(d, hex(d)) for d in range(16)]
dec_hex_dict2 = {d: h for (d, h) in dec_hex_list}

"""Do the previous entirely with a dict comprehension – should be a one-liner
"""

dec_hex_dict3 = {dec: hex(dec) for dec in range(16)}

"""

