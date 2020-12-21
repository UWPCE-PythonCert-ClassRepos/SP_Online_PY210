#!/usr/bin/env python3

import sys
import pathlib
import os
import re

# Print all files in current directory

cwd = os.listdir('.')
for f in cwd:
    print(os.path.abspath(f))


# Copy a file from source to destination

def copy_file(source, dest):
    file = open(source, 'rb')
    file_copy = file.read()
    out_file = open(dest, 'wb') 
    out_file.write(file_copy)

# Parse students.txt and create the list of languages

filename = pathlib.Path(__file__).parent / 'students.txt'
file = open(filename, 'r')
languages = {}
for line in file.readlines():
    if line == 'Name: Nickname, languages\n':
        continue
    lines = re.split(':|,', line)
    for s in lines:
        if s.islower():
            s = s.strip()
            # Add language to dict and keep a count of usage
            if not s in languages:
                languages[s] = 1
            elif s in languages:
                languages[s] += 1

print('{:15} {}'.format('\nLanguage', 'Number of users'))
print('-' * 40)
for k, v in languages.items():
    print("{:13} {:>9}".format(k, v))






