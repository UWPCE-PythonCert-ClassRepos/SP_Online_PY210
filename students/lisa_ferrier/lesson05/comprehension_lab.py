#!/usr/bin/env python
# comprehension_lab.py
# Lisa Ferrier, Python 210, Lesson 05


# count even numbers using a list comprehension
def count_evens(nums):
    ct_evens = len([num for num in nums if num % 2 == 0])
    return ct_evens


food_prefs = {"name": "Chris",
              "city": "Seattle",
              "cake": "chocolate",
              "fruit": "mango",
              "salad": "greek",
              "pasta": "lasagna"}


# 1 .Using the string format method, read food_prefs as a sentence.
food_prefs_string = "{name} is from {city} and he likes {cake} cake, {fruit} fruit, {salad} salad, and {pasta} pasta.".format(**food_prefs)

# 2 Using a list comprehension,build a dictionary of numbers from zero to fifteen and the hexadecimal equivalent
num_list = [(n, hex(n)) for n in list(range(0, 16))]


# 3 Same as before, but using a dict comprehension.
num_list = {n: hex(n) for n in range(0, 16)}

# 4 Make a new dict with same keys but with the number of a's in each value
food_prefsa = {(k, v.count('a')) for k, v in food_prefs.items()}

# 5 Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible 2, 3 and 4

# 5a Do this with one set comprehension for each set.
s2 = {n for n in list(range(0, 21)) if n % 2 == 0}
s3 = {n for n in list(range(0, 21)) if n % 3 == 0}
s4 = {n for n in list(range(0, 21)) if n % 4 == 0}

# 5c create sets using nested set comprehension on one line:
nums = list(range(0, 21))
divisors = [2, 3, 4, 5]

divisor_sets = [{n for n in nums if n % d == 0} for d in divisors]
