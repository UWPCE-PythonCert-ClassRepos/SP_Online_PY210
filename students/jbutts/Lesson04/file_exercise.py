#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import datetime

'''
Lesson 4: Practice working with files and filesystem objects
'''

TXTFILE = "./students.txt"
TXTFILE_COPY = "./students_copy.txt"
JPEGFILE = "./horse.jpeg"
JPEGFILE_COPY = "./horse_copy.jpeg"
LARGE_FILE = "./large_file"
LARGE_FILE_COPY = "./large_file_copy"
BLOCK_SIZES = [512, 1024, 2048, 4096, 8192, 16384, 32768]


'''
Paths and File Processing
'''

# Write a program which prints the full path for all files in the current directory, one per lined

for filename in os.listdir():
    print(os.path.abspath(os.getcwd()) + filename)

# Write a program which copies a file from a source, to a destination (without using shutil, or
# the OS copy command).
# Advanced: make it work for any size file: i.e. don’t read the entire contents of the file into
# memory at once.


def binary_copy(file1, file2, block_size=4096):
    '''
    Copy a file byte by byte
    '''
    file_original = open(file1, 'rb')
    file_copy = open(file2, "wb")

    byte = file_original.read()

    while byte:
        file_copy.write(byte)
        byte = file_original.read(block_size)  # block size on OSX.

    file_original.close()
    file_copy.close()


def timing(file1, file2, block_size):
    '''
    Use a timer to find how quickly a file gets copied
    '''
    start = datetime.datetime.now()
    binary_copy(file1, file2, block_size)
    finish = datetime.datetime.now()
    print("block size of " + str(block_size) + " bytes: " + str(finish - start))


# copy students.txt
binary_copy(TXTFILE, TXTFILE_COPY)
# copy a jpeg
binary_copy(JPEGFILE, JPEGFILE_COPY)

'''
Bonus: very large binary file copy speeds.

run > cat /dev/random > ./large_file (hit ctrl-c after about 10 seconds)
Yields this:
-rw-r--r--  1 jamesbutts  staff   534M May  1 18:05 large_file
... full of randomness. 

I initially started reading byte-by-byte but that was agonizingly slow. Taking chunks closer to the 
block size of the filesystem, in my case 4096 bytes, allowed the copy to complete in under 1 second.
 The sweet spot seemed to be 2048 on my system.

Results:

block size of 512 bytes: 0:00:00.609085
block size of 1024 bytes: 0:00:00.620046
block size of 2048 bytes: 0:00:00.610354
block size of 4096 bytes: 0:00:00.602073
block size of 8192 bytes: 0:00:00.614088
block size of 16384 bytes: 0:00:00.606930
block size of 32768 bytes: 0:00:00.626366
'''

print("\n\nRunning multiple tests of a large binary file with different block sizes:\n")
print("{} {:.2f} MB\n".format(os.path.basename(LARGE_FILE), os.stat(LARGE_FILE).st_size / 1048576))

for block_size in BLOCK_SIZES:
    os.remove(LARGE_FILE_COPY) # delete the file so it's hopefully not cached by the os.
    timing(LARGE_FILE, LARGE_FILE_COPY, block_size)


'''

File reading and parsing

Download this text file:

students.txt

In it, you will find a list of names and what programming languages they have used in the past. 
This may be similar to a list generated at the beginning of this class.

Write a little script that reads that file, and generates a list of all the languages that have 
been used.


'''


# Nicks, Stevie:  java, perl, c#, c++, python

def get_languages(txtfile):
    '''
    Get a list of languages from a text file, deduplicate and remove bogus entries returning
    a clean list (set).
    '''
    languages = set()  # Use a set because they don't allow dupes
    input_file = open(txtfile)
    for line in input_file:
        languages_raw = line.split(":")[1].replace(' ', '').strip("\n").split(",")  # strip didn't
        # work for whitespace (?!)
        for word in languages_raw:
            for letter in word:
                if word in ("nothing", "languages"):  # 'Nothing' isn't a programming language,
                    # neither is language.
                    break
                elif letter.isupper():  # If this word has an upper case
                                        # letter it's a nickname. Skip it.
                    break
            else:
                if word != "":  # Handle empty strings. (John Lennon and Chuck Berry, both valid)
                    languages.add(word)

    languages = sorted(languages)  # return a sorted dupe-free list

    input_file.close()
    return languages


print("\n\nWrite a little script that reads that file, and generates a list of all the languages "
      "that have been used.\n")
print(get_languages(TXTFILE))
