#!/usr/bin/env python3
# =============================================================================
# Python210 | Fall 2020
# -----------------------------------------------------------------------------
# Lesson05
# Comprehensions Lab (comprehensions_lab.py)
# Steve Long 2020-10-31 | v0
#
# Requirements:
# =============
#
#   Listed inline.
#
# Assumptions:
# ============
#
#   Minimalist solutions are satisfactory.
#
# Implementation:
# ===============
#
#   See below. Confirmation mostly accomplished with "assert".
#   Code format checked with flake8.
#
# Script Usage:
# =============
#
#   Not specified in instructions. Use "python comprehensions_lab.py".
#
# Issues:
# =======
#
#   Directions lack enumeration so please read instruction statement in the
#   inline comments.
#
#   Some ambiguity in requested output.
#
#   Decomp trick "**" for sequences not explicitly covered but based on the
#   fact that Python shares a lot of features found in Common Lisp, it makes
#   sense that this capability should exist (and it's a lot less weird than
#   Lisp syntax.) I had to Google for this.
#
# History:
# ========
# 000/2020-10-31/sal/Created and completed.
#
# =============================================================================

# List comprehensions. What is the output of comprehension[0] and
# comprehension[2]:

feast = ["lambs", "sloths", "orangutans", "breakfast cereals", "fruit bats"]

comprehension = [delicacy.capitalize() for delicacy in feast]

assert(comprehension[0] == "Lambs")
assert(comprehension[2] == "Orangutans")

# Filtering lists with list comprehensions. What is len(feast) and len(comp)?

feast = ["spam", "sloths", "orangutans", "breakfast cereals", "fruit bats"]

comp = [delicacy for delicacy in feast if len(delicacy) > 6]

assert(len(feast) == 5)
assert(len(comp) == 3)

# Unpacking tuples in list comprehensions. What is comprehension[0] and
# comprehension[2]?

list_of_tuples = [(1, "lumberjack"), (2, "inquisition"), (4, "spam")]

comprehension = [skit * number for number, skit in list_of_tuples]

assert(comprehension[0] == "lumberjack")
assert(comprehension[2] == "spamspamspamspam")

# Double list comprehensions. What is len(comprehension) and
# len(comprehension[0]?

eggs = ["poached egg", "fried egg"]

meats = ["lite spam", "ham spam", "fried spam"]

comprehension = \
    ["{0} and {1}".format(egg, meat) for egg in eggs for meat in meats]

assert(len(comprehension) == 6)
assert(len(comprehension[0]) == 25)

# Set comprehensions. What is comprehension?

comprehension = {c for c in "aabbbcccc"}

assert(comprehension == {"a", "b", "c"})

# Dictionary comprehensions. What is "first" in dict_comprehension,
# "FIRST" in dict_comprehension, len(dict_of_weapons), and
# len(dict_comprehension)?

dict_of_weapons = {"first": "fear", "second": "surprise",
                   "third": "ruthless efficiency",
                   "forth": "fanatical devotion",
                   "fifth": None}

dict_comprehension = \
    {k.upper(): weapon for k, weapon in dict_of_weapons.items() if weapon}

assert(("first" in dict_comprehension) is False)
assert(("FIRST" in dict_comprehension) is True)
assert(len(dict_of_weapons) == 5)
assert(len(dict_comprehension) == 4)


# Count Even Numbers. In a function called  count_evens, use list
# comprehension to return the number of even integers in the given list. Do
# this with a single line comprehension.

numberz = [3, 2, 6, 8, 12, 18, 17, 5, 7, 11, 10]


def count_evens(nums):
    return len([n for n in nums if (n % 2 == 0)])


expected = 6
actual = count_evens(numberz)
assert(actual == expected)


# Dict and set comprehensions

# [1] Use food_prefs and str.format to print "Chris is from Seattle, and he
#     likes chocolate cake, mango fruit, greek salad, and lasagna pasta".

food_prefs = {"name": "Chris", "city": "Seattle",
              "cake": "chocolate",
              "fruit": "mango",
              "salad": "greek",
              "pasta": "lasagna"}

expected = ("Chris is from Seattle, and he likes chocolate cake, mango fruit,"
            " greek salad, and lasagna pasta")

actual = ("{name} is from {city},"
          " and he likes {cake} cake,"
          " {fruit} fruit, {salad} salad,"
          " and {pasta} pasta").format(**food_prefs)

print(actual)
assert(actual == expected)


# [2] Use list comprehension to build a dict mapping of numbers from 0 to 15
#     to their hex equivalent.

expected = {0: '0x0', 1: '0x1', 2: '0x2', 3: '0x3', 4: '0x4', 5: '0x5',
            6: '0x6', 7: '0x7', 8: '0x8', 9: '0x9', 10: '0xa', 11: '0xb',
            12: '0xc', 13: '0xd', 14: '0xe', 15: '0xf'}

i_list = [i for i in range(0, 16)]
h_list = [hex(i) for i in i_list]
actual = dict(zip(i_list, h_list))

assert(actual == expected)


# [3] Solve previous problem with single line of dict comprehension.

actual = {i: hex(i) for i in range(0, 16)}
assert(actual == expected)


# [4] Using the dictionary from item [1]: Make a dictionary using the same
#     keys but with the number of "a"s in each value.

expected = {'name': 0, 'city': 1, 'cake': 1, 'fruit': 1,
            'salad': 0, 'pasta': 3}

food_pref_acounts = \
    {food: value.count("a") for (food, value) in food_prefs.items()}

print(food_pref_acounts)

assert(food_pref_acounts == expected)


# [5] Create sets s2, s3 and s4 that contain numbers from zero through twenty,
#     divisible 2, 3 and 4.

# [5a] Do this with one set comprehension for each set.

s2 = {n for n in range(0, 21) if ((n % 2) == 0)}
s3 = {n for n in range(0, 21) if ((n % 3) == 0)}
s4 = {n for n in range(0, 21) if ((n % 4) == 0)}


# [5b]   What if you had a lot more than 3?
# [5b.a] Create a sequence that holds all the divisors you might want – could
#        be 2,3,4, or could be any other arbitrary divisors.
# [5b.b] Loop through that sequence to build the sets up – so no repeated
#        code. You will end up with a list of sets – one set for each divisor
#        in your sequence.

expected = [{0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20},
            {0, 3, 6, 9, 12, 15, 18},
            {0, 4, 8, 12, 16, 20}]

actual = []
for d in range(2, 5):
    actual.append({n for n in range(0, 21) if ((n % d) == 0)})
print(actual)

assert(actual == expected)

# [5b.c] The idea here is that when you see three (Or more!) lines of code
#        that are almost identical, then you you want to find a way to
#        generalize that code and have it act on a set of inputs, so the
#        actual code is only written once.


def multiples_of(from_n, to_n, from_divisor, to_divisor):
    """
    Generate sets of multiples of numbers over a specified number and multiple
    range. A generalized [5c] solution.
    """
    sets = []
    result = None
    try:
        for d in range(from_divisor, to_divisor + 1):
            sets.append({n for n in range(from_n, to_n + 1) if ((n % d) == 0)})
    except TypeError as ex:
        #
        # At this point, this is only useful in academic exercise. For
        # production code, this error should be raised again and caught
        # at the next level.
        #
        print("multiples_of({}, {}, {}, {}): {}"
              .format(from_n, to_n, from_divisor, to_divisor, ex))
        result = None
    else:
        result = sets
    return result


actual = multiples_of(0, 20, 2, 4)
assert(actual == expected)

# [5c] Extra credit: do it all as a one-liner by nesting a set comprehension
#      inside a list comprehension.

expected = [{0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20},
            {0, 3, 6, 9, 12, 15, 18},
            {0, 4, 8, 12, 16, 20}]

actual = [{n for n in range(0, 21) if (n % d == 0)} for d in range(2, 5)]
assert(actual == expected)


def multiples_of(from_n, to_n, from_divisor, to_divisor):
    """
    Generate sets of multiples of numbers over a specified number and multiple
    range. A generalized [5c] solution.

    :param from_n ::= Lower number
    :param to_n ::= Upper number
    :param from_divisor ::= Lower multiple
    :param to_divisor ::= Upper multiple
    """
    sets = None
    try:
        sets = [{n for n in range(from_n, (to_n + 1)) if (n % d == 0)}
                for d in range(from_divisor, (to_divisor + 1))]
    except TypeError as ex:
        sets = None
        raise ex
    return sets


actual = multiples_of(0, 20, 2, 4)
assert(actual == expected)
