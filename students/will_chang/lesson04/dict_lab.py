# Dictionaries 1

print("Dictionaries 1\n--------------\n")
dict_1 = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
print(dict_1)

print("\nThe entry for cake was removed from the dictionary.")
dict_1.pop('cake')
print(dict_1)

print("\nAn entry for fruit was added to the dictionary.")
dict_1['fruit'] = 'Mango'
print("\nHere are the dictionary's current keys:")
print(dict_1.keys())
print("\nHere are the dictionary's current values:")
print(dict_1.values())

print("\nCheck if 'cake' is a key in the dictionary: {}".format('cake' in dict_1.keys()))
print("\nCheck if 'Mango' is a value in the dictionary: {}".format('Mango' in dict_1.values()))


# Dictionaries 2
print("\n\nDictionaries 2\n--------------\n")
print("Here's the dictionary from Dictionaries 1:")
print(dict_1)
dict_2 = dict_1.copy()
for key in dict_2:
    dict_2[key] = dict_2[key].lower().count('t')
print("\nThis is a new dictionary with the same keys from dictionary 1 but with the number of 't's in each value as the corresponding dictionary 1 value:")
print(dict_2)


# Sets 1
print("\n\nSets 1\n------\n")
s2 = set(range(0, 21, 2))
s3 = set(range(0, 21, 3))
s4 = set(range(0, 21, 4))

print("Here is a set s2 containing numbers from 0 - 20 that are divisble by 2:\n{}".format(s2))
print("\nHere is a set s3 containing numbers from 0 - 20 that are divisble by 3:\n{}".format(s3))
print("\nHere is a set s4 containing numbers from 0 - 20 that are divisble by 4:\n{}".format(s4))

print("\nCheck if s3 is a subset of s2: {}".format(s3.issubset(s2)))
print("\nCheck if s4 is a subset of s2: {}".format(s4.issubset(s2)))


# Sets 1
print("\n\nSets 2\n------\n")
s_python = set(['P','y','t','h','o','n'])
s_python.add('i')
print("This is a set with the letters in 'Python' with 'i' added:\n{}".format(s_python))

fs_marathon = frozenset(['m', 'a', 'r', 't', 'h', 'o', 'n'])
print("\nThis is a frozenset with the letters in 'marathon':\n{}".format(fs_marathon))

print("\nThis is the union of the set and frozenset:\n{}".format(s_python.union(fs_marathon)))
print("\nThis is the intersection of the set and frozenset:\n{}".format(s_python.intersection(fs_marathon)))