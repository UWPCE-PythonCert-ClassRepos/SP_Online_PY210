#!/usr/bin/env python3
# PY210 Lesson 04 Paths and File Processing - Chase Dullinger

import os
current_dir = os.getcwd()

for file in os.listdir():
    print(current_dir + "/" + file)

# input_file = "/Users/chase/Documents/Python_Certificate/Python210/git/SP_Online_PY210/students/chasedullinger/lesson04/dict_lab.py"
input_file = "/Users/chase/Desktop/sign_o_the_times_digital_album_remastered/603497846511.jpg"
output_file = input_file+"copy"

with open(input_file, "rb") as infile:
    with open(output_file, "wb") as outfile:
        outfile.write(infile.read())
