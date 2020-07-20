#!/usr/bin/env python3
"""
Purpose: Lessen 4 homework one, Dictionaries, Sets, and file lab, python certificate from UW
Author: Pirouz Naghavi
Date: 07/06/2020
"""

# imports
import copy
import os
import pathlib

# Dictionaries One
dict_1 = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}

# Displaying dictionary
print(dict_1)

# Delete cake
del dict_1['cake']

# Displaying dictionary
print(dict_1)

# Adding fruit: Mango
dict_1['fruit'] = 'Mango'

# Displaying dictionary keys
print(dict_1.keys())

# Displaying dictionary values
print(dict_1.values())

# Displaying if cake is in the dictionary
print('cake' in dict_1)

# Displaying if Mango is in dictionary
print('Mango' in dict_1.values())

# Dictionaries Two

# Creating shallow copy
dict_2 = dict_1.copy()

# Creating deep copy
dict_2_deep = copy.deepcopy(dict_1)

# Changing values to match what is shown
dict_2['name'] = 0
dict_2_deep['name'] = 0

dict_2['city'] = 2
dict_2_deep['city'] = 2

dict_2['cake'] = 2
dict_2_deep['cake'] = 2

del dict_2['fruit']
del dict_2_deep['fruit']

# Displaying results
print('Normal copy:', dict_2)
print('Deep copy:', dict_2_deep)

# Sets

# Creating sets s2, s3, s4
s2 = set(range(0, 21, 2))
s3 = set(range(0, 21, 3))
s4 = set(range(0, 21, 4))

# Printing sets s2, s3, s4
print('Printing s2:', s2)
print('Printing s3:', s3)
print('Printing s4:', s4)

# Printing id s3 is a subset of s2
print('Is s3 a subset of s2?', s3.issubset(s2))

# Printing id s4 is a subset of s2
print('Is s4 a subset of s2?', s4.issubset(s2))

# Sets 2

# Python and I set
python_and_i_set = set('python')
python_and_i_set.add('i')

# Frozen set of marathon
marathon_frozenset = frozenset('marathon')

# Printing both sets
print('Python and I set:', python_and_i_set)
print('Frozen marathon set:', marathon_frozenset)

# Displaying intersection
print('Intersection of \'pythoni\' and \'marathon\' is :', python_and_i_set.intersection(marathon_frozenset))

# Displaying union
print('Union of \'pythoni\' and \'marathon\' is :', python_and_i_set.union(marathon_frozenset))

# File Exercise

# Deep file at path
'''print(r'Files at paths (deep operation) "C:/Users/pinag/Desktop/" are:')
current_path = pathlib.Path('C:/Users/pinag/Desktop/')
files_list = []
for (dirpath, dirnames, filenames) in os.walk(current_path):
    for file in filenames:
        files_list.append(pathlib.Path(dirpath + '/' + file))

for file in files_list:
    print(file)'''

# Shallow file at path
current_path = pathlib.Path('C:/Users/pinag/Desktop/')
print(r'Files at paths "C:\Users\pinag\Desktop\" are:')
files_list_shallow = []
for (dirpath, dirnames, filenames) in os.walk(current_path):
    files_list_shallow.extend(filenames)
    break

for file in files_list_shallow:
    print(file)

# Copying a small file
small_file_path = pathlib.Path('C:/Users/pinag/Desktop/CSE547DMBD/project/IMG_0013.jpg')
small_file_path_copy = pathlib.Path('C:/Users/pinag/Desktop/CSE547DMBD/project/IMG_0013_copy.jpg')

with open(small_file_path, 'rb', buffering=10000) as input_file:
    with open(small_file_path_copy, 'wb') as output_file:
        for line in input_file:
            output_file.write(line)

'''# Copying a big file
big_file_path = pathlib.Path('C:/Users/pinag/Desktop/CSE547DMBD/project/data.zip')
big_file_path_copy = pathlib.Path('C:/Users/pinag/Desktop/CSE547DMBD/project/data_copy.zip')

with open(big_file_path, 'rb', buffering=10000) as input_file:
    with open(big_file_path_copy, 'wb') as output_file:
        for line in input_file:
            output_file.write(line)'''

# All the programming languages
all_languages = set()
students_path = pathlib.Path(
    'C:/Users/pinag/Desktop/Python Certificate/PirouzNaghavi/SP_Online_PY210/students/Pirouz_N/lesson04/students.txt')
skip_first_line = True
with open(students_path, 'r') as input_file:
    for line in input_file:
        if skip_first_line:
            skip_first_line = False
            continue
        for languages in line.split(':')[1].split(','):
            languages = languages.split()
            for language in languages:
                if not language.istitle() and language != 'nothing':
                    all_languages.add(language.strip())
print('All the languages in the file are:', all_languages)
