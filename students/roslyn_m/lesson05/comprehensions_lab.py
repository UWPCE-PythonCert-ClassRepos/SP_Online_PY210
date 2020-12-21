feast = ['lambs', 'sloths', 'orangutans', 'breakfast cereals', 'fruit bats']
comprehension = [thing.capitalize() for thing in feast]
print(comprehension)
print(comprehension[0])
print(comprehension[1])

feast = ['spam', 'sloths', 'orangutans', 'breakfast cereals', 'fruit bats']
comp = [delicacy for delicacy in feast if len(delicacy) > 6]
print(len(feast))
print(len(comp))

list_of_tuples = [(1, 'lumberjack'), (2, 'inquisition'), (4, 'spam')]
comprehension = [ skit * number for number, skit in list_of_tuples ]
print(comprehension[0])
print(len(comprehension[2]))

eggs = ['poached egg', 'fried egg']
meats = ['lite spam', 'ham spam', 'fried spam']
comprehension = [ '{0} and {1}'.format(egg, meat) for egg in eggs for meat in meats]
print(comprehension)
print(len(comprehension))
print(comprehension[0])

comprehension = { c for c in 'aabbbcccc'}
print(comprehension)

dict_of_weapons = {'first': 'fear', 'second': 'surprise', 'third':'ruthless efficiency', 'forth':'fanatical devotion','fifth': None}
dict_comprehension = { k.upper(): weapon for k, weapon in dict_of_weapons.items() if weapon}
print(dict_comprehension)
print('first' in dict_comprehension)
print('FIRST' in dict_comprehension)
print(len(dict_of_weapons))
print(len(dict_comprehension))

listcount = [1, 2, 3, 4, 5]
comprehension = [number % 2 == 0 for number in listcount]
print(comprehension)

# Print the dict by passing it to a string format method, so that you get something like:
# “Chris is from Seattle, and he likes chocolate cake, mango fruit, greek salad, and lasagna pasta”
food_prefs = {"name": "Chris",
              "city": "Seattle",
              "cake": "chocolate",
              "fruit": "mango",
              "salad": "greek",
              "pasta": "lasagna"}
comprehension = {'{name} is from {city}, and he likes {cake}, {fruit}, {salad}, and {pasta}'.format(**food_prefs) for pref in food_prefs}
print(comprehension)

# Using a list comprehension, build a dictionary of numbers from zero to fifteen and the hexadecimal equivalent (string is fine). (the hex() function gives you the hexidecimal representation of a number as a string)
hexlist = [i for i in range(16)]
print(hexlist)
hexkey = [hex(thing) for thing in hexlist]
dict_hex = dict(zip(hexkey, hexlist))
print(dict_hex)

# Do the previous entirely with a dict comprehension – should be a one-liner
# ^ Need to come back to this one. Not sure how to do it

# Using the dictionary from item (1): Make a dictionary using the same keys but with the number of ‘a’s in each value. You can do this either by editing the dict in place, or making a new one. If you edit in place make a copy first!





