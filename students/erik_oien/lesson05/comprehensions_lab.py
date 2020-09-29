#!/usr/bin/python

# List comprehensions

feast = ['lambs', 'sloths', 'orangutans', 'breakfast cereals', 'fruit bats']

comprehension = [delicacy.capitalize() for delicacy in feast]

print(comprehension[0])
print(comprehension[2])


# Filtering lists with list comprehensions

feast = ['spam', 'sloths', 'orangutans', 'breakfast cereals', 'fruit bats']

comp = [delicacy for delicacy in feast if len(delicacy) > 6]

print(len(feast))
print(len(comp))

# Unpacking tuples in list comprehensions

list_of_tuples = [(1, 'lumberjack'), (2, 'inquisition'), (4, 'spam')]

comprehension = [ skit * number for number, skit in list_of_tuples ]

print(comprehension[0])
print(len(comprehension[2]))

# Double list comprehensions

eggs = ['poached egg', 'fried egg']
meats = ['lite spam', 'ham spam', 'fried spam']

comprehension = [ '{0} and {1}'.format(egg, meat) for egg in eggs for meat in meats]

print(len(comprehension))
print(comprehension[0])

# Set comprehensions

comprehension = { c for c in 'aabbbcccc'}

print(comprehension)

# Dictionary comprehensions

dict_of_weapons = {'first': 'fear',
                       'second': 'surprise',
                       'third':'ruthless efficiency',
                       'forth':'fanatical devotion',
                       'fifth': None}

dict_comprehension = { k.upper(): weapon for k, weapon in dict_of_weapons.items() if weapon}

print('first' in dict_comprehension)
print('FIRST' in dict_comprehension)
print(len(dict_of_weapons))
print(len(dict_comprehension))

# Count Even Numbers

def count_evens(nums):
    new_nums = [num for num in nums if num %2 == 0]
    return len(new_nums)

print(count_evens([2, 1, 2, 3, 4])== 3)
print(count_evens([2, 2, 0]) == 3)
print(count_evens([1, 3, 5]) == 0)

# dict and set comprehensions

# food_prefs = {"name": "Chris",
#               "city": "Seattle",
#               "cake": "chocolate",
#               "fruit": "mango",
#               "salad": "greek",
#               "pasta": "lasagna"}

# food_prefs = {"name": "Chris", "city": "Seattle"}

# Print the dict by passing it to a string format method, so that you get something like:

# "Chris is from Seattle, and he likes chocolate cake, mango fruit, greek salad, and lasagna pasta"


# '{} is from {}, and he likes {} cake, {} fruit, {} salad, and {} pasta'.format(test)

data = {prefs in prefs for food_prefs.items()}

print(food_prefs)
