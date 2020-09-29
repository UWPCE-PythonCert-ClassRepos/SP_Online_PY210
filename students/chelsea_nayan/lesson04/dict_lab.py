# chelsea_nayan, UWPCE Python 210, Lesson04: Dictionary Lab Exercise

# Dictinaries 1--------------------------------------------

about = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'} # A Dictionary

print(about)# Displays the dictionary
del about['cake']# Deletes the 'cake' entry
print(about)# Displays the new dictionary
about['fruit'] = 'mango'# Adds an entry for 'fruit' and 'mango' and displays the new Dictionary
print(about)

print(about.keys())# Displays the keys
print(about.values())# Displays the values
print('cake' in about.keys())# Displays whether or not 'cake' is a key in the Dictionary (False)
print('mango' in about.values())# Displays whether or not 'mango' is a value in the dictionary (True)

# Dictionaries 2 ------------------------------------------

# Make a dictionary using the same keys but with the number of 't's in each value as the value
about0, about1 = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}, {} # A Dictionary
for k, v in about0.items():
    about1[k] = v.lower().count('t')
print(about1)

# Sets 1 ---------------------------------------------------
# Create sets s2, s3, and s4 that contain numbers from 0-20, divisible by 2,3,and 4
lst = range(0, 21)
s2, s3, s4 = set(lst[0:21:2]), set(lst[0:21:3]), set(lst[0:21:4])

# Displays the sets
print(s2)
print(s3)
print(s4)

print(s3.issubset(s2))# Displays if s3 is a subset of s2 (False)
print(s4.issubset(s2))# Displays if s4 is a subset of s2 (True)

# Sets 2 ------------------------------------------------------
# Create a set with the letters in 'Python' and add 'i' to the sets
lst1 = "python"
s5 = set(lst1)
s5.update('i')
print(s5)

# Create a frozenset with the letters in 'marathon'
fs = frozenset('marathon')
print(fs)
# Display the union and intersection of the two sets
print(fs.union(s5)) # Combines all keys from fs and s5 with no repeats
print(fs.intersection(s5)) # Combines keys that appear in fs AND s5

# Activity 2 ----------------------------------------------- Program writing!

# Prints the full path for all files in the current dictionary, one per line
# Copies a file from a source to a destination (without using shutil, or the OS copy command)
## Make it work for any size file
## Should open the files in binary mode:open(filename, 'rb') or 'wb' for writing
## Test it with both text and binary files
