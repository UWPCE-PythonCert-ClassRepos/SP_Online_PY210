#!/usr/bin/env python

import os
from pathlib import Path

# print file paths in current directory

p = Path('./')

# cycle through files in directory and print them
for dirpath, dirnames, filenames in os.walk(p):
    for f in filenames:
        print(os.path.abspath(os.path.join(dirpath, f)))

# copy contents of one file to another

# open infile
with open('students.txt', 'rb') as infile:

    # open outfile
    with open('students_copy.txt', 'wb') as outfile:
        for i in range(os.path.getsize('students.txt')):
            infile.seek(i)
            outfile.write(infile.read(1))
    outfile.close()
infile.close()


no_names = list()
languages = set()
with open('students.txt', 'r') as infile:
    lines = infile.readlines()
    for line in lines:
        line = line.split(':', 1)[-1].strip()
        no_names.append(line)
    for line in no_names:
        list_words = line.split(', ')
        for word in list_words:
            if word.islower() is True:
                languages.add(word)


print(languages)


