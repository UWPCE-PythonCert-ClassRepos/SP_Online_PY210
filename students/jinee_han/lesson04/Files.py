# --------------------------------
# 07/16/19 Jinee Han
# Python Programming Lesson 4
# Paths and File Processing
# ---------------------------------

'''
1. Write a program which prints the full path for all files in the current directory, one per line
2. Write a program which copies a file from a source, to a destination (without using shutil, or the OS copy command
'''

import os

# Path and File Processing

for file in os.listdir(os.getcwd()):
    print(os.path.abspath(file))

# File Reading and Parsing

# split on : for name to language break
# split on comma, if element starts with uppercase, skip it because it's a nick name

file_obj = open("students.txt", "r")

students_to_languages = {}
language_count = {}
for line in file_obj:
    if line.startswith("Name"):
        continue
    line_split = line.strip("\n").split(':')
    language_list = []
    languages_split = line_split[1].strip(' ').split(',')
    name = line_split[0]
    for language in languages_split:
        lang_cleaned = language.replace(" ", "")
        # Assuming all Nicknames start with upper case character, if it is uppercase skip because not a language
        if len(lang_cleaned) > 0 and lang_cleaned[0] == lang_cleaned[0].upper():
            continue

        language_list.append(lang_cleaned)
        # Store how many languages each student specifies
        if lang_cleaned in language_count:
            language_count[lang_cleaned] += 1
        else:
            language_count[lang_cleaned] = 1

    students_to_languages.update({name: language_list})

for k, v in students_to_languages.items():
    print("{} : {}".format(k, v))

for k, v in language_count.items():
    print("{} : {}".format(k, v))