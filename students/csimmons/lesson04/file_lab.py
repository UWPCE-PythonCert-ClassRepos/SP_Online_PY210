#!/usr/bin/env python3
# Craig Simmons
# Python 210
# file_lab.py 
# Created 12/6/2020 - csimmons

import os 
import pathlib
'''
def dir_list():
    cwd = os.getcwd()
    files = os.listdir(cwd)
    print('CDW is: ', cwd)
    for file in files:
        print(file)

dir_list()


f = open('secrets.bin', 'rb')
secret_data = f.read()
f.close()

f = open('secrets.txt')
while True:
    line = f.readline()
    if not line:
        break
    do_something_with_line()
    with open(d_path, 'r') as reader, open(d_r_path, 'w') as writer:
    dog_breeds = reader.readlines()
    writer.writelines(reversed(dog_breeds))

'''
def file_copy():
    f_orig = 'file1.txt'
    f_new = 'file2.txt'

    with open('file1.txt', 'r') as f_orig, open('file2.txt', 'w') as f_new:
        for line in f_orig:
            f_new.write(line)
    print("Copied filet")

file_copy()


