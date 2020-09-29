#!/usr/bin/env python3
import os
import pathlib

source = pathlib.Path.home() / "Desktop/Python/students.txt"
dest = pathlib.Path.home() / "Desktop/Python/newstudents.txt"
with open(str(source), 'rb') as infile, open(dest, 'wb') as outfile:
    outfile.write(infile.read())

for line in open(dest):
    print(line)

