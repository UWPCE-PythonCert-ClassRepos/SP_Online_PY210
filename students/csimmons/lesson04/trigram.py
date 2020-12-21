#!/usr/bin/env python3
# Craig Simmons
# Python 210
# trigram.py 
# Created 12/17/2020 - csimmons

import sys
import os
import random
#input = 'small.txt'
input = 'sherlock_small.txt'
welcome_prompt = "\nWelcome to the automatic book generator!\n"
trigrams = {}

def open_file(input):
    with open (input, 'r') as textfile:
        while True:
            line = textfile.readline()
            if not line:
                break
            clean_line(line)

def clean_line(line):
    line = line.replace('\n', '').replace('--', ' ').replace(',','').replace('.', '').replace('(', '').replace(')', '')
    clean_words = line.split(' ')
    process_text(clean_words)

def process_text(clean_words):
    for i in range(len(clean_words)-2):
        pair = tuple(clean_words[i:i+2])
        third = clean_words[i+2]
        if pair in trigrams:
            trigrams[pair].append(third)
        else:
            trigrams[pair] = [third]
    print(trigrams)

        #trigram[tuple(pair)] = third
        #print(trigram)
       
        
        #trigram[tuple(pair)] = [follower]
                #print(clean_line)
                #print(pair)
                #print(follower)clear

def main(input):
    print(input)
    print(welcome_prompt)
    open_file(input)
    
    

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