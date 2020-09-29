#!/usr/bin/env python3

import os

def file_paths():
    wd = os.getcwd()
    files = os.listdir()
    for i in files:
        print(f"{wd}/{i}")

# f = open("students.txt", 'rb')
# print(f.read())

# def copy_file(file_src, file_dest):
#     with open("students.txt", 'rb') as f:

#         print(f.read())

if __name__ == "__main__":
    file_paths()
    # copy_file("students.txt", "new_students.txt")
