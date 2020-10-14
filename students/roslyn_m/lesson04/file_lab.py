#!/usr/bin/env python3

# File Lab
# Dev: Roslyn Melookaran
# Date: 9/17/20
# Change Log: (Who, When, What)
# R. Melookaran, 9/9/20, created script

import pathlib

# # Write a program which prints the full path for all files in the current directory, one per line.
# pth = pathlib.Path('./')
# print(pth.is_dir())
# print(pth.absolute())
# for f in pth.iterdir():
#     if f.is_file():
#         print(f.absolute())
#
# # File copy
# file_in = 'salmon_population.txt'
# file_out = 'copy_salmon.txt'
# with open(file_in,'rb') as infile, open(file_out, 'wb') as outfile:
#     outfile.write(infile.read())
#
# # Image copy
# pic_in = 'Mountain.jpg'
# pic_out = 'copy_mountian.jpg'
# with open(pic_in,'rb') as infile, open(pic_out, 'wb') as outfile:
#     outfile.write(infile.read())

# Creating list of student langauages
student_info = []
all_students = []
language_set = set()
with open('students.txt', 'r') as file:
    lines = file.readlines() # reads all the file lines into one list
    lines = [line.replace(" ", "") for line in lines] # removes all the extra spaces
    lines = [line.replace(":", ",") for line in lines] # replaces the colon with a comma
    lines = [line.strip() for line in lines] # strips the last "\n" off of each line
    for row in lines:
        student_info = row.split(",")
        all_students.append(student_info)
        student_info = []
all_students.remove(all_students[0]) # Removes the title line
for item in all_students:
    print(item)
    length = len(item)
    if item[2] == item[2].title(): # This line tells you whether there is a nickname or not
        if length == 3: # This line is for when there is a student and nickname but no languages
            print("no languages")
        else:
            for i in range(3,length):
                language_set.add(item[i])
                print(item[i])

    else:
        if length == 2:  # This line is for when there is a student and nickname but no languages
            print("no languages")
        else:
            for i in range(2, length):
                language_set.add(item[i])
                print(item[i])

language_set.remove("")
language_set.remove("nothing")
print(language_set)












