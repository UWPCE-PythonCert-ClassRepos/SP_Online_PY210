#!/usr/bin/env python3

#### Files Lab Exercises

import sys
import pathlib
import os

# Write a program that lists all files in the current directory
cur_dir = os.listdir()

for f in cur_dir:
    print(f)

# Copy a file
print('Not sure how to do this')

# Read students.txt and list languages that are in list
students_lang = list()
s_l = list()
languages = set()
unique_lang = set()

with open('students.txt', 'r') as infile:
    rows = infile.readlines()
    for line in rows:
        line = line.split(':', 1)[-1]
        students_lang.append(line)
        
    for row in students_lang:
        row = row[:-1]
        s_l.append(row)
        
    for l in s_l:
        all_lang = l.split(', ')
        for lang in all_lang:
            if lang.islower() is True:
                languages.add(lang)

# Need to dedup set
for x in languages:
    if x not in unique_lang:
        unique_lang.add(x)

print('Here is a list of langauges used by the students.')
print(unique_lang)
print('Ok I guess it did not completely remove dups...'n)


        



