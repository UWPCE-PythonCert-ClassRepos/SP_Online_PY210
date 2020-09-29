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
dec_hex_dict1 = dict(zip(dec_list, hex_list))

print("First list comprehension way:")
print(dec_hex_dict1)

# second way
dec_hex_list = [(d, hex(d)) for d in range(16)]
dec_hex_dict2 = {d: h for (d, h) in dec_hex_list}

print("Second list comprehension way:")
print(dec_hex_dict2)

"""Do the previous entirely with a dict comprehension – should be a one-liner
"""

dec_hex_dict3 = {dec: hex(dec) for dec in range(16)}

print("Dict comprehension way:")
print(dec_hex_dict2)

"""Using the dictionary from item (1): Make a dictionary using the same keys
but with the number of ‘a’s in each value. You can do this either by editing
the dict in place, or making a new one. If you edit in place make a copy first!
"""

food_prefs_a = {key: food_prefs[key].count('a') for key in food_prefs}

"""Create sets s2, s3 and s4 that contain numbers from zero through twenty,
divisible by 2, 3 and 4.
"""

"""a. Do this with one set comprehension for each set.
"""

def divisible_by_n(n):
    return {a for a in range(21) if a % n == 0}

s2 = divisible_by_n(2)
s3 = divisible_by_n(3)
s4 = divisible_by_n(4)

print(s2)
print(s3)
print(s4)

"""b. What if you had a lot more than 3? – Don’t Repeat Yourself (DRY).
-- create a sequence that holds all the divisors you might want –
    could be 2,3,4, or could be any other arbitrary divisors.
-- loop through that sequence to build the sets up – so no repeated code. you
    will end up with a list of sets – one set for each divisor in your sequence.
-- The idea here is that when you see three (Or more!) lines of code that
    are almost identical, then you you want to find a way to generalize
    that code and have it act on a set of inputs, so the actual code
    is only written once.
"""

def divisible_by_n_sets(max_divisor):
    set_list = []
    for d in range(2, max_divisor + 1):
        set_list.append(divisible_by_n(d))
    return set_list

print(divisible_by_n_sets(10))

"""Extra credit: do it all as a one-liner by nesting a set comprehension
inside a list
"""

divisible_up_to_10 = [{a for a in range(21) if a % n == 0} for n in range(2, 11)]
print(divisible_up_to_10)