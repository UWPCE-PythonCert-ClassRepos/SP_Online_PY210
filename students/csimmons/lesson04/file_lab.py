#!/usr/bin/env python3
# Craig Simmons
# Python 210
# file_lab.py 
# Created 12/6/2020 - csimmons

import os 
import pathlib

def dir_list():
    cwd = os.getcwd()
    files = os.listdir(cwd)
    print('\nThe CDW is: ', cwd)
    print('\nList of files and directories in CWD:')
    for file in files:
        print(file)
    print('\n')
dir_list()

def file_copy(original, copy):
    with open(original, 'rb') as original, open(copy, 'wb') as copy:
        for byte in original:
            copy.write(byte)
    original.close()
    copy.close()
    print('Copied file: ', original)
file_copy('file1.txt', './copydir/file2.txt')
file_copy('anniedog.jpg', './copydir/anniedog.jpg')

def large_copy(original, copy):
    buff = 4080
    with open(original, 'rb') as original, open(copy, 'wb') as copy:
        while True:
            data_chunk = original.read(buff)
            if not data_chunk:
                break
            copy.write(data_chunk)
    original.close()
    copy.close()
    print('Copied really large file: ', original)
# My largefile.zip was a ~15GB file
# Program copied it successfully in approx 11 mins.
# for obvious reasons, did not include largefile.zip.
# Use anniedog.jpg to test if this works or make your own largedile.zip
# large_copy('largefile.zip', './copydir/largefile.zip')
large_copy('anniedog.jpg', './copydir/anniedog2.jpg')


def languages(input_file):
    datalist = {}
    langs_set = set()
    count = 0
    with open(input_file, 'rt') as textfile:
        lines = textfile.readlines()
        for line in lines[1:]:
            line = line.replace('\n', '').replace(' ', '').replace('nothing', '')
            names = line.split(':')[0]
            langs = line.split(':')[1].split(',')
            for lang in langs:
                if lang.islower(): 
                    break
                else:
                    langs.remove(lang)
            datalist[names] = langs
            for lang in langs:
                langs_set.add(lang)
        print('\nList of (unique) programming languages known by celebrities\n')
        count = 0
        for lang in langs_set:
            count = count + 1
            print('#', count, ': ', lang)
        print('\nSet of unique programming languages:\n\n', langs_set) 
languages('students.txt')