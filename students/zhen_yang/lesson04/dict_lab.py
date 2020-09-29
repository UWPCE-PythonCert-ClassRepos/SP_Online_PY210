###################################
# Exercise for Dictionary and Set #
###################################


##################
# Dictionaries 1 #
##################
# create a dictionary
print("-------------- Dictionaries 1 Exercise ----------------")
dic_1 = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
print(f"1. The dic1 :{dic_1}")
# delete the entry for "cake"
dic_1.pop('cake')
print(f"2. The dic1 :{dic_1}")
# add an entry for "fruit" with "Mango"
dic_1['fruit'] = 'Mango'
print(f"3. The dic1 :{dic_1}")
# display the dictionary keys.
print("Dictionary Keys: ", end="")
for key in dic_1:
    print(f"{key} ", end="")
print("\n")
# display the dictionary values.
print("Dictionary Values: ", end="")
for val in dic_1.values():
    print(f"{val} ", end="")
print("\n")
# Display whether or not "cake" is a key in the dictonary
print(f" Is cake in dic_1?: {'cake' in dic_1}")
# Display whether or not "Mango" is a value in the dictonary
print(f" Is Mango in dic_1?: {'Mango' in dic_1.values()}")


##################
# Dictionaries 2 #
##################
# Based on the dictionary from Dictonaries 1,
# Make a new dictionary using the same keys but with the number of 't's
# in each value as the value.
print("-------------- Dictionaries 2 Exercise ----------------")
print(f" Old dictionary: {dic_1}")
dic_2 = {}
for key, val in dic_1.items():
    num = val.lower().count('t') # tot number of 't's in value
    dic_2[key] = num
print(f" New dictionary: {dic_2}")

##########
# Sets   #
##########
# Create sets s2, s3 and s4 that contain numbers from zero through twenty,
# divisible by 2, 3, and 4 (figure out a way to compute those)
# set s2 divisible by 2
print("-------------- Sets Exercise ----------------")
s2 = set(range(0, 21, 2))
print(f"Set s2: {s2}")
s3 = set(range(0, 21, 3))
print(f"Set s3: {s3}")
s4 = set(range(0, 21, 4))
print(f"Set s4: {s4}")
# Display if s3 is a subset of s2
print(f" Is set s3 a subset of s2? {s3.issubset(s2)}")
# Display if s4 is a subset of s2
print(f" Is set s4 a subset of s2? {s4.issubset(s2)}")


###########
# Sets  2 #
###########
# Create a set with the letters in 'Python' and add 'i' to the set
print("-------------- Sets 2 Exercise ----------------")
my_set = {'Python'}
my_set.add('i')
print(f" my_set:{my_set}")
# create a frozenset with letters in 'marathon'
frozenset = {'marathon'}
print(f" frozenset:{frozenset}")
# Display the union and intersection of the two sets
print(f" Union of my_set and frozenset: {my_set.union(frozenset)}")
print(f" Intersection of my_set and frozenset:\
    {my_set.intersection(frozenset)}")
