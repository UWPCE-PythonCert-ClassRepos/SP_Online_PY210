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

def file_copy(original, copy):
    with open(original, 'rb') as original, open(copy, 'wb') as copy:
        for byte in original:
            copy.write(byte)
    original.close()
    copy.close()
    print("Copied ", original)

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
    print("Copied ", original)
# largefile.zip was a ~15GB file
# copied it successfully in approx 11 mins
# large_copy('largefile.zip', './copydir/largefile.zip')

large_copy('anniedog.jpg', './copydir/anniedog2.jpg')
for i in range(len(set1)):
    if (set1[i].islower()):
        finalList.append(set1[i])

    if char in line.islower():
'''

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
        for lang in langs_set:
            count = count + 1
            print(count, ' ', lang)
        print(langs_set) 

languages('students.txt')