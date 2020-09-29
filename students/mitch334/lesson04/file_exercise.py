"""Lesson 04 | File Exercise"""
# Goal: Get a little bit of practice with handling files and parsing simple text.

# Paths and File Processing
# Write a program which prints the full path for all files in the current directory, one per line
import os

cwd = os.getcwd()
for file in os.listdir(cwd):
    if not os.path.isdir(file):
        # print(os.path.join(cwd, file))
        print(os.path.abspath(file))

# Write a program which copies a file from a source, to a destination (without using shutil, or the OS copy command).
master = 'C:\SP_Online_PY210\students\mitch334\lesson04\dict_lab.py' #source file name
copy = 'C:\SP_Online_PY210__test\dict_lab__temp.py' #destination file name
with open(master, 'rb') as master_file, open(copy, 'wb') as copy_file:
    copy_file.write(master_file.read())

# Advanced: make it work for any size file: i.e. don’t read the entire contents of the file into memory at once.
# This should work for any kind of file, so you need to open the files in binary mode: open(filename, 'rb') (or 'wb' for writing). Note that for binary files, you can’t use readline() – lines don’t have any meaning for binary files.
# Test it with both text and binary files (maybe jpeg or something of your choosing).
master = 'C:\SP_Online_PY210__test\IMG_0853.jpg' #destination file name
copy = 'C:\SP_Online_PY210__test\IMG_0853__copy.jpg' #destination file name
with open(master, 'rb') as master_file, open(copy, 'wb') as copy_file:
    for line in master_file:
        copy_file.write(line)


# File reading and parsing
# Download this text file: students.txt
#
# In it, you will find a list of names and what programming languages they have used in the past. This may be similar to a list generated at the beginning of this class.
# Write a little script that reads that file, and generates a list of all the languages that have been used.
# What might be the best data structure to use to keep track of bunch of values without duplication?
#
# The file format:
# The first line of the file is:
# Name: Nickname, languages
# And each line looks something like this:
# Jagger, Michael: Mick, shell, python
# So a colon after the name, then the nickname, and then one or more languages.
# However, like real data files, the file is NOT well-formed. Only some lines have nicknames, and other small differences, so you will need to write some code to make sure you get it all correct.
x=0

languages = set()
languages_count = dict()
students = 'C:\SP_Online_PY210\students\mitch334\lesson04\students.txt' #source file name

with open(students, 'r') as students_file:
    for line in students_file:
        if x > 0:
            line_split = line.strip('\n').split(':')
            line_code = line_split[1].strip(' ').split(',')

            for item in line_code:
                if item.strip().islower() and item.strip() != 'nothing':
                    languages.add(item.strip())

                    if item.strip() not in languages_count:
                        languages_count[item.strip()] = 1
                    else:
                        languages_count[item.strip()] += 1
        x += 1
    print('languages: ',languages)

    # Extra challenge: keep track of how many students specified each language.
    print(f'{"Language":15}{"Count"}')

    for item in sorted(languages_count, key=languages_count.get, reverse=True):
        print(f'{item:15}{languages_count[item]}')
