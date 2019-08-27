#!/usr/bin/env python3
#https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/file_lab.html

import os
#Write a program which prints the full path for all files in the current directory, one per line

def file_print():
    #for each entry in working directory
    for entry in os.scandir('.'):
        #if its a file print its name
        if entry.is_file():
            print(entry.name)
            
#write a program which copies a file from a source, to a destination
#no shutil or OS copy command
def file_copy(source, dest):
    #declare which file to write and read from
    with open(source, 'rb') as infile, open(dest, 'wb') as outfile:
        #read while you write
        outfile.write(infile.read())

#Write a little script that reads that file and generates a list of all the languages that have been used

def program_count(source):
    #build empty variables to fill
    programs_no_count = set()
    programs_with_count = {}
    with open(source, 'r') as infile:
        #skip the header row
        next(infile)
        for lines in infile:
            #split to everything after the colon
            languages = lines.split(':')[1]
            #remove spaces on either side before iterating.
            languages = languages.rstrip().lstrip()
            #iterate throug items seperated by space.
            for items in languages.split(' '):
                #Some names have no programing, use try catch to skip these shenanigans
                try:
                    if items[0].islower():
                        program = items.split(',')[0]
                        #update the none counting set with distinct values
                        programs_no_count.update([program])
                        #update the counting dictionary with a new value or increment the count.
                        if program in programs_with_count:
                            programs_with_count[program] = programs_with_count[program] + 1
                        else:
                            programs_with_count[program] = 1      
                except:
                    continue
    return programs_no_count, programs_with_count
