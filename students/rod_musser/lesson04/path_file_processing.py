#!/usr/bin/env python3
import pathlib
# Print files in current directory with absolute file na,e
curr_pth = pathlib.Path('./')
for f in curr_pth.iterdir():
    if (f.is_file()):
        print(f.absolute())
# Copy file
file_to_copy = input("Enter in the name of a file to copy: ")
copy_of_file = input("Enter the name of the file to copy it to: ")
with open(file_to_copy, 'rb') as infile, open(copy_of_file, 'wb') as outfile:
    outfile.write(infile.read())
