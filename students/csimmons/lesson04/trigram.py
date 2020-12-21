#!/usr/bin/env python3
# Craig Simmons
# Python 210
# trigram.py 
# Created 12/17/2020 - csimmons

import sys
import os
import random

input = 'small.txt'
welcome_prompt = "\nWelcome to the automatic book generator!\n"
copy = 'copyfile.txt'

def open_file(input, copy):
    print(input)
    with open (input, 'r') as textfile, open(copy, 'w') as copy:
        while True:
            line = textfile.readline()
            print(line)
            copy.write(line)
            if not line:
                break
            prep_file(line)

def prep_file(line):
    line = line.replace('\n', '').replace('--', ' ').replace(',','').replace('.', '').replace('(', '').replace(')', '')
    clean_line = line.split(' ')
    print(len(clean_line))
    print(clean_line, '\n')
    process_text(clean_line)

def process_text(clean_line):
    trigram ={}
    for i in range(len(clean_line)-2):
        pair = clean_line[i:i+2]
        follower = clean_line[i+2]
        trigram[tuple(pair)] = follower
                #print(clean_line)
                #print(pair)
                #print(follower)clear
    print(trigram)

def main(input):
    print(input)
    print(welcome_prompt)
    open_file(input, copy)
    
    

def old_main(input):
    trigram ={}
    with open (input, 'r') as textfile:
        while True:
            line = textfile.readline()
            if not line:
                break
            line = line.replace('\n', '').replace('--', ' ').replace(',','').replace('.', '').replace('(', '').replace(')', '')
            clean_line = line.split(' ')
            print(len(clean_line))
            print(clean_line, '\n')
            #for i in range(len(clean_line)-2):
            for i in range(10):
                pair = clean_line[i:i+2]
                follower = clean_line[i+2]
                trigram[tuple(pair)] = follower
                #print(clean_line)
                #print(pair)
                #print(follower)clear
            print(trigram)

               

        

if __name__ == '__main__':
    main(input)