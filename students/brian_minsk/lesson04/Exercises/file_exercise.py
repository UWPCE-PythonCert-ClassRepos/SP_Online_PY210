# Author: Brian Minsk

# Paths and File Processing

""" Write a program which prints the full path for all files in the current directory, one per line. 
Use either the os module or pathlib.
"""
import pathlib
pth = pathlib.Path('./')
for f in pth.iterdir():
    print(f.resolve())

""" Write a program which copies a file from a source, to a destination without using shutil, or the OS copy command. 
This should work for any kind of file, so you need to open the files in binary mode: open(filename, 'rb') (or 'wb' for writing). Note that for binary files, you can’t use readline() – lines don’t have any meaning for binary files.
Test it with both text and binary files (maybe a jpeg or something of your choosing).
Advanced: make it work for any size file: i.e. don’t read the entire contents of the file into memory at once.
This should only be a few lines of code :-)
"""

source_filename = None
destination_path = None

# collect and validate necessary user input
while True:
    source_filename = pathlib.Path(input("Type a file name: "))
    if source_filename.is_file():
        break
    else:
        print("Not a valid file path.")

while True:
    destination_path = pathlib.Path(input("Type a destination directory: "))
    if destination_path.is_dir():
        destination_filename = pathlib.Path("")
        destination_filename = destination_path / source_filename
        print(destination_filename)
        break
    else:
        print("Not a valid directory.")

# Not validating the user response for this. Passing -1 (or any negative number) to read will read the whole file at once.
num_bytes = int(input("Type number of bytes to copy at a time (e.g. 1024) or type '-1' to read the whole file into memory: "))
with open(source_filename, "rb") as infile, open(destination_filename, "wb") as outfile:
    while outfile.write(infile.read(num_bytes)):
        pass

# "Write a little script that reads that file and generates a list of all the languages that have been used." task
language_dict = {}
with open("students.txt") as f:
    while True:
        line = f.readline()
        if not line:
            break
        if line == "Name: Nickname, languages": #header line
            continue
        


