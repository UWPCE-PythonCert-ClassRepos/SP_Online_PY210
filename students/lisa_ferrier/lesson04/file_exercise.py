# file_exercise.py
# Lisa Ferrier, Python 210, Lesson04

import os

# os method to list full path of files in directory
cwd = os.getcwd()

for file in os.listdir(cwd):
    print(os.path.abspath(file))

# Copy a file (original) in a new directory
original = cwd + "/original.txt"
copy = cwd + "/copy/copy.txt"

# read the original file, and write to copy
with open(original, "rb") as o, open(copy, "wb") as c:
    read = o.read()
    c.write(read)

# Advanced - copy file line by line (as opposed to all at once)
with open(original, "rb") as o, open(copy, "wb") as c:
    for line in o:
        c.write(line)

# read students.txt file, create a set of languages, and count distinct number of languages.
languages = set()
student_language_dict = {}

with open("students.txt", "rb") as f:
    keys = []
    values = []
    lines = [line.decode(encoding="utf-8").strip("\n").split(":") for line in f]
    for line in lines[1:]:  # skip the header row
        if len(line[1]) == 0:
            continue
        langs = line[1].strip().split(", ")
        for lang in langs:
            if lang.islower():
                # print(language)
                values.append(lang)
                languages.add(lang)
print(languages)
print('There are ', len(languages), ' languages in the language set.')
